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


class USFoodsScraper(Scraper):
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
		'timestamp': '',

		# Fields from US_FOODS_SPEC
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
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/usfoods'

	CATEGORY_IDS = {
		"BEEF": 15,
		"BEVERAGE": 16,
		"FRUIT": 17,
		"CHEESE": 18,
		"CHEMICALS": 19,
		"APPETIZER": 20,
		"DAIRY": 21,
		"GROCERY_DRY": 22,
		"EQUIPMENT": 23,
		"DISPOSABLES": 24,
		"PRODUCE": 25,
		"GROCERY_FRZ": 26,
		"OIL": 29,
		"PORK": 30,
		"POULTRY": 31,
		"PROCESSED": 32,
		"SEAFOOD": 33,
		"SPECIALTY_MEAT": 34,
		"SALADS": 35,
		"MEAT_SUB": 37,
	}
	# Category Names (can use category ID as key)
	CATEGORY_NAMES = {
		15: "Beef",
		16: "Beverage",
		17: "Fruits & Vegetables, Canned & Dried",
		18: "Cheese",
		19: "Chemicals & Cleaning Agents",
		20: "Appetizers, Entrees, & Potatoes Ref & Fzn",
		21: "Dairy",
		22: "Grocery, Dry",
		23: "Equipment & Supplies",
		24: "Disposables",
		25: "Produce, Fresh",
		26: "Grocery, Ref & Fzn",
		29: "Oils & Shortening",
		30: "Pork",
		31: "Poultry",
		32: "Processed Meat",
		33: "Seafood",
		34: "Specialty Meats",
		35: "Salads, Wet, Ref & Fzn",
		37: "Meat Substitute",
	}
	URL_FILE_NAMES = {
		15: "beef_product_urls.csv",
		16: "bev_product_urls.csv",
		17: "fruit_product_urls.csv",
		18: "cheese_product_urls.csv",
		19: "chem_product_urls.csv",
		20: "app_product_urls.csv",
		21: "dairy_product_urls.csv",
		22: "dry_product_urls.csv",
		23: "equip_product_urls.csv",
		24: "disp_product_urls.csv",
		25: "produce_product_urls.csv",
		26: "frozen_product_urls.csv",
		29: "oil_product_urls.csv",
		30: "pork_product_urls.csv",
		31: "poultry_product_urls.csv",
		32: "processed_product_urls.csv",
		33: "seafood_product_urls.csv",
		34: "specialty_product_urls.csv",
		35: "salad_product_urls.csv",
		37: "ms_product_urls.csv",
	}
	DATA_FILE_NAMES = {
		15: "beef_product_data.csv",
		16: "bev_product_data.csv",
		17: "fruit_product_data.csv",
		18: "cheese_product_datas.csv",
		19: "chem_product_data.csv",
		20: "app_product_data.csv",
		21: "dairy_product_data.csv",
		22: "dry_product_data.csv",
		23: "equip_product_data.csv",
		24: "disp_product_data.csv",
		25: "produce_product_data.csv",
		26: "frozen_product_data.csv",
		29: "oil_product_data.csv",
		30: "pork_product_data.csv",
		31: "poultry_product_data.csv",
		32: "processed_product_data.csv",
		33: "seafood_product_data.csv",
		34: "specialty_product_data.csv",
		35: "salad_product_data.csv",
		37: "ms_product_data.csv",
	}
	CHOSEN_CATEGORY = CATEGORY_IDS["GROCERY_DRY"]
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
		'home_directory': DEFAULT_DIRECTORY,
		'url': 'https://order.usfoods.com/desktop/search/browse',
		'search_term': 'Spices',
	}

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}

	def get_category_ids(self):
		return self.CATEGORY_IDS

	def get_category_names(self):
		return self.CATEGORY_NAMES

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
			# Get the first item's product assets
			product_assets = response_data['summary'].get('productAssets', {})
			product_images = product_assets.get('productImages', {})

			# Get the first image group (C1CD, C1CB, etc.)
			if product_images:
				first_image_group = next(iter(product_images.values()))
				renditions = first_image_group.get('renditions', {})

				# Try to get the Original image first, then fall back to other sizes
				for size in ['Original', 'Large', 'Medium', 'Small', 'XLarge', 'Thumbnail']:
					if size in renditions:
						return renditions[size]

		except (KeyError, IndexError, AttributeError) as e:
			print(f"⛔️⛔️⛔️Error extracting image URL: {e}")

		return None

	def process_product_detail(self, product_data, row_spec):
		print("processing product data from response...")
		# print(product_data)
		if product_data:
			try:
				product_name = product_data.get('summary', {}).get('productDescTxtl', '')
				print(f"product_name: {product_name}")
				product_sku = product_data.get('summary', {}).get('productNumber', '')
				print(f"product_sku: {product_sku}")
				product_ps = product_data.get('summary', {}).get('salesPackSize', '')
				print(f"product_ps: {product_ps}")
				product_brand = product_data.get('summary', {}).get('brand', {})
				print(f"product_brand: {product_brand}")
				product_image = self.get_first_image_url(product_data)
				print(f"product_image: {product_image}")
				row_spec["name"] = product_name
				row_spec["pack_size"] = product_ps
				row_spec["brand"] = product_brand
				row_spec["image"] = product_image
				# print(row_spec)
				row_spec['extra_data_1'] = json.dumps(product_data)
			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing product additional data Complete...")
		return row_spec

	def get_product_data(self, data, row_spec):
		print("processing product data from response...")
		# print(data)
		if data:
			try:
				# TODO implement
				print("processing product data from response...")
			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing product additional data Complete...")
		return row_spec

	def get_classification(self, product_data, row_spec):
		print("processing product classification...")
		if product_data:
			row_spec['classCode'] = product_data.get('summary').get('classCode')
			row_spec['classDescription'] = product_data.get('summary').get('classDescription')
			row_spec['categoryCode'] = product_data.get('summary').get('categoryCode')
			row_spec['categoryDescription'] = product_data.get('summary').get('categoryDescription')
			row_spec['groupCode'] = product_data.get('summary').get('groupCode')
			row_spec['groupDescription'] = product_data.get('summary').get('groupDescription')
			print(f"classification completed using product data...{row_spec['classCode']}")
		else:
			try:
				classification = self.wait.until(
					EC.presence_of_element_located((By.CSS_SELECTOR, 'section.desktop-tablet-classification-details'))
				)
				self.driver.execute_script("arguments[0].scrollIntoView();", classification)
				classification_list = classification.find_elements(By.TAG_NAME, 'li')
				level_1 = classification_list[0].text.strip()
				print(f" Level 1: {level_1}")
				level_2 = classification_list[1].text.strip()
				print(f" Level 2: {level_2}")
				level_3 = classification_list[2].text.strip()
				print(f" Level 3: {level_3}")
				row_spec['classCode'], row_spec['classDescription'] = self.split_code_and_text(level_1)
				row_spec['categoryCode'], row_spec['categoryDescription'] = self.split_code_and_text(level_2)
				row_spec['groupCode'], row_spec['groupDescription'] = self.split_code_and_text(level_3)
			except Exception as e:
				print(f"⛔️⛔️⛔️Error processing product classification: {e}")
			print("processing product classification Complete...")

		return row_spec

	def get_manufacturer(self, data, row_spec):
		# Scrape the section that contains the manufacturer information. It is in an unordered list

		level_1 = ''
		level_2 = ''
		level_3 = ''
		print("processing product manufacturer...")
		if data:
			try:
				level_1 = data.get('manufacturerName')
				level_2 = data.get('manufacturerProductNumber')
				html = f"<td>{level_1}</td><td>{level_2}</td><td>{level_3}</td>"
			except Exception as e:
				print(f"⛔️️ Error processing product overview from data: {e}")
		else:
			try:
				container = self.wait.until(
					EC.presence_of_element_located((By.CSS_SELECTOR, 'section.desktop-tablet-manufacturer'))
				)
				self.driver.execute_script("arguments[0].scrollIntoView();", container)
				ul_list = container.find_elements(By.TAG_NAME, 'li')
				level_1 = ul_list[0].text.replace("Manufacturer: ", "").strip()
				print(f"  Level 1: {level_1}")
				level_2 = ul_list[1].text.replace("Manufacturer Product #:", "").strip()
				print(f"  Level 2: {level_2}")
				row_spec['manufacturer_name'] = level_1
				row_spec['manufacturer_sku'] = level_2
			except Exception as e:
				print(f"⛔️⛔️⛔️Error processing product manufacturer from scrape:")
		print("processing product manufacturer Complete...")
		return row_spec

	def get_description(self, data, row_spec):
		print("processing product overview...")
		description = ''
		level_1 = ''
		level_2 = ''
		level_3 = ''
		if data:
			try:
				description = data.get('additionalDescription')
				level_1 = data.get('countryOfOriginGrownHarvested')
				level_2 = data.get('countryOfOriginProcessed')
				row_spec['description'] = description
				row_spec['countryOfOriginGrownHarvested'] = level_1
				row_spec['countryOfOriginProcessed'] = level_2
			except Exception as e:
				print(f"⛔️️ Error processing product overview from data: {e}")
		else:
			try:
				container = self.wait.until(
					EC.presence_of_element_located((By.CSS_SELECTOR, 'div.overview-benefits section'))
				)
				self.driver.execute_script("arguments[0].scrollIntoView();", container)
				try:
					description = container.find_element(By.CSS_SELECTOR, 'p').text.strip()
				except Exception as e:
					print(f"  Description not found:")

				processing_list = container.find_elements(By.TAG_NAME, 'li')
				level_1 = processing_list[0].text.strip()
				print(f"  Level 1: {level_1}")
				level_2 = processing_list[1].text.strip()
				print(f"  Level 2: {level_2}")
				level_3 = processing_list[2].text.strip()
				print(f"  Level 3: {level_3}")
				row_spec['description'] = level_1
				row_spec['countryOfOriginGrownHarvested'] = level_2
				row_spec['countryOfOriginProcessed'] = level_3
			except Exception as e:
				print(f"⛔️️ Error processing product overview from scrape:")

		print("processing product overview Complete...")
		return row_spec

	def get_additional_info(self, data, row_spec):
		"""
				Processes the product's additional data from the API response and stores it into `row_spec`.
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
				row_spec['standardComparisonUOM'] = data.get('standardComparisonUOM')
				row_spec['standardComparisonValue'] = data.get('standardComparisonValue')
				row_spec['volume'] = data.get('volume')
				row_spec['volumeUnits'] = data.get('volumeUnits')
				row_spec['yield'] = data.get('yield')
				row_spec['yieldUOM'] = data.get('yieldUOM')
				row_spec['extra_data_2'] = json.dumps(data)
			except Exception as e:
				print(f"⛔️⛔️⛔️Error processing additional data: {e}")

		print("processing product additional data Complete...")
		return row_spec

	# ************************************************************************

	def process_product_list_search_api(self, main_window, html, category, sub_category, url_output_file):
		# Build a list of product URLs
		detail_urls = []
		all_urls = []

		product_wrappers = self.wait.until(
			EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-wrapper'))
		)
		print(f"Found Product Wrapper: {len(product_wrappers)}")

		for request in self.driver.requests:
			# https://panamax-api.ama.usfoods.com/product-domain-api/v2/products
			if request.response and "commerce/v2/search" in request.url:  # Filter for API requests
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
						detail_urls = [product['clickUri'] for product in data['products']]
						self.save_urls_to_csv(detail_urls, category, sub_category)
					else:
						print(f"Response Body (Text): {body}")
					all_urls.extend(detail_urls)

				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding response body: {e}")
		print(f"========= Number of products: {len(all_urls)}")
		del self.driver.requests
		return html, all_urls

	def process_product_list_search_p_api(self, main_window, html, category, sub_category, url_output_file):
		# Build a list of product URLs
		detail_urls = []

		product_wrappers = self.wait.until(
			EC.presence_of_all_elements_located((By.TAG_NAME, 'app-selectable-search-result'))
		)
		print(f"Found Product Wrapper: {len(product_wrappers)}")

		for request in self.driver.requests:
			# https://panamax-api.ama.usfoods.com/product-domain-api/v1/search?worksWellWith=true
			if request.response and "domain-api/v1/search" in request.url:  # Filter for API requests
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
						# url = f"https://order.usfoods.com/desktop/products/{product_sku}?isSearch=true"
						detail_urls = [f"https://order.usfoods.com/products/{product}" for product in
						               data['productNumbers']]
						self.save_urls_to_csv(detail_urls, category, sub_category)
					else:
						print(f"Response Body (Text): {body}")

				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding response body: {e}")
		print(f"========= Number of products: {len(detail_urls)}")
		del self.driver.requests
		return html, detail_urls

	@staticmethod
	def create_interceptor(max_api_products=MAX_API_PRODUCTS):
		def interceptor(request):
			# https://usfoodsproduction10upnbvk4.org.coveo.com/rest/organizations/usfoodsproduction10upnbvk4/commerce/v2/search
			# https://panamax-api.ama.usfoods.com/product-domain-api/v1/search?worksWellWith=true
			if request.method == 'POST' and 'commerce/v2/search' in request.url:  # Replace 'your_target_url'
				print(f"👽👽👽Intercepting request: {request.url}")
				# Get the current POST data
				current_data = request.body.decode('utf-8')
				print(f"Original POST data: {current_data}")

				try:
					payload = json.loads(current_data)
					page = payload.get('page', {})
					if int(page) == 0:
						payload['page'] = 0  # Replace 'key_to_change' and 'new_value'
						payload['perPage'] = max_api_products  # Replace 'key_to_change' and 'new_value'
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
		"""Scrape products from the website"""
		html = ""
		all_urls = []
		# Use the options with fallback to module-level variables
		test_categories = self.options.get('test_categories', self.TEST_CATEGORIES)
		max_products = self.options.get('max_products', self.MAX_API_PRODUCTS)
		category_to_process = self.options.get('category_to_process', 0)
		chosen_category = self.options.get('chosen_category', self.CHOSEN_CATEGORY)
		chosen_category_id = self.CATEGORY_IDS[chosen_category]
		category_name = self.options.get('chosen_category', self.CATEGORY_NAMES[chosen_category_id])
		url_output_file = self.options.get('url_output_file', self.URL_FILE_NAMES[chosen_category_id])
		# data_output_file = options.get('data_output_file', DATA_FILE_NAMES[chosen_category_id])
		# csv_start_row = options.get('csv_start_row', CSV_START_ROW)

		category_URL = f"https://order.usfoods.com/desktop/search/browse/categories/{chosen_category_id}"
		# Wait for the page to be fully loaded
		wait = WebDriverWait(self.driver, 10)
		print(f"Scraping products from category {category_name}")
		print(f"Output File Name: {url_output_file}")
		self.driver.get(category_URL)
		self.driver.request_interceptor = self.create_interceptor(max_products)
		total_products = 0
		loop_counter = 0
		category_found_count = 1

		html_table = "<table><tr><th>URL</th><th>Name</th><th>SKU</th><th>PS</th><th>Brand</th><th>Image</th><th>Category</th><th>Sub Category</th><th>Classification 1</th><th>Classification 2</th><th>Classification 3</th><th>Description</th><th>Desc 1</th><th>Desc 2</th><th>Desc 3</th><th>Man 1</th><th>Man 2</th><th>Man 3</th></tr></<tbody>"
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
			# Target URL for the product category

			# Wait for product cards to be present and visible
			sub_categories = wait.until(
				EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ion-card.md.hydrated'))
			)
			print(f"Page title: {self.driver.title}")

			category_found_count = len(sub_categories)
			print(f"Found {category_found_count} categories to process...")

			# Store the main window handle
			main_window = self.driver.current_window_handle

			try:
				# for category_index, sub_category in enumerate(sub_categories[loop_counter:loop_counter]):
				sub_category = sub_categories[loop_counter - 1]
				print(f"\nProcessing category {loop_counter} of {category_found_count}...")
				self.driver.execute_script("arguments[0].scrollIntoView();", sub_category)
				name_element = WebDriverWait(sub_category, 10).until(
					EC.presence_of_element_located((By.CLASS_NAME, 'browse-sub-category-card-description'))
				)
				sub_category_name = name_element.text.strip()
				print(f"Category name: {sub_category_name}")
				html += f"<h2>Category Name: {sub_category_name}</h2>"

				# Click on the category to open detail page
				name_element.click()
				print("Clicked on category, waiting for detail page to load...")

				# Wait for the detail page to load
				time.sleep(12)  # Wait for the page to load
				print("Looking for Page: Search New | US Foods")
				print(f"Found:           {self.driver.title}")
				print(f"Current URl: {self.driver.current_url}")

				# Find all window handles and switch to the new window if it opens in a new tab
				if len(self.driver.window_handles) > self.TEST_TABS:
					print("must be a tab...")
					for handle in self.driver.window_handles:
						if handle != main_window:
							self.driver.switch_to.window(handle)
							break
				try:
					# There are 2 URLS to look for
					# https://order.usfoods.com/desktop/search2?correlationId=43939&facetFilters=ec_category:Cheese%252BCHEESE%252C%2520CHEDDAR
					# https://order.usfoods.com/desktop/search?searchFilterProperties=336&categoryId=336&pageType=browse&originSearchPage=catalog
					if "search2" in self.driver.current_url:
						print("Found search2 page")
						time.sleep(6)
						html, detail_urls = self.process_product_list_search_api(main_window, html,
						                                                    category_name, sub_category_name,
						                                                    url_output_file)
					else:
						print("Found search page")
						time.sleep(6)
						html, detail_urls = self.process_product_list_search_p_api(main_window, html,
						                                                      category_name, sub_category_name,
						                                                      url_output_file)
					products_found_count = len(detail_urls)
					html += f"<div>Found {products_found_count} products for category {sub_category_name}</div>"
					print(f"Found {products_found_count} products for category {sub_category_name}")
					total_products += products_found_count

					all_urls.extend(detail_urls)

				except Exception as e:
					print(f"****************** ⛔️⛔️⛔️ Error getting details: {e}")
					html += f"<div>Name: {sub_category_name} (Error getting details) {loop_counter}</div>"
				# driver.quit()
				# return html

				# Close the detail tab and switch back to the main window
				# if len(driver.window_handles) > 2:
				# 	driver.close()
				# 	driver.switch_to.window(main_window)

				self.driver.back()
				print(f"Going back to get next category: {self.driver.title}")
				# Wait before processing next category
				time.sleep(3)

			except Exception as e:
				print(f"⛔️⛔️⛔️Error processing category: {e}")
				continue

		time.sleep(3)

		html_table += "</tbody></table>"
		# html_table_to_csv(html_table)
		html += f"<h2>Total products found: {total_products}</h2>"
		html += html_table
		print(f"Total products found: {len(all_urls)}")
		return html

	def get_product_details(self, url, row_spec=None):
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print("processing product detail page")
		del self.driver.requests
		print(f"Loading page...{url}")
		start_time = time.perf_counter()
		self.driver.get(url)
		end_time = time.perf_counter()

		elapsed_time = end_time - start_time
		print(f"Elapsed time: {elapsed_time} seconds")

		self.driver.execute_script("document.body.style.zoom = '50%'")
		print(f"Loaded page...{self.driver.title}")
		data = ''
		request = self.driver.wait_for_request('domain-api/v1/productdetail', 30)
		if request.response and "domain-api/v1/productdetail" in request.url:  # Filter for API requests
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

		# Check to see we got a product details response. This only populates part of the product detail page
		product_data = ''
		for request in self.driver.requests:
			if data and product_data:
				break
			# https://panamax-api.ama.usfoods.com/product-domain-api/v1/search?worksWellWith=true
			if request.response and "domain-api/v1/productdetail" in request.url:  # Filter for API requests
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
					print(f"⛔️⛔️⛔️Error decoding data from response body: {e}")
			if request.response and "product-domain-api/v2/products" in request.url and not product_data:  # Filter for API requests
				print(f"URL: {request.url}")
				print(f"Status Code: {request.response.status_code}")
				print(f"Content Type: {request.response.headers.get('Content-Type')}")

				# Decode the response body (it's bytes by default)
				try:
					# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
					body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

					# If the body is JSON, parse it
					if 'application/json' in request.response.headers.get('Content-Type', ''):
						response_data = json.loads(body)

						# Check if the response contains items and it's a list
						if 'items' in response_data and isinstance(response_data['items'], list):
							# Find the product with matching SKU
							target_sku = str(row_spec.get('sku', '')).strip()
							for item in response_data['items']:
								# Check both string and integer SKU matches
								if (str(item.get('summary', {}).get('productNumber', '')) == target_sku or
										str(item.get('summary', {}).get('productNumber')) == str(
											int(target_sku) if target_sku.isdigit() else '')):
									product_data = item
									print(f"✅✅✅ Found matching product: {target_sku}")
									# print(item)
									break
							else:
								print(f"No matching product found for SKU: {target_sku}")
						else:
							print("❌ No items found in the API response")

				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding product data from response body: {e}")
		print(f"Product Details Captured")

		if product_data:
			# print(f"Product Data: {product_data}")
			row_spec["content_url"] = url
			row_spec = self.process_product_detail(product_data, row_spec)
		else:
			# Let's scrape the product page
			container = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, 'ion-row.pdp-summary-info'))
			)
			product_brand = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, 'div.pdp-summary-brand-text'))
			).text.strip()
			product_name = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, 'div.pdp-summary-desc-text'))
			)
			# Scrape other information from the product page
			product_name = product_name.text.strip()
			print(product_name)

			other_info = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, 'div.pdp-summary-other-info-container'))
			)

			product_sku = other_info.find_element(By.TAG_NAME, 'p').text

			product_ps = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, 'p.ng-star-inserted'))
			).text.strip()
			product_sku = product_sku.replace("#", "").strip()
			print(product_sku)
			print(product_ps)

			print("Getting image")
			product_image = ""
			try:
				product_image = container.find_element(By.CSS_SELECTOR, "div.main-image-container img").get_attribute(
					"src")
			except Exception as e:
				print(f"⛔️⛔️⛔️Error getting product image:")
			row_spec["content_url"] = url
			row_spec["name"] = product_name
			row_spec["pack_size"] = product_ps
			row_spec["brand"] = product_brand
			row_spec["image"] = product_image

		# These use the data if available, then try to scrape from the page
		row_spec = self.get_classification(product_data, row_spec)
		row_spec = self.get_description(data, row_spec)
		row_spec = self.get_manufacturer(data, row_spec)
		row_spec = self.get_additional_info(data, row_spec)

		del self.driver.requests
		return row_spec