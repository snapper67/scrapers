import csv
import json
import logging
import re
import requests
import time
import string

from bs4 import BeautifulSoup
from pathlib import Path
import seleniumwire.undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumwire import webdriver as seleniumwire_webdriver
from seleniumwire.utils import decode

from urllib.parse import urlparse, parse_qs, urlunparse
from io import StringIO
import csv
import os
from collections import OrderedDict
import sys
import glob
import pandas as pd

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
	# Class variables for default values
	PRODUCT_DATA_SPEC = {}

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

	# Import specification
	IMPORT_SPEC = [
		'name', 'sku', 'gtin', 'image', 'pack', 'size', 'retail_price', 'ordering_unit',
		'is_catch_weight', 'is_broken_case', 'average_case_weight', 'brand', 'taxonomy',
		'level_1', 'level_2', 'level_3', 'manufacturer_name', 'manufacturer_sku',
		'distributor_name', 'content_url', 'description', 'unit_price', 'extra_data_1', 'extra_data_2'
	]

	# Default options
	DEFAULT_OPTIONS = {
		'scrape_products': False,
		'process_csv': False,
		'reprocess_csv': False,
		'dedupe_csv': False,
		'count_csv': False,
		'test_products': TEST_PRODUCTS,
		'max_products': 999,
		'csv_start_row': CSV_START_ROW,
		'category_to_process': 0,
		'test_categories': 100,
		'chosen_category': '10001',  # Default to Meat
		'url_output_file': URL_OUTPUT_FILE,
		'data_output_file': DATA_OUTPUT_FILE,
		'home_directory': DEFAULT_DIRECTORY
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
		'count_csv': False,
		'chosen_category': '',
		'url_output_file': URL_OUTPUT_FILE,
		'data_output_file': DATA_OUTPUT_FILE,
		'category_name': '',
		'category_to_process': 0,
		'home_dir': ''
	}

	def __init__(self, options=None):
		"""Initialize the scraper with options"""
		# Update default options with any provided options
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		# self.options['home_directory'] = self.DEFAULT_DIRECTORY
		# Initialize Chrome options
		self.chrome_options = uc.ChromeOptions()
		# Uncomment for headless mode
		self.chrome_options.add_argument('--headless')
		self.chrome_options.add_argument('--disable-gpu')
		self.chrome_options.add_argument('--no-sandbox')
		prefs = {"profile.managed_default_content_settings.images": 2}  # 2 blocks images
		self.chrome_options.add_experimental_option("prefs", prefs)

		# Selenium Wire options
		self.seleniumwire_options = {
			'disable_encoding': True,
		}
		self.current_task_id = None
		logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(threadName)s - %(message)s')

		# seleniumwire_options = {
		# 		'request_filter': lambda request: 'product-domain-api/v2/products' in request.url,
		# 		'disable_encoding': True,
		# 	}

		# Initialize WebDriver
		self.driver = None
		self.wait = None

	def __enter__(self):
		"""Context manager entry"""
		self.setup_driver()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""Context manager exit - ensure driver is closed"""
		self.cleanup()

	def get_product_spec(self):
		return self.PRODUCT_DATA_SPEC.copy()

	def setup_driver(self):
		"""Initialize the WebDriver"""
		if not self.driver:
			# Get the directory where the current script is located
			script_dir = os.path.dirname(os.path.abspath(__file__))
			# Build the path to chromedriver in the chrome-mac-arm64 directory
			chromedriver_path = os.path.join(script_dir, 'chrome-mac-arm64', 'chromedriver')
			service = Service(chromedriver_path)
			self.driver = seleniumwire_webdriver.Chrome(
				service=service,
				options=self.chrome_options,
				seleniumwire_options=self.seleniumwire_options
			)
		self.driver.command_executor.set_timeout(1000)
		self.wait = WebDriverWait(self.driver, 60)

	def cleanup(self):
		"""Clean up resources"""
		if self.driver:
			self.driver.quit()
			self.driver = None

	def set_options(self, options):
		"""
		Set options for the scraper

		Args:
			options (dict): Dictionary of options
		"""
		self.options = {**self.options, **options}

	def get_options(self):
		return self.options

	def save_urls_to_csv(self ,urls, category_name="", subcategory_name=""):
		"""
		Save a list of URLs to a CSV file. If the file exists, it will append to it.

		Args:
			urls (list): List of URLs to save
			category_name (str): Name of the category
			subcategory_name (str): Name of the sub category
		"""
		import csv
		import os
		from datetime import datetime

		print(f"save_urls_to_csv()")
		# print(f"save_urls_to_csv(){urls}")

		# Resolve the file path
		home_dir = self.options.get('home_directory')
		filename = self.get_url_file_path(home_dir)

		# Ensure the directory exists
		os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)

		file_exists = os.path.isfile(filename)

		try:
			with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
				writer = csv.writer(csvfile)

				# Write header only if file is new
				if not file_exists:
					writer.writerow(['SKU', 'URL', 'Timestamp', 'Category', 'Subcategory'])

				# Write each URL with timestamp
				for url in urls:
					clean_url = url.rstrip('/')
					sku = clean_url.split('/')[-1].split('?')[0]  # Remove any query parameters
					writer.writerow(
						[sku, url, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), category_name, subcategory_name])

			mode = "Appended to" if file_exists else "Created new"
			print(f"Successfully {mode} {len(urls)} URLs to {filename}")

		except Exception as e:
			print(f"⛔️⛔️⛔️Error saving URLs to CSV: {e}")

	def print_element(self, element):
		print(f"Text: {element.text}")
		print(f"Tag Name: {element.tag_name}")
		print(f"Class Attribute: {element.get_attribute('class')}")
		print(f"Outer HTML: {element.get_attribute('outerHTML')}")
		print(f"Location: {element.location}")
		print(f"Size: {element.size}")
		print(f"Is Displayed: {element.is_displayed()}")

	# ************************************************************************

	# 	Product Scraping Functions
	# ************************************************************************

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

	def make_filename_safe(self, s):
		valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
		cleaned_filename = ''.join(c for c in s if c in valid_chars)
		cleaned_filename = cleaned_filename.replace(' ', '_')  # Replace spaces with underscores
		return cleaned_filename

	def get_url_file_path(self, home_dir=DEFAULT_DIRECTORY, input_file=None):
		if not input_file:
			input_file = self.options.get('url_output_file', '')
		return self.get_file_path(input_file, home_dir)

	def get_data_file_path(self, home_dir=DEFAULT_DIRECTORY, input_file=None):
		print("get_data_file_path")
		if not input_file:
			input_file = self.options.get('data_output_file', '')
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
			home_dir (str): Home directory for relative paths

		Returns:
			bool: True if successful, False otherwise
		"""
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
		else:
			return "No action specified. Please select an option."

	def build_products_list(self):
		"""Scrape products from the website"""
		raise NotImplementedError("scrape_products method not implemented")

	def build_categories_list(self):
		"""Scrape products from the website"""
		raise NotImplementedError("build_categories_list method not implemented")

	def scraping_setup(self):
		"""Scrape products from the website"""
		raise NotImplementedError("scraping_setup method not implemented")

	def process_products_from_csv(self):
		"""
		Read product URLs from a CSV file, process each product, and save results to a CSV file.
		Updates progress in cache for real-time tracking.
		"""
		import uuid
		from django.core.cache import cache

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
			'task_id': task_id
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
								'status': 'processing'
							})
							update_progress()

							# Process the product
							row_spec.update({
								'subcategory': row.get('Subcategory', ''),
								'timestamp': row.get('Timestamp', ''),
								'content_url': url,
								'sku': row.get('SKU', ''),
								'category': row.get('Category', '')
							})

							# Call the product processing function
							row_spec = self.get_product_details(url, row_spec)

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

	def process_extra_data_from_csv(self):
		"""
		Process extra data from a CSV file by reading the extra_data column and passing it to get_product_data.

		The CSV file should have at least these columns: 'sku' and 'extra_data_1'.
		The method will update the product data using the extra data.
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

				for row in reader:
					if not row.get('extra_data_1'):
						# Skip rows without extra data
						writer.writerow(row)
						continue

					try:
						# Create a copy of the row to avoid modifying the original
						row_spec = row.copy()

						# Parse the extra data (assuming it's a JSON string)
						# First check if it's already a dict (from previous processing)
						extra_data = row['extra_data_1']
						if isinstance(extra_data, str):
							try:
								extra_data = json.loads(extra_data)
							except json.JSONDecodeError:
								# If it's not valid JSON, keep it as is
								pass

						# Process the product with extra data
						row_spec = self.get_product_data(extra_data, row_spec)

						# Write the updated row to the output file
						writer.writerow(row_spec)
						processed_count += 1

					except json.JSONDecodeError as e:
						print(f"Error parsing JSON in extra_data_1 for SKU {row.get('sku', 'unknown')}: {e}")
						# Write the original row if there's an error
						writer.writerow(row)
					except Exception as e:
						print(f"Error processing row with SKU {row.get('sku', 'unknown')}: {e}")
						writer.writerow(row)

			return f"Successfully processed {processed_count} products. Results saved to {output_path}"

		except Exception as e:
			return f"Error in process_extra_data_from_csv: {str(e)}"
		
	def get_unique_keys(self, data_file):
		keys = set()
		if os.path.exists(data_file):
			with open(data_file, 'r', newline='', encoding='utf-8') as f:
				reader = csv.DictReader(f)
				csv.field_size_limit(sys.maxsize)
				if 'sku' in reader.fieldnames:
					keys = {row['sku'] for row in reader}
		return keys

	def process_missing_skus(self, url_file=URL_OUTPUT_FILE, data_file=DATA_OUTPUT_FILE,
		                         home_dir=DEFAULT_DIRECTORY):

		print("Starting Processing missing SKUs")
		self.scraping_setup()
		print(self.options)
		skus_to_check = self.options.get('skus_to_check', [])
		specified_skus = len(skus_to_check) > 0

		url_file = self.options.get('url_output_file', url_file)
		data_file = self.options.get('data_output_file', url_file)

		url_file = self.get_file_path(url_file, self.options['home_directory'])
		data_file = self.get_file_path(data_file, self.options['home_directory'])
		print(f"url_file: {url_file}")
		print(f"data_file: {data_file}")
		# Read existing data to check which SKUs we already have
		existing_skus = self.get_unique_keys(data_file)

		# Read URL file to get URL for each SKU
		print(f"Existing SKUs: {len(existing_skus)}")
		# Process missing SKUs
		processed_skus = []
		not_found_skus = []

		if os.path.exists(url_file):
			print("Path Exists")
			with open(url_file, 'r', newline='', encoding='utf-8') as f:
				reader = csv.DictReader(f)
				print("Here 2")

				if 'SKU' in reader.fieldnames and 'URL' in reader.fieldnames:
					print("Here 3")
					for row in reader:
						sku = row['SKU']
						print(f"SKU: {sku}")
						if (sku in skus_to_check or not specified_skus) and sku not in existing_skus:
							row_spec = self.get_product_spec()
							try:
								print(f"Processing missing SKU: {sku}")
								# Copy values from import file
								row_spec['subcategory'] = row['Subcategory']
								row_spec['timestamp'] = row['Timestamp']
								row_spec['content_url'] = row['URL']
								row_spec['sku'] = row['SKU']
								row_spec['category'] = row['Category']
								row_spec = self.get_product_details(row['URL'], row_spec)
								processed_skus.append(row['SKU'])

								# Write to CSV
								print(f"Saving product {row_spec['name']} to {data_file}")
								self.write_product_to_csv(row_spec, data_file)
							except Exception as e:
								print(f"⛔️⛔️⛔️Error processing SKU {sku}: {str(e)}")
								not_found_skus.append(sku)

		return f"<div>Processed SKUs{processed_skus}. </div><div>Not found SKUs: {not_found_skus}<div>"

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
				print("Lets Try 4")
				# Process each row
				for row in reader:
					total_rows += 1
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

			# Count duplicates
			duplicates_removed = total_rows - len(unique_rows)

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

	def get_product_data(self, data, row_spec):
		"""Process products from a CSV file"""
		"""
		Each class should implement this method to define how to process the product data
		This can be called from the process_products_from_csv method and 
		from process_extra_data_from_csv
		"""
		raise NotImplementedError("get_product_data method not implemented")

	def get_product_details(self, url, row_spec=None):
		"""Process a product single product. This could be from an api call or by scraping the website"""
		"""
		This method gets the product data from the page or the api
		"""
		raise NotImplementedError("process_product method not implemented")

	def search_requests(self):
		"""
		Load a URL and search the traffic for a search term
		"""
		print("Starting search_requests")
		url = self.options.get('url', '')
		search_term = self.options.get('search_term', '')
		self.driver.get(url)
		time.sleep(10)
		self.driver.get(url)
		time.sleep(10)
		html = "<ul>"
		found = False
		for request in self.driver.requests: # Filter for API requests
			# print(f"URL: {request.url}")
			# print(f"Status Code: {request.response.status_code}")
			# print(f"Content Type: {request.response.headers.get('Content-Type')}")

			# Decode the response body (it's bytes by default)
			try:
				# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
				# body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

				if search_term in str(request.response.body):
					print(f"Request URL: {request.url}")
					# print(f"Response Body (Text): {request.response.body}")
					found = True
					html = html + "<li>" + request.url + "</li>"

			except Exception as e:
				print(f"⛔️Error decoding detail response body: {e}")

		del self.driver.requests
		html = html + "</ul>"
		return html, found


