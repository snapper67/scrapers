import csv
import json
import re
import requests
import time
import os
from collections import OrderedDict
import sys
import glob
import pandas as pd

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


class ChefWarehouseScraper(Scraper):
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
		'pricingUnitOfMeasure': '',
	}

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/cw'

	BASE_URL = 'https://www.chefswarehouse.com'

	CATEGORY_IDS = {
		"MEAT": 1,
		"SEAFOOD": 2,
		"CHEESE": 3,
		"OIL": 4,
		"BAKING": 5,
		"PANTRY": 6,
		"PRODUCE": 7,
		"FROZEN": 8,
		"BEVERAGE": 9,
		"SUPPLIES": 10,
		"DAIRY": 21,
	}
	# Category Names (can use category ID as key)
	CATEGORY_NAMES = {
		1: "Meat & Poultry",
		2: "Seafood",
		3: "cheese-and-charcuterie/",
		4: "oil-and-vinegar",
		5: "baking-and-pastry",
		6: "pantry-staples",
		7: "fresh-produce",
		8: "frozen-grocery",
		9: "beverages",
		10: "supplies",
		21: "dairy-and-eggs",
	}
	CATEGORY_URLS = {
		1: "meat-and-poultry",
		2: "Seafood",
		3: "cheese-and-charcuterie",
		4: "oil-and-vinegar",
		5: "baking-and-pastry",
		6: "pantry-staples",
		7: "fresh-produce",
		8: "frozen-grocery",
		9: "beverages",
		10: "supplies",
		21: "dairy-and-eggs",
	}
	URL_FILE_NAMES = {
		1: "meat_product_urls.csv",
		2: "seafood_product_urls.csv",
		3: "cheese_product_urls.csv",
		4: "oil_product_urls.csv",
		5: "bakery_product_urls.csv",
		6: "pantry_product_urls.csv",
		7: "produce_product_urls.csv",
		8: "frozen_product_urls.csv",
		9: "beverage_product_urls.csv",
		10: "supplies_product_urls.csv",
		21: "dairy_product_urls.csv",
	}
	DATA_FILE_NAMES = {
		1: "meat_product_data.csv",
		2: "seafood_product_data.csv",
		3: "cheese_product_data.csv",
		4: "oil_product_datas.csv",
		5: "bakery_product_data.csv",
		6: "pantry_product_data.csv",
		7: "produce_product_data.csv",
		8: "frozen_product_data.csv",
		9: "beverage_product_data.csv",
		10: "supplies_product_data.csv",
		21: "dairy_product_data.csv",
	}
	CHOSEN_CATEGORY = CATEGORY_IDS["DAIRY"]
	CATEGORY_NAME = CATEGORY_NAMES[CHOSEN_CATEGORY]
	URL_OUTPUT_FILE = URL_FILE_NAMES[CHOSEN_CATEGORY]
	DATA_OUTPUT_FILE = DATA_FILE_NAMES[CHOSEN_CATEGORY]
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
		'chosen_category': '10001',  # Default to Meat
		'url_output_file': URL_OUTPUT_FILE,
		'data_output_file': DATA_OUTPUT_FILE,
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

	def get_first_image_url(self, response_data):
		"""
		Extract the first available image URL from the product API response.

		Args:
			response_data (dict): The parsed JSON response from the API

		Returns:
			str: URL of the first available image, or None if no image found
		"""
		try:
			view_model = response_data.get('viewModel', {})
			assets = view_model.get('assets', [])

			# If there are assets, get the first one's URL
			if assets and isinstance(assets, list) and len(assets) > 0:
				# Get the first asset and extract the URL
				first_asset = assets[0]
				if isinstance(first_asset, dict):
					return self.BASE_URL + first_asset.get('featuredSrc', '')

		except Exception as e:
			print(f"Error extracting image from viewModel.assets: {str(e)}")

		return ''

	def get_product_data(self, data, row_spec):
		print("processing product data from response...")
		# print(data)
		if data:
			try:
				row_spec["name"] = data.get("name", "")
				row_spec["brand"] = data.get("displayBrand", "")

				view_model = data.get('viewModel', {})
				row_spec["pack_size"] = view_model.get('size', {})

				row_spec["image"] = self.get_first_image_url(data)
				row_spec = self.get_classification(view_model, row_spec)
				row_spec = self.get_description(view_model, row_spec)
				row_spec = self.get_manufacturer(data, row_spec)
				row_spec = self.get_additional_info(data, row_spec)
				row_spec["extra_data_1"] = json.dumps(data)

			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing get_product_data Complete...")
		return row_spec

	def get_classification(self, product_data, row_spec):
		print("processing product classification...")
		if product_data:
			row_spec["level_1"] = product_data.get("category", "").get('text', '')
			row_spec["level_2"] = product_data.get("subcategory", "")
			row_spec["level_3"] = product_data.get("subsubcategory", "")
		return row_spec

	def get_manufacturer(self, data, row_spec):
		# Scrape the section that contains the manufacturer information. It is in an unordered list
		if data:
			try:
				row_spec["manufacturer_sku"] = data.get("manufacturerItemNumber", "")
				row_spec["manufacturer_name"] = data.get("manufacturerDisplayName", "")
			except Exception as e:
				print(f"⛔️⛔️⛔️Error processing manufacturer data: {e}")
		return row_spec

	def get_description(self, data, row_spec):
		print("processing product overview...")
		description = ''
		if data:
			try:
				row_spec["description"]  = data.get('description', description)
			except Exception as e:
				print(f"⛔️️ Error processing product overview from data: {e}")

		print("processing product overview Complete...")
		return row_spec

	def get_additional_info(self, data, row_spec):
		"""
		Processes the product additional data from the API response and stores it into `row_spec`.
		This function specifically handles the extra fields that are not present in the standard product spec .

		Args:
			data (dict): The API response containing the product additional data
			row_spec (dict): The dictionary containing the scraped product data

		Returns:
			dict: The updated `row_spec` with the additional data
		"""
		print("processing product additional data...")
		if data:
			try:
				view_model = data.get('viewModel', {})
				row_spec["pricingUnitOfMeasure"] = view_model.get("pricingUnitOfMeasure", "")
			except Exception as e:
				print(f"⛔️⛔️⛔️Error processing additional data: {e}")

		print("processing product additional data Complete...")
		return row_spec

	# ************************************************************************

	def process_product_list_search_api(self, category, sub_category, url_output_file):
		# Build a list of product URLs
		detail_urls = []
		all_urls = []

		product_wrappers = self.wait.until(
			EC.presence_of_all_elements_located((By.CLASS_NAME, 'search-result-col'))
		)
		print(f"Found Product Wrapper: {len(product_wrappers)}")

		for request in self.driver.requests:
			#
			if request.response and "//search" in request.url:  # Filter for API requests
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
						# https://www.chefswarehouse.com/products/10303734/
						detail_urls = [f"https://www.chefswarehouse.com{product['url']}" for product in data['results']]
						print(f"== Number of products: {len(detail_urls)}")
						self.save_urls_to_csv(detail_urls, category, sub_category)
					else:
						print(f"Response Body (Text): {body}")
					all_urls.extend(detail_urls)

				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding response body: {e}")
		print(f"========= Number of products: {len(all_urls)}")
		del self.driver.requests
		return all_urls

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

	def build_products_list(self):
		"""Given a category, get the list of products
		The ability to choose a specific category to process is not yet implemented
		"""
		print("build_products_list()")
		html = ""
		all_urls = []
		detail_urls = []
		# Use the options with fallback to module-level variables
		test_categories = self.options.get('test_categories', self.TEST_CATEGORIES)
		max_products = self.options.get('max_products', self.MAX_API_PRODUCTS)
		category_to_process = self.options.get('category_to_process', 0)
		chosen_category = self.options.get('chosen_category', self.CHOSEN_CATEGORY)
		chosen_category_id = self.CATEGORY_IDS[chosen_category]
		category_url_part = self.CATEGORY_URLS[chosen_category_id]
		category_name = self.options.get('chosen_category', self.CATEGORY_NAMES[chosen_category_id])
		url_output_file = self.options.get('url_output_file', self.URL_FILE_NAMES[chosen_category_id])
		# data_output_file = options.get('data_output_file', DATA_FILE_NAMES[chosen_category_id])
		# https://www.chefswarehouse.com/products/dairy-and-eggs
		category_URL = f"https://www.chefswarehouse.com/products/{category_url_part}"
		# Wait for the page to be fully loaded

		print(f"Scraping products from category {category_name}")
		print(f"Output File Name: {url_output_file}")
		self.driver.get(category_URL)
		self.driver.request_interceptor = self.create_interceptor(max_products)
		total_products = 0

		html_table = ""
		# Starting on the page for a specific category
		print(f"Loading category page {category_URL}")
		self.driver.execute_script("document.body.style.zoom = '50%'")

		print(f"Page title: {self.driver.title}")

		subcategories, category_name = self.process_subcategories()
		loop_counter = 0
		for subcategory in subcategories:
			# {
			# 	"name": "Foie Gras",
			# 	"imageUrl": "/siteassets/foie-gras_330.png",
			# 	"url": "/products/meat-and-poultry/foie-gras/"
			# },
			loop_counter += 1
			if loop_counter > test_categories:
				break
			sub_category_name = subcategory.get('name', '')
			sub_category_url = subcategory.get('url', '')
			sub_category_image = subcategory.get('imageUrl', '')
			print(f"Processing subcategory {sub_category_name}")
			full_sub_category_url = f"https://www.chefswarehouse.com{sub_category_url}"
			self.driver.get(full_sub_category_url)
			detail_urls = self.process_product_list_search_api(category_name, sub_category_name, url_output_file)
			products_found_count = len(detail_urls)
			html += f"<h2>Category Name: {sub_category_name}</h2>"
			html += f"<div>Found {products_found_count} products for category {sub_category_name}</div>"
			print(f"Found {products_found_count} products for category {sub_category_name}")
			total_products += products_found_count

			all_urls.extend(detail_urls)

		time.sleep(3)

		# html_table_to_csv(html_table)
		html += f"<h2>Total products found: {total_products}</h2>"
		html += html_table
		print(f"Total products found: {len(all_urls)}")
		return html

	def get_product_details(self, url, row_spec=None):
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print("processing product detail page")
		print(f"Loading page...{url}")

		data = ''
		sku = row_spec['sku']
		request_filter_escaped = sku + "/\?expand"
		request_filter = sku + "/?expand"
		# https://www.chefswarehouse.com/products/QZ106085/?expand=*&currentPageUrl=%252Fproducts%252FQZ106085%252F&tz=America%252FNew_York&t=1753508466488
		# https://www.chefswarehouse.com/products/M502/?expand=*&currentPageUrl=%252Fproducts%252FM502%252F&tz=America%252FNew_York&t=1753510472740
		self.driver.get(url)
		print(f"Sent Request")
		try:
			request = self.driver.wait_for_request(request_filter_escaped)
			if request.response and request_filter in request.url:  # Filter for API requests
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
					else:
						print(f"Response Body (Text): {body}")

				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

			# These use the data if available, then try to scrape from the page
			row_spec = self.get_product_data(data, row_spec)

		except Exception as e:
			print(f"⛔️⛔️⛔️Error waiting for request: {e}")

			# for request in self.driver.requests:
			# 	print(request.url)

		del self.driver.requests
		return row_spec