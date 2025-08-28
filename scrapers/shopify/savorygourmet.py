import json
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
from scrapers.shopify.shopify import ShopifyScraper
from typing import List, Dict, Any, Optional

class SavoryGourmetScraper(ShopifyScraper):
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
		'subsubcategory': '',
		'shop_id': '',
		'price': 0,
	}

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/savory_gourmet'

	BASE_URL = 'https://savorygourmet.com/'
	VENDOR_NAME = 'Savory Gourmet'

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "id": 1,
        "name": "Culinary",
        "subcategories": [
          {
            "name": "Land & Sea",
            "subcategories": [
              {
                "name": "Appetizers",
                "url": "https://savorygourmet.com/collections/appetizers"
              },
              {
                "name": "Butter & Dairy",
                "url": "https://savorygourmet.com/collections/butter-dairy"
              },
              {
                "name": "Caviar",
                "url": "https://savorygourmet.com/collections/caviar"
              },
              {
                "name": "Charcuterie",
                "url": "https://savorygourmet.com/collections/charcuterie"
              },
              {
                "name": "Cheese",
                "url": "https://savorygourmet.com/collections/cheeses"
              },
              {
                "name": "Escargots (Snails)",
                "url": "https://savorygourmet.com/collections/escargots"
              },
              {
                "name": "Seafood",
                "url": "https://savorygourmet.com/collections/seafood"
              },
              {
                "name": "Truffle & Mushroom",
                "url": "https://savorygourmet.com/collections/truffles-mushrooms"
              }
            ],
            "url": "https://savorygourmet.com/pages/culinary"
          },
          {
            "name": "Appetizers",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/appetizers"
          },
          {
            "name": "Butter & Dairy",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/butter-dairy"
          },
          {
            "name": "Caviar",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/caviar"
          },
          {
            "name": "Charcuterie",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/charcuterie"
          },
          {
            "name": "Cheese",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/cheeses"
          },
          {
            "name": "Escargots (Snails)",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/escargots"
          },
          {
            "name": "Seafood",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/seafood"
          },
          {
            "name": "Truffle & Mushroom",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/truffles-mushrooms"
          },
          {
            "name": "Side & Seasoning",
            "subcategories": [
              {
                "name": "Bread",
                "url": "https://savorygourmet.com/collections/bread"
              },
              {
                "name": "Dried Fruits & Nuts",
                "url": "https://savorygourmet.com/collections/dried-fruits-nuts"
              },
              {
                "name": "Flour",
                "url": "https://savorygourmet.com/collections/flours"
              },
              {
                "name": "Gourmet Snacks",
                "url": "https://savorygourmet.com/collections/snack"
              },
              {
                "name": "Grains, Pasta & Rice",
                "url": "https://savorygourmet.com/collections/pasta-rice-grains"
              },
              {
                "name": "Olives & Vegetables",
                "url": "https://savorygourmet.com/collections/olives-vegetables"
              },
              {
                "name": "Salt & Spices",
                "url": "https://savorygourmet.com/collections/herbs-spices-salt-pepper"
              }
            ],
            "url": "https://savorygourmet.com/pages/culinary"
          },
          {
            "name": "Bread",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/bread"
          },
          {
            "name": "Dried Fruits & Nuts",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/dried-fruits-nuts"
          },
          {
            "name": "Flour",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/flours"
          },
          {
            "name": "Gourmet Snacks",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/snack"
          },
          {
            "name": "Grains, Pasta & Rice",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/pasta-rice-grains"
          },
          {
            "name": "Olives & Vegetables",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/olives-vegetables"
          },
          {
            "name": "Salt & Spices",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/herbs-spices-salt-pepper"
          },
          {
            "name": "See all culinary items",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/culinary"
          }
        ],
        "url": "https://savorygourmet.com/pages/culinary"
      },
      {
        "id": 2,
        "name": "Pastry",
        "subcategories": [
          {
            "name": "Baking",
            "subcategories": [
              {
                "name": "Butter & Dairy",
                "url": "https://savorygourmet.com/collections/butter-dairy"
              },
              {
                "name": "Flour",
                "url": "https://savorygourmet.com/collections/flours"
              },
              {
                "name": "Tart Shells",
                "url": "https://savorygourmet.com/collections/https-savorygourmet-com-collections-tart-shells-dough"
              }
            ],
            "url": "https://savorygourmet.com/pages/pastry"
          },
          {
            "name": "Butter & Dairy",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/butter-dairy"
          },
          {
            "name": "Flour",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/flours"
          },
          {
            "name": "Tart Shells",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/https-savorygourmet-com-collections-tart-shells-dough"
          },
          {
            "name": "Flavoring",
            "subcategories": [
              {
                "name": "Chocolate & Praline",
                "url": "https://savorygourmet.com/collections/chocolate"
              },
              {
                "name": "Fruit Pur\u00e9es",
                "url": "https://savorygourmet.com/collections/la-fruitiere"
              },
              {
                "name": "Honey & Sweet",
                "url": "https://savorygourmet.com/collections/honey-sugar"
              },
              {
                "name": "Jam & Extra Jam",
                "url": "https://savorygourmet.com/collections/fruit-jams"
              },
              {
                "name": "Vanilla & Flavoring",
                "url": "https://savorygourmet.com/collections/vanilla-flavorings"
              }
            ],
            "url": "https://savorygourmet.com/pages/pastry"
          },
          {
            "name": "Chocolate & Praline",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/chocolate"
          },
          {
            "name": "Fruit Pur\u00e9es",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/la-fruitiere"
          },
          {
            "name": "Honey & Sweet",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/honey-sugar"
          },
          {
            "name": "Jam & Extra Jam",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/fruit-jams"
          },
          {
            "name": "Vanilla & Flavoring",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/vanilla-flavorings"
          },
          {
            "name": "See all pastry items",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/pastry"
          }
        ],
        "url": "https://savorygourmet.com/pages/pastry"
      },
      {
        "id": 3,
        "name": "Selections",
        "subcategories": [
          {
            "name": "Themes",
            "subcategories": [
              {
                "name": "Afternoon Tea",
                "url": "https://savorygourmet.com/collections/afternoon-tea"
              },
              {
                "name": "Breakfast & Brunch",
                "url": "https://savorygourmet.com/collections/breakfast"
              },
              {
                "name": "Burgers and Sandwiches",
                "url": "https://savorygourmet.com/collections/burger"
              },
              {
                "name": "Cheese & Charcuterie Board",
                "url": "https://savorygourmet.com/collections/cheese-charcuterie-board"
              },
              {
                "name": "Confectionery",
                "url": "https://savorygourmet.com/collections/chocolate-manufacturer"
              },
              {
                "name": "Ice Cream & Gelato",
                "url": "https://savorygourmet.com/collections/ice-cream-gelato-sorbet"
              },
              {
                "name": "Minibar",
                "url": "https://savorygourmet.com/collections/minibar"
              },
              {
                "name": "Pizza & Pasta",
                "url": "https://savorygourmet.com/collections/pizza"
              },
              {
                "name": "Viennoiserie Ingredients",
                "url": "https://savorygourmet.com/collections/croissants-viennoiserie"
              }
            ],
            "url": "https://savorygourmet.com/pages/collections"
          },
          {
            "name": "Afternoon Tea",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/afternoon-tea"
          },
          {
            "name": "Breakfast & Brunch",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/breakfast"
          },
          {
            "name": "Burgers and Sandwiches",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/burger"
          },
          {
            "name": "Cheese & Charcuterie Board",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/cheese-charcuterie-board"
          },
          {
            "name": "Confectionery",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/chocolate-manufacturer"
          },
          {
            "name": "Ice Cream & Gelato",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/ice-cream-gelato-sorbet"
          },
          {
            "name": "Minibar",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/minibar"
          },
          {
            "name": "Pizza & Pasta",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/pizza"
          },
          {
            "name": "Viennoiserie Ingredients",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/croissants-viennoiserie"
          },
          {
            "name": "Influences",
            "subcategories": [
              {
                "name": "Cinco de Mayo",
                "url": "https://savorygourmet.com/collections/cinco-de-mayo"
              },
              {
                "name": "Asian Menu",
                "url": "https://savorygourmet.com/collections/asian-menu"
              },
              {
                "name": "California Menu",
                "url": "https://savorygourmet.com/collections/californian-menu"
              },
              {
                "name": "Fine Dining",
                "url": "https://savorygourmet.com/collections/fine-dining-menu"
              },
              {
                "name": "French Menu",
                "url": "https://savorygourmet.com/collections/french-menu"
              },
              {
                "name": "Italian Menu",
                "url": "https://savorygourmet.com/collections/italian-menu"
              }
            ],
            "url": "https://savorygourmet.com/pages/collections"
          },
          {
            "name": "Cinco de Mayo",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/cinco-de-mayo"
          },
          {
            "name": "Asian Menu",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/asian-menu"
          },
          {
            "name": "California Menu",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/californian-menu"
          },
          {
            "name": "Fine Dining",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/fine-dining-menu"
          },
          {
            "name": "French Menu",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/french-menu"
          },
          {
            "name": "Italian Menu",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/italian-menu"
          },
          {
            "name": "See all",
            "subcategories": [
              {
                "name": "Selection for retailers",
                "url": "https://savorygourmet.com/collections/retail"
              },
              {
                "name": "Selection for distributors",
                "url": "https://savorygourmet.com/pages/distributors"
              }
            ],
            "url": "https://savorygourmet.com/pages/collections"
          },
          {
            "name": "Selection for retailers",
            "subcategories": null,
            "url": "https://savorygourmet.com/collections/retail"
          },
          {
            "name": "Selection for distributors",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/distributors"
          }
        ],
        "url": "https://savorygourmet.com/pages/collections"
      },
      {
        "id": 4,
        "name": "Resources",
        "subcategories": [
          {
            "name": "About",
            "subcategories": [
              {
                "name": "About Us",
                "url": "https://savorygourmet.com/pages/about-us"
              },
              {
                "name": "Team",
                "url": "https://savorygourmet.com/pages/team"
              },
              {
                "name": "Contact",
                "url": "https://savorygourmet.com/pages/contact"
              },
              {
                "name": "Delivery Zones",
                "url": "https://savorygourmet.com/pages/delivery-zones"
              },
              {
                "name": "FAQ",
                "url": "https://savorygourmet.com/pages/frequently-asked-questions"
              },
              {
                "name": "Petrovich Caviar",
                "url": "https://www.petrovichcaviar.com/"
              }
            ],
            "url": "https://savorygourmet.com/pages/about-us"
          },
          {
            "name": "About Us",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/about-us"
          },
          {
            "name": "Team",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/team"
          },
          {
            "name": "Contact",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/contact"
          },
          {
            "name": "Delivery Zones",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/delivery-zones"
          },
          {
            "name": "FAQ",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/frequently-asked-questions"
          },
          {
            "name": "Petrovich Caviar",
            "subcategories": null,
            "url": "https://www.petrovichcaviar.com/"
          },
          {
            "name": "Work With Us",
            "subcategories": [
              {
                "name": "New Customer",
                "url": "https://savorygourmet.com/pages/new-customer"
              },
              {
                "name": "Order Online via Rekki",
                "url": "https://get.rekki.com/savory-gourmet"
              },
              {
                "name": "New Supplier",
                "url": "https://savorygourmet.com/pages/new-vendor"
              },
              {
                "name": "Refer a Friend",
                "url": "https://savorygourmet.com/pages/referral-page"
              },
              {
                "name": "Job Offer",
                "url": "https://savorygourmet.com/pages/join-us"
              }
            ],
            "url": "https://savorygourmet.com/pages/new-customer"
          },
          {
            "name": "New Customer",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/new-customer"
          },
          {
            "name": "Order Online via Rekki",
            "subcategories": null,
            "url": "https://get.rekki.com/savory-gourmet"
          },
          {
            "name": "New Supplier",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/new-vendor"
          },
          {
            "name": "Refer a Friend",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/referral-page"
          },
          {
            "name": "Job Offer",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/join-us"
          },
          {
            "name": "Catalogs",
            "subcategories": [
              {
                "name": "See all Catalogs & Brochures",
                "url": "https://savorygourmet.com/pages/catalog"
              }
            ],
            "url": "https://savorygourmet.com/pages/catalog"
          },
          {
            "name": "See all Catalogs & Brochures",
            "subcategories": null,
            "url": "https://savorygourmet.com/pages/catalog"
          }
        ],
        "url": "https://savorygourmet.com/pages/contact"
      }
    ]
  }
}

