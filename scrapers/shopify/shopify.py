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

class ShopifyScraper(Scraper):
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
		'id': '',
		'pack_size': '',
		'category': '',
		'subcategory': '',
		'subsubcategory': '',
		'shop_id': '',
		'price': 0,
	}

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/default'

	BASE_URL = ''
	BASE_PRODUCT_URL = ''
	VENDOR_NAME = ''

	CATEGORY_IDS = {
		"FRUIT": 1,
		"VEGETABLES": 2,
		"CONVENIENCE": 3,
		"ASIAN": 4,
		"LATIN": 5,
	}
	# Category Names (can use category ID as key)
	CATEGORY_NAMES = {
		1: "fruits",
		2: "vegetables",
		3: "convenience",
		4: "asian",
		5: "latin",
	}
	CATEGORY_URLS = {
		1: "fruits",
		2: "vegetables",
		3: "convenience",
		4: "asian",
		5: "latin",
	}

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

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
		'chosen_category': '10001',
		'url_output_file': '',
		'data_output_file': '',
		'home_directory': DEFAULT_DIRECTORY
	}

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY
		self.options['base_url'] = self.BASE_URL

	def get_category_ids(self):
		return self.CATEGORY_IDS

	def get_category_names(self):
		return self.CATEGORY_NAMES

	def get_category_urls(self):
		return self.CATEGORY_URLS

	def get_taxonomy(self):
		"""Load a category page"""
		raise NotImplementedError("get_taxonomy method not implemented")

	def scraping_setup(self):
		"""Scrape products from the website"""
		return

	def get_category_url(self, category):
		return category['url']

	def get_unique_keys(self, data_file):
		keys = set()
		if os.path.exists(data_file):
			with open(data_file, 'r', newline='', encoding='utf-8') as f:
				reader = csv.DictReader(f)
				csv.field_size_limit(sys.maxsize)
				if 'id' in reader.fieldnames:
					keys = {row['id'] for row in reader}
		return keys

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
				row_spec["price"] = data.get("price", "")
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
	def get_category_page(self, url, category_name, sub_category_name, sub_sub_category_name):
		"""Load a category page"""
		raise NotImplementedError("scrape_products method not implemented")

	def grab_products(self):

		products = self.wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.productitem--image-link'))
		)

		print(f"products found: {len(products)}")
		detail_urls = [product.get_attribute("href") for product in products]
		return '', detail_urls

	def build_products_list(self):
		"""Scrape products from the website"""
		html = ""
		all_urls = []
		# Use the options with fallback to module-level variables
		max_products = self.options.get('max_products', self.MAX_API_PRODUCTS)
		category_to_process = self.options.get('category_to_process', 0)
		chosen_category = int(self.options.get('chosen_category', 0))
		test_categories = self.options.get('test_categories', 100)
		category_count = 0
		if int(self.options['chosen_category']) == 0:
			categories = self.get_taxonomy()
			print(f"All Categories ")
		else:
			for category in self.get_taxonomy():
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

		if category_to_process > 0:
			print(f"Category to process: {category_to_process}")
			loop_counter = category_to_process - 1
			test_categories = category_to_process
			category_found_count = category_to_process
		for category in categories:
			category_name = category['name']
			print(f"category: {category_name}")
			sub_categories = category['subcategories']
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
							detail_urls, html = self.get_category_page(url, category_name, sub_category_name, sub_sub_category_name)
							all_urls.extend(detail_urls)
						time.sleep(2)
				else:
					url = self.get_category_url(sub_category)
					print(f"Url: {url}")
					detail_urls, html = self.get_category_page(url, category_name, sub_category_name, '')
					all_urls.extend(detail_urls)

		# html_table_to_csv(html_table)
		html += f"<h2>Total products found: {total_products}</h2>"

		print(f"Total products found: {len(all_urls)}")
		return html

	def get_product_details(self, url, row_spec=None):
		"""Get Product Details"""
		raise NotImplementedError("scrape_products method not implemented")

	def get_product_details_json(self, url, row_spec=None):
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print("processing product detail page")
		print(f"Loading page...{url}")

		data = ''
		sku = row_spec['sku']
		request_filter = f"{self.BASE_PRODUCT_URL}{sku}.js"

		self.driver.get(url)
		print(f"Sent Request {request_filter}")
		try:
			request = self.driver.wait_for_request(request_filter)
			if request.response and request_filter in request.url:  # Filter for API requests
				print(f"URL: {request.url}")
				print(f"Status Code: {request.response.status_code}")
				print(f"Content Type: {request.response.headers.get('Content-Type')}")

				# Decode the response body (it's bytes by default)
				try:
					body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

					# If the body is JSON, parse it
					data = json.loads(body)
					print(f"Response Body (Text): {data}")

				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

		except Exception as e:
			print(f"⛔️⛔️⛔️Error waiting for request: {e}")

		del self.driver.requests
		return data

	def get_product_details_scrape(self, url, row_spec=None, target="script[type='application/json']"):
		#  Wait for the product name element on the product page detail page
		print("Scraper.get_product_details()")
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print("processing product detail page")
		print(f"Loading page...{url}")

		data = ''
		sku = row_spec['sku']
		request_filter = url

		self.driver.get(url)
		print(f"Sent Request")
		product_data = ''
		try:
			# Wait for the page to load
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(
				(By.CSS_SELECTOR, target))
			)

			# Get the page source and parse it with BeautifulSoup
			soup = BeautifulSoup(self.driver.page_source, 'html.parser')

			# Find the script tag with the product data
			script_tag = soup.find('script', {
				'type': 'application/json',
				'data-section-type': 'static-product'
			})

			if not script_tag:
				script_tag = soup.find('script', {
					'type': 'application/json',
					'data-product-json': ''
				})

			if script_tag and script_tag.string:
				try:
					# Parse the JSON data from the script tag
					product_data = json.loads(script_tag.string)

				except json.JSONDecodeError as e:
					print(f"Error parsing JSON data: {e}")
			else:
				print("Could not find the product data script tag")

		except Exception as e:
			print(f"Error getting product details: {e}")
		finally:
			del self.driver.requests

		return product_data

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

	def get_navigation_structure(self, url: str, headers: Optional[Dict] = None, pretty: bool = True) -> str:
		"""
		Fetches and parses the navigation structure from the Bitters & Bottles website.

		Args:
			url: The URL of the Bitters & Bottles website
			headers: Optional headers for the HTTP request
			pretty: If True, returns pretty-printed JSON

		Returns:
			A JSON string containing the navigation structure with categories
		"""
		nav_dict = {
			"data": []
		}
		try:
			nav_dict = self.get_navigation_dict(url, headers)
			if pretty:
				return json.dumps(nav_dict, indent=2, sort_keys=True)
			return json.dumps(nav_dict)
		except Exception as e:
			error_msg = f"Error in get_navigation_structure: {str(e)}"
			print(error_msg)
			return json.dumps({"error": error_msg}, indent=2 if pretty else None)

	def get_navigation_dict(self, url: str, headers: Optional[Dict] = None) -> Dict:
		"""
		Fetches and parses the navigation structure and returns it as a dictionary.
		This is a helper method used by get_navigation_structure.

		Args:
			url: The URL of the Bitters & Bottles website
			headers: Optional headers for the HTTP request

		Returns:
			A dictionary containing the navigation structure
		"""
		print("get_navigation_dict()")
		print(f"Url: {url}")
		if headers is None:
			headers = {
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
			}

		try:
			# Fetch the page content
			response = requests.get(url, headers=headers, timeout=10)
			response.raise_for_status()

			# Parse the HTML content
			soup = BeautifulSoup(response.text, 'html.parser')

			# Find the main navigation container
			nav = soup.find('nav', class_='site-navigation')
			if not nav:
				print("Could not find the main navigation menu")
				return {}

			# Find the top-level navigation items
			top_level_items = nav.select('ul.navmenu-depth-1 > li.navmenu-item-parent')
			navigation = {'data': {'categories': []}}
			print(f"navs found {len(top_level_items)}")
			i = 0;
			for item in top_level_items:
				# Get the category link
				i += 1
				category_link = item.find('a', class_='navmenu-link-parent')
				if not category_link:
					continue

				category_name = category_link.get_text(strip=True).replace('Chevron down icon', '')
				category_url = urljoin(url, category_link.get('href', ''))

				# Initialize subcategories list
				subcategories = []

				# Find the submenu if it exists
				submenu = item.find('ul', class_='navmenu-depth-2')
				if submenu:
					# Find all second-level items
					sub_items = submenu.find_all('li', class_=lambda x: x and 'navmenu-item' in x.split())

					for sub_item in sub_items:
						sub_link = sub_item.find('a')
						if not sub_link:
							continue

						sub_name = sub_link.get_text(strip=True).replace('Chevron down icon', '')
						sub_url = urljoin(url, sub_link.get('href', ''))

						# Check for third level items
						sub_submenu = sub_item.find('ul', class_='navmenu-depth-3')
						sub_subcategories = []

						if sub_submenu:
							# Find all third-level items
							sub_sub_items = sub_submenu.find_all('li',
							                                     class_=lambda x: x and 'navmenu-item' in x.split())

							for sub_sub_item in sub_sub_items:
								sub_sub_link = sub_sub_item.find('a')
								if not sub_sub_link:
									continue

								sub_sub_name = sub_sub_link.get_text(strip=True)
								sub_sub_url = urljoin(url, sub_sub_link.get('href', ''))

								sub_subcategories.append({
									'name': sub_sub_name,
									'url': sub_sub_url
								})

						subcategories.append({
							'name': sub_name,
							'url': sub_url,
							'subcategories': sub_subcategories if sub_subcategories else None
						})

				# Add to navigation
				navigation['data']['categories'].append({
					'name': category_name,
					'id': i,
					'url': category_url,
					'subcategories': subcategories if subcategories else None
				})

			return navigation

		except requests.RequestException as e:
			print(f"Error fetching navigation: {e}")
			return {}
		except Exception as e:
			print(f"Error parsing navigation: {str(e)}")
			return {}

	def print_navigation_structure(self, navigation: Dict):
		"""Prints the navigation structure in a readable format."""
		for category, data in navigation.items():
			print(f"- {category} ({data['url']})")
			for subcategory in data['subcategories']:
				print(f"  - {subcategory['name']} ({subcategory['url']})")