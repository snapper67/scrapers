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

from typing import List, Dict, Any, Optional

from scrapers.scraper import Scraper
from scrapers.shopify.shopify import ShopifyScraper

class MelissasScraper(ShopifyScraper):
	# 203/edit_note/1499/
	CRM_ID = 203
	CRM_NOTE_ID = 1499
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	# DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/odd_produce'
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/melissas_produce'

	BASE_URL = 'https://www.melissas.com/pages/asian'
	BASE_PRODUCT_URL = 'https://www.melissas.com/products/'
	VENDOR_NAME = 'Melissa\'s Produce'

	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "id": 1,
        "name": "Shop",
        "subcategories": [
          {
            "name": "Fruits",
            "subcategories": [
              {
                "name": "Apples",
                "url": "/collections/apples"
              },
              {
                "name": "Bananas",
                "url": "/collections/bananas"
              },
              {
                "name": "Berries",
                "url": "/collections/berries"
              },
              {
                "name": "Citrus",
                "url": "/collections/citrus"
              },
              {
                "name": "Dates & Figs",
                "url": "/collections/dates-figs"
              },
              {
                "name": "Grapes",
                "url": "/collections/grapes"
              },
              {
                "name": "Mangos",
                "url": "/collections/mangoes"
              },
              {
                "name": "Melons",
                "url": "/collections/melons"
              },
              {
                "name": "Organic Fruit",
                "url": "/collections/organic-fruit"
              },
              {
                "name": "Pears",
                "url": "/collections/pears"
              },
              {
                "name": "Pineapples",
                "url": "/collections/pineapples"
              },
              {
                "name": "Stone Fruit",
                "url": "/collections/stone-fruit"
              },
              {
                "name": "Tropicals",
                "url": "/collections/tropical-exotic-fruit"
              },
              {
                "name": "Season's Best",
                "url": "/collections/seasons-best"
              },
              {
                "name": "All Fruit",
                "url": "/collections/all-fruit"
              },
              {
                "name": "Fruit Gifts",
                "url": "/collections/fruit-gifts"
              }
            ],
            "url": "/pages/fruits"
          },
          {
            "name": "Vegetables",
            "subcategories": [
              {
                "name": "Eggplants",
                "url": "/collections/eggplant"
              },
              {
                "name": "Herbs",
                "url": "/collections/herbs"
              },
              {
                "name": "Lettuce & Greens",
                "url": "/collections/lettuce-greens"
              },
              {
                "name": "Mushrooms",
                "url": "/collections/all-mushrooms"
              },
              {
                "name": "Onions & Garlic",
                "url": "/collections/onions-garlic"
              },
              {
                "name": "Organic Vegetables",
                "url": "/collections/organic-vegetables"
              },
              {
                "name": "Peppers",
                "url": "/collections/peppers"
              },
              {
                "name": "Potatoes & Yams",
                "url": "/collections/potatoes"
              },
              {
                "name": "Radishes",
                "url": "/collections/radishes"
              },
              {
                "name": "Squash",
                "url": "/collections/squash"
              },
              {
                "name": "Tomatoes",
                "url": "/collections/tomatoes"
              },
              {
                "name": "Truffles",
                "url": "/collections/truffles"
              },
              {
                "name": "Season's Best",
                "url": "/collections/seasons-best"
              },
              {
                "name": "All Vegetables",
                "url": "/collections/all-vegetables"
              },
              {
                "name": "Vegetable Gifts",
                "url": "/collections/vegetable-gifts"
              }
            ],
            "url": "/pages/vegetables"
          },
          {
            "name": "Convenience",
            "subcategories": [
              {
                "name": "Clean Snax\u00ae",
                "url": "/collections/clean-snax"
              },
              {
                "name": "Condiments",
                "url": "/collections/condiments"
              },
              {
                "name": "Dried",
                "url": "/collections/all-dried-items"
              },
              {
                "name": "Grains & Seeds",
                "url": "/collections/grains-seeds"
              },
              {
                "name": "Jarred",
                "url": "/collections/jarred-items"
              },
              {
                "name": "Kits",
                "url": "/collections/culinary-kits"
              },
              {
                "name": "Nuts",
                "url": "/collections/nuts"
              },
              {
                "name": "Snacks",
                "url": "/collections/snacks"
              },
              {
                "name": "Soy",
                "url": "/collections/soy"
              },
              {
                "name": "Spices",
                "url": "/collections/spices"
              },
              {
                "name": "Steamed Line",
                "url": "/collections/steamed-line"
              },
              {
                "name": "All Convenience",
                "url": "/collections/packaged-items"
              }
            ],
            "url": "/pages/convenience"
          },
          {
            "name": "Asian",
            "subcategories": [
              {
                "name": "Asian Fruit",
                "url": "/collections/asian-fruit"
              },
              {
                "name": "Asian Vegetables",
                "url": "/collections/asian-vegetables"
              },
              {
                "name": "Asian Snacks",
                "url": "/collections/asian-snacks"
              },
              {
                "name": "Asian Organics",
                "url": "/collections/asian-organics"
              },
              {
                "name": "Asian Convenience",
                "url": "/collections/asian-convenience"
              },
              {
                "name": "Asian Gifts",
                "url": "/collections/asian-gifts"
              },
              {
                "name": "Asian Kits",
                "url": "/collections/asian-kits"
              }
            ],
            "url": "/pages/asian"
          },
          {
            "name": "Latin",
            "subcategories": [
              {
                "name": "Latin Fruit",
                "url": "/collections/latin-fruit"
              },
              {
                "name": "Latin Vegetables",
                "url": "/collections/latin-vegetables"
              },
              {
                "name": "Latin Snacks",
                "url": "/collections/latin-snacks"
              },
              {
                "name": "Latin Organics",
                "url": "/collections/latin-organics"
              },
              {
                "name": "Latin Condiments",
                "url": "/collections/latin-condiments"
              },
              {
                "name": "Latin Kits",
                "url": "/collections/culinary-kits"
              }
            ],
            "url": "/pages/latin"
          },
          {
            "name": "Organics",
            "subcategories": [
              {
                "name": "Organic Mixed Boxes & Subscriptions",
                "url": "/collections/organic-mixed-boxes"
              },
              {
                "name": "Organic Dried Fruit",
                "url": "/collections/organic-dried-fruit"
              },
              {
                "name": "Organic Gifts",
                "url": "/collections/organic-gifts"
              }
            ],
            "url": "/collections/organics"
          },
          {
            "name": "All Items",
            "subcategories": [],
            "url": "/collections/all-items"
          },
          {
            "name": "Hatch Essentials",
            "subcategories": [],
            "url": "/collections/hatch-pepper-essentials"
          }
        ],
        "url": "/pages/shop"
      },
      {
        "id": 2,
        "name": "Recipes",
        "subcategories": [],
        "url": "/pages/recipe-categories"
      },
      {
        "id": 3,
        "name": "Blogs",
        "subcategories": [],
        "url": "/pages/melissas-blogs"
      },
      {
        "id": 4,
        "name": "About Us",
        "subcategories": [],
        "url": "/pages/about-us"
      },
      {
        "id": 5,
        "name": "Shipping FAQ",
        "subcategories": [],
        "url": "/pages/shipping-information"
      }
    ]
  }
}                  
	''')

	def __init__(self, options=None):
		super().__init__(options)


	def get_categories(self):
		"""
		Returns a list of category dictionaries from the CATEGORIES data. This is the preferred way to store the categories

		Returns:
			list: A list of dictionaries, each containing 'id' and 'name' of a category
		"""
		category_options = self.CATEGORIES.get('data', {}).get('categories', {})
		return [
			{'id': option['id'], 'name': option['name'], 'url': option['url'], 'subcategories': option['subcategories']}
			for option in category_options
			if option.get('id') and option.get('name')
		]

	# ************************************************************************
	# Core Functions
	# These are overrides of the core functions
	# ************************************************************************

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
		category_URL = self.get_category_url()
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
							html_line, detail_urls = self.get_products_from_html()
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

	# ************************************************************************
	# Core Function Hooks
	# These are the methods called by the core functions
	# ************************************************************************

	def get_product_details(self, url, row_spec=None):
		"""Get Product Details"""
		data = self.get_product_details_json( url, row_spec)
		row_spec = self.get_product_data(data, row_spec)
		return row_spec

	# ************************************************************************
	# Category URL retrieval Functions
	# ************************************************************************

	def get_navigation_dict(self, url: str, headers: Optional[Dict] = None) -> Dict[str, Any]:
		"""
		Scrapes and parses the navigation structure from the Melissa's website.

		Args:
			url: The URL of the page containing the navigation menu
			headers: Optional headers for the request

		Returns:
			A dictionary representing the navigation structure with categories and subcategories
		"""
		try:
			self.driver.get(url)
			time.sleep(3)  # Allow page to load

			# Get the page source and parse with BeautifulSoup
			soup = BeautifulSoup(self.driver.page_source, 'html.parser')

			# Find the main navigation menu
			nav = soup.find('nav', {'class': 'site-navigation'})
			if not nav:
				print("Navigation menu not found")
				return {'data': {'categories': []}}

			# Initialize the navigation structure
			navigation = {'data': {'categories': []}}
			category_id = 1

			# Find all top-level menu items
			top_level_items = nav.find('ul', class_='navmenu-depth-1').find_all('li', recursive=False)

			for item in top_level_items:
				# Skip items without links (like dividers)
				link = item.find('a', class_='navmenu-link')
				if not link:
					continue

				category_name = link.get_text(strip=True)
				category_url = link.get('href', '')

				# Skip non-shop categories
				if not category_url.startswith(('/collections/', '/pages/')):
					continue

				# Initialize category data
				category_data = {
					'id': category_id,
					'name': category_name,
					'url': category_url,
					'subcategories': []
				}
				category_id += 1

				# Check for megamenu content
				megamenu = item.find('div', class_='navmenu-meganav')
				if megamenu:
					# Process megamenu items
					megamenu_items = megamenu.find_all('li', class_='navmenu-meganav-item')
					for megamenu_item in megamenu_items:
						subcategory_link = megamenu_item.find('a', class_='navmenu-item-text')
						if not subcategory_link:
							continue

						subcategory_name = subcategory_link.get_text(strip=True)
						subcategory_url = subcategory_link.get('href', '')

						# Skip if it's not a collection or page
						if not subcategory_url.startswith(('/collections/', '/pages/')):
							continue

						subcategory_data = {
							'name': subcategory_name,
							'url': subcategory_url,
							'subcategories': []
						}

						# Check for third level subcategories
						submenu = megamenu_item.find('ul', class_='navmenu-depth-3')
						if submenu:
							for submenu_item in submenu.find_all('li', class_='navmenu-item'):
								submenu_link = submenu_item.find('a', class_='navmenu-link')
								if not submenu_link:
									continue

								submenu_name = submenu_link.get_text(strip=True)
								submenu_url = submenu_link.get('href', '')

								if not submenu_url.startswith(('/collections/', '/pages/')):
									continue

								subcategory_data['subcategories'].append({
									'name': submenu_name,
									'url': submenu_url
								})

						category_data['subcategories'].append(subcategory_data)

				navigation['data']['categories'].append(category_data)

			return navigation

		except Exception as e:
			print(f"Error getting navigation structure: {e}")
			return {'data': {'categories': []}}

	# ************************************************************************
	# Product List Functions
	# ************************************************************************

	# ************************************************************************
	# Product Detail Functions
	# ************************************************************************
