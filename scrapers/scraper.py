import csv
import json
import re
from datetime import datetime

import requests
import time

from bs4 import BeautifulSoup
from pathlib import Path
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


class Scraper:
	# Class variables for default values
	PRODUCT_DATA_SPEC = {
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
		'content_url': '',
		'description': '',
		'unit_price': '',
		'extra_data_1': '',
		'extra_data_2': '',

		# Fields from US_FOODS_SPEC
		'timestamp': '',
		'pack_size': '',
		'category': '',
		'subcategory': '',
		'classCode': '',
		'classDescription': '',
		'groupCode': '',
		'groupDescription': '',
		'categoryCode': '',
		'categoryDescription': '',
		'standardComparisonUOM': '',
		'standardComparisonValue': '',
		'volume': '',
		'volumeUnits': '',
		'yield': '',
		'yieldUOM': '',
		'countryOfOriginGrownHarvested': '',
		'countryOfOriginProcessed': ''
	}

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

		# Initialize Chrome options
		self.chrome_options = Options()
		# Uncomment for headless mode
		# self.chrome_options.add_argument('--headless')
		self.chrome_options.add_argument('--disable-gpu')
		self.chrome_options.add_argument('--no-sandbox')

		# Selenium Wire options
		self.seleniumwire_options = {
			'disable_encoding': True,
		}

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
		self.wait = WebDriverWait(self.driver, 15)

	def cleanup(self):
		"""Clean up resources"""
		if self.driver:
			self.driver.quit()
			self.driver = None

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

	def set_options(self, options):
		"""
		Set options for the scraper

		Args:
			options (dict): Dictionary of options
		"""
		self.options = {**self.options, **options}

	def get_options(self):
		return self.options

	def count_csv_rows(self, directory='./Product_URLS_999_Max', home_dir=DEFAULT_DIRECTORY):
		"""
		Counts the number of rows in all CSV files in the specified directory.

		Args:
			directory (str): Path to the directory containing CSV files. Defaults to current directory.
			home_dir (str): Home directory for relative paths

		Returns:
			str: HTML formatted string with the results
		"""
		# Resolve directory path
		directory = self.get_file_path(directory, home_dir)
		# Dictionary to store file counts
		file_counts = {}
		total_rows = 0

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

		html += f"<tr><td><strong>Total Rows</strong></td><td><strong>{total_rows}</strong></td></tr>"
		html += "</tbody></table>"

		return html

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

	def write_product_to_csv(self, product_data, filename=DATA_OUTPUT_FILE, home_dir=DEFAULT_DIRECTORY):
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
			product_data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			# Convert all values to strings and handle None values
			row_data = {k: str(v) if v is not None else '' for k, v in product_data.items()}

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
			return False

	def run(self):
		"""
		Main entry point that determines which action to take based on the options
		"""
		if self.options.get('scrape_products'):
			return self.build_products_list()
		elif self.options.get('process_csv'):
			return self.process_products_from_csv()
		elif self.options.get('reprocess_csv'):
			return self.process_missing_skus()
		elif self.options.get('dedupe_csv'):
			return self.remove_duplicate_skus()
		elif self.options.get('count_csv'):
			return self.count_csv_rows()
		else:
			return "No action specified. Please select an option."

	def build_products_list(self):
		"""Scrape products from the website"""
		raise NotImplementedError("scrape_products method not implemented")

	def process_products_from_csv(self):
		"""Process products from a CSV file"""
		raise NotImplementedError("process_products_from_csv method not implemented")

	def process_missing_skus(self, url_file=URL_OUTPUT_FILE, data_file=DATA_OUTPUT_FILE,
		                         home_dir=DEFAULT_DIRECTORY):

		print("Starting Processing missing SKUs")
		print(self.options)
		skus_to_check = self.options.get('skus_to_check', [])

		specified_skus = len(skus_to_check) > 0

		url_file = self.options.get('url_output_file', url_file)
		data_file = self.options.get('data_output_file', url_file)

		url_file = self.get_file_path(url_file, home_dir)
		data_file = self.get_file_path(data_file, home_dir)

		# Read existing data to check which SKUs we already have
		existing_skus = set()
		if os.path.exists(data_file):
			with open(data_file, 'r', newline='', encoding='utf-8') as f:
				reader = csv.DictReader(f)
				csv.field_size_limit(sys.maxsize)
				if 'sku' in reader.fieldnames:
					existing_skus = {row['sku'] for row in reader}

		# Read URL file to get URL for each SKU
		print("Here")
		# Process missing SKUs
		processed_skus = []
		not_found_skus = []

		if os.path.exists(url_file):
			with open(url_file, 'r', newline='', encoding='utf-8') as f:
				reader = csv.DictReader(f)
				print("Here 2")

				if 'SKU' in reader.fieldnames and 'URL' in reader.fieldnames:
					print("Here 3")
					for row in reader:
						sku = row['SKU']
						if (sku in skus_to_check or not specified_skus) and sku not in existing_skus:
							row_spec = self.PRODUCT_DATA_SPEC.copy()
							try:
								print(f"Processing missing SKU: {sku}")
								# Copy values from import file
								row_spec['subcategory'] = row['Subcategory']
								row_spec['timestamp'] = row['Timestamp']
								row_spec['content_url'] = row['URL']
								row_spec['sku'] = row['SKU']
								row_spec['category'] = row['Category']
								row_spec = self.process_product(row['URL'], row_spec)
								processed_skus.append(row['SKU'])

								# Write to CSV
								print(f"Saving product {row_spec['name']} to {data_file}")
								self.write_product_to_csv(row_spec, data_file)
							except Exception as e:
								print(f"⛔️⛔️⛔️Error processing SKU {sku}: {str(e)}")
								not_found_skus.append(sku)

		return processed_skus, not_found_skus

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
		print("Lets Try")
		try:
			# Read the input file
			with open(input_file, 'r', newline='', encoding='utf-8') as infile:
				reader = csv.DictReader(infile)
				print("Lets Try 2")
				fieldnames = reader.fieldnames
				print("Lets Try 3")
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
					print(sku_field)
					sku = row[sku_field]
					print(sku)
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

	def reprocess_products(self):
		"""Reprocess products that failed previously"""
		raise NotImplementedError("reprocess_products method not implemented")

	def process_product(self, url, row_spec=None):
		"""Process a product single product. This could be from an api call or by scraping the website"""
		raise NotImplementedError("process_product method not implemented")

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

		# Resolve the file path
		filename = self.options.get('url_output_file')
		home_dir = self.options.get('home_directory')
		filename = self.get_file_path(filename, home_dir)

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
					sku = url.split('/')[-1].split('?')[0]  # Remove any query parameters
					writer.writerow(
						[sku, url, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), category_name, subcategory_name])

			mode = "Appended to" if file_exists else "Created new"
			print(f"Successfully {mode} {len(urls)} URLs to {filename}")

		except Exception as e:
			print(f"⛔️⛔️⛔️Error saving URLs to CSV: {e}")
