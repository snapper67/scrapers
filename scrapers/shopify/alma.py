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
from scrapers.shopify.shopify import ShopifyScraper
from typing import List, Dict, Any, Optional


class AlmaScraper(ShopifyScraper):
	# /17/edit_note/1710/
	CRM_ID = 17
	CRM_NOTE_ID = 1710
	CRM_PRICE_TYPE = 'Retail'
	CRM_STATUS_OVERRIDE = ''

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/alma'

	BASE_URL = 'https://almagourmet.com'
	BASE_PRODUCT_URL = 'https://almagourmet.com/collections/all'
	VENDOR_NAME = 'Alma Gourmet'

	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "id": 1,
        "name": "Risotto Rice",
        "subcategories": [
          {
            "id": 2,
            "name": "Carnaroli Rice",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/risotto?filter.p.m.custom.product_type=Carnaroli+Rice&sort_by=manual"
          },
          {
            "id": 3,
            "name": "Arborio Rice",
            "subcategories": [],
            "url": "https://almagourmet.com/collections/risotto?filter.p.m.custom.product_type=Arborio+Rice&sort_by=manual"
          },
          {
            "id": 4,
            "name": "Vialone Nano Rice",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/risotto?filter.p.m.custom.product_type=Vialone+Nano+Rice&sort_by=manual"
          },
          {
            "id": 5,
            "name": "Black Rice",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/risotto?filter.p.m.custom.product_type=Black+Rice&sort_by=manual"
          },
          {
            "id": 6,
            "name": "Mix for Risotto",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/risotto?filter.p.m.custom.product_type=Risotto+Mix&sort_by=manual"
          },
          {
            "id": 7,
            "name": "Risotto Dinner Kits",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/risotto?filter.p.m.custom.product_type=Culinary+Kits+%26+Holiday+Gift&sort_by=manual"
          }
        ],
        "url": "/collections/risotto"
      },
      {
        "id": 8,
        "name": "Pasta Sauce Pantry",
        "subcategories": [
          {
            "id": 9,
            "name": "Tomato Sauces",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/pasta-sauce-pantry?filter.p.m.custom.product_type=Tomato+Sauces&sort_by=manual"
          },
          {
            "id": 10,
            "name": "Tomato Staples",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/pasta-sauce-pantry?filter.p.m.custom.product_type=Tomato+Staples&sort_by=manual"
          },
          {
            "id": 11,
            "name": "Pesto Sauces",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/pasta-sauce-pantry?filter.p.m.custom.product_type=Pesto+Sauces&sort_by=manual"
          },
          {
            "id": 12,
            "name": "Traditional Italian Sauces",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/pasta-sauce-pantry?filter.p.m.custom.product_type=Traditional+Italian+Sauces&sort_by=manual"
          },
          {
            "id": 13,
            "name": "Truffle Pasta Sauces",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/pasta-sauce-pantry?filter.p.m.custom.product_type=Truffle+Pasta+Sauces&sort_by=manual"
          }
        ],
        "url": "/collections/pasta-sauce-pantry"
      },
      {
        "id": 14,
        "name": "Italian Beans",
        "subcategories": [],
        "url": "/collections/italian-beans"
      },
      {
        "id": 15,
        "name": "Veggies & Nuts",
        "subcategories": [
          {
            "id": 16,
            "name": "Fresh Veggies",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/veggies-nuts-and-beans?filter.p.m.custom.product_type=Fresh+Veggies&sort_by=manual"
          },
          {
            "id": 17,
            "name": "Preserved Veggies",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/veggies-nuts-and-beans?filter.p.m.custom.product_type=Preserved+Veggies&sort_by=manual"
          },
          {
            "id": 18,
            "name": "Dried Veggies",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/veggies-nuts-and-beans?filter.p.m.custom.product_type=Dried+Veggies&sort_by=manual"
          },
          {
            "id": 19,
            "name": "Nuts",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/veggies-nuts-and-beans?filter.p.m.custom.product_type=Nuts&sort_by=manual"
          }
        ],
        "url": "/collections/veggies-nuts-and-beans"
      },
      {
        "id": 20,
        "name": "Polenta & Flour",
        "subcategories": [
          {
            "id": 21,
            "name": "Polenta",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/polenta-flour?filter.p.m.custom.product_type=Polenta&sort_by=manual"
          },
          {
            "id": 22,
            "name": "Flour",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/polenta-flour?filter.p.m.custom.product_type=Flour&sort_by=manual"
          }
        ],
        "url": "/collections/polenta-flour"
      },
      {
        "id": 23,
        "name": "Crackers & Breadstiks",
        "subcategories": [
          {
            "id": 24,
            "name": "Taralli & Stuzzichini Pugliesi",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/crackers-breadstiks?filter.p.m.custom.product_type=Taralli+%26+Stuzzichini+Pugliesi&sort_by=manual"
          },
          {
            "id": 25,
            "name": "Friselle Pugliesi",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/crackers-breadstiks?filter.p.m.custom.product_type=Friselle+Pugliesi&sort_by=manual"
          },
          {
            "id": 26,
            "name": "Pane Carasatu",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/crackers-breadstiks?filter.p.m.custom.product_type=Pane+Carasatu&sort_by=manual"
          },
          {
            "id": 27,
            "name": "Piadina Bread",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/crackers-breadstiks?filter.p.m.custom.product_type=Piadina+Bread&sort_by=manual"
          },
          {
            "id": 28,
            "name": "Grissini I Macoritti",
            "subcategories": [],
            "url": "https://almagourmet.com/collections/crackers-breadstiks?filter.p.m.custom.product_type=Grissini"
          },
          {
            "id": 29,
            "name": "Bruschette",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/crackers-breadstiks?filter.p.m.custom.product_type=Bruschette&sort_by=manual"
          }
        ],
        "url": "/collections/crackers-breadstiks"
      },
      {
        "id": 30,
        "name": "Herbs, Sea Salt & Spices",
        "subcategories": [
          {
            "id": 31,
            "name": "Herbs",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/spices-herbs-sea-salt?filter.p.m.custom.product_type=Herbs&sort_by=manual"
          },
          {
            "id": 32,
            "name": "Sea Salt",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/spices-herbs-sea-salt?filter.p.m.custom.product_type=Sea+Salt&sort_by=manual"
          },
          {
            "id": 33,
            "name": "Flavored Salt",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/spices-herbs-sea-salt?filter.p.m.custom.product_type=Flavored+Salt&sort_by=manual"
          },
          {
            "id": 34,
            "name": "Spices",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/spices-herbs-sea-salt?filter.p.m.custom.product_type=Spices&sort_by=manual"
          }
        ],
        "url": "/collections/spices-herbs-sea-salt"
      },
      {
        "id": 35,
        "name": "Sweet Pantry",
        "subcategories": [
          {
            "id": 36,
            "name": "Panettone & Pandoro",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/italian-sweets?filter.p.m.custom.product_type=Pandoro+%26+Panettone&sort_by=manual"
          },
          {
            "id": 37,
            "name": "Torrone & Chocolate Gifts",
            "subcategories": [],
            "url": "https://almagourmet.com/collections/italian-sweets?filter.p.m.custom.product_type=Chocolate&filter.p.m.custom.product_type=Torrone&sort_by=manual"
          },
          {
            "id": 38,
            "name": "Italian Biscotti",
            "subcategories": [],
            "url": "/collections/italian-biscotti"
          },
          {
            "id": 39,
            "name": "Spreadable Creams",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/italian-sweets?filter.p.m.custom.product_type=Spreadable+Creams&sort_by=manual"
          },
          {
            "id": 40,
            "name": "Marmalades & Jams",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/italian-sweets?filter.p.m.custom.product_type=Marmalades+%26+Jams&sort_by=manual"
          },
          {
            "id": 41,
            "name": "Topping Sauces",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/italian-sweets?filter.p.m.custom.product_type=Topping+Sauces&sort_by=manual"
          },
          {
            "id": 42,
            "name": "Honey",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/italian-sweets?filter.p.m.custom.product_type=Honey&sort_by=manual"
          },
          {
            "id": 43,
            "name": "Italian Cakes",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/italian-sweets?filter.p.m.custom.product_type=Torte&sort_by=best-selling"
          },
          {
            "id": 44,
            "name": "Sicilian Cannoli",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/italian-sweets?filter.p.m.custom.product_type=Sicilian+Cannoli&sort_by=manual"
          },
          {
            "id": 45,
            "name": "Ricotta Cannoli Cream",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/italian-sweets?filter.p.m.custom.product_type=Cannoli+Cream&sort_by=manual"
          },
          {
            "id": 46,
            "name": "Dried Italian Figs",
            "subcategories": [],
            "url": "https://almagourmet.com/collections/italian-sweets?filter.p.m.custom.product_type=Dried+Italian+Figs&sort_by=manual"
          },
          {
            "id": 47,
            "name": "Modica Chocolate",
            "subcategories": [],
            "url": "https://almagourmet.com/collections/italian-sweets?filter.p.m.custom.product_type=Modica+Chocolate&sort_by=manual"
          },
          {
            "id": 48,
            "name": "Confetti",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/italian-sweets?filter.p.m.custom.product_type=Confetti&sort_by=manual"
          },
          {
            "id": 49,
            "name": "Edible Gold & Silver",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/italian-sweets?filter.p.m.custom.product_type=Edible+Gold+%26+Silver&sort_by=manual"
          },
          {
            "id": 50,
            "name": "Sweet Kits",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/italian-sweets?filter.p.m.custom.product_type=Culinary+Kits+%26+Holiday+Gift&sort_by=manual"
          }
        ],
        "url": "/collections/italian-sweets"
      },
      {
        "id": 51,
        "name": "Culinary Kits, Gifts & Baskets",
        "subcategories": [
          {
            "id": 52,
            "name": "Gift Cards",
            "subcategories": [],
            "url": "/collections/gift-baskets?filter.p.m.custom.product_type=Gift+Cards"
          },
          {
            "id": 53,
            "name": "Holiday Gift Boxes",
            "subcategories": [],
            "url": "https://almagourmet.com/collections/gift-baskets?filter.p.m.custom.product_type=Gift+Box&sort_by=manual"
          },
          {
            "id": 54,
            "name": "Culinary Kits",
            "subcategories": [],
            "url": "/collections/gift-baskets?filter.p.m.custom.product_type=Culinary+Kits+%26+Holiday+Gift"
          }
        ],
        "url": "/collections/gift-baskets"
      },
      {
        "id": 55,
        "name": "Bottled Water",
        "subcategories": [
          {
            "id": 56,
            "name": "Filette Water",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/bottles-water?filter.p.m.custom.product_brand=Filette&sort_by=best-selling"
          },
          {
            "id": 57,
            "name": "Lurisia Water",
            "subcategories": [],
            "url": "https://35ee2e-2.myshopify.com/collections/bottles-water?filter.p.m.custom.product_brand=Lurisia&sort_by=best-selling"
          }
        ],
        "url": "/collections/bottles-water"
      },
      {
        "id": 58,
        "name": "Kitchen Ware",
        "subcategories": [
          {
            "id": 59,
            "name": "Specialty Kitchen Tools",
            "subcategories": [],
            "url": "https://almagourmet.com/collections/kitchen-ware?filter.p.m.custom.product_type=Specialty+Kitchen+Tools&sort_by=manual"
          },
          {
            "id": 60,
            "name": "Restaurant Supplies",
            "subcategories": [],
            "url": "https://almagourmet.com/collections/kitchen-ware?filter.p.m.custom.product_type=Restaurant+Supplies&sort_by=manual"
          }
        ],
        "url": "/collections/kitchen-ware"
      },
      {
        "id": 61,
        "name": "NEW ARRIVAL",
        "subcategories": [],
        "url": "/collections/new-arrival"
      },
      {
        "id": 62,
        "name": "SALE",
        "subcategories": [],
        "url": "/collections/sale"
      },
      {
        "id": 63,
        "name": "Truffles & Mushrooms",
        "subcategories": [],
        "url": "/collections/truffles"
      },
      {
        "id": 64,
        "name": "Meats",
        "subcategories": [],
        "url": "/collections/meats"
      },
      {
        "id": 65,
        "name": "Cheeses",
        "subcategories": [],
        "url": "/collections/cheeses"
      },
      {
        "id": 66,
        "name": "Seafood",
        "subcategories": [],
        "url": "/collections/seafood"
      },
      {
        "id": 67,
        "name": "Pasta",
        "subcategories": [],
        "url": "/collections/pasta"
      },
      {
        "id": 68,
        "name": "Olive Oil & Vinegar",
        "subcategories": [],
        "url": "/collections/olive-oil-vinegar"
      },
      {
        "id": 69,
        "name": "Saffron",
        "subcategories": [],
        "url": "/collections/saffron"
      }
    ]
  }
}            
	''')

	def __init__(self, options=None):
		super().__init__(options)

	def get_category_url(self, category):
		print(f"get_category_url: {category}")
		if ("http" in category['url']):
			return category['url']
		else:
			return f"https://www.almagourmet.com{category['url']}"

	# ************************************************************************
	# Core Functions
	# These are overrides of the core functions
	# ************************************************************************

	# ************************************************************************
	# Core Function Hooks
	# These are the methods called by the core functions
	# ************************************************************************

	def get_category_page(self, url, category_name, sub_category_name, sub_sub_category_name):
		print("get_category_page()")
		detail_urls = []
		main_window = self.driver.current_window_handle
		html = ''
		total_products = 0
		self.driver.get(url)
		self.wait = WebDriverWait(self.driver, 10)
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
						html_line, detail_urls = self.get_products_from_html()
					products_found_count = len(detail_urls)
					html += f"<div>Found {products_found_count} products for category {sub_category_name}</div>"
					print(f"Found {products_found_count} products for category {sub_category_name}")
					total_products += products_found_count
					self.save_urls_to_csv(detail_urls, category_name, sub_category_name, sub_sub_category_name)

				except Exception as e:
					print(f"****************** ⛔️⛔️⛔️ Error getting details: {e}")
					html += f"<div>Name: {sub_category_name} (Error getting details)</div>"

				next_page = self.get_next_page()


		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing category: {e}")

		return detail_urls, html

	def get_product_details(self, url, row_spec=None):
		"""Get Product Details"""
		print("AlmaScraper.get_product_details()")
		data = self.get_product_details_scrape(url, row_spec,
		                                       target="script[type='application/ld+json']")
		print(data)
		row_spec = self.get_product_data(data, row_spec)
		return row_spec

	# ************************************************************************
	# Category URL retrieval Functions
	# ************************************************************************

	def get_navigation_dict(self, url: str, headers: Optional[Dict] = None) -> Dict[str, Any]:
		"""
		Scrapes and parses the navigation structure from the Alma Gourmet website.

		Args:
			url: The URL of the page containing the navigation menu
			headers: Optional headers for the request

		Returns:
			A dictionary containing the navigation structure with categories and subcategories
		"""
		try:
			# For testing with the provided HTML
			if url == "test":
				html_content = """
	            [THE_HTML_CONTENT_YOU_PROVIDED]
	            """
				soup = BeautifulSoup(html_content, 'html.parser')
			else:
				self.driver.get(url)
				time.sleep(3)  # Allow page to load
				soup = BeautifulSoup(self.driver.page_source, 'html.parser')

			# Initialize the navigation structure
			navigation = {
				'data': {
					'categories': []
				}
			}

			# Find the main navigation menu
			nav = soup.find('ul', {'id': 'SiteNavLabel-all-categories-classic-sticky'})

			if not nav:
				print("Navigation menu not found")
				return navigation
			print(nav)
			# Find all top-level menu items
			holder = nav.find('div', class_="submenu-holder")
			menu_items = holder.find_all('li', recursive=False)
			category_id = 1
			print("menu_items")

			for item in menu_items:
				print(item)
				# Skip if it's a divider or empty
				if 'divider' in item.get('class', []) or not item.find('a'):
					continue

				# Get the main category link
				main_link = item.find('a', class_='menu-link')
				if not main_link:
					continue

				# Extract category name and URL
				category_name = main_link.get_text(strip=True)
				category_url = main_link.get('href', '')

				# Create category entry
				category = {
					'id': category_id,
					'name': category_name,
					'url': category_url,
					'subcategories': []
				}
				category_id += 1

				# Check for submenu
				submenu = item.find('div', class_='babymenu')
				if submenu:
					submenu_ul = submenu.find('ul')
					if submenu_ul:
						for sub_item in submenu_ul.find_all('li'):
							sub_link = sub_item.find('a', class_='menu-link')
							if not sub_link:
								continue

							subcategory_name = sub_link.get_text(strip=True)
							subcategory_url = sub_link.get('href', '')

							category['subcategories'].append({
								'id': category_id,
								'name': subcategory_name,
								'url': subcategory_url,
								'subcategories': []
							})
							category_id += 1

				navigation['data']['categories'].append(category)

			# For debugging
			print(f"Found {len(navigation['data']['categories'])} main categories")
			return navigation

		except Exception as e:
			print(f"Error getting navigation: {str(e)}")
			return {
				'data': {
					'categories': []
				}
			}

	# ************************************************************************
	# Product List Functions
	# ************************************************************************

	def get_products_from_html(self, start=None):
		print("get_products_from_html()")
		product_count = 0
		if start:
			products = self.wait.until(
				EC.presence_of_all_elements_located((By.CSS_SELECTOR, f'#{start} a.card__image.product-item__image'))
			)
		else:
			products = self.wait.until(
				EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.card__image.product-item__image'))
			)
		while len(products) > product_count:
			product_count = len(products)
			self.driver.execute_script("arguments[0].scrollIntoView();", products[product_count - 1])
			products = self.wait.until(
				EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.card__image.product-item__image'))
			)

		print(f"products found: {len(products)}")
		detail_urls = [product.get_attribute("href") for product in products]
		return '', detail_urls

	def get_next_page(self):
		try:
			paging = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '.page_c'))
			)
			print("Checking 1")
			next_disabled = paging.find_element(By.CSS_SELECTOR, 'a.next')
			class_attribute = next_disabled.get_attribute("class")
			classes = class_attribute.split()
			print(next_disabled)
			print("Checking 2")
			if not 'disabled' in classes:
				paging.find_element(By.CLASS_NAME, 'next').click()
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

	def get_first_image_url(self, response_data):
		"""
		Extract the first available image URL from the product API response.

		Args:
			response_data (dict): The parsed JSON response from the API

		Returns:
			str: URL of the first available image, or None if no image found
		"""
		try:
			image = response_data.get('image', {})

			# If there are assets, get the first one's URL
			if image:
				# Get the first asset and extract the URL
				return image.get('url', '')

		except Exception as e:
			print(f"Error extracting image from viewModel.assets: {str(e)}")

		return ''

	def get_product_details_scrape(self, url, row_spec=None, target="script[type='application/json']"):
		#  Wait for the product name element on the product page detail page
		print("AlmaScraper.get_product_details_scrape()")
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print(f"processing product detail page for target {target}")
		print(f"Loading page...{url}")

		data = ''
		sku = row_spec['sku']
		request_filter = url

		self.driver.get(url)
		print(f"Sent Request")
		product_data = ''
		try:
			# Wait for the page to load
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(
				(By.CSS_SELECTOR, target))
			)
			print(f"Script Loaded")
			# Get the page source and parse it with BeautifulSoup
			soup = BeautifulSoup(self.driver.page_source, 'html.parser')

			scripts = soup.find_all('script', {'type': 'application/ld+json'})
			for script in scripts:
				print(script.string)
				if script and script.string:
					print("Loading product data")
					try:
						# Parse the JSON data from the script tag
						product_data = json.loads(script.string)
						try:
							if product_data.get('@type') == "Product":
								del self.driver.requests
								return product_data
						except Exception as e:
							print(f"Error getting product data: {type(e)}")
					except json.JSONDecodeError as e:
						print(f"Error parsing JSON data: {e}")
				else:
					print("Could not find the product data script tag")

		except Exception as e:
			print(f"Error getting product details: {e}")
		finally:
			del self.driver.requests

		return product_data

	def get_product_data_additional(self, data, row_spec):
		row_spec["name"] = data.get("name", "")
		row_spec['sku'] = data.get('sku', '')
		price = round(data.get("offers", [])[0].get("price", 0) * 100)
		row_spec["retail_price"] = "" if price == 0 else price
		return row_spec
