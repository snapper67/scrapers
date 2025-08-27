import json
from typing import List, Dict, Any, Optional
from urllib.parse import urljoin

import requests
import time
import os

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
		'pack_size': '',
		'category': '',
		'subcategory': '',
		'shop_id': '',
		'price': 0,
	}

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/melissas_produce'

	BASE_URL = 'https://www.melissas.com/pages/asian'
	VENDOR_NAME = 'Melissa\'s Produce'

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

	def get_category_ids(self):
		return self.CATEGORY_IDS

	def get_category_names(self):
		return self.CATEGORY_NAMES

	def get_category_urls(self):
		return self.CATEGORY_URLS

	def split_code_and_text(self, input_string):
		"""
		Splits a string in the format '9999 - text text-text' into code and text.

		Args:
			input_string (str): The input string to split

		Returns:
			tuple: (code, text) where code is the numeric part and text is the rest
		"""
		# Split on the first occurrence of ' - ' (space-hyphen-space)
		try:
			parts = input_string.split(' - ', 1)

			if len(parts) == 2:
				code = parts[0].strip()
				text = parts[1].strip()
			else:
				# Handle case where the delimiter isn't found
				code = input_string.strip()
				text = ''

			return code, text
		except Exception as e:
			return '', ''

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
				row_spec["price"] = data.get("price", "")
				row_spec["shop_id"] = data.get("id", "")
				row_spec["pack_size"] = self.get_pack_size(data, row_spec)
				row_spec["image"] = self.get_first_image_url(data)

				variants = data.get('variants', [])
				row_spec["sku"] = variants[0].get("sku", "")

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
		print("get_manufacturer()")
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
					print("⚠️ pack size name not found in specifications")

		except Exception as e:
			print(f"⛔️ Error processing manufacturer information: {type(e).__name__} - {str(e)}")

		print("Processing manufacturer information complete...")
		return row_spec

	# ************************************************************************


	def process_subcategories(self):
		"""
		Processes the subcategories from the API response and stores it into `subcategories`.

		Args:
			None

		Returns:
			tuple: A tuple containing the subcategories and category name.
		"""
		urls = []
		subcategories = ''
		category_name = ''

		sub_categories = self.wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.card__wrap'))
		)
		print(f"Found Category Wrapper: {len(sub_categories)}")
		category_url_part = str(self.options['category_url_part']) + "?expand"
		print(f"category_url_part: {category_url_part}")
		for request in self.driver.requests:
			#
			# https://www.chefswarehouse.com/products/meat-and-poultry/?expand=*&currentPageUrl=%252Fproducts%252Fmeat-and-poultry%252F&tz=America%252FNew_York&t=1753496336262
			if request.response and category_url_part in request.url:  # Filter for API requests
				print(f"URL: {request.url}")
				print(f"Status Code: {request.response.status_code}")
				print(f"Content Type: {request.response.headers.get('Content-Type')}")

				# Decode the response body (it's bytes by default)
				try:
					# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
					body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

					# If the body is JSON, parse it
					if 'application/json' in request.response.headers.get('Content-Type', ''):
						data = json.loads(body)
						# {
						# 	"name": "Foie Gras",
						# 	"imageUrl": "/siteassets/foie-gras_330.png",
						# 	"url": "/products/meat-and-poultry/foie-gras/"
						# },
						category_name = data.get('name', '')
						view_model = data.get('viewModel', {})
						subcategories = view_model.get('subCategories', [])
						urls = [category['url'] for category in subcategories]
						print(f"==== sub categories: {subcategories}")
					else:
						print(f"Response Body was not JSON:")

				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding response body: {e}")
		print(f"========= Number of sub categories: {len(urls)}")

		del self.driver.requests
		return subcategories, category_name

	@staticmethod
	def create_interceptor(max_api_products=MAX_API_PRODUCTS):
		def interceptor(request):
			# https://www.chefswarehouse.com/products/dairy-and-eggs/dairy-products//search
			if request.method == 'POST' and '//search' in request.url:  # Replace 'your_target_url'
				print(f"👽👽👽Intercepting request: {request.url}")
				# Get the current POST data
				current_data = request.body.decode('utf-8')
				print(f"Original POST data: {current_data}")

				# Modify the POST data
				# Example: change a value in a JSON payload
				try:
					payload = json.loads(current_data)
					search = payload.get('search', {})
					search['pageSize'] = max_api_products  # Replace 'key_to_change' and 'new_value'
					request.body = json.dumps(payload).encode('utf-8')
					# Update the Content-Length header to reflect the new body size
					del request.headers['Content-Length']
					request.headers['Content-Length'] = str(len(request.body))
					print(f"Modified POST data: {request.body.decode('utf-8')}")
				except json.JSONDecodeError:
					# Handle cases where the body is not JSON
					print("Request body is not JSON. Cannot modify in this example.")
			if request.method == 'POST' and 'product-domain-api/v1/search' in request.url:  # Replace 'your_target_url'
				print(f"👽👽👽Intercepting request: {request.url}")
				# Get the current POST data
				current_data = request.body.decode('utf-8')
				print(f"Original POST data: {current_data}")

				# Modify the POST data
				# Example: change a value in a JSON payload
				try:
					payload = json.loads(current_data)
					payload['recordsPerPage'] = max_api_products  # Replace 'key_to_change' and 'new_value'
					request.body = json.dumps(payload).encode('utf-8')
					# Update the Content-Length header to reflect the new body size
					del request.headers['Content-Length']
					request.headers['Content-Length'] = str(len(request.body))
					print(f"Modified POST data: {request.body.decode('utf-8')}")
				except json.JSONDecodeError:
					# Handle cases where the body is not JSON
					print("Request body is not JSON. Cannot modify in this example.")
			# https://panamax-api.ama.usfoods.com/product-domain-api/v2/products
			if request.method == 'POST' and 'product-domain-api/v2/products' in request.url:
				print(f"👽👽👽Intercepting request: {request.url}")
				current_data = request.body.decode('utf-8')
				print(f"Original POST data: {current_data}")

		return interceptor

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
		test_categories = self.options.get('test_categories', self.TEST_CATEGORIES)
		max_products = self.options.get('max_products', self.MAX_API_PRODUCTS)
		category_to_process = self.options.get('category_to_process', 0)
		chosen_category = self.options.get('chosen_category', '')
		chosen_category_id = self.CATEGORY_IDS[chosen_category]
		category_url_part = self.CATEGORY_URLS[chosen_category_id]
		category_name = self.options.get('chosen_category', self.CATEGORY_NAMES[chosen_category_id])
		url_output_file = self.options.get('url_output_file', '')

		category_URL = f"https://www.melissas.com/pages/{category_url_part}"
		# Wait for the page to be fully loaded
		wait = WebDriverWait(self.driver, 10)
		print(f"Scraping products from category {category_name}")
		print(f"Output File Name: {url_output_file}")
		self.driver.get(category_URL)
		self.driver.request_interceptor = self.create_interceptor(max_products)
		total_products = 0
		loop_counter = 0
		category_found_count = 1

		# Starting on the page for a specific category
		print(f"Loading category page {category_URL}")
		self.driver.get(category_URL)
		self.driver.execute_script("document.body.style.zoom = '50%'")

		print(f"Page title: {self.driver.title}")

		if category_to_process > 0:
			print(f"Category to process: {category_to_process}")
			loop_counter = category_to_process - 1
			test_categories = category_to_process
			category_found_count = category_to_process

		while loop_counter < category_found_count and loop_counter < test_categories:
			loop_counter += 1

			# Wait for category cards to be present and visible
			sub_categories = wait.until(
				EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.shogun-image-link'))
			)
			print(f"Page title: {self.driver.title}")

			category_found_count = len(sub_categories)
			print(f"Found {category_found_count} categories to process...")

			# Store the main window handle
			main_window = self.driver.current_window_handle

			try:
				# for category_index, sub_category in enumerate(sub_categories[loop_counter:loop_counter]):
				sub_category = sub_categories[loop_counter - 1]
				link = sub_category.get_attribute("href")
				print(f"\nProcessing category {loop_counter} of {category_found_count}...")
				self.driver.execute_script("arguments[0].scrollIntoView();", sub_category)

				sub_category_name = os.path.basename(link)
				print(f"Category name: {sub_category_name}")
				html += f"<h2>Category Name: {sub_category_name}</h2>"

				# Click on the category to open detail page
				sub_category.click()
				print("Clicked on category, waiting for detail page to load...")

				# Wait for the detail page to load
				time.sleep(6)  # Wait for the page to load
				print(f"Looking for Page: {sub_category_name} - Melissas Produce")
				print(f"Found:           {self.driver.title}")
				print(f"Current URl: {self.driver.current_url}")

				# Find all window handles and switch to the new window if it opens in a new tab
				if len(self.driver.window_handles) > self.TEST_TABS:
					print("must be a tab...")
					for handle in self.driver.window_handles:
						if handle != main_window:
							self.driver.switch_to.window(handle)
							break
				page_count = 1
				next_page = True

				while next_page:
					try:
						# Wait for page to load
						detail_urls = []
						if link in self.driver.current_url:
							print("Found products page")
							time.sleep(2)
							html_line, detail_urls = self.grab_products(category_name, sub_category_name,  url_output_file)
						products_found_count = len(detail_urls)
						html += f"<div>Found {products_found_count} products for category {sub_category_name}</div>"
						print(f"Found {products_found_count} products for category {sub_category_name}")
						total_products += products_found_count
						self.save_urls_to_csv(detail_urls, category_name, sub_category_name)
						all_urls.extend(detail_urls)

					except Exception as e:
						print(f"****************** ⛔️⛔️⛔️ Error getting details: {e}")
						html += f"<div>Name: {sub_category_name} (Error getting details) {loop_counter}</div>"

					try:
						paging = wait.until(
							EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination--inner'))
						)
						paging.find_element(By.CLASS_NAME, 'pagination--next').click()
						next_page = True
					except Exception as e:
						next_page = False

				self.driver.get(category_URL)
				self.driver.execute_script("document.body.style.zoom = '50%'")
				print(f"Going back to get next category: {self.driver.title}")
				# Wait before processing next category
				time.sleep(3)

			except Exception as e:
				print(f"⛔️⛔️⛔️Error processing category: {e}")
				continue

		time.sleep(3)


		# html_table_to_csv(html_table)
		html += f"<h2>Total products found: {total_products}</h2>"

		print(f"Total products found: {len(all_urls)}")
		return html

	def get_product_details(self, url, row_spec=None):
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print("processing product detail page")
		print(f"Loading page...{url}")

		data = ''
		sku = row_spec['sku']
		request_filter = f"https://www.melissas.com/products/{sku}.js"

		self.driver.get(url)
		print(f"Sent Request")
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

			# These use the data if available, then try to scrape from the page
			row_spec = self.get_product_data(data, row_spec)
			# row_spec['content_url'] = url

		except Exception as e:
			print(f"⛔️⛔️⛔️Error waiting for request: {e}")

			# for request in self.driver.requests:
			# 	print(request.url)

		del self.driver.requests
		return row_spec

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