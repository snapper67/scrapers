import csv
import json
import re
import string

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
from typing import List, Dict, Any, Optional

from scrapers.scraper import Scraper

class BreakthruScraper(Scraper):
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
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/breakthru'

	BASE_URL = 'https://www.chefswarehouse.com'
	CATEGORIES = [{'id': 'Beer', 'count': 5626, 'filename': 'Beer', 'number': 1},
	              {'id': 'Cider/Perry/Mead', 'count': 439, 'filename': 'CiderPerryMead', 'number': 2},
	              {'id': 'FMB/Coolers/Hard', 'count': 761, 'filename': 'FMBCoolersHard', 'number': 3},
	              {'id': 'Non-Alcoholic', 'count': 835, 'filename': 'Non-Alcoholic', 'number': 4},
	              {'id': 'Non-Alcoholic - Energy Drink', 'count': 45, 'filename': 'Non-Alcoholic_-_Energy_Drink', 'number': 5},
	              {'id': 'Non-Alcoholic - Food Items', 'count': 49, 'filename': 'Non-Alcoholic_-_Food_Items', 'number': 6},
	              {'id': 'Non-Alcoholic - Functional CBD', 'count': 15, 'filename': 'Non-Alcoholic_-_Functional_CBD', 'number': 7},
	              {'id': 'Non-Alcoholic - Functional Other', 'count': 26, 'filename': 'Non-Alcoholic_-_Functional_Other', 'number': 8},
	              {'id': 'Non-Alcoholic - Non Bev Bitters', 'count': 119, 'filename': 'Non-Alcoholic_-_Non_Bev_Bitters', 'number': 9},
	              {'id': 'Non-Alcoholic - Other', 'count': 97, 'filename': 'Non-Alcoholic_-_Other', 'number': 10},
	              {'id': 'Non-Alcoholic - Soda / Soft Drinks', 'count': 215, 'filename': 'Non-Alcoholic_-_Soda__Soft_Drinks', 'number': 11},
	              {'id': 'Non-Alcoholic - Water', 'count': 162, 'filename': 'Non-Alcoholic_-_Water', 'number': 12},
	              {'id': 'Other - Saleables', 'count': 7, 'filename': 'Other_-_Saleables', 'number': 13},
	              {'id': 'SP - Tequila/Mezcal/Agave Spirits', 'count': 1926, 'filename': 'SP_-_TequilaMezcalAgave_Spirits', 'number': 14},
	              {'id': 'Sp - Brandy', 'count': 589, 'filename': 'Sp_-_Brandy', 'number': 15},
	              {'id': 'Sp - Cognac', 'count': 314, 'filename': 'Sp_-_Cognac', 'number': 16},
	              {'id': 'Sp - Cordials & Liqueurs', 'count': 2332, 'filename': 'Sp_-_Cordials__Liqueurs', 'number': 17},
	              {'id': 'Sp - Gin', 'count': 685, 'filename': 'Sp_-_Gin', 'number': 18},
	              {'id': 'Sp - Grain Alcohol', 'count': 29, 'filename': 'Sp_-_Grain_Alcohol', 'number': 19},
	              {'id': 'Sp - Other Spirits', 'count': 129, 'filename': 'Sp_-_Other_Spirits', 'number': 20},
	              {'id': 'Sp - Pisco', 'count': 22, 'filename': 'Sp_-_Pisco', 'number': 21},
	              {'id': 'Sp - Prepared Cocktails', 'count': 1375, 'filename': 'Sp_-_Prepared_Cocktails', 'number': 22},
	              {'id': 'Sp - Rum', 'count': 1140, 'filename': 'Sp_-_Rum', 'number': 23},
	              {'id': 'Sp - Seltzer', 'count': 184, 'filename': 'Sp_-_Seltzer', 'number': 24},
	              {'id': 'Sp - Spirits', 'count': 61, 'filename': 'Sp_-_Spirits', 'number': 25},
	              {'id': 'Sp - Vodka', 'count': 2259, 'filename': 'Sp_-_Vodka', 'number': 26},
	              {'id': 'Sp - Whiskey', 'count': 4562, 'filename': 'Sp_-_Whiskey', 'number': 27},
	              {'id': 'Wine - Cocktail', 'count': 285, 'filename': 'Wine_-_Cocktail', 'number': 28},
	              {'id': 'Wine - Non-Alcoholic', 'count': 121, 'filename': 'Wine_-_Non-Alcoholic', 'number': 29},
	              {'id': 'Wine - Other', 'count': 131, 'filename': 'Wine_-_Other', 'number': 30},
	              {'id': 'Wine - Sake', 'count': 918, 'filename': 'Wine_-_Sake', 'number': 31},
	              {'id': 'Wine - Seltzer', 'count': 64, 'filename': 'Wine_-_Seltzer', 'number': 32},
	              {'id': 'Wine - Sparkling  / Champagne', 'count': 2491, 'filename': 'Wine_-_Sparkling___Champagne', 'number': 33},
	              {'id': 'Wine - Specialty', 'count': 701, 'filename': 'Wine_-_Specialty', 'number': 34},
	              {'id': 'Wine - Still Table', 'count': 29516, 'filename': 'Wine_-_Still_Table', 'number': 35}]
	CATEGORY_IDS = {
		"BEER": 1,
		"VODKA": 2,
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
		1: "Beer",
		2: "SP Vodka",
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
		1: "Beer",
		2: "https://app.salsify.com/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products?filter=%3D%27Product%20Category%27%3A%27Sp%20-%20Vodka%27&page=1",
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
		1: "beer_product_urls.csv",
		2: "vodka_product_urls.csv",
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
		1: "beer_product_data.csv",
		2: "vodka_product_data.csv",
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
		'get_categories': False,
		'scrape_products': False,
		'process_csv': False,
		'reprocess_csv': False,
		'dedupe_csv': False,
		'count_csv': False,
		'process_extra': False,
		'test_products': TEST_PRODUCTS,
		'max_products': 30,
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

	def get_categories(self):
		return self.CATEGORIES

	def get_category_names(self):
		return self.CATEGORY_NAMES

	def get_category_urls(self):
		return self.CATEGORY_URLS

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
		print("get_first_image_url()")
		try:
			assets = response_data.get('profile_asset', {})
			print("assets: ", assets)
			# If there are assets, get the first one's URL
			if assets:
				# Get the first asset and extract the URL
				if isinstance(assets, dict):
					return assets.get('download_url', '')

		except Exception as e:
			print(f"Error extracting image from viewModel.assets: {str(e)}")

		return ''

	def get_product_categories(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
		"""
		Extract product categories from search response data.

		Args:
			data: Dictionary containing the search response data (already parsed JSON)

		Returns:
			List of dictionaries containing category information with 'id' and 'name' keys
		"""
		try:
			# Ensure data is a dictionary
			if not isinstance(data, dict):
				print("Error: Expected a dictionary input")
				return []

			# Initialize categories list
			categories = []
			i = 0
			# print("data: ", data)

			if 'meta' in data:
				print("found meta")
				data = data['meta']
			# Check if there are facets in the response
			if 'facets' in data:
				print("found facets")
				for facet in data['facets']:

					print("facet")
					print(facet)
					if facet.get('property_id') == 'Product Category':
						print('property_id')
						print(facet.get('property_id'))
						# Extract category values from the facet
						children = facet.get('children', [])
						print("children")
						print(children)
						for child in children:
							i = i + 1
							if 'value' in child:
								categories.append({
									'id': child['value'],
									'count': child.get('count', 0),
									'filename': self.make_filename_safe(child['value']),
									'number': i
								})
						break  # Found the category facet, no need to check others

			# If no facets found, try to extract from products
			if not categories and 'products' in data:
				# Create a set to track unique categories
				seen_categories = set()

				for product in data['products']:
					for prop in product.get('properties', []):
						if prop.get('id') == 'Product Category' or prop.get('name') == 'Product Category':
							for value in prop.get('values', []):
								if 'name' in value and value['name'] not in seen_categories:
									seen_categories.add(value['name'])
									categories.append({
										'id': value.get('id', value['name'].lower().replace(' ', '-')),
										'name': value['name'],
										'count': 1  # We can't determine count without facets
									})

			return sorted(categories, key=lambda x: x['id'].lower())

		except (KeyError, AttributeError) as e:
			print(f"Error extracting categories: {e}")
			return []

	def get_product_data(self, data, row_spec):
		print("processing product data from response...")
		# print(product_data)
		if data:
			try:
				row_spec["extra_data_1"] = json.dumps(data)
				print(f"Getting Name: ")
				row_spec["name"] = data.get("name", "")
				row_spec = self.get_description(data, row_spec)
				# print(row_spec["description"])
				row_spec["image"] = self.get_first_image_url(data)
				# Get Brand
				title = data.get('title', {})
				# print(f"title: {title}")
				if title:
					pre_title = title.get('pre_title', {})
					if pre_title:
						# print(f"pre_title: {pre_title}")
						row_spec["brand"] = pre_title.get('values', [])[0].get('name', '')
				property_groups = data.get('property_groups', [])
				# print(f"property_groups: {property_groups}")
				if property_groups:
					for property_group in property_groups:
						if property_group.get('name', '') == 'Product Details':
							properties = property_group.get('properties', [])
							for property in properties:
								# print(f"property: {property}")
								if property.get('name', '') == 'Bottles Per Case':
									# print(f"Bottles Per Case: {property}")
									row_spec["pack_size"] = property.get('values', [])[0].get('name', '') + " / Case"
			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing product data Complete...")
		return row_spec

	def get_description(self, data, row_spec):
		print("processing product overview...")
		description = ''
		if data:
			try:
				print(f"Getting Summary: ")
				summary = data.get('summary', {})
				# print(f"summary: {summary}")
				description = summary.get('description', {})
				if description:
					row_spec["description"] = description.get('values', [])[0].get('name', '')
			except Exception as e:
				print(f"⛔️️ Error processing product overview from data: {e}")

		print("processing product overview Complete...")
		return row_spec

	# ************************************************************************

	def process_product_list_search_api(self, html, category, sub_category=None):
		# Build a list of product URLs
		all_urls = []
		i = 0
		still_looking = True
		# Until we find a page with less than 250 products, keep sending the request and bumping the page size
		while still_looking and i < self.options['max_products']:
			i = i + 1

			self.options['url_output_file'] = category.get('filename', '') + "_product_urls.csv"
			print(f"category_name : {category}")
			url = f"https://app.salsify.com/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products?filter=%3D%27Product%20Category={category_name}&page={i}"

			self.driver.request_interceptor = self.create_interceptor(i, category)
			self.driver.get(url)

			request_filter = 'catalogs/api/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products?'
			request_filter2 = f"page={i}"
			# https://app.salsify.com/catalogs/api/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products?filter=%3D%27Product%20Category%27%3A%27Beer%27&page=1&per_page=36&product_identifier_collection_id=&query=
			request = self.driver.wait_for_request(request_filter)
			if request.response and request_filter in request.url and request_filter2 in request.url:  # Filter for API requests
				print(f"URL: {request.url}")
				print(f"Status Code: {request.response.status_code}")
				print(f"Content Type: {request.response.headers.get('Content-Type')}")

				# Decode the response body (it's bytes by default)
				try:
					body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

					# If the body is JSON, parse it
					if 'application/json' in request.response.headers.get('Content-Type', ''):
						data = json.loads(body)
						# https://app.salsify.com/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products/9258080
						if 'products' in data:
							detail_urls = [
								f"https://app.salsify.com/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products/{product['id']}"
								for product in data['products']]
							print(f"== Number of products: {len(detail_urls)}")
							all_urls.append(detail_urls)
							self.save_urls_to_csv(detail_urls, category, '')
							print(f"=== Number of products: {len(detail_urls)}")

							if len(detail_urls) < 250:
								still_looking = False
						else:
							print(f"Response products missing: {'products' in data} ")
							print(f"data: {data} ")
					else:
						print(f"Response Body (Text): ")
						print(f"Response not JSON  ")
				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

			del self.driver.request_interceptor
			del self.driver.requests
		return html, all_urls

	def process_subcategories(self):
		# Build a list of product URLs
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

	def build_categories_list(self):
		# Run on all to get a category list then copy the list to CATEGORIES
		url = "https://app.salsify.com/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products?filter=%3D&page=1"
		self.driver.get(url)
		request = self.driver.wait_for_request("catalogs/api/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products")
		data = None
		if request.response and "catalogs/api/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products" in request.url:  # Filter for API requests
			print(f"Found response :")
			try:
				# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
				body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

				# If the body is JSON, parse it
				if 'application/json' in request.response.headers.get('Content-Type', ''):
					data = json.loads(body)
				else:
					print(f"Response not JSON :")
			except Exception as e:
				print(f"⛔️⛔️⛔️Error decoding search response body: {e}")
		categories = self.get_product_categories(data)
		print(f"categories : {categories}")
		del self.driver.requests

		return categories

	@staticmethod
	def create_interceptor(page=0, category_name=''):
		def interceptor(request):
			# https://app.salsify.com/catalogs/api/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products?filter=%3D%27Product%20Category%27%3A%27Beer%27&page=1&per_page=36&product_identifier_collection_id=&query=
			# Intercept and modify GET requests to update per_page parameter
			request_filter = f"page={page}"
			if request.method == 'GET' and 'catalogs/api/catalogs/' in request.url and request_filter in request.url:
				from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
				print(f"👽👽👽Intercepting request: {request.url} Page: {page}")
				# Parse the URL
				parsed_url = urlparse(request.url)
				query_params = parse_qs(parsed_url.query)
				
				# Update per_page parameter
				query_params['per_page'] = ['250']
				query_params['page'] = [str(page)]
				query_params['filter'] = "='Product Category':'" + category_name + "'"
				print(query_params['filter'])
				# Rebuild the query string
				new_query = urlencode(query_params, doseq=True)
				
				# Reconstruct the URL with the updated query string
				new_url = urlunparse(parsed_url._replace(query=new_query))
				
				# Update the request URL
				request.url = new_url
				print(f"👽👽👽 Updated URL: {request.url}")
				
			# Existing POST request handling

		return interceptor

	def build_products_list(self):
		"""Scrape products from the website"""
		print(f"build_products_list()")
		html = ''
		html_table = ''
		all_urls = []
		categories = []
		chosen_category = int(self.options.get('chosen_category', 0))
		test_categories = self.options.get('test_categories', 100)
		test_products = self.options.get('test_products', 0)
		category_count = 0
		if int(self.options['chosen_category']) == 0:
			categories = self.CATEGORIES
			print(f"All Categories ")
		else:
			for category in self.CATEGORIES:
				if int(category.get('number', '')) == chosen_category:
					categories = [category]  # Only process the chosen category
					print(f"Category found : {categories}")
					break
		del self.driver.requests
		for category in categories:
			category_count = category_count + 1
			category_name = category.get('id', '')
			if category_count > test_categories:
				break
			html, detail_urls = self.process_product_list_search_api(html, category_name)

			time.sleep(3)

		html_table += "</tbody></table>"
		# html_table_to_csv(html_table)
		html += f"<h2>Total products found: {len(all_urls)}</h2>"
		html += html_table
		print(f"Total products found: {len(all_urls)}")
		return html

	def process_product(self, url, row_spec=None):
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print("processing product detail page")
		print(f"Loading page...{url}")

		# self.driver.execute_script("document.body.style.zoom = '50%'")

		data = ''
		sku = row_spec['sku']
		request_filter_escaped = sku + "/\?expand"
		request_filter = r'catalogs/api/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products/' + sku
		# https://app.salsify.com/catalogs/api/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products/9197779
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
					if 'application/json' in request.response.headers.get('Content-Type', ''):
						data = json.loads(body)
					else:
						print(f"Response Body (Text): {body}")

				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

			# These use the data if available, then try to scrape from the page
			row_spec = self.get_product_data(data, row_spec)

			# print(row_spec)

		except Exception as e:
			print(f"⛔️⛔️⛔️Error waiting for request: {e}")

			# for request in self.driver.requests:
			# 	print(request.url)

		del self.driver.requests
		return row_spec