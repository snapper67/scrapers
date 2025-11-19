import os
from os import times_result

import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

from scrapers.scraper import Scraper, SkuNotFound

"""
	City Hive
	Type: Standard shop website
	Method: 
		Get Categories: Scape Navigation
		Get Products: Scape Product List
		Get Product Manual Scrape and json data from html
	Issues:
		The embedded json data does not have all the information needed to create a product. Data like 
		sku and description are not included in the json data.
"""


class WineSearcherScraper(Scraper):
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
		'timestamp': '',
		# Fields from Southern Glazier
		'extra_data_2': '',
		'vintage': '',
		'varietal': '',
		'appellation': '',
		'pack_size': '',
		'category': '',
		'subcategory': '',
		'subsubcategory': '',
		'bpc': '',
		'supplier': '',
		'producer': '',
		'region': '',
		'country_of_origin': '',
		'alcohol_proof': '',
		'alcohol_by_volume': '',
		'sub-type': '',
		'producer_description': '',
		'container_type': '',
		'closure_type': '',
		'units_per_case': '',
		'packs_per_case': '',
		'units_per_pack': '',
		'outer_pkg': '',
		'product_id': '',
		'option_id': '',
		'page_description': '',
		'page_image': '',
		'page_sku': '',
		'state': '',
	}

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/wine_searcher/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = 'https://empire360.com'
	VENDOR_NAME = 'Wine Searcher'
	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "name": "Red wines",
        "id": 2,
        "url": "https://www.wine-searcher.com/discover/red-wine",
        "subcategories": []
      },
      {
        "name": "White wines",
        "id": 3,
        "url": "https://www.wine-searcher.com/discover/white-wine",
        "subcategories": []
      },
      {
        "name": "Rose wines",
        "id": 4,
        "url": "https://www.wine-searcher.com/discover/rose-wine",
        "subcategories": []
      },
      {
        "name": "Sparkling wines",
        "id": 5,
        "url": "https://www.wine-searcher.com/discover/sparkling-wine",
        "subcategories": []
      },
      {
        "name": "Dessert wines",
        "id": 6,
        "url": "https://www.wine-searcher.com/discover/dessert-wine",
        "subcategories": []
      },
      {
        "name": "Whiskey",
        "id": 8,
        "url": "https://www.wine-searcher.com/discover/whiskey",
        "subcategories": []
      },
      {
        "name": "Rum",
        "id": 9,
        "url": "https://www.wine-searcher.com/discover/rum",
        "subcategories": []
      },
      {
        "name": "Brandy",
        "id": 10,
        "url": "https://www.wine-searcher.com/discover/brandy",
        "subcategories": []
      },
      {
        "name": "Gin",
        "id": 11,
        "url": "https://www.wine-searcher.com/discover/gin",
        "subcategories": []
      },
      {
        "name": "Vodka",
        "id": 12,
        "url": "https://www.wine-searcher.com/discover/vodka",
        "subcategories": []
      },
      {
        "name": "Tequila",
        "id": 13,
        "url": "https://www.wine-searcher.com/discover/tequila",
        "subcategories": []
      },
      {
        "name": "Other Spirits",
        "id": 14,
        "url": "https://www.wine-searcher.com/discover/other-spirits",
        "subcategories": []
      },
      {
        "name": "All wines",
        "id": 1,
        "url": "https://www.wine-searcher.com/discover?t=w",
        "subcategories": []
      },
      {
        "name": "All spirits",
        "id": 7,
        "url": "https://www.wine-searcher.com/discover?t=s",
        "subcategories": []
      }
    ]
  }
}        
		''')

	def __init__(self, options=None):
		super().__init__(firefox=True)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY
		self.options['base_url'] = self.BASE_URL
		# There are only 2 navigation categories we want to process and we only want to process 1 sub category
		self.options['test_categories'] = 8

	def bypass_cookie_consent(self, url):
		print("bypass_cookie_consent()")
		try:
			self.driver.get(url)
			time.sleep(20)
			modal = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '.cookie-notice'))
			)
			select = modal.find_element(By.CSS_SELECTOR, '.cookie-accept')
			select.click()
			print("Bypassed cookie consent")
		except Exception as e:
			print(f"Error: {e}")

	def scraping_setup(self):
		"""Scrape products from the website"""
		print("scraping_setup()")
		url = "https://www.wine-searcher.com/"
		self.bypass_cookie_consent(url)
		time.sleep(10)
		return

	# ************************************************************************
	# Utility Functions
	# ************************************************************************


	# ************************************************************************
	# 	Product Scraping Functions
	# ************************************************************************

	def get_first_image_url(self, data):
		"""
		Extract the first available image URL from the product detail page.

		Args:
			row_spec (dict): the row that will be written to the output file

		Returns:
			str: URL of the first available image, or None if no image found
		"""
		print("get_first_image_url()")
		image_url = ''
		try:

			image_url = data.get("image", "")

		except Exception as e:
			print(f"Error extracting image from page: {str(e)}")

		return image_url

	def get_first_image_url_scrape(self):
		"""
		Extract the first available image URL from the product detail page.

		Args:

		Returns:
			str: URL of the first available image, or None if no image found
		"""
		print("get_first_image_url_scrape()")
		image_url = ''
		try:
			image_element = self.driver.find_element(By.CSS_SELECTOR,
			                                         "ch-elements.product.page [data-hook='loaded-product-image']")
			self.print_element(image_element)
			image_url = image_element.get_attribute("src")

		except NoSuchElementException as e:
			print(f"No Image found")
		except Exception as e:
			print(f"⛔️️ Error processing get_first_image_url_scrape: {type(e)}")
		print(image_url)
		return image_url

	def get_product_data(self, data, data_2, row_spec):
		print("processing product data from response...")
		print(data)
		if data:
			try:
				row_spec["image"] = self.get_first_image_url(data)
				row_spec['option_id'] = row_spec['sku']
				row_spec['sku'] = ''
				row_spec["product_id"] = data.get("product_id", "")

				row_spec = self.parse_product_schema(data, row_spec)
				row_spec = self.parse_product_schema(data_2, row_spec)

				row_spec['pack_size'] = row_spec['size']
				row_spec['size'] = row_spec['pack_size'].get('measure', '')
				row_spec['pack'] = row_spec['pack_size'].get('quantity', '')
				print(row_spec['brand'])
				row_spec['brand'] = row_spec['brand'][0].get('name', '')
				row_spec["extra_data_1"] = json.dumps(data)
				row_spec["extra_data_2"] = json.dumps(data_2)

			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing get_product_data Complete...")
		return row_spec

	def get_table_section(self, row_spec):
		# Scrape the section that contains the manufacturer information. It is in an unordered list
		print("get_table_section()")
		# product-info-table-container
		details = self.driver.find_element(By.CSS_SELECTOR, 'div.product-info-table-container')
		print(details)
		try:
			hidden_element = self.driver.find_element(By.CSS_SELECTOR,
			                                          '.product-info-table-container div.product-info-hide')
			self.driver.execute_script("arguments[0].style.display = 'block';", hidden_element)
		except Exception as e:
			print(f"No hidden element: {type(e)}")
		try:
			rows = details.find_elements(By.CSS_SELECTOR, 'div.g-row')
			print(rows)
			for row in rows:
				key = row.find_element(By.CSS_SELECTOR, '.product-info-table-left').text.strip()
				key = key.lower().replace(' ', '_').replace('_(%)', '')
				print(key)
				value = row.find_element(By.CSS_SELECTOR, '.product-info-table-right').text.strip()
				if key in self.PRODUCT_DATA_SPEC.keys():
					row_spec[key] = value

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing table data: {type(e)}")
		return row_spec

	def get_merchant_section(self, data, row_spec):
		# Scrape the section that contains the manufacturer information. It is in an unordered list
		print("get_merchant_section()")
		try:
			if not data or 'merchants' not in data or not data['merchants']:
				return row_spec

			merchant_info = data['merchants'][0]
			if 'product_options' in merchant_info and merchant_info['product_options']:
				product_options = merchant_info['product_options'][0]
				row_spec['product_id'] = product_options.get('product_id', '')
				option_params = product_options.get('option_params', {})
				row_spec['vintage'] = option_params.get('vintage', '')
				additional_properties = option_params.get('additional_properties', {})
				row_spec['sku'] = additional_properties.get('sku', '')
				row_spec['country_of_origin'] = additional_properties.get('country', '')
				row_spec['closure_type'] = additional_properties.get('closure', '')

				option_display = product_options.get('option_display_data', {})
				if option_display:
					props = option_display.get('properties', {})
					row_spec['varietal'] = props.get('varietal', [''])[0] if isinstance(props.get('varietal'),
					                                                                    list) else props.get('varietal',
					                                                                                         '')
					row_spec['region'] = props.get('region', '')
					row_spec['state'] = props.get('state', '')
					row_spec['country_of_origin'] = props.get('country', '')

				# Extract units of measure
				units = product_options.get('units_of_measure', [])
				if units:
					# Get the first unit of measure (usually the smallest)
					unit = units[0]
					row_spec['ordering_unit'] = unit.get('unit_name', '')
					row_spec['units_per_pack'] = unit.get('num_of_base_units', '')

					# If there's a case size (usually the second unit)
					if len(units) > 1:
						row_spec['units_per_case'] = units[1].get('num_of_base_units', '')

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing variant data: {type(e)}")
		return row_spec

	def get_description(self, row_spec):
		print("get_description()")
		description = ''
		# product-info-about-container
		self.driver.execute_script("document.body.style.zoom = '20%'")
		try:
			description = self.driver.find_element(By.CSS_SELECTOR, "[data-hook='product-description']").text.strip()
			print(description)
			if description:
				row_spec["page_description"] = description
		except NoSuchElementException as e:
			print(f"No Description found")
		except Exception as e:
			print(f"⛔️️ Error processing product description: {type(e)}")
			print(f"⛔️️ Error processing product description: {e}")

		print("processing product overview Complete...")
		return row_spec

	# ************************************************************************
	# 	Core
	# ************************************************************************

	# Step One:
	def build_categories_list(self):
		"""Parse the navigation menu to extract categories and their subcategories."""
		""" ******* This only works in with headless mode disabled ******* """
		print(f"{self.__class__}->build_categories_list()")
		url = "https://www.wine-searcher.com/"
		# url = "https://www.wine-searcher.com/find/real+co+velha+royal+forty+old+tawny+port+aged+oporto+douro+portugal/1/usa-va-y?offer=ws-1-1qe3h8y-0-29%2F521"
		# self.scraping_setup()
		self.driver.get(url)

		target = "script[type='application/ld+json']"
		try:
			# Wait for the navigation data to load
			script_element = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, target))
			)

			script_content = script_element.get_attribute('innerHTML')
			menu_data = {}
			if script_content:
				try:
					# Parse the JSON data
					menu_data = json.loads(script_content)
					print("Successfully extracted and parsed JSON data")
					print(menu_data)
				except json.JSONDecodeError as e:
					print(f"Error parsing JSON data: {e}")
			else:
				print(f"No menu content found")
		except Exception as e:
			print(f"Error processing menu item: {e}")
			input_file = self.get_url_file_path(input_file="company.json")
			# Ensure the directory exists
			os.makedirs(os.path.dirname(input_file), exist_ok=True)

			# Check if input file exists, if not return empty list
			if not os.path.exists(input_file):
				print(f"Input file not found: {input_file}")
				return []
				# Read the file content
			with open(input_file, 'r', encoding='utf-8') as f:
				content = f.read().strip()
			try:
				# Check if the content is a JSON array or object
				menu_data = json.loads(content)
			except json.JSONDecodeError as je:
				print(f"Error parsing JSON: {je}")

		# Initialize the categories structure
		all_categories = {
			'data': {
				'categories': []
			}
		}

		# Get all top-level menu items
		menu_items = []
		for item in menu_data:
			if isinstance(item, dict) and item.get("@type") == "ItemList":
				menu_items =  item

		print(f"menu_items: {len(menu_items)}")
		i = 0
		for item in menu_items.get('itemListElement', []):
			i += 1
			try:
				print(f"item: {item}")
				# Get the main category link
				category_name = item.get('name')
				category_url = item.get('url')

				# Skip if no meaningful name
				if not category_name or category_name.lower() in ['All Wines', 'All Spirits', '']:
					continue

				category_data = {
					'name': category_name,
					'id': i,
					'url': category_url,
					'subcategories': []
				}

				all_categories['data']['categories'].append(category_data)

			except Exception as e:
				print(f"Error processing menu item: {e}")
				continue

		# Print the result for debugging

		print(json.dumps(all_categories, indent=2))

		return json.dumps(all_categories, indent=2)

	def build_categories_list2(self):
		"""Parse the navigation menu to extract categories and their subcategories using HTTP requests."""
		print(f"{self.__class__}->build_categories_list()")
		url = "https://www.wine-searcher.com/"
		url = "https://www.wine-searcher.com/find/real+co+velha+royal+forty+old+tawny+port+aged+oporto+douro+portugal/1/usa-va-y?offer=ws-1-1qe3h8y-0-29%2F521"

		try:
			# Make HTTP request to get the page content
			headers = {
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
			}
			headers = {
				"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
			}
			response = requests.get(url, headers=headers)
			response.raise_for_status()  # Raise an exception for bad status codes

			# Parse the HTML content
			soup = BeautifulSoup(response.text, 'html.parser')

			# Find all script tags with type application/ld+json
			script_tags = soup.find_all('script', type='application/ld+json')

			# Initialize the categories structure
			all_categories = {
				'data': {
					'categories': []
				}
			}

			# Process each script tag to find the one with ItemList
			for script in script_tags:
				try:
					script_content = script.string
					if not script_content:
						continue

					# Parse the JSON content
					json_data = json.loads(script_content)

					# If it's a list, process each item
					if isinstance(json_data, list):
						for item in json_data:
							if isinstance(item, dict) and item.get("@type") == "ItemList":
								return self._process_item_list(item)
					# If it's a single object
					elif isinstance(json_data, dict) and json_data.get("@type") == "ItemList":
						return self._process_item_list(json_data)

				except json.JSONDecodeError:
					continue

			return json.dumps(all_categories, indent=2)

		except Exception as e:
			print(f"Error fetching or parsing categories: {e}")
			return json.dumps({
				'data': {
					'categories': [],
					'error': str(e)
				}
			}, indent=2)

	# Step Two: Get links to products
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
			print(f"category: {category_name}")
			sub_categories = category['subcategories']
			sub_category_found_count = len(sub_categories)
			print(f"Found {sub_category_found_count} sub categories to process...")

			url = self.get_category_url(category)
			print(f"Url: {url}")
			detail_urls, html = self.get_category_page(url, category_name, '', '')
			all_urls.extend(detail_urls)

		# html_table_to_csv(html_table)
		html += f"<h2>Total products found: {total_products}</h2>"

		print(f"Total products found: {len(all_urls)}")
		return html

	def _process_item_list(self, item_list):
		"""Process the ItemList and return formatted categories."""
		all_categories = {
			'data': {
				'categories': []
			}
		}

		for i, item in enumerate(item_list.get('itemListElement', []), 1):
			try:
				category_name = item.get('name', '')
				category_url = item.get('url', '')

				# Skip if no meaningful name
				if not category_name or category_name.lower() in ['all wines', 'all spirits', '']:
					continue

				category_data = {
					'name': category_name,
					'id': i,
					'url': category_url,
					'subcategories': []
				}

				all_categories['data']['categories'].append(category_data)

			except Exception as e:
				print(f"Error processing category {item.get('name', 'unknown')}: {e}")
				continue

		return json.dumps(all_categories, indent=2)

	def get_product_details(self, url, row_spec=None):
		"""
		Product detail pages are rendered server-side. Page must be manually scraped.
		Additional packages also need to be pulled or visited from the dropdown
		To get the product detail page, visit the product detail page and then pull the additional packages
		"""
		# The initial row_spec contains the information from the product list page
		initial_row_spec = row_spec
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print(f"{self.__class__}->get_product_details()")

		print(f"Loading page: {url}")
		self.driver.get(url)

		data = ''
		# sku = row_spec['sku']
		row_spec['content_url'] = url

		print(f"Loading page...{url}")
		try:
			data = self.get_product_detail_from_json_in_html(url, row_spec=row_spec, target="script[type='application/ld+json']")
			row_spec['extra_data_1'] = data
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing get_product_details: {type(e)}")
			raise
		return row_spec

	def get_product_detail_from_json_in_html(self, url, row_spec=None, target="script[type='application/json']"):
		"""
		Extract JSON data from a script tag with the specified ID.

		Args:
			url (str): The URL to load
			row_spec (dict, optional): Product data specification. Defaults to None.
			target (str, optional): CSS selector for the script tag. Defaults to "script[type='application/json']".

		Returns:
			dict: Parsed JSON data from the script tag
		"""
		print(f"EmpireMetro.get_product_detail_from_json_in_html() - Target: {target}")
		if not row_spec:
			row_spec = self.PRODUCT_DATA_SPEC.copy()

		product_data = {}
		product_data2 = {}
		try:
			# Wait for the target script tag to be present
			script_element = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, target))
			)
			# Get the inner HTML of the script tag
			script_content = script_element.get_attribute('innerHTML')

			if script_content:
				try:
					# Parse the JSON data
					product_data = json.loads(script_content)
					print("Successfully extracted and parsed JSON data")
					print(product_data)
				except json.JSONDecodeError as e:
					print(f"Error parsing JSON data: {e}")
			else:
				print(f"No content found in script tag matching: {target}")

		except Exception as e:
			print(f"Error extracting data from script tag: {e}")
		finally:
			# Clean up any pending requests
			if hasattr(self, 'driver') and hasattr(self.driver, 'requests'):
				del self.driver.requests
		# Force a wait before the next one is called
		time.sleep(5)
		return product_data

	def get_product_detail_from_html(self, url, row_spec=None):
		print(f"get_product_detail_from_html()")
		try:
			print("here")
			container = self.wait.until(
				EC.presence_of_element_located((By.TAG_NAME, 'ch-elements.product.page'))
			)
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing get_product_detail_from_html: {type(e)}")
			raise
		try:
			# row_spec['content_url'] = self.driver.current_url
			print("here2")
			# name = container.find_element(By.CSS_SELECTOR, 'div.product-card-title h3').text.strip()
			# print(f"name: {name}")
			# row_spec['name'] = name

			row_spec = self.get_description(row_spec)
			# row_spec = self.get_table_section(row_spec)
			row_spec = self.get_first_image_url_scrape()

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing get_product_detail_from_html: {type(e)}")
		return row_spec

	# ************************************************************************
	# Product List Extraction Functions
	# ************************************************************************
	def get_category_page(self, url, category_name, sub_category_name, sub_sub_category_name):
		print("get_category_page()")
		main_window = self.driver.current_window_handle
		html = ''
		total_products = 0
		all_urls = []
		detail_urls = []
		page_count = 0

		self.driver.get(url)
		try:
			# Update URL from the redirect
			url = self.driver.current_url
			print(f"Current URl: {self.driver.current_url}")

			# Find all window handles and switch to the new window if it opens in a new tab
			if len(self.driver.window_handles) > self.TEST_TABS:
				print("must be a tab...")
				for handle in self.driver.window_handles:
					if handle != main_window:
						self.driver.switch_to.window(handle)
						break
			next_page = True


			page_count += 1
			try:
				# Wait for page to load
				detail_urls = []
				if url in self.driver.current_url:
					print("Found products page")

					# while next_page:
					# 	try:
					# 		button = self.wait.until(
					# 			EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.pager.js-load-more"))
					# 		)
					# 		self.driver.execute_script("arguments[0].scrollIntoView();", button)
					# 		button.click()
					# 		next_page = True
					# 		print("go to next page")
					# 		time.sleep(4)
					# 	except Exception as e:
					# 		next_page = False
					# 		print(f"no next page")
					html_line, detail_urls = self.get_products_from_html()
				products_found_count = len(detail_urls)
				all_urls.extend(detail_urls)
				html += f"<div>Found {products_found_count} products for category {category_name} page {page_count}</div>"
				print(f"Found {products_found_count} products for category {category_name} page {page_count}")
				total_products += products_found_count
			# self.save_urls_to_csv(detail_urls, category_name, sub_category_name, sub_sub_category_name)

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
			EC.presence_of_element_located((By.CSS_SELECTOR, '.result-list #selection-list-widget'))
		)
		print("got container")
		products = container.find_elements(By.CSS_SELECTOR, ".card")

		print(f"products found: {len(products)}")
		detail_urls = [product.find_element(By.CSS_SELECTOR, 'a').get_attribute("href") for product in products]
		return '', detail_urls
