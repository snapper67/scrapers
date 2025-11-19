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

class BigCommerceScraper(Scraper):
	SCRAPER_TYPE = 'BigCommerce'
	BIGCOMMERCE_PRODUCT_DATA_SPEC = {
		'shop_id': '',
		'productId': '',
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

	def __init__(self, options=None):
		super().__init__(options)
		self.options['home_directory'] = self.DEFAULT_DIRECTORY
		# self.options['base_url'] = self.BASE_URL
		self.PRODUCT_DATA_SPEC = self.BASE_PRODUCT_DATA_SPEC.copy()
		for spec in self.BIGCOMMERCE_PRODUCT_DATA_SPEC:
			self.PRODUCT_DATA_SPEC[spec] = ''
		print(self.PRODUCT_DATA_SPEC)

	def get_category_ids(self):
		return self.CATEGORY_IDS

	def get_category_names(self):
		return self.CATEGORY_NAMES

	def get_category_urls(self):
		return self.CATEGORY_URLS

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
	def get_next_page(self):
		try:
			paging = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination-list'))
			)
			print("Checking 1")
			next_disabled = paging.find_element(By.CSS_SELECTOR, '.pagination-item.pagination-item--next')
			class_attribute = next_disabled.get_attribute("class")
			classes = class_attribute.split()
			print(next_disabled)
			print("Checking 2")
			if not 'disabled' in classes:
				print("Clicking next")
				next_disabled.find_element(By.TAG_NAME, 'a').click()
				print("Going to next page")
				return True
			else:
				print("Next is disabled")
				return False
		except Exception as e:
			print("There is no next page")
			return False

	def get_price(self, data, row_spec):
		print("get_price()")
		return row_spec

	def get_more_data(self, data, row_spec):
		print("get_more_data()")
		return row_spec

	def get_category_page(self, url, category_name, sub_category_name, sub_sub_category_name):
		print("get_category_page()")
		main_window = self.driver.current_window_handle
		html = ''
		total_products = 0
		all_urls = []
		detail_urls = []
		page_count = 0
		try:
			self.driver.get(url)

			# Update URL from the redirect
			url = self.driver.current_url
			base_url = url
			print(f"Current URl: {self.driver.current_url}")

			# Find all window handles and switch to the new window if it opens in a new tab
			if len(self.driver.window_handles) > self.TEST_TABS:
				print("must be a tab...")
				for handle in self.driver.window_handles:
					if handle != main_window:
						self.driver.switch_to.window(handle)
						break
			next_page = True
			while next_page:
				page_count += 1
				try:
					# Wait for page to load
					detail_urls = []
					if url in self.driver.current_url:
						print("Found products page")
						html_line, detail_urls = self.get_products_from_html()
					products_found_count = len(detail_urls)
					all_urls.extend(detail_urls)
					html += f"<div>Found {products_found_count} products for category {category_name} page {page_count}</div>"
					print(f"Found {products_found_count} products for category {category_name} page {page_count}")
					total_products += products_found_count

					next_page = self.get_next_page()
				except Exception as e:
					print(f"****************** ⛔️⛔️⛔️ Error getting details: {e}")
					html += f"<div>Name: {sub_category_name} (Error getting details)</div>"

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing category: {e}")

		html += f"<h2>Total products found: {total_products}</h2>"
		print(f"Total Products {len(all_urls)}")

		# write all the urls to file
		self.save_urls_to_csv(all_urls, category_name, sub_category_name, sub_sub_category_name)
		# return results to results page
		return all_urls, html

	def get_products_from_html(self):
		print("get_products_from_html")

		container = self.wait.until(
			EC.presence_of_element_located((By.CSS_SELECTOR, '.productGrid'))
		)
		print("got container")
		products = container.find_elements(By.CSS_SELECTOR, ".product")

		print(f"products found: {len(products)}")
		detail_urls = [product.find_element(By.CSS_SELECTOR, '.card-figure__link').get_attribute("href") for product in products]
		return '', detail_urls

	def get_product_data(self, data, row_spec):
		print("processing product data from response...")
		print(data)
		if data:
			try:
				row_spec['sku'] = ''
				row_spec = self.parse_product_schema(data, row_spec)
				row_spec = self.get_price(data, row_spec)
				row_spec = self.get_more_data(data, row_spec)
			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing get_product_data Complete...")
		return row_spec

	def get_packs_sizes(self, row_spec):
		"""
		Get the packs sizes from the product page
		Convert row_spec into a list of row_specs
		Allow the calling function to write the last one
		"""
		print("get_packs_sizes()")
		specs = []
		try:
			for request in self.driver.requests:
				category_url_part = "/remote/v1/product-attributes/"
				row_spec_base = row_spec.copy()
				if request.response and category_url_part in request.url:
					print(f"URL: {request.url}")
					print(f"Status Code: {request.response.status_code}")
					content_type = request.response.headers.get('Content-Type', '')
					print(f"Content Type: {content_type}")

					try:
						# Decode the response body
						body = decode(
							request.response.body,
							request.response.headers.get('Content-Encoding', 'identity')
						)

						if not body:
							print("Empty response body")
							continue

						# Clean the JSON string before parsing
						if 'application/json' in content_type:
							try:
								# Try to parse the JSON directly first
								data = json.loads(body)
							except json.JSONDecodeError as e:
								print(f"Initial JSON parse failed, attempting to clean and retry: {str(e)}")
								try:
									# Clean the JSON string and try again
									cleaned_body = self.clean_json_string(body)
									data = json.loads(cleaned_body)
								except json.JSONDecodeError as e2:
									print(f"❌ Failed to parse JSON even after cleaning: {str(e2)}")
									print(f"Problematic JSON (first 500 chars): {cleaned_body[:500]}")
									return specs  # Return empty list if we can't parse the JSON

							print("Successfully parsed JSON data")
							data = data.get('data', {})

							if not data:
								print("No data found in response")
								continue

							price = data.get('price', {})
							row_spec_base['sku'] = data.get('sku', '')
							row_spec_base['retail_price'] = price.get('without_tax', {}).get('value', '')
							row_spec_base['pack_size'] = data.get('weight', {}).get('formatted', '')

							if row_spec_base['sku']:  # Only add if we have a valid SKU
								specs.append(row_spec_base)
								print(f"Added product: {row_spec_base['sku']}")
							else:
								print("Skipping product - missing SKU")

					except json.JSONDecodeError as e:
						print(f"❌ JSON decode error: {str(e)}")
						print(f"Response body (first 500 chars): {str(body)[:500]}")
					except Exception as e:
						print(f"❌ Error processing response: {str(e)}")
						import traceback
						traceback.print_exc()

		except Exception as e:
			print(f"❌ Unexpected error in get_packs_sizes: {str(e)}")
			import traceback
			traceback.print_exc()

		print(f"Found {len(specs)} pack sizes")
		return specs


	def get_product_details(self, url, row_spec=None):
		"""
		Product detail pages are rendered server-side. Page must be manually scraped.
		Additional packages also need to be pulled or visited from the dropdown
		To get the product detail page, visit the product detail page and then pull the additional packages
		"""
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print(f"{self.__class__}->get_product_details()")
		del self.driver.requests

		print(f"Loading page: {url}")
		self.driver.get(url)
		# request = self.driver.wait_for_request("/remote/v1/product-attributes/")
		time.sleep(3)

		row_spec['content_url'] = url
		row_spec['id'] = row_spec['sku']
		try:
			data, data_2 = self.get_product_detail_from_schema_in_html(row_spec=row_spec,
			                                                           target="application/ld+json")

			row_spec["extra_data_1"] = json.dumps(data)
			row_spec["extra_data_2"] = json.dumps(data_2)

			row_spec = self.get_product_data(data, row_spec)
			row_spec = self.get_packs_sizes(row_spec)
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing get_product_details: {type(e)}")
			raise
		return row_spec

	# ************************************************************************
	def build_categories_list(self):
		url = self.BASE_URL
		navigation = self.get_navigation_structure(url)
		# self.print_navigation_structure(navigation)
		return f"<div>{navigation}</div>"

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

