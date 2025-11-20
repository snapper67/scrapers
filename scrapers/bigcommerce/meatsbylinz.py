import json
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

import csv
import sys
from typing import List, Dict, Any, Optional
from urllib.parse import urljoin

import requests
import os

class MeatsByLinzScraper(BigCommerceScraper):
	# 202/edit_note/1724/
	CRM_ID = 202
	CRM_NOTE_ID = 1724
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/meats_by_linz'

	BASE_URL = 'https://shop.linzheritageangus.com/'
	VENDOR_NAME = 'Meats by Linz'

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "id": 1,
        "name": "Shop By",
        "subcategories": [
          {
            "name": "Shop ByCut",
            "subcategories": [
              {
                "name": "Filet Mignon - Tenderloin",
                "url": "https://shop.linzheritageangus.com/beef/filet-mignon-tenderloin"
              },
              {
                "name": "Ribeyes & Tomahawks",
                "url": "https://shop.linzheritageangus.com/beef/ribeyes-and-tomahawks"
              },
              {
                "name": "Porterhouses",
                "url": "https://shop.linzheritageangus.com/beef/porterhouses"
              },
              {
                "name": "Roasts",
                "url": "https://shop.linzheritageangus.com/beef/roasts"
              },
              {
                "name": "Strip Steaks",
                "url": "https://shop.linzheritageangus.com/beef/strip-steaks"
              },
              {
                "name": "Gourmet Burgers & Franks",
                "url": "https://shop.linzheritageangus.com/beef/gourmet-burgers-franks"
              },
              {
                "name": "Briskets",
                "url": "https://shop.linzheritageangus.com/beef/briskets"
              },
              {
                "name": "Short Ribs",
                "url": "https://shop.linzheritageangus.com/beef/short-ribs"
              },
              {
                "name": "Skirt, Bavette & Flat Iron",
                "url": "https://shop.linzheritageangus.com/beef/skirt-bavette-flat-iron"
              }
            ],
            "url": "https://shop.linzheritageangus.com/cut"
          }
        ],
        "url": "https://shop.linzheritageangus.com/beef"
      },
      {
        "id": 2,
        "name": "Other",
        "subcategories": [
          {
            "name": "OtherProteins",
            "subcategories": [
              {
                "name": "Chicken & Poultry",
                "url": "https://shop.linzheritageangus.com/other-proteins/chicken-poultry"
              },
              {
                "name": "Pork & Ribs",
                "url": "https://shop.linzheritageangus.com/other-proteins/pork-and-ribs"
              },
              {
                "name": "Sausages & Bratwurst",
                "url": "https://shop.linzheritageangus.com/other-proteins/sausage"
              },
              {
                "name": "Premium Seafood & Lobster Tails",
                "url": "https://shop.linzheritageangus.com/other-proteins/seafood"
              },
              {
                "name": "Australian Lamb",
                "url": "https://shop.linzheritageangus.com/other-proteins/lamb"
              },
              {
                "name": "Bacon",
                "url": "https://shop.linzheritageangus.com/other-proteins/bacon"
              }
            ],
            "url": ""
          }
        ],
        "url": "https://shop.linzheritageangus.com/other-proteins"
      },
      {
        "id": 3,
        "name": "Sides & Soups",
        "subcategories": [
          {
            "name": "Sides & Soups",
            "subcategories": [
              {
                "name": "Side Dishes",
                "url": "https://shop.linzheritageangus.com/sides-soups/sides"
              },
              {
                "name": "Soups",
                "url": "https://shop.linzheritageangus.com/sides-soups/soups"
              },
              {
                "name": "Desserts",
                "url": "https://shop.linzheritageangus.com/sides-soups/desserts"
              },
              {
                "name": "Finishing Butter & Seasoning",
                "url": "https://shop.linzheritageangus.com/sides-soups/seasoning-and-butter"
              }
            ],
            "url": ""
          }
        ],
        "url": "https://shop.linzheritageangus.com/soups-sides"
      },
      {
        "id": 4,
        "name": "Sale",
        "subcategories": null,
        "url": "https://shop.linzheritageangus.com/on-sale"
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

	def get_more_data(self, data, row_spec):
		print("get_more_data()")
		try:
			# Get the brand information from the data
			brand_data = data.get('brand', {})
			if isinstance(brand_data, dict) and brand_data.get('@type') == 'Brand':
				row_spec['brand'] = brand_data.get('name', '')
			elif isinstance(brand_data, list) and brand_data:
				# Handle case where brand is a list
				row_spec['brand'] = brand_data[0].get('name', '')
			else:
				row_spec['brand'] = str(brand_data)  # Fallback to string representation if format is unexpected
		except Exception as e:
			print(f"⛔️ Error processing brand information: {type(e).__name__} - {str(e)}")
			row_spec['brand'] = ''

		# Get the second line of the description for pack_size
		try:
			description = row_spec.get('description', '')
			if description:
				# Split the description into lines and get the second line (index 1)
				lines = [line.strip() for line in description.splitlines() if line.strip()]
				if len(lines) > 1:
					row_spec['pack_size'] = lines[1]
				else:
					row_spec['pack_size'] = lines[0] if lines else ''
		except Exception as e:
			print(f"⛔️ Error extracting pack size from description: {type(e).__name__} - {str(e)}")
			row_spec['pack_size'] = ''

		print(f"Brand: {row_spec.get('brand', 'N/A')}")
		print(f"Pack Size: {row_spec.get('pack_size', 'N/A')}")
		return row_spec

	# ************************************************************************
	# Category URL retrieval Functions
	# ************************************************************************

	def get_navigation_dict(self, url: str, headers: Optional[Dict] = None) -> Dict:
		"""
		Fetches and parses the navigation structure from the Meats by Linz website.

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

			# Initialize navigation structure
			navigation = {'data': {'categories': []}}
			category_id = 1
			seen_urls = set()  # To track processed URLs and avoid duplicates

			def process_category(link, parent_url=None):
				"""Helper function to process a category link and its subcategories"""
				nonlocal category_id

				# Get category name and URL
				category_name = ' '.join(span.text.strip() for span in link.find_all('span', recursive=False))
				if not category_name.strip():
					category_name = link.get_text(strip=True)

				category_url = urljoin(url, link.get('href', ''))

				# Skip if we've already processed this URL
				if category_url in seen_urls:
					return None

				seen_urls.add(category_url)

				# Initialize subcategories list
				subcategories = []

				# Find the parent item to look for submenu
				parent_item = link.find_parent('li', class_=lambda x: x and ('navPages-item' in x.split()))
				if parent_item:
					# Check for desktop submenu
					submenu = parent_item.find('div', class_=lambda x: x and ('navPage-subMenu' in x.split()))

					if submenu:
						# Process megamenu sections
						for section in submenu.select('.megamenu-item'):
							section_title_elem = section.find('h2', class_='menu-title')
							if not section_title_elem:
								continue

							section_title = ' '.join(
								span.text.strip() for span in section_title_elem.find_all('span', recursive=False))
							if not section_title.strip():
								section_title = section_title_elem.get_text(strip=True)

							section_link = section_title_elem.find('a')
							section_url = urljoin(url, section_link.get('href', '')) if section_link else ''

							# Initialize section items
							section_items = []

							# Process section links
							for item_link in section.select('.megamenu-categories a'):
								item_name = item_link.get_text(strip=True)
								item_url = urljoin(url, item_link.get('href', ''))

								if item_url not in seen_urls:
									section_items.append({
										'name': item_name,
										'url': item_url
									})
									seen_urls.add(item_url)

							if section_title or section_items:
								subcategories.append({
									'name': section_title,
									'url': section_url if section_url != category_url else '',
									'subcategories': section_items if section_items else None
								})

				# Create category dictionary
				category = {
					'name': category_name.strip(),
					'id': category_id,
					'url': category_url,
					'subcategories': subcategories if subcategories else None
				}

				category_id += 1
				return category

			# Process desktop navigation
			desktop_nav = soup.find('div', class_='desktop-view')
			if desktop_nav:
				for link in desktop_nav.select('.navPages-action[href]'):
					if link.get('aria-hidden') == 'true':
						continue

					category = process_category(link)
					if category:
						navigation['data']['categories'].append(category)

			# Process mobile navigation (only if we didn't find anything in desktop nav)
			if not navigation['data']['categories']:
				mobile_nav = soup.find('div', class_='mobile-view')
				if mobile_nav:
					for link in mobile_nav.select('.navPages-action[href]'):
						if link.get('aria-hidden') == 'true':
							continue

						category = process_category(link)
						if category:
							navigation['data']['categories'].append(category)

			return navigation

		except requests.RequestException as e:
			print(f"Error fetching navigation: {e}")
			return {'data': {'categories': []}}
		except Exception as e:
			print(f"Error parsing navigation: {str(e)}")
			import traceback
			traceback.print_exc()
			return {'data': {'categories': []}}

	# ************************************************************************
	# Product List Functions
	# ************************************************************************

	def get_next_page(self):
		print("meat->get_next_page()")
		try:
			paging = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination-list'))
			)
			print("Checking 1")
			next_disabled = paging.find_element(By.CSS_SELECTOR, '.pagination-item.pagination-item--next')
			class_attribute = next_disabled.get_attribute("class")
			classes = class_attribute.split()

			print("Checking 2")
			if not 'disabled' in classes:
				print("Clicking next")
				url = next_disabled.find_element(By.CLASS_NAME, 'pagination-link').get_attribute('href')
				print(f"Going to next page {url}")
				self.driver.get(url)
				return True
			else:
				print("Next is disabled")
				return False
		except Exception as e:
			print("There is no next page")
			print(e)
			return False

	# ************************************************************************
	# Product Detail Functions
	# ************************************************************************

	def get_packs_sizes(self, row_spec):
		"""
		Get the packs sizes from the product page
		Convert row_spec into a list of row_specs
		Allow the calling function to write the last one
		"""
		return row_spec

	def get_price(self, data, row_spec):
		print("get_price()")
		try:
			price = data.get('offers', {}).get('price', '')
			row_spec['retail_price'] = price
		except Exception as e:
			print(f"⛔️ Error processing price information: {type(e).__name__} - {str(e)}")

		print("Processing price information complete...")
		return row_spec

	@staticmethod
	def process_json_product(json_str):
		"""
		Allow a scraper to modify the product schema data prior to processing
		"""
		print("process_json_product()")
		if not isinstance(json_str, str):
			print("converting to string")
			json_str = str(json_str)
		json_str.replace('%0A', '<br>')
		import urllib
		json_str = urllib.parse.unquote(json_str)
		cleaned = []
		for char in json_str:
			if char in "\n":
				cleaned.append("\n")
			else:
				cleaned.append(char)
		json_str = "".join(cleaned)
		print(json_str)
		return json_str