''')

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

	def get_categories(self):
		"""
		Returns a list of category dictionaries from the CATEGORIES data.

		Returns:
			list: A list of dictionaries, each containing 'id' and 'name' of a category
		"""
		category_options = self.CATEGORIES.get('data', {}).get('categories', {})
		return [
			{'id': option['id'], 'name': option['name']}
			for option in category_options
			if option.get('id') and option.get('name')
		]

	def get_taxonomy(self):
		categories = self.CATEGORIES.get('data', {}).get('categories', [])
		print(f"Categories: {categories}")
		return categories

	# ************************************************************************

	# 	Product Scraping Functions
	# ************************************************************************



	# ************************************************************************
	def build_categories_list(self):
		url = self.BASE_URL
		navigation = self.get_navigation_structure(url)
		# self.print_navigation_structure(navigation)
		return f"<div>{navigation}</div>"



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
			category_found_count = len(sub_categories)
			print(f"Found {category_found_count} categories to process...")
			for sub_category in sub_categories:
				sub_category_name = sub_category['name']
				print(f"sub category: {sub_category_name}")
				if sub_category.get('subcategories', False):
					for sub_sub_category in sub_category['subcategories']:
						sub_sub_category_name = sub_sub_category['name']
						print(f"sub sub category: {sub_sub_category_name}")
						if loop_counter < category_found_count and loop_counter < test_categories:
							loop_counter += 1
							url = sub_sub_category['url']
							print(f"Url: {url}")
							detail_urls, html = self.get_category_page(url, category_name, sub_category_name, sub_sub_category_name)
							all_urls.extend(detail_urls)
						time.sleep(3)
				else:
					url = sub_category['url']
					print(f"Url: {url}")
					detail_urls, html = self.get_category_page(url, category_name, sub_category_name, '')
					all_urls.extend(detail_urls)

		# html_table_to_csv(html_table)
		html += f"<h2>Total products found: {total_products}</h2>"

		print(f"Total products found: {len(all_urls)}")
		return html

	def get_category_page(self, url, category_name, sub_category_name, sub_sub_category_name):
		print("get_category_page()")
		main_window = self.driver.current_window_handle
		html = ''
		total_products = 0
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
			page_count = 1
			next_page = True

			while next_page:
				try:
					# Wait for page to load
					detail_urls = []
					if url in self.driver.current_url:
						print("Found products page")
						time.sleep(2)
						html_line, detail_urls = self.grab_products()
					products_found_count = len(detail_urls)
					html += f"<div>Found {products_found_count} products for category {sub_category_name}</div>"
					print(f"Found {products_found_count} products for category {sub_category_name}")
					total_products += products_found_count
					self.save_urls_to_csv(detail_urls, category_name, sub_category_name, sub_sub_category_name)

				except Exception as e:
					print(f"****************** ⛔️⛔️⛔️ Error getting details: {e}")
					html += f"<div>Name: {sub_category_name} (Error getting details)</div>"

				try:
					paging = self.wait.until(
						EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination--inner'))
					)
					paging.find_element(By.CLASS_NAME, 'pagination--next').click()
					next_page = True
				except Exception as e:
					next_page = False


		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing category: {e}")

		return detail_urls, html

	def get_product_details(self, url, row_spec=None):
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print("processing product detail page")
		print(f"Loading page...{url}")

		data = ''
		sku = row_spec['sku']
		request_filter = url

		self.driver.get(url)
		print(f"Sent Request")
		try:
			# Wait for the page to load
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(
					(By.CSS_SELECTOR, "script[type='application/json'][data-section-type='static-product']"))
			)

			# Get the page source and parse it with BeautifulSoup
			soup = BeautifulSoup(self.driver.page_source, 'html.parser')

			# Find the script tag with the product data
			script_tag = soup.find('script', {
				'type': 'application/json',
				'data-section-type': 'static-product'
			})

			if script_tag and script_tag.string:
				try:
					# Parse the JSON data from the script tag
					product_data = json.loads(script_tag.string)

					# Extract product information
					product = product_data.get('product', {})

					row_spec = self.get_product_data(product, row_spec)

					# Update row_spec with the extracted data
					# row_spec['name'] = product.get('title', '')
					# row_spec['description'] = product.get('description', '')
					# row_spec['price'] = str(product.get('price', 0) / 100)  # Convert cents to dollars
					# row_spec['sku'] = product.get('variants', [{}])[0].get('sku', '')
					# row_spec['upc'] = ''  # Not available in the provided data
					#
					# # Handle images if needed
					# if 'images' in product and product['images']:
					# 	row_spec['image_url'] = f"https:{product['images'][0]}" if not product['images'][0].startswith(
					# 		'http') else product['images'][0]

				except json.JSONDecodeError as e:
					print(f"Error parsing JSON data: {e}")
			else:
				print("Could not find the product data script tag")

		except Exception as e:
			print(f"Error getting product details: {e}")
		finally:
			del self.driver.requests

		return row_spec

