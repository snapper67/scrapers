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

	def get_category_url(self, category):
		return category['url']

	# ************************************************************************

	# 	Product Scraping Functions
	# ************************************************************************



	# ************************************************************************
	def build_categories_list(self):
		url = self.BASE_URL
		navigation = self.get_navigation_structure(url)
		# self.print_navigation_structure(navigation)
		return f"<div>{navigation}</div>"

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
		"""Get Product Details"""
		return self.get_product_details_scrape( url, row_spec)

