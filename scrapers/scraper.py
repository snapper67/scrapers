import csv
import json
import logging
import os
import re
import string
import sys
import time
import urllib.parse
from collections import OrderedDict
from datetime import datetime
from math import trunc
from pathlib import Path

import pandas as pd
import requests
import seleniumwire.undetected_chromedriver as uc
from bs4 import BeautifulSoup
from django.core.cache import cache
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver as seleniumwire_webdriver
from seleniumwire.utils import decode

class SkuNotFound(Exception):
	"""Exception raised when a product cannot be found during scraping.

	Attributes:
		message -- explanation of the error
		product_identifier -- identifier of the product that was not found (e.g., URL, SKU, name)
	"""

	def __init__(self, message="SKU not found for product", product_identifier=None):
		self.message = message
		self.product_identifier = product_identifier
		super().__init__(self.message)

	def __str__(self):
		if self.product_identifier:
			return f"{self.message}: {self.product_identifier}"
		return self.message

class ProductNotFound(Exception):
	"""Exception raised when a product cannot be found during scraping.

	Attributes:
		message -- explanation of the error
		product_identifier -- identifier of the product that was not found (e.g., URL, SKU, name)
	"""

	def __init__(self, message="Product not found", product_identifier=None):
		self.message = message
		self.product_identifier = product_identifier
		super().__init__(self.message)

	def __str__(self):
		if self.product_identifier:
			return f"{self.message}: {self.product_identifier}"
		return self.message

