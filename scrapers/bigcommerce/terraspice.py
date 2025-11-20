import json
from urllib.parse import urljoin

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

from scrapers.scraper import Scraper
from scrapers.bigcommerce.bigcommerce import BigCommerceScraper
from typing import List, Dict, Any, Optional

class TerraSpiceScraper(BigCommerceScraper):
	# 1104/edit_note/1723/
	CRM_ID = 1104
	CRM_NOTE_ID = 1723
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = 'Ready'

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/terra_spice'

	BASE_URL = 'https://www.terraspicemarketplace.com/shop-all/#'
	VENDOR_NAME = 'Terra Spice'

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "id": 2,
        "name": "SPICES",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/spices/"
      },
      {
        "id": 3,
        "name": "CHEF-CRAFTED BLENDS",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/blends/"
      },
      {
        "id": 4,
        "name": "CHILES",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/chiles/"
      },
      {
        "id": 5,
        "name": "CHOCOLATE & COCOA",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/chocolate-cocoa/"
      },
      {
        "id": 6,
        "name": "CULINARY KITS",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/culinary-kits/"
      },
      {
        "id": 7,
        "name": "DRIED FRUITS & VEGETABLES",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/dried-fruits-vegetables/"
      },
      {
        "id": 8,
        "name": "SUGARS & SWEETENERS",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/sugars-sweeteners/"
      },
      {
        "id": 9,
        "name": "DAIRY",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/dairy/"
      },
      {
        "id": 10,
        "name": "SEA SALTS",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/sea-salts/"
      },
      {
        "id": 11,
        "name": "EXTRACTS & FLAVORS",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/flavors/"
      },
      {
        "id": 12,
        "name": "TEA",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/tea/"
      },
      {
        "id": 13,
        "name": "INDUSTRIAL INGREDIENTS",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/industrial-ingredients/"
      },
      {
        "id": 14,
        "name": "KOSHER",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/kosher/"
      },
      {
        "id": 15,
        "name": "KOSHER DAIRY",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/kosher-dairy/"
      },
      {
        "id": 16,
        "name": "SALT FREE",
        "subcategories": null,
        "url": "https://www.terraspicemarketplace.com/salt-free/"
      }
    ]
  }
}
''')

	def __init__(self, options=None):
		super().__init__(options)

	# ************************************************************************
	# Core Functions
	# These are overrides of the core functions
	# ************************************************************************

	# ************************************************************************
	# Core Function Hooks
	# These are the methods called by the core functions
	# ************************************************************************

	# ************************************************************************
	# Category URL retrieval Functions
	# ************************************************************************

	def get_navigation_dict(self, url: str, headers: Optional[Dict] = None) -> Dict:
		"""
		Fetches and parses the navigation structure and returns it as a dictionary.
		This is a helper method used by get_navigation_structure.

		Args:
			url: The URL of the website
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

			# Find the shop all submenu container
			shop_all_menu = soup.find('div', id='tsShopAllSubMenu')
			if not shop_all_menu:
				print("Could not find the shop all submenu")
				return {'data': {'categories': []}}

			# Initialize navigation structure
			navigation = {'data': {'categories': []}}
			category_id = 1

			# Find all column divs
			columns = shop_all_menu.select('div.large-4.columns')
			print(f"Found {len(columns)} navigation columns")

			for column in columns:
				# Get all list items in this column
				items = column.select('ul li')

				for item in items:
					link = item.find('a', class_='navPages-action')
					if not link:
						continue

					# Get category name and URL
					category_name = link.get_text(strip=True)
					# Remove '>' from the end of the name if present (for SHOP ALL >)
					if category_name.endswith('>'):
						category_name = category_name[:-1].strip()

					category_url = urljoin(url, link.get('href', ''))

					# Add to navigation
					navigation['data']['categories'].append({
						'name': category_name,
						'id': category_id,
						'url': category_url,
						'subcategories': None  # No subcategories in this structure
					})
					category_id += 1

			return navigation

		except requests.RequestException as e:
			print(f"Error fetching navigation: {e}")
			return {'data': {'categories': []}}
		except Exception as e:
			print(f"Error parsing navigation: {str(e)}")
			return {'data': {'categories': []}}

	# ************************************************************************
	# Product List Functions
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

	# ************************************************************************
	# Product Detail Functions
	# ************************************************************************
	def get_price(self, data, row_spec):
		print("get_price()")
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

