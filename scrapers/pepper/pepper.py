import csv
import json
import sys
from typing import List, Dict, Any, Optional
from urllib.parse import urljoin

import requests
import time
import os

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire.utils import decode

from scrapers.scraper import Scraper

class PepperScraper(Scraper):
	SCRAPER_TYPE = 'Pepper'
	PEPPER_PRODUCT_DATA_SPEC = {
		'external_item_id': '',
	}

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/default'

	INPUT_FILE = ''
	OUTPUT_FILE = ''

	BASE_URL = ''
	BASE_PRODUCT_URL = ''
	VENDOR_NAME = ''

	ONLY_DATA = True

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

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
		'chosen_category': '10001',
		'url_output_file': '',
		'data_output_file': '',
		'home_directory': DEFAULT_DIRECTORY
	}

	def __init__(self, options=None):
		super().__init__(options)
		self.PRODUCT_DATA_SPEC = self.BASE_PRODUCT_DATA_SPEC.copy()
		for spec in self.PEPPER_PRODUCT_DATA_SPEC:
			self.PRODUCT_DATA_SPEC[spec] = ''
		print(self.PRODUCT_DATA_SPEC)

	def get_taxonomy(self):
		"""Load a category page"""
		raise NotImplementedError("get_taxonomy method not implemented")

	def scraping_setup(self):
		"""Scrape products from the website"""
		return

	# ************************************************************************

	# 	Product Scraping Functions
	# ************************************************************************

	def get_product_data(self, data, row_spec):
		print("processing product data from response...")
		# print(data)
		if data:
			try:
				row_spec["name"] = data.get("title", "")
				row_spec["description"] = data.get("description", "")
				row_spec["retail_price"] = data.get("price", "")
				row_spec["shop_id"] = data.get("id", "")
				self.get_pack_size(data, row_spec)
				row_spec["image"] = self.get_first_image_url(data)

				# move sku - which was just a unique identifier to id
				row_spec['id'] = row_spec['sku']
				row_spec['sku'] = data.get('variants', [{}])[0].get('sku', '')

				row_spec["extra_data_1"] = json.dumps(data)

			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing get_product_data Complete...")
		return row_spec

	def get_first_image_url(self, response_data):
		"""
		Extract the first available image URL from the product API response.

		Args:
			response_data (dict): The parsed JSON response from the API

		Returns:
			str: URL of the first available image, or None if no image found
		"""
		try:
			images = response_data.get('images', [])

			# If there are assets, get the first one's URL
			if images and isinstance(images, list) and len(images) > 0:
				# Get the first asset and extract the URL
				first_asset = images[0]
				return "https:" + first_asset

		except Exception as e:
			print(f"Error extracting image from viewModel.assets: {str(e)}")

		return ''

	def get_pack_size(self, data, row_spec):
		print("get_pack_size()")
		try:
			options = data.get('options', None)
			# Find the specification with displayName "Manufacturer Name"
			if options:
				pack_size = next(
					(option for option in options
					 if isinstance(option, dict) and option.get('name') == 'Quantity/Pack:'),
					None
				)

				if pack_size and 'values' in pack_size:
					row_spec['pack_size'] = pack_size['values'][0]
					print(f"Found pack size: {pack_size['values'][0]}")
				else:
					row_spec['pack_size'] = ''
					print("⚠️ pack size name not found in specifications")

		except Exception as e:
			print(f"⛔️ Error processing pack size information: {type(e).__name__} - {str(e)}")

		print("Processing pack size information complete...")
		return row_spec

	# ************************************************************************
	def get_product_details(self, url, row_spec=None):
		"""Get Product Details"""
		raise NotImplementedError("scrape_products method not implemented")

	def get_product_details_json(self, input_file: str = None, output_file: str = None):
		"""
		Parse pepper_data.txt and export products to a CSV file.

		Args:
			input_file (str, optional): Path to the input JSON file. Defaults to 'pepper_data.txt' in the same directory.
			output_file (str, optional): Path to the output CSV file. Defaults to 'pepper_products.csv' in the same directory.

		Returns:
			str: Path to the generated CSV file
		"""
		print("pepperscraper->get_product_details_json()")
		import json
		import os

		try:
			# Set default file paths if not provided
			if input_file is None:
				input_file = self.get_url_file_path(input_file=self.INPUT_FILE)
			if output_file is None:
				output_file = self.get_data_file_path(input_file=self.OUTPUT_FILE)

			print(f"Reading file: {input_file}")
			print(f"Output File: {output_file}")

			# Ensure the directory exists
			os.makedirs(os.path.dirname(input_file), exist_ok=True)

			# Check if input file exists, if not return empty list
			if not os.path.exists(input_file):
				print(f"Input file not found: {input_file}")
				return []

			# Read the file content
			with open(input_file, 'r', encoding='utf-8') as f:
				content = f.read().strip()
			print("File has opened")
			# Try to parse as JSON
			try:
				# Check if the content is a JSON array or object
				if content.startswith('['):
					# If it's an array, wrap it in a dictionary with 'data' key
					data = {'data': json.loads(content)}
				else:
					# Try to parse as a regular JSON object
					data = json.loads(content)
					# If the data doesn't have a 'data' key, wrap it
					if 'data' not in data:
						data = {'data': [data]} if not isinstance(data, list) else {'data': data}
			except json.JSONDecodeError as je:
				print(f"Error parsing JSON: {je}")
				# Try to find JSON objects in the file
				import re
				json_objects = re.findall(r'\{(?:[^{}]|(?R))*\}', content)
				if json_objects:
					print(f"Found {len(json_objects)} potential JSON objects in file")
					data = {'data': [json.loads(obj) for obj in json_objects]}
				else:
					raise ValueError("No valid JSON data found in the file")

			print(f"Successfully parsed JSON data. Found {len(data.get('data', []))} items")

			# Extract products from the data structure
			products = []
			for item in data.get('data', {}).get('getSupplierVariantPackGroupItems', []):
				# print(json.dumps(item))
				try:
					if not isinstance(item, dict):
						print(f"Skipping non-dictionary item: {item}")
						continue
					variant_pack = item.get('variant_pack', {})
					# print("Loaded Variant Pack")
					item_data = variant_pack.get('item', {})
					# print("Loaded Item Data")
					if not isinstance(item_data, dict):
						print(f"Skipping item with invalid item data: {item_data}")
						continue

					description = item_data.get('description', '')
					photo_list = item_data.get('photo_url_list', [])
					if not isinstance(photo_list, list):
						photo_list = []
					# print("Loaded description and photo_list")
					try:
						brand = variant_pack.get("metadata", {}).get('additional_info', {}).get('Brand', '')
						gtin = variant_pack.get("metadata", {}).get('additional_info', {}).get('gtin_14', '')
						manufacturer_code = variant_pack.get("metadata", {}).get('additional_info', {}).get(
							'manufacturer_code', '')
					except Exception as e:
						print(f"Failed to process variant pack: {e}")

					product = {
						'id': item_data.get('uuid', ''),
						'name': item_data.get('display_name', ''),
						'category': item_data.get('category', ''),
						'sku': variant_pack.get('external_item_id', ''),
						'description': description,
						'brand': brand,
						'pack_size': self._extract_pack_size(description),
						'image': self._get_primary_image(photo_list),
						'gtin': gtin,
						'manufacturer_code': manufacturer_code,
						'uuid': item_data.get('uuid', ''),
						'extra_data': json.dumps(item)
					}

					# Extract additional details from descriptions if available
					descriptions = {}
					for desc in item_data.get('descriptions', []):
						if isinstance(desc, dict):
							name = str(desc.get('name', '')).lower().replace(' ', '_')
							descriptions[name] = str(desc.get('value', ''))

					# Add additional fields from descriptions
					product.update({
						'short_description': descriptions.get('short_description', ''),
						'additional_description': descriptions.get('additional_description', ''),
						'label_description': descriptions.get('label_description', ''),
						'full_description': descriptions.get('description', '')
					})
					print(f"Added descriptions")
					products.append(product)

				except Exception as e:
					print(f"Error processing item: {e}")
					continue

			# Write to CSV
			# print(output_file)
			# output_file = "/Users/mark/Downloads/scrapers/default/pepper_data.csv"
			if products:
				# Create output directory if it doesn't exist
				os.makedirs(os.path.dirname(output_file), exist_ok=True)

				# Write to CSV
				import csv
				with open(output_file, 'w', newline='', encoding='utf-8') as f:
					writer = csv.DictWriter(f, fieldnames=products[0].keys())
					writer.writeheader()
					writer.writerows(products)

				print(f"Successfully exported {len(products)} products to {output_file}")
				return output_file
			else:
				print("No valid products found in the input file.")
				return None

		except json.JSONDecodeError as e:
			print(f"Error parsing JSON data: {e}")
			return None
		except Exception as e:
			print(f"An error occurred: {str(e)}")
			import traceback
			traceback.print_exc()
			return None

	def get_product_details_json_2(self, input_file: str = None, output_file: str = None):
		"""
		Parse pepper_data.txt and export products to a CSV file.

		Args:
			input_file (str, optional): Path to the input JSON file. Defaults to 'pepper_data.txt' in the same directory.
			output_file (str, optional): Path to the output CSV file. Defaults to 'pepper_products.csv' in the same directory.

		Returns:
			str: Path to the generated CSV file
		"""
		print("pepperscraper->get_product_details_json_2()")
		import json
		import os

		try:
			# Set default file paths if not provided
			if input_file is None:
				input_file = self.get_url_file_path(input_file=self.INPUT_FILE)
			if output_file is None:
				output_file = self.get_data_file_path(input_file=self.OUTPUT_FILE)

			print(f"Reading file: {input_file}")
			print(f"Output File: {output_file}")

			# Read the file content
			with open(input_file, 'r', encoding='utf-8') as f:
				content = f.read().strip()

			# Try to parse as JSON
			try:
				# Check if the content is a JSON array or object
				if content.startswith('['):
					# If it's an array, wrap it in a dictionary with 'data' key
					data = {'data': json.loads(content)}
				else:
					# Try to parse as a regular JSON object
					data = json.loads(content)
					# If the data doesn't have a 'data' key, wrap it
					if 'data' not in data:
						data = {'data': [data]} if not isinstance(data, list) else {'data': data}
			except json.JSONDecodeError as je:
				print(f"Error parsing JSON: {je}")
				# Try to find JSON objects in the file
				import re
				json_objects = re.findall(r'\{(?:[^{}]|(?R))*\}', content)
				if json_objects:
					print(f"Found {len(json_objects)} potential JSON objects in file")
					data = {'data': [json.loads(obj) for obj in json_objects]}
				else:
					raise ValueError("No valid JSON data found in the file")

			print(f"Successfully parsed JSON data. Found {len(data.get('data', {}).get('getSupplierCategoryItems', []))} items")

			# Extract products from the data structure
			products = []
			for item in data.get('data', {}).get('getSupplierCategoryItems', []):

				try:
					if not isinstance(item, dict):
						print(f"Skipping non-dictionary item: {item}")
						continue
					variant_pack = item.get('variant_pack', {})

					item_data = variant_pack.get('item', {})
					# print(item_data)
					if not isinstance(item_data, dict):
						print(f"Skipping item with invalid item data: {item_data}")
						continue

					description = item_data.get('description', '')
					photo_list = item_data.get('photo_url_list', [])
					if not isinstance(photo_list, list):
						photo_list = []

					# brand = variant_pack.get("metadata", {}).get('additional_info', {}).get('Brand', '')
					# gtin = variant_pack.get("metadata", {}).get('additional_info', {}).get('gtin_14', '')
					# manufacturer_code = variant_pack.get("metadata", {}).get('additional_info', {}).get(
					# 	'manufacturer_code', '')

					product = {
						'id': item_data.get('uuid', ''),
						'name': item_data.get('display_name', ''),
						'category': item_data.get('category', ''),
						'sku': variant_pack.get('external_item_id', ''),
						'description': description,
						# 'brand': brand,
						'pack_size': self._extract_pack_size(description),
						'image': self._get_primary_image(photo_list),
						# 'gtin': gtin,
						# 'manufacturer_code': manufacturer_code,
						'uuid': item_data.get('uuid', ''),
						'extra_data': json.dumps(item)
					}

					# Extract additional details from descriptions if available
					descriptions = {}
					for desc in item_data.get('descriptions', []):
						if isinstance(desc, dict):
							name = str(desc.get('name', '')).lower().replace(' ', '_')
							descriptions[name] = str(desc.get('value', ''))

					# Add additional fields from descriptions
					product.update({
						'short_description': descriptions.get('short_description', ''),
						'additional_description': descriptions.get('additional_description', ''),
						'label_description': descriptions.get('label_description', ''),
						'full_description': descriptions.get('description', '')
					})

					products.append(product)

				except Exception as e:
					print(f"Error processing item: {e}")
					continue

			# Write to CSV
			# print(output_file)
			# output_file = "/Users/mark/Downloads/scrapers/default/pepper_data.csv"
			if products:
				# Create output directory if it doesn't exist
				os.makedirs(os.path.dirname(output_file), exist_ok=True)

				# Write to CSV
				import csv
				with open(output_file, 'w', newline='', encoding='utf-8') as f:
					writer = csv.DictWriter(f, fieldnames=products[0].keys())
					writer.writeheader()
					writer.writerows(products)

				print(f"Successfully exported {len(products)} products to {output_file}")
				return output_file
			else:
				print("No valid products found in the input file.")
				return None

		except json.JSONDecodeError as e:
			print(f"Error parsing JSON data: {e}")
			return None
		except Exception as e:
			print(f"An error occurred: {str(e)}")
			import traceback
			traceback.print_exc()
			return None

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

	def process_products_from_csv(self):
		print("pepperscraper->process_products_from_csv()")
		return self.get_product_details_json()

	def _extract_brand(self, description: str) -> str:
		"""Extract brand from description if it follows 'Brand: ' pattern."""
		import re
		# print("_extract_brand()")
		match = re.search(r'Brand:\s*([^\n|]+)', description)
		return match.group(1).strip().replace('Brand: ', '') if match else ''

	def _extract_pack_size(self, description: str) -> str:
		"""Extract pack size from description if it follows 'Pack Size: ' pattern."""
		if not description:
			return ''
		import re
		print("_extract_pack_size()")
		match = re.search(r'Pack Size:\s*([^\n|]+)', description, re.IGNORECASE)
		return match.group(1).strip() if match else ''

	def _get_primary_image(self, image_urls: list) -> str:
		"""Get the primary image URL from a list of image URLs."""
		print("_get_primary_image()")
		return image_urls[0] if image_urls and len(image_urls) > 0 else ''