class Scraper:
	SCRAPER_TYPE = 'Misc'
	# Class variables for default values
	PRODUCT_DATA_SPEC = {}

	BASE_URL = ''
	CRM_ID = ''
	CRM_BASE_URL = 'https://distributors.snappersworld.com'

	ENCODING = "utf-8"

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/'

	# Default file names
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'
	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	VENDOR_NAME = ''

	CATEGORIES = json.loads('''
	    {
	      "data": {
	        "catalogCategoryOptions": [
	          {
	            "category": {
	              "id": "1",
	              "baseName": "all-items",
	              "name": "All Items",
	              "visibleOnHeader": true,
	              "visibleOnSidebar": true,
	              "__typename": "ProductCategory"
	            },
	            "productCount": 0,
	            "subcategories": [],
	            "__typename": "categoryOption"
	          }
	        ]
	      }
	    }
	    ''')

	# Import specification
	BASE_IMPORT_SPEC = [
		'name', 'sku', 'gtin', 'image', 'pack', 'size', 'retail_price', 'ordering_unit',
		'is_catch_weight', 'is_broken_case', 'average_case_weight', 'brand', 'taxonomy',
		'level_1', 'level_2', 'level_3', 'manufacturer_name', 'manufacturer_sku',
		'distributor_name', 'content_url', 'description', 'unit_price', 'extra_data_1', 'extra_data_2'
	]

	BASE_PRODUCT_DATA_SPEC = {
		# Fields from IMPORT_SPEC
		'name': '',
		'sku': '',
		'gtin': '',
		'image': '',
		'pack': '',
		'size': '',
		'retail_price': '',
		'ordering_unit': '',
		'is_catch_weight': '',
		'is_broken_case': '',
		'average_case_weight': '',
		'brand': '',
		'taxonomy': '',
		'level_1': '',
		'level_2': '',
		'level_3': '',
		'manufacturer_name': '',
		'manufacturer_sku': '',
		'distributor_name': '',
		'distributor_address': '',
		'distributor_city': '',
		'distributor_state': '',
		'distributor_zip': '',
		'content_url': '',
		'description': '',
		'unit_price': '',
		'extra_data_1': '',
		'timestamp': '',
		'extra_data_2': '',
		'id': '',
		'pack_size': '',
		'category': '',
		'subcategory': '',
		'subsubcategory': '',
	}

	# Default options
	DEFAULT_OPTIONS = {
		'scrape_products': False,
		'process_csv': False,
		'reprocess_csv': False,
		'dedupe_csv': False,
		'format_csv': False,
		'scan_csv': False,
		'count_csv': False,
		'test_products': TEST_PRODUCTS,
		'max_products': 999,
		'csv_start_row': CSV_START_ROW,
		'category_to_process': 0,
		'test_categories': 100,
		'chosen_category': '10001',  # Default to Meat
		'url_output_file': URL_OUTPUT_FILE,
		'data_output_file': DATA_OUTPUT_FILE,
		'home_directory': DEFAULT_DIRECTORY,
		'base_url': '',
		'crm_url': '',
	}
	scrape_options = {
		'max_products': MAX_API_PRODUCTS,
		'test_categories': TEST_CATEGORIES,
		'test_products': TEST_PRODUCTS,
		'csv_start_row': CSV_START_ROW,
		'scrape_products': False,
		'process_csv': True,
		'reprocess_csv': False,
		'dedupe_csv': False,
		'format_csv': False,
		'scan_csv': False,
		'count_csv': False,
		'chosen_category': '',
		'url_output_file': URL_OUTPUT_FILE,
		'data_output_file': DATA_OUTPUT_FILE,
		'category_name': '',
		'category_to_process': 0,
		'home_dir': '',
        'attempts': '40',
	}

	def __init__(self, options=None, headless=True, firefox=False):
		"""Initialize the scraper with options"""
		# Update default options with any provided options
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['crm_url'] = self.get_crm_link()
		self.options['base_url'] = self.BASE_URL
		self.options['home_directory'] = self.DEFAULT_DIRECTORY
		print(self.options)

		# Initialize Chrome options
		self.chrome_options = uc.ChromeOptions()
		if headless:
			self.chrome_options.add_argument('--headless')
		self.chrome_options.add_argument('--disable-gpu')
		self.chrome_options.add_argument('--no-sandbox')
		self.chrome_options.add_argument('--proxy-bypass-list=<-loopback>')
		self.chrome_options.add_argument('--ignore-certificate-errors')
		self.chrome_options.add_argument("proxy-bypass-list=<-loopback>")
		prefs = {"profile.managed_default_content_settings.images": 2}  # 2 blocks images
		self.chrome_options.add_experimental_option("prefs", prefs)

		# Selenium Wire options
		self.seleniumwire_options = {
			'disable_encoding': True,
		}

		self.firefox_options = FireFoxOptions()
		if headless:
			self.firefox_options.add_argument("--headless")
		self.firefox_options.add_argument('--disable-gpu')
		self.firefox_options.add_argument('--no-sandbox')
		self.firefox_options.set_capability("acceptInsecureCerts", True)
		# Prevent Firefox from bypassing proxy for localhost
		self.firefox_options.set_preference("network.proxy.allow_hijacking_localhost", True)


		self.current_task_id = None
		logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(threadName)s - %(message)s')

		# seleniumwire_options = {
		# 		'request_filter': lambda request: 'product-domain-api/v2/products' in request.url,
		# 		'disable_encoding': True,
		# 	}
		self.firefox = firefox

		self.driver = None
		self.wait = None

	def __enter__(self):
		"""Context manager entry"""
		self.setup_driver()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""Context manager exit - ensure driver is closed"""
		self.cleanup()

	def setup_driver(self):
		"""Initialize the WebDriver"""
		if not self.driver:
			# Get the directory where the current script is located
			script_dir = os.path.dirname(os.path.abspath(__file__))
			# Build the path to chromedriver in the chrome-mac-arm64 directory
			chromedriver_path = os.path.join(script_dir, 'chrome-mac-arm64', 'chromedriver')
			chrome_binary_path = os.path.join(script_dir, 'chrome-mac-arm64', 'Google Chrome for Testing.app')
			# chrome_binary_path = "/path/to/chrome-for-testing/chrome.exe"  # Adjust for your OS

			service = Service(chromedriver_path)
			# self.chrome_options.binary_location = chrome_binary_path
			if self.firefox:
				self.driver = seleniumwire_webdriver.Firefox(
					options=self.firefox_options,
					seleniumwire_options=self.seleniumwire_options
				)
			else:
				self.driver = seleniumwire_webdriver.Chrome(
					service=service,
					options=self.chrome_options,
					seleniumwire_options=self.seleniumwire_options
				)
		self.driver.command_executor.set_timeout(1000)
		self.wait = WebDriverWait(self.driver, 60)

	def cleanup(self):
		"""Clean up resources"""
		print("cleanup()")
		if self.driver:
			self.driver.quit()
			self.driver = None

	# ************************************************************************
	# 	Getters and Setters
	# ************************************************************************

	def get_categories(self):
		"""
		Returns a list of category dictionaries from the CATEGORIES data. This is the preferred way to store the categories

		Returns:
			list: A list of dictionaries, each containing 'id' and 'name' of a category
		"""
		category_options = self.CATEGORIES.get('data', {}).get('categories', {})
		return [
			{'id': option['id'], 'name': option['name'], 'url': option['url'], 'subcategories': option['subcategories']}
			for option in category_options
			if option.get('id') and option.get('name')
		]

	def set_options(self, options):
		"""
		Set options for the scraper

		Args:
			options (dict): Dictionary of options
		"""
		self.options = {**self.options, **options}

	def get_options(self):
		# print("get_options()")
		# print(self.options)
		return self.options

	def get_product_spec(self):
		return self.PRODUCT_DATA_SPEC.copy()

	def get_name(self):
		return self.VENDOR_NAME

	def get_type(self):
		return self.SCRAPER_TYPE

	def get_unique_keys(self, data_file):
		""" Some websites do not use SKU as the unique identifier"""
		keys = set()
		if os.path.exists(data_file):
			with open(data_file, 'r', newline='', encoding='utf-8') as f:
				reader = csv.DictReader(f)
				csv.field_size_limit(sys.maxsize)
				if 'sku' in reader.fieldnames:
					keys = {row['sku'] for row in reader}
		return keys

	# ************************************************************************
	# Utility Functions
	# ************************************************************************
	@staticmethod
	def print_element(element):
		print(f"Text: {element.text}")
		print(f"Tag Name: {element.tag_name}")
		print(f"Class Attribute: {element.get_attribute('class')}")
		print(f"Inner HTML: {element.get_attribute('innerHTML')}")
		print(f"Outer HTML: {element.get_attribute('outerHTML')}")
		print(f"Inner Text: {element.get_attribute('innerText')}")
		print(f"Text Content: {element.get_attribute('textContent')}")
		print(f"Location: {element.location}")
		print(f"Size: {element.size}")
		print(f"Is Displayed: {element.is_displayed()}")

	@staticmethod
	def extract_unique_id_from_url(url):
		"""
		Get a unique identifier from the url.
		Standard version example https://website.com/4345353
		"""
		try:
			# get the last part of the url and remove any querystring parameters
			sku = url.split('/')[-1].split('?')[0]
		except Exception as e:
			print(f"⛔️⛔️⛔️Error saving URLs to CSV: {e}")
			sku = ''
		return sku

	@staticmethod
	def clean_json_string(json_str):
		"""Helper function to clean JSON string from control characters and fix common issues"""
		if not isinstance(json_str, str):
			json_str = str(json_str)

		# Remove control characters except for newlines and tabs
		cleaned = []
		for char in json_str:
			if ord(char) >= 32 or char in "\n\r\t":
				cleaned.append(char)

		cleaned_str = "".join(cleaned)
		# cleaned_str = urllib.parse.unquote(cleaned_str)

		# Fix common JSON issues
		# cleaned_str = cleaned_str.replace('\\"', '"')  # Unescape quotes
		# cleaned_str = cleaned_str.replace('\\n', ' ')  # Replace newlines with spaces
		# cleaned_str = cleaned_str.replace('\\r', '')  # Remove carriage returns
		# cleaned_str = cleaned_str.replace('\\t', ' ')  # Replace tabs with spaces
		cleaned_str = cleaned_str.replace("<!--", "").replace("-->", "")
		cleaned_str = re.sub(r'[\x00-\x1F\x7F]', ' ', cleaned_str)  # Remove other control chars

		return cleaned_str

	@staticmethod
	def make_filename_safe(s):
		valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
		cleaned_filename = ''.join(c for c in s if c in valid_chars)
		cleaned_filename = cleaned_filename.replace(' ', '_')  # Replace spaces with underscores
		return cleaned_filename


	# ************************************************************************
	# 	Class Functions
	# ************************************************************************
	def clean_data_file(self, input_file=None, output_file=None, field='name'):
		"""
		Clean the URL file by removing rows that don't have a value in the 'name' column.

		Args:
			input_file (str, optional): Path to the input CSV file. If None, uses the URL output file from options.
			output_file (str, optional): Path to save the cleaned CSV. If None, overwrites the input file.

		Returns:
			tuple: (success: bool, message: str) indicating the result of the operation
		"""
		print(f"Cleaning data file: {input_file}")
		try:
			# Get input file path
			if input_file is None:
				input_file = self.get_data_file_path(self.options.get('home_directory', self.DEFAULT_DIRECTORY))

			# Set default output file to input file if not specified
			if output_file is None:
				output_file = input_file

			# Read the CSV file
			# df = pd.read_csv(csv_file, encoding=ENCODING)
			df = pd.read_csv(input_file, dtype=str, keep_default_na=False, encoding=self.ENCODING, on_bad_lines='skip')

			# Check if field column exists
			if field not in df.columns:
				return False, f"Error: {field} column not found in {input_file}"

			# Count rows before cleaning
			initial_count = len(df)

			# Remove rows where name is empty or whitespace
			clean_df = df[df[field].str.strip().astype(bool)]

			# Count rows after cleaning
			final_count = len(clean_df)
			removed_count = initial_count - final_count

			# Save the cleaned data
			clean_df.to_csv(output_file, index=False)

			# If we removed any rows, return success with count
			if removed_count > 0:
				return True, f"Removed {removed_count} rows without {field}s. {final_count} rows remaining in {output_file}"
			else:
				return True, f"No rows without {field}s found. File was not modified."

		except Exception as e:
			return False, f"Error cleaning URL file: {str(e)}"

	def get_crm_link(self):
		if hasattr(self, 'CRM_ID') and  self.CRM_ID != '':
			print(self.CRM_ID)
			return f"<a href='{self.CRM_BASE_URL}/{self.CRM_ID}' target='_blank'>View in CRM</a>"
		return ''

	def get_file_path(self, filename, home_dir=None):
		"""
		Get the full file path by joining with the home directory if the path is not absolute.

		Args:
			filename (str): The filename or path to resolve
			home_dir (str, optional): The home directory to use as base for relative paths

		Returns:
			str: The resolved absolute file path
		"""
		if not filename:
			return filename

		# Convert to Path object
		path = Path(filename)

		# If it's already an absolute path, return as is
		if path.is_absolute():
			return str(path)

		# Otherwise, join with home directory
		home_dir = home_dir or self.options.get('home_directory', self.DEFAULT_DIRECTORY)
		home_path = Path(home_dir).expanduser().resolve()
		return str(home_path / path)

	def get_url_file_path(self, home_dir=None, input_file=None):
		if not home_dir:
			home_dir = getattr(self, 'DEFAULT_DIRECTORY')
		if not input_file:
			input_file = self.options.get('url_output_file', '')
		print(f"home_dir: {home_dir}, input_file: {input_file}")
		return self.get_file_path(input_file, home_dir)

	def get_data_file_path(self, home_dir=None, input_file=None):
		print("get_data_file_path")
		if not home_dir:
			home_dir = getattr(self, 'DEFAULT_DIRECTORY')
		if not input_file:
			input_file = self.options.get('data_output_file', '')
		print(f"home_dir: {home_dir}, input_file: {input_file}")
		return self.get_file_path(input_file, home_dir)

	def html_table_to_csv(self, html_content, output_file='products_export.csv', home_dir=DEFAULT_DIRECTORY):
		"""
		Convert an HTML table to a CSV file.

		Args:
			html_content (str): HTML content containing a table
			output_file (str): Path to save the CSV file
			home_dir (str): Home directory for relative paths
		"""
		try:
			# Parse the HTML
			# Resolve output file path
			output_file = self.get_file_path(output_file, home_dir)

			# Ensure the output directory exists
			os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)

			soup = BeautifulSoup(html_content, 'html.parser')
			table = soup.find('table')

			if not table:
				print("No table found in the HTML content")
				return False

			# Open the CSV file for writing
			with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
				writer = csv.writer(csvfile)

				# Process each row in the table
				rows = table.find_all('tr')
				for row in rows:
					# Get all cells in the row
					cells = row.find_all(['th', 'td'])
					# Extract text from each cell and clean it
					row_data = [cell.get_text(strip=True) for cell in cells]
					# Write the row to CSV
					writer.writerow(row_data)

			print(f"Successfully exported data to {output_file}")
			return True

		except Exception as e:
			print(f"⛔️⛔️⛔️Error exporting to CSV: {e}")
			return False

	def write_product_to_csv(self, product_data, filename=None):
		"""
		Write a product data dictionary to a CSV file. If the file doesn't exist,
		it will be created with headers. If it exists, the data will be appended.

		Args:
			product_data (dict): Dictionary containing product data following PRODUCT_DATA_SPEC
			filename (str): Path to the CSV file (defaults to DATA_OUTPUT_FILE)

		Returns:
			bool: True if successful, False otherwise
		"""
		home_dir = ""
		try:
			# Convert all values to strings and handle None values
			row_data = {k: str(v) if v is not None else '' for k, v in product_data.items()}

			if not filename:
				filename = self.options.get('data_output_file', '')
			home_dir = self.options.get('home_directory', '')

			# Resolve filename
			filename = self.get_file_path(filename, home_dir)

			# Ensure the directory exists
			os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)

			# Check if file exists to determine if we need to write headers
			file_exists = os.path.isfile(filename)

			with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
				writer = csv.DictWriter(csvfile, fieldnames=self.PRODUCT_DATA_SPEC.keys())

				# Write header if file is being created
				if not file_exists or os.path.getsize(filename) == 0:
					writer.writeheader()

				# Write the product data
				writer.writerow(row_data)
				csvfile.flush()

			print(f"Successfully wrote product {product_data.get('sku', '')} to {filename}")

			return True

		except Exception as e:
			print(f"⛔️⛔️⛔️Error writing product to CSV: {e}")
			print(f"filename: {filename}")
			print(f"home_dir: {home_dir}")
			return False

	def convert_category_to_output_filename(self, category):
		return category.replace(" ", "_").replace("/", "_") + "_product_urls.csv"

	def save_urls_to_csv(self, urls, category_name="", subcategory_name="", sub_subcategory_name=""):
		"""
		Save a list of URLs to a CSV file. If the file exists, it will append to it.

		Args:
			urls (list): List of URLs to save
			category_name (str): Name of the category
			subcategory_name (str): Name of the sub category
			sub_subcategory_name (str): Name of the sub category of the sub category
		"""

		print(f"save_urls_to_csv()")
		# print(f"save_urls_to_csv(){urls}")

		# Resolve the file path
		home_dir = self.options.get('home_directory')
		filename = self.get_url_file_path(home_dir)

		# Ensure the directory exists
		os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)

		file_exists = os.path.isfile(filename)

		print(f"Home Directory: {home_dir}, Filename: {filename}")

		try:
			with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
				writer = csv.writer(csvfile)

				# Write header only if file is new
				if not file_exists:
					writer.writerow(['SKU', 'URL', 'Timestamp', 'Category', 'Subcategory', "Sub Subcategory"])

				# Write each URL with timestamp
				for url in urls:
					print(url)
					clean_url = url.rstrip('/')
					sku = self.extract_unique_id_from_url(clean_url)
					writer.writerow(
						[sku, url, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), category_name, subcategory_name,
						 sub_subcategory_name])

			mode = "Appended to" if file_exists else "Created new"
			print(f"Successfully {mode} {len(urls)} URLs to {filename}")

		except Exception as e:
			print(f"⛔️⛔️⛔️Error saving URLs to CSV: {e}")

	def search_requests(self):
		"""
		Load a URL and search the traffic for a search term
		"""
		print("Starting search_requests")
		url = self.options.get('url', '')
		search_term = self.options.get('search_term', '')
		print(search_term)
		self.driver.get(url)
		time.sleep(10)
		html = "<ul>"
		found = False
		for request in self.driver.requests:  # Filter for API requests
			try:
				if request.response:
					print(request.url)
					body = decode(request.response.body,
					              request.response.headers.get('Content-Encoding', 'identity'))
					# If the body is JSON, parse it
					# if 'application/json' in request.response.headers.get('Content-Type', ''):
					# 	data = json.loads(body)
					# else:
					# 	data = str(body)
					# print(data)
					if search_term in str(body):
						print('Found')
						print(f"Request URL: {request.url}")
						found = True
						html = html + "<li>" + request.url + "</li>"

			except Exception as e:
				print(f"⛔️Error decoding detail response body of {request.url}: {e}")

		del self.driver.requests
		html = html + "</ul>"
		return html, found

	def get_category_url(self, category):
		"""Get the URL for a category"
			Override this to perform any additional processing
		"""
		return category['url']

	# ************************************************************************
	# 	Core
	# ************************************************************************

	def scraping_setup(self):
		"""Scrape products from the website"""
		raise NotImplementedError("scraping_setup method not implemented")

	def run(self):
		"""
		Main entry point that determines which action to take based on the options
		Currently only processing a single option this could easily be changed to support multiple
		"""
		# logging.info(f"Running scraper with options: {self.options}")
		print(f"Running scraper with options: {self.options}")
		if self.options.get('get_categories'):
			return self.build_categories_list()
		elif self.options.get('scrape_products'):
			return self.build_products_list()
		elif self.options.get('process_csv'):
			return self.process_products_from_csv()
		elif self.options.get('reprocess_csv'):
			return self.process_missing_skus()
		elif self.options.get('dedupe_csv'):
			return self.remove_duplicate_skus()
		elif self.options.get('process_extra'):
			return self.process_extra_data_from_csv()
		elif self.options.get('count_csv'):
			return self.count_csv_rows()
		elif self.options.get('search_requests'):
			return self.search_requests()
		elif self.options.get('format_csv'):
			return self.update_csv_columns()
		elif self.options.get('scan_csv'):
			return self.scan_files()
		else:
			return "No action specified. Please select an option."

	# Step One: Get the categories. These will be used to get the products
	def build_categories_list(self):
		"""Scrape products from the website"""
		raise NotImplementedError("build_categories_list method not implemented")

		# Step Two: Get links to products
	def build_products_list(self):
		"""
		Scrape product urls from the website
		Description: Cycles through the category urls and calls get_category_page
		Calls: get_category_page
		Built in Sleep: Yes - 2 seconds between categories
		"""
		html = ""
		all_urls = []
		self.scraping_setup()
		# Use the options with fallback to module-level variables
		max_products = self.options.get('max_products', self.MAX_API_PRODUCTS)
		category_to_process = self.options.get('category_to_process', 0)
		chosen_category = int(self.options.get('chosen_category', 0))
		test_categories = self.options.get('test_categories', 100)
		category_count = 0
		if int(self.options['chosen_category']) == 0:
			categories = self.get_categories()
			print(f"All Categories ")
		else:
			for category in self.get_categories():
				print(f"category : {category.get('name', '')}")
				if int(category.get('id', '')) == chosen_category:
					categories = [category]  # Only process the chosen category
					print(f"Category found : {categories}")
					break
		url_output_file = self.options.get('url_output_file', '')

		# Wait for the page to be fully loaded
		print(f"Output File Name: {url_output_file}")
		total_products = 0
		loop_counter = 0
		category_found_count = 1

		# Check to see if we asked for a specific category
		if category_to_process > 0:
			print(f"Category to process: {category_to_process}")
			loop_counter = category_to_process - 1
			test_categories = category_to_process
			category_found_count = category_to_process

		for category in categories:
			category_name = category['name']
			self.options['url_output_file'] = self.convert_category_to_output_filename(category_name)
			print(f"category: {category_name}")

			sub_categories = category.get('subcategories', False)
			if sub_categories:
				sub_category_found_count = len(sub_categories)
				print(f"Found {sub_category_found_count} sub categories to process...")
				for sub_category in sub_categories:
					sub_category_name = sub_category['name']
					print(f"sub category: {sub_category_name}")

					sub_sub_categories = sub_category.get('subcategories', False)
					if sub_sub_categories:
						sub_sub_category_found_count = len(sub_sub_categories)
						print(f"Found {sub_sub_category_found_count} sub categories to process...")
						for sub_sub_category in sub_category['subcategories']:
							sub_sub_category_name = sub_sub_category['name']
							print(f"sub sub category: {sub_sub_category_name}")
							if loop_counter < test_categories:
								loop_counter += 1

								url = self.get_category_url(sub_sub_category)
								print(f"Url: {url}")
								detail_urls, html = self.get_category_page(url, category_name, sub_category_name,
								                                           sub_sub_category_name)
								all_urls.extend(detail_urls)
							time.sleep(2)
					else:
						url = self.get_category_url(sub_category)
						print(f"Url: {url}")

						detail_urls, html = self.get_category_page(url, category_name, sub_category_name, '')
						all_urls.extend(detail_urls)
			else:
				url = self.get_category_url(category)
				print(f"Url: {url}")

				detail_urls, html = self.get_category_page(url, category_name, "", '')
				all_urls.extend(detail_urls)

		# html_table_to_csv(html_table)
		html += f"<h2>Total products found: {total_products}</h2>"

		print(f"Total products found: {len(all_urls)}")
		return html

	# Step Three: Process the product links
	def process_products_from_csv(self):
		"""
		Read product URLs from a CSV file, process each product, and save results to a CSV file.
		Updates progress in cache for real-time tracking.

		Calls get_product_details
		"""

		# Generate a unique task ID for this processing run
		task_id = self.current_task_id
		logging.info(f"process_products_from_csv() - Task ID: {task_id}")
		# task_id = str(uuid.uuid4())
		# self.current_task_id = task_id  # Store task ID on the instance for the view to access
		self.scraping_setup()
		print(f"process_products_from_csv() - Task ID: {task_id}")
		# print(self.options)

		start_row = self.options.get('csv_start_row', 0)
		test_products = self.options.get('test_products', 0)
		home_dir = self.options.get('home_directory', '')

		# Initialize progress tracking
		progress_data = {
			'status': 'processing',
			'current': 0,
			'total': 0,
			'processed': 0,
			'errors': 0,
			'current_product': '',
			'output_file': '',
			'task_id': task_id,
			'percent': 0
		}

		def update_progress():
			"""Helper function to update progress in cache"""
			print(f"Updating progress for task {task_id}: {progress_data}")
			cache.set(f'product_processing_progress_{task_id}', progress_data, timeout=3600)  # 1 hour timeout

		try:
			input_file = self.get_url_file_path(home_dir)
			output_file = self.get_data_file_path(home_dir)
			progress_data['output_file'] = output_file

			if not os.path.exists(input_file):
				error_msg = f"Error: File {input_file} not found"
				print(error_msg)
				progress_data.update({
					'status': 'error',
					'error': error_msg
				})
				update_progress()
				return f"Error: File {input_file} not found"

			# Define output CSV file
			output_filename = output_file
			file_exists = os.path.exists(output_filename)
			print(f"Output file exists: {file_exists}")

			# First count total rows for progress tracking
			with open(input_file, 'r', encoding='utf-8') as csvfile:
				reader = csv.DictReader(csvfile)
				total_rows = sum(1 for _ in reader)
				progress_data['total'] = total_rows
				print(f"Total rows: {total_rows}")
				update_progress()

			# Now process the file
			with open(input_file, 'r', encoding='utf-8') as csvfile:
				reader = csv.DictReader(csvfile)

				# Skip to start_row
				for _ in range(start_row):
					next(reader, None)

				for row_num, row in enumerate(reader, start=start_row):
					row_spec = self.PRODUCT_DATA_SPEC.copy()
					try:
						url = row.get('URL', '')
						if not url:
							continue

						current_product = f"Row {row_num + 1}/{total_rows}"
						if (row_num + 1) < (start_row + test_products):
							print(f"\nProcessing {current_product} - {url}")
							progress_data.update({
								'current': row_num + 1,
								'current_product': current_product,
								'status': 'processing',
								'percent': trunc(((row_num + 1) / progress_data['total']) * 100)
							})
							update_progress()

							sub_subcategory = ''
							if hasattr(row, 'Sub Subcategory'):
								sub_subcategory = row['Sub Subcategory']
							print(row)

							# Process the product
							row_spec.update({
								'subcategory': row.get('Subcategory', ''),
								'timestamp': row.get('Timestamp', ''),
								'content_url': url,
								'sku': row.get('SKU', ''),
								'category': row.get('Category', ''),
								'subsubcategory': row.get('Sub Subcategory', ''),
							})
							print(row_spec)

							# Call the product processing function
							row_spec = self.get_product_details(url, row_spec)
							if isinstance(row_spec, list):
								print("Found a list")
								for spec in row_spec:
									product_name = spec.get('name', 'Unknown Product')
									print(f"Saving product {product_name} to {output_filename}")
									self.write_product_to_csv(spec, output_filename)
									print(f"Saved product {product_name} to {output_filename}")
							else:
								# Write to CSV
								product_name = row_spec.get('name', 'Unknown Product')
								print(f"Saving product {product_name} to {output_filename}")
								self.write_product_to_csv(row_spec, output_filename)
								print(f"Saved product {product_name} to {output_filename}")

							# Update progress
							progress_data['processed'] += 1
							update_progress()

							# Add a small delay to prevent overwhelming the system
							# time.sleep(0.1)

					except Exception as e:
						error_msg = f"Error processing row {row_num + 1}: {str(e)}"
						print(error_msg)
						progress_data['errors'] = progress_data.get('errors', 0) + 1
						progress_data['last_error'] = error_msg
						update_progress()
						continue

			# Processing complete
			completion_msg = f"Processing complete. Processed {progress_data['processed']} products. "
			completion_msg += f"Errors: {progress_data['errors']}. "
			completion_msg += f"Results saved to {output_filename}"

			progress_data.update({
				'status': 'completed',
				'message': completion_msg
			})
			update_progress()

			print(completion_msg)
			return f"<p>{completion_msg}</p>"

		except Exception as e:
			error_msg = f"Unexpected error in process_products_from_csv: {str(e)}"
			print(error_msg)
			progress_data.update({
				'status': 'error',
				'error': error_msg
			})
			update_progress()
			return f"<p class='error'>{error_msg}</p>"

	# Step Four: Process any missing rows due to products failed to load or step 3 eneded early
	def process_missing_skus(self, url_file=URL_OUTPUT_FILE, data_file=DATA_OUTPUT_FILE,
		                         home_dir=DEFAULT_DIRECTORY):
		"""
		Process SKUs that are in the URL file but not in the data file.
		Reports progress through the task's progress tracking.
		"""
		print("Starting process_missing_skus()")
		task_id = self.current_task_id
		logging.info(f"process_missing_skus() - Task ID: {task_id}")
		if not task_id:
			return "Error: Task ID not provided"

		# Initialize progress
		progress = {
			'status': 'running',
			'current': 0,
			'total': 0,
			'current_sku': '',
			'processed_skus': [],
			'not_found_skus': [],
			'message': 'Initializing...',
            'percent': 0
		}
		
		# Update progress in cache
		cache.set(f'product_processing_progress_{task_id}', progress, timeout=3600)

		try:
			# Get file paths
			url_file = self.get_file_path(self.options.get('url_output_file', url_file), 
                                       self.options.get('home_directory', home_dir))
			data_file = self.get_file_path(self.options.get('data_output_file', data_file), 
                                        self.options.get('home_directory', home_dir))
			
			# Read existing data to check which SKUs we already have
			existing_skus = self.get_unique_keys(data_file)
			
			# Read URL file to get URL for each SKU
			missing_skus = []
			sku_url_map = {}
			
			if os.path.exists(url_file):
				with open(url_file, 'r', newline='', encoding='utf-8') as f:
					reader = csv.DictReader(f)
					if 'SKU' in reader.fieldnames and 'URL' in reader.fieldnames:
						for row in reader:
							sku = row['SKU']
							if sku not in existing_skus:
								missing_skus.append(sku)
								sku_url_map[sku] = row
			
			progress['total'] = len(missing_skus)
			progress['message'] = f'Found {progress["total"]} missing SKUs to process'
			cache.set(f'product_processing_progress_{task_id}', progress, timeout=3600)
			
			# Process missing SKUs
			for i, sku in enumerate(missing_skus, 1):
				# Check if task was cancelled
				if cache.get(f'task_cancelled_{task_id}'):
					progress['status'] = 'cancelled'
					progress['message'] = 'Processing was cancelled by user'
					cache.set(f'product_processing_progress_{task_id}', progress, timeout=3600)
					return "Processing cancelled"
				
				try:
					row = sku_url_map[sku]
					progress['current'] = i
					progress['current_sku'] = sku
					progress['message'] = f'Processing SKU: {sku} ({i} of {progress["total"]})'
					cache.set(f'product_processing_progress_{task_id}', progress, timeout=3600)
					
					# Process the product
					row_spec = self.get_product_spec()
					row_spec['subcategory'] = row.get('Subcategory', '')
					row_spec['timestamp'] = row.get('Timestamp', '')
					row_spec['content_url'] = row['URL']
					row_spec['sku'] = sku
					row_spec['category'] = row.get('Category', '')
					
					# Get product details
					row_spec = self.get_product_details(row['URL'], row_spec)
					
					# Write to CSV
					self.write_product_to_csv(row_spec, data_file)
					
					progress['processed_skus'].append(sku)
					progress['percent'] = trunc((i / progress['total']) * 100)
					progress['message'] = f'Successfully processed SKU: {sku}'
					
				except Exception as e:
					error_msg = f"Error processing SKU {sku}: {str(e)}"
					print(error_msg)
					progress['not_found_skus'].append(sku)
					progress['message'] = f'Error processing SKU {sku}: {str(e)[:100]}...'
				
				# Update progress
				cache.set(f'product_processing_progress_{task_id}', progress, timeout=3600)
			
			# Final status
			progress['status'] = 'completed'
			progress['message'] = (
				f'Processing complete. Success: {len(progress["processed_skus"])}, '
				f'Failed: {len(progress["not_found_skus"])}'
			)
			cache.set(f'product_processing_progress_{task_id}', progress, timeout=3600)
			
			return progress['message']
			
		except Exception as e:
			error_msg = f"Error in process_missing_skus: {str(e)}"
			print(error_msg)
			progress['status'] = 'error'
			progress['message'] = error_msg
			cache.set(f'product_processing_progress_{task_id}', progress, timeout=3600)
			return error_msg

	# Use the data stored in extra data to reprocess a file without having to visit the page again
	def process_extra_data_from_csv(self):
		"""
		Process extra data from a CSV file by reading the extra_data column and passing it to get_product_data.

		The CSV file should have at least these columns: 'sku' and 'extra_data_1'.
		The method will update the product data using the extra data.

		Calls: get_product_data
		Calls: get_more_extra_data
		"""
		try:
			# Get file paths from options with fallbacks
			input_file = self.options.get('data_output_file', self.DATA_OUTPUT_FILE)
			output_file = f"processed_{input_file}"
			home_dir = self.options.get('home_directory', self.DEFAULT_DIRECTORY)

			input_path = self.get_file_path(input_file, home_dir)
			output_path = self.get_file_path(output_file, home_dir)

			if not os.path.exists(input_path):
				return f"Error: Input file not found: {input_path}"

			# Open input and output files
			with open(input_path, 'r', newline='', encoding='utf-8') as infile, \
					open(output_path, 'w', newline='', encoding='utf-8') as outfile:

				reader = csv.DictReader(infile)
				fieldnames = reader.fieldnames

				# Ensure required fields exist
				if 'extra_data_1' not in fieldnames or 'sku' not in fieldnames:
					return "Error: Input CSV must contain 'sku' and 'extra_data_1' columns"

				writer = csv.DictWriter(outfile, fieldnames=fieldnames)
				writer.writeheader()

				processed_count = 0
				count = 0
				for row in reader:
					count += 1

					# if not row.get('extra_data_1'):
					# 	# Skip rows without extra data
					# 	writer.writerow(row)
					# 	continue

					try:
						# Create a copy of the row to avoid modifying the original
						row_spec = row.copy()

						# Parse the extra data (assuming it's a JSON string)
						# First check if it's already a dict (from previous processing)
						if row.get('extra_data_1'):
							extra_data = row['extra_data_1']
							if isinstance(extra_data, str):
								try:
									extra_data = json.loads(extra_data)
								except json.JSONDecodeError:
									# If it's not valid JSON, keep it as is
									print(f"⛔️⛔️⛔️Error getting JSON in extra_data_1 for SKU {row.get('sku', 'unknown')}: {e}")
									pass

							# Process the product with extra data
							row_spec = self.get_product_data(extra_data, row_spec)

						# Process any additional data
						print("Get more data")
						row_spec = self.get_more_extra_data(row_spec)

						# Write the updated row to the output file
						writer.writerow(row_spec)
						processed_count += 1

					except json.JSONDecodeError as e:
						print(f"⛔️⛔️⛔️Error parsing JSON in extra_data_1 for SKU {row.get('sku', 'unknown')}: {e}")
						# Write the original row if there's an error
						writer.writerow(row)
					except Exception as e:
						print(f"⛔️⛔️⛔️Error processing row with SKU {row.get('sku', 'unknown')}: {e}")
						writer.writerow(row)

					print(f"******* Processing row {count} successful rows {processed_count}")

			return f"Successfully processed {processed_count} products. Results saved to {output_path}"

		except Exception as e:
			return f"⛔️⛔️⛔️Error in process_extra_data_from_csv: {str(e)}"

	def remove_duplicate_skus(self, input_file=None, output_file=None, home_dir=DEFAULT_DIRECTORY):
		"""
		Remove duplicate rows from a CSV file based on the SKU column.

		Args:
			input_file (str): Path to the input CSV file
			output_file (str, optional): Path to save the deduplicated CSV. If None, will append '_deduped' to input filename.
		    home_dir (str): Home directory for relative paths

		Returns:
			str: Path to the output file with duplicates removed
		"""
		print("Starting remove_duplicate_skus")
		print(self.options)
		input_file = self.options.get('url_output_file')
		home_dir = self.options.get('home_directory')
		input_file = self.get_file_path(input_file, home_dir)

		if output_file is None:
			file_parts = os.path.splitext(input_file)
			output_file = f"{file_parts[0]}_deduped{file_parts[1]}"
		else:
			output_file = self.get_file_path(output_file, home_dir)

		# Dictionary to store unique rows by SKU
		unique_rows = OrderedDict()
		total_rows = 0
		duplicates_removed = 0
		sample_sku = ''
		try:
			# Read the input file
			with open(input_file, 'r', newline='', encoding='utf-8') as infile:
				reader = csv.DictReader(infile)
				fieldnames = reader.fieldnames
				sku_field = 'SKU'
				# Check if 'SKU' or 'sku' column exists
				if 'SKU' not in fieldnames:
					sku_field = 'sku'
					csv.field_size_limit(sys.maxsize)
					if 'sku' not in fieldnames:
						raise ValueError("Input file must contain an 'SKU' column")
				found = False

				# Process each row
				for row in reader:
					total_rows += 1
					print(f"Rows {total_rows}")
					sku = row[sku_field]
					# Keep the first occurrence of each SKU
					if sku not in unique_rows:
						unique_rows[sku] = row
					else:
						if not found:
							print(f"Duplicate SKU found at line : {total_rows}")
							print(f"SKU was : {sku}")
							sample_sku = sku
							found = True
			print("Lets Try 4")
			# Count duplicates
			duplicates_removed = total_rows - len(unique_rows)
			print(f"Found {duplicates_removed} duplicates")
			# Write the deduplicated rows to the output file
			with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
				writer = csv.DictWriter(outfile, fieldnames=fieldnames)
				writer.writeheader()
				writer.writerows(unique_rows.values())

			print(f"Processed {total_rows} rows")
			print(f"Removed {duplicates_removed} duplicate SKUs")
			print(f"Saved {len(unique_rows)} unique rows to {output_file}")
			html = f"<p>Processed {total_rows} rows</p>"
			html += f"<p>Removed {duplicates_removed} duplicate SKUs</p>"
			html += f"<p>Example Duplicate SKU: {sample_sku}</p><p>Removed</p>"
			html += f"<p>Saved {len(unique_rows)} unique rows to {output_file}</p>"
			return html

		except FileNotFoundError:
			print(f"⛔️⛔️⛔️Error: Input file '{input_file}' not found")
			return None
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing file: {e}")
			return None

	def count_csv_rows(self, directory='./Product_URLS_999_Max'):
		"""
		Counts the number of rows in all CSV files in the specified directory.

		Args:
			directory (str): Path to the directory containing CSV files. Defaults to current directory.
			home_dir (str): Home directory for relative paths

		Returns:
			str: HTML formatted string with the results
		"""
		directory_path = self.options.get('home_directory', '')
		# Resolve directory path
		directory = self.get_file_path(directory_path)
		# Dictionary to store file counts
		file_counts = {}
		data_rows = url_rows = total_rows = 0

		# Get all CSV files in the directory
		csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

		if not csv_files:
			return "<p>No CSV files found in the directory.</p>"
		csv.field_size_limit(sys.maxsize)

		# Count rows in each CSV file
		for filename in csv_files:
			filepath = os.path.join(directory, filename)
			try:
				with open(filepath, 'r', encoding='utf-8') as file:
					# Count rows (excluding header)
					row_count = sum(1 for row in csv.reader(file)) - 1
					print(f"Processed {row_count} rows in {filename}")
					file_counts[filename] = row_count
					total_rows += row_count
					if 'data' in filename:
						data_rows += row_count
					elif 'url' in filename:
						url_rows += row_count
			except Exception as e:
				print(f"⛔️⛔️⛔️Error processing {filename}: {e}")
				file_counts[filename] = f"Error: {str(e)}"

		# Generate HTML output
		html = "<h3>CSV File Row Counts:</h3>"
		html += "<table class='table table-striped'><thead><tr><th>File</th><th>Rows</th></tr></thead><tbody>"

		# Sort files by name for consistent output
		for filename in sorted(file_counts.keys()):
			row_count = file_counts[filename]
			html += f"<tr><td>{filename}</td><td>{row_count}</td></tr>"

		html += f"<tr><td><strong>URL Rows</strong></td><td><strong>{url_rows}</strong></td></tr>"
		html += f"<tr><td><strong>Data Rows</strong></td><td><strong>{data_rows}</strong></td></tr>"
		html += f"<tr><td><strong>Total Rows</strong></td><td><strong>{total_rows}</strong></td></tr>"
		html += "</tbody></table>"

		return html

	# ************************************************************************
	# Functions for getting product lists
	# ************************************************************************
	def get_category_page(self, url, category_name, sub_category_name, sub_sub_category_name):
		"""Load a category page, handle all paging and return a list of product urls"""
		raise NotImplementedError("get_category_page method not implemented")

	def get_products_from_html(self):
		"""Scrape products from the website"""
		raise NotImplementedError("get_products_from_html method not implemented")

	def get_products_from_json_in_html(self):
		"""Scrape products from json returned in the htnml response"""
		raise NotImplementedError("get_products_from_json_in_html method not implemented")

	def get_products_from_json(self):
		"""Scrape products from an api request"""
		raise NotImplementedError("get_products_from_json method not implemented")

	# ************************************************************************
	# Functions for extracting product data
	# ************************************************************************
	def get_more_extra_data(self, row_spec):
		return row_spec

	def get_product_data(self, data, row_spec):
		"""Process products from a CSV file"""
		"""
		Each class should implement this method to define how to process the product data
		This can be called from the process_products_from_csv method and 
		from process_extra_data_from_csv
		"""
		raise NotImplementedError("get_product_data method not implemented")

	def parse_product_schema(self, data, row_spec):
		print("parse_product_schema()")
		"""Parse product schema"""
		# print(row_spec)
		for key, value in row_spec.items():
			# print(key)
			if key in data:
				value = data[key]
				if value:
					# print(f"key: {key}, value: {value}")
					row_spec[key] = value
		print("parse_product_schema complete")
		return row_spec

	def get_product_details(self, url, row_spec=None):
		"""Process a product single product. This could be from an api call or by scraping the website"""
		"""
		This method gets the product data from the page or the api
		"""
		raise NotImplementedError("process_product method not implemented")


	def get_product_detail_from_html(self, url, row_spec=None):
		"""Scrape products from the website"""
		raise NotImplementedError("get_products_from_html method not implemented")

	def get_product_detail_from_json_in_html(self, url, row_spec=None, target="script[type='application/json']"):
		"""Scrape products from json returned in the htnml response"""
		raise NotImplementedError("get_product_detail_from_json_in_html method not implemented")

	def get_product_detail_from_json(self, row_spec=None):
		"""Scrape products from an api request"""
		raise NotImplementedError("get_products_from_json method not implemented")

	@staticmethod
	def process_json_product(script):
		"""
		Allow a scraper to modify the product schema data prior to processing
		"""
		return script

	def get_product_detail_from_schema_in_html(self, row_spec=None, target="application/ld+json'"):
		"""
		Cycles through the target script tag to find product schema and product group schema

		Args:
			url (str): Url to search
			row_spec (array): data to write to csv
			target (str): Home directory for relative paths

		Returns:
			str: HTML formatted string with the results
		"""
		#  Wait for the product name element on the product page detail page
		print("Scraper.get_product_detail_from_schema_in_html()")
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print(f"processing product detail page for target {target}")
		# print(f"Loading page...{url}")

		data = ''
		sku = row_spec['sku']
		# request_filter = url

		# self.driver.get(url)
		print(f"Sent Request")
		script_data = ''
		product_data = ''
		product_group_data = ''
		try:

			# Get the page source and parse it with BeautifulSoup
			soup = BeautifulSoup(self.driver.page_source, 'html.parser')
			print(f"Script Loaded")
			scripts = soup.find_all('script', {'type': target})
			for script in scripts:
				print(script.string)
				if script and script.string:
					body = self.process_json_product(script.string)
					body = urllib.parse.unquote(body)
					print("Loading product data")
					try:
						# Try to parse the JSON directly first
						script_data = json.loads(body, strict=False)
					except json.JSONDecodeError as e:
						print(f"Initial JSON parse failed, attempting to clean and retry: {str(e)}")
						try:
							# Clean the JSON string and try again
							cleaned_body = self.clean_json_string(body)
							script_data = json.loads(cleaned_body)
						except json.JSONDecodeError as e2:
							print(f"❌ Failed to parse JSON even after cleaning: {str(e2)}")
							print(f"Problematic JSON (first 500 chars): {cleaned_body[:500]}")
					try:
						if script_data.get('@type') == "Product":
							print("Found Product Schema")
							product_data = script_data
						if script_data.get('@type') == "ProductGroup":
							print("Found Group Schema")
							product_group_data = script_data
					except Exception as e:
						print(f"Error getting product data: {type(e)}")

				else:
					print("Could not find the product data script tag")

		except Exception as e:
			print(f"Error getting product details: {e}")
		# finally:
		# 	del self.driver.requests

		return product_data, product_group_data

	def update_csv_columns(self):
		"""
		Update all CSV files in DEFAULT_DIRECTORY to include any missing columns from PRODUCT_DATA_SPEC.
		Columns will be added in the same order as they appear in PRODUCT_DATA_SPEC.
		"""
		directory = self.options.get('home_directory', self.DEFAULT_DIRECTORY)

		# Get all CSV files in the directory
		csv_files = [f for f in os.listdir(directory) if f.endswith('.csv') and '_data' in f]

		if not csv_files:
			print(f"No CSV files found in {directory}")
			return

		for filename in csv_files:
			self._process_csv_file(directory, filename)

		return f"Successfully processed {len(csv_files)} Files."

	def _process_csv_file(self, directory, filename):
		"""Process a single CSV file to add missing columns and remove columns without headers."""
		filepath = os.path.join(directory, filename)
		temp_file = f"{filepath}.tmp"

		try:
			# Read the existing CSV
			with open(filepath, 'r', newline='', encoding='utf-8') as f:
				reader = csv.DictReader(f)
				fieldnames = reader.fieldnames or []
				rows = list(reader)

			# Remove any columns that don't have a header
			if fieldnames:
				# Filter out None or empty string headers
				valid_headers = [str(h) for h in fieldnames if h is not None and str(h).strip()]
				if len(valid_headers) < len(fieldnames):
					print(
						f"Removing {len(fieldnames) - len(valid_headers)} columns without valid headers from {filename}")
					# Update rows to only include valid columns
					rows = [{k: v for k, v in row.items() if k in valid_headers} for row in rows]
					fieldnames = valid_headers

			# Get all expected columns from PRODUCT_DATA_SPEC
			expected_columns = list(self.PRODUCT_DATA_SPEC.keys())
			print(f"Expected columns: {expected_columns}")
			# Find missing columns that need to be added
			missing_columns = [col for col in expected_columns if col not in fieldnames]

			if not missing_columns:
				print(f"No missing columns in {filename}")
				return

			print(f"Updating {filename}: Adding missing columns: {', '.join(missing_columns)}")

			# Add missing columns to fieldnames in the correct order
			updated_fieldnames = fieldnames + missing_columns

			# Write the updated data back to the file
			with open(temp_file, 'w', newline='', encoding='utf-8') as f:
				writer = csv.DictWriter(f, fieldnames=expected_columns)
				writer.writeheader()

				# Write each row with the new columns, ensuring all fieldnames are present
				for row in rows:
					# Create a new row with all expected fields
					new_row = {k: row.get(k, '') for k in expected_columns}
					writer.writerow(new_row)

			# Replace the original file with the updated one
			os.replace(temp_file, filepath)
			print(f"Successfully updated {filename}")

		except Exception as e:
			print(f"Error processing {filename}: {str(e)}")
			# Clean up temp file if it exists
			if os.path.exists(temp_file):
				os.remove(temp_file)

	def scan_files(self):
		from .parse import scan_distributor_files
		directory = self.options.get('home_directory', self.DEFAULT_DIRECTORY)
		result, html = scan_distributor_files(directory, self.PRODUCT_DATA_SPEC)
		return html

	def update_product_count(self, data_count, url_count):
		"""
		Update the product count by making a POST request to the distributor's API.

		Args:
			data_count: Number of products to report
			url_count: Number of products to report

		Returns:
			bool: True if update was successful, False otherwise
		"""
		print("update_product_count()")
		print(f"data_count {data_count} url_count {url_count}")
		if not hasattr(self, 'CRM_NOTE_ID'):
			print("⚠️ CRM_NOTE_ID not defined, skipping product count update")
			return False

		if url_count == 0 and data_count > 0:
			url_count = data_count

		if hasattr(self, "CRM_STATUS_OVERRIDE") and self.CRM_STATUS_OVERRIDE:
			status = self.CRM_STATUS_OVERRIDE
			scraped = 1
		else:
			if url_count == data_count:
				status = "Completed"
				scraped = 1
			else:
				if url_count > 0:
					status = "In Progress"
					scraped = 0
				else:
					status = ''
					scraped = 0
		print(f"status: {status}")

		if hasattr(self, "CRM_PRICE_TYPE"):
			price_type = self.CRM_PRICE_TYPE
		else:
			price_type = ''

		url = f"https://distributors.snappersworld.com/api/notes/{self.CRM_NOTE_ID}/update_products/"
		headers = {
			'Content-Type': 'application/json',
			# 'Authorization': f'Token {settings.DISTRIBUTOR_API_KEY}'  # Make sure to set this in your settings
		}

		data = {
			"products": str(data_count),
			"suggested_products": str(url_count),
			"status": str(status),
			"price_type": str(price_type),
			"scraped": str(scraped),
			"extra_data": 1,
		}
		print(f"Sending Request {data}")
		try:
			response = requests.post(
				url,
				headers=headers,
				json=data,
				timeout=10
			)

			if response.status_code == 200:
				print(f"✅ Successfully updated product count to {data_count}")
				return True
			else:
				print(f"⚠️ Failed to update product count. Status code: {response.status_code}")
				print(f"Response: {response.text}")
				return False

		except requests.exceptions.RequestException as e:
			print(f"⚠️ Error updating product count: {str(e)}")
			return False

	def update_crm_note(self, crm_note_id, note_content):
		"""
		Update a CRM note with the given content via API.

		Args:
			crm_note_id (int): The ID of the CRM note to update
			note_content (str): The content to update the note with

		Returns:
			bool: True if the update was successful, False otherwise
		"""
		print("update_crm_note{}")
		try:
			# Get the CRM base URL from the class or use a default
			crm_base_url = getattr(self, 'CRM_BASE_URL', 'http://127.0.0.1:8083')
			update_url = f"{crm_base_url}/api/notes/{crm_note_id}/update_sku/"
			# update_url = f"http://127.0.0.1:8083/api/notes/{self.CRM_NOTE_ID}/update_sku/"
			print(f"update_url {update_url}")
			# Get the CSRF token from the session
			csrf_token = getattr(self, 'csrf_token', '')

			headers = {
				'Content-Type': 'application/json',
				'X-CSRFToken': csrf_token,
				'Referer': f'{crm_base_url}/'
			}

			data = {
				'leading_zero_skus': note_content,
				'is_public': True
			}

			response = requests.post(
				update_url,
				json=data,
				headers=headers,
				cookies={'csrftoken': csrf_token}
			)

			if response.status_code == 200:
				print(f"✅ Successfully updated CRM note {crm_note_id}")
				return True
			else:
				print(f"❌ Failed to update CRM note {crm_note_id}. Status code: {response.status_code}")
				print(f"Response: {response.text}")
				return False

		except Exception as e:
			print(f"❌ Error updating CRM note {crm_note_id}: {str(e)}")
			return False



	# ************************************************************************
	# Core Functions
	# These are overrides of the core functions
	# ************************************************************************

	# ************************************************************************
	# Core Function Hooks
	# These are the methods called by the core functions
	# ************************************************************************

	# ************************************************************************
	# Category URL retrieval Functions
	# ************************************************************************

	# ************************************************************************
	# Product List Functions
	# ************************************************************************

	# ************************************************************************
	# Product Detail Functions
	# ************************************************************************
