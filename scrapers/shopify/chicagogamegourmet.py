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

class ChicagoMeatGourmetScraper(ShopifyScraper):
	# 849/edit_note/1753/
	CRM_ID = 849
	CRM_NOTE_ID = 1753
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/chicago_meat_gourmet'

	BASE_URL = 'https://chicagogame.us/'
	BASE_PRODUCT_URL = 'https://chicagogame.us/'
	VENDOR_NAME = 'Chicago Meat Gourmet'

	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "id": 1,
        "name": "Butcher Shop",
        "subcategories": [
          {
            "name": "Game Meats",
            "subcategories": [
              {
                "name": "Bison",
                "url": "/collections/bison"
              },
              {
                "name": "Exotics",
                "url": "/collections/bacon-hams-smoked-meats"
              },
              {
                "name": "Elk",
                "url": "/collections/elk"
              },
              {
                "name": "Rabbit",
                "url": "/collections/rabbit"
              },
              {
                "name": "Venison",
                "url": "/collections/venison"
              },
              {
                "name": "Wild Boar",
                "url": "/collections/wild-boar"
              },
              {
                "name": "Yak",
                "url": "/collections/yak"
              }
            ],
            "url": "/collections/game-meats-all"
          },
          {
            "name": "Tame Meats",
            "subcategories": [
              {
                "name": "U.S.D.A Beef",
                "url": "/collections/usda-beef1"
              },
              {
                "name": "Wagyu Beef",
                "url": "/collections/onlinestore-beef"
              },
              {
                "name": "Lamb & Goat",
                "url": "/collections/lamb"
              },
              {
                "name": "Heritage Pork",
                "url": "/collections/onlinestore-pork"
              }
            ],
            "url": "/collections/tame-meats-all"
          },
          {
            "name": "Game Birds / Poultry",
            "subcategories": [],
            "url": "/collections/poultry"
          },
          {
            "name": "Sausages",
            "subcategories": [],
            "url": "/collections/onlinestore-sausage"
          },
          {
            "name": "Jerky / Meat Sticks / Salami",
            "subcategories": [],
            "url": "/collections/snack-sticks-jerky"
          }
        ],
        "url": "/"
      },
      {
        "id": 2,
        "name": "Kitchen / Pantry",
        "subcategories": [
          {
            "name": "Seasonings / Spices / Rubs",
            "subcategories": [],
            "url": "/collections/spices-seasonings"
          },
          {
            "name": "Cooking Sauces & Bases",
            "subcategories": [],
            "url": "/collections/gravy-stocks-demi-glace"
          },
          {
            "name": "Fats / Oils / Tallows",
            "subcategories": [],
            "url": "/collections/cooking-fat-tallow"
          },
          {
            "name": "Side Dishes",
            "subcategories": [],
            "url": "/collections/side-dishes"
          },
          {
            "name": "Sauces / Condiments",
            "subcategories": [],
            "url": "/collections/seaces-condiments"
          },
          {
            "name": "Tinfish",
            "subcategories": [],
            "url": "/collections/seafood"
          },
          {
            "name": "Smoking Woods",
            "subcategories": [],
            "url": "/collections/aromatic-smoking-woods"
          }
        ],
        "url": "/"
      },
      {
        "id": 3,
        "name": "Gift Boxes",
        "subcategories": [],
        "url": "/collections/gift-boxes"
      },
      {
        "id": 4,
        "name": "Crescent City Meat",
        "subcategories": [],
        "url": "/collections/crescent-city-meats"
      },
      {
        "id": 5,
        "name": "Limited Time Products",
        "subcategories": [],
        "url": "/pages/limited-time-products"
      }
    ]
  }
}                      
''')

	def __init__(self, options=None):
		super().__init__(options)

	def get_category_url(self, category):
		return f"https://chicagogame.us{category['url']}"

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
					if not 'disabled'  in classes:
						paging.find_element(By.CLASS_NAME, 'next').click()
						print("Going to next page")
						next_page = True
					else:
						print("Next is disabled")
						next_page = False
				except Exception as e:
					print("There is no next page")
					next_page = False


		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing category: {e}")

		return detail_urls, html

	def get_product_details(self, url, row_spec=None):
		"""Get Product Details"""
		data = self.get_product_details_json( url, row_spec)
		self.get_product_data(data.get('product', {}), row_spec)
		return row_spec

	# ************************************************************************
	# Category URL retrieval Functions
	# ************************************************************************

	def get_navigation_dict(self, url: str, headers: Optional[Dict] = None) -> Dict[str, Any]:
		"""
		Scrapes and parses the navigation structure from the Chicago Game website.

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
			nav = soup.find('ul', {'class': 'main-nav'})
			if not nav:
				print("Navigation menu not found")
				return {'data': {'categories': []}}

			# Initialize the navigation structure
			navigation = {'data': {'categories': []}}
			category_id = 1

			# Find all top-level menu items
			top_level_items = nav.find_all('li', recursive=False)

			for item in top_level_items:
				# Check if it's a dropdown menu (has details tag)
				details = item.find('details')
				if not details:
					# Simple menu item without dropdown
					link = item.find('a', class_='main-nav__item--primary')
					if not link:
						continue

					category_name = link.get_text(strip=True)
					category_url = link.get('href', '')

					# Skip if it's a non-category link
					if not category_url.startswith('/collections/') and not category_url.startswith('/pages/'):
						continue

					# Create category data
					category_data = {
						'id': category_id,
						'name': category_name,
						'url': category_url,
						'subcategories': []
					}
					category_id += 1
					navigation['data']['categories'].append(category_data)
					continue

				# Handle dropdown menu
				summary = details.find('summary')
				if not summary:
					continue

				# Get category name and URL
				category_link = summary.find('a', class_='main-nav__item--primary')
				if not category_link:
					continue

				category_name = category_link.get_text(strip=True).replace('›', '').strip()
				category_url = category_link.get('href', '/')  # Default to home if no URL

				# Initialize category data
				category_data = {
					'id': category_id,
					'name': category_name,
					'url': category_url,
					'subcategories': []
				}
				category_id += 1

				# Find subcategories in the dropdown
				child_nav = details.find('ul', class_='child-nav--dropdown')
				if not child_nav:
					navigation['data']['categories'].append(category_data)
					continue

				# Process subcategories
				for sub_item in child_nav.find_all('li', recursive=False):
					# Skip back button and header in mobile view
					if 'md:hidden' in sub_item.get('class', []):
						continue

					# Check for nav-menu component (nested subcategories)
					nav_menu = sub_item.find('nav-menu')
					if nav_menu:
						sub_details = nav_menu.find('details')
						if not sub_details:
							continue

						# Get subcategory name and URL
						sub_link = sub_details.find('a', class_='child-nav__item')
						if not sub_link:
							continue

						subcategory_name = sub_link.get_text(strip=True).replace('›', '').strip()
						subcategory_url = sub_link.get('href', '')

						# Skip if it's a non-category link
						if not subcategory_url.startswith('/collections/'):
							continue

						# Initialize subcategory data
						subcategory_data = {
							'name': subcategory_name,
							'url': subcategory_url,
							'subcategories': []
						}

						# Find sub-subcategories
						grandchild_nav = sub_details.find('ul', class_='main-nav__grandchild')
						if grandchild_nav:
							for grandchild_item in grandchild_nav.find_all('li', recursive=False):
								# Skip "Go to" links and other non-category items
								if 'col-start-1' in grandchild_item.get('class', []):
									continue

								grandchild_link = grandchild_item.find('a', class_='grandchild-nav__item')
								if not grandchild_link:
									continue

								grandchild_name = grandchild_link.get_text(strip=True)
								grandchild_url = grandchild_link.get('href', '')

								# Skip if it's a non-category link
								if not grandchild_url.startswith('/collections/'):
									continue

								subcategory_data['subcategories'].append({
									'name': grandchild_name,
									'url': grandchild_url
								})

						category_data['subcategories'].append(subcategory_data)
					else:
						# Simple subcategory link
						sub_link = sub_item.find('a', class_='child-nav__item')
						if not sub_link:
							continue

						subcategory_name = sub_link.get_text(strip=True)
						subcategory_url = sub_link.get('href', '')

						# Skip if it's a non-category link
						if not subcategory_url.startswith('/collections/'):
							continue

						category_data['subcategories'].append({
							'name': subcategory_name,
							'url': subcategory_url,
							'subcategories': []
						})

				navigation['data']['categories'].append(category_data)

			return navigation

		except Exception as e:
			print(f"Error getting navigation structure: {e}")
			return {'data': {'categories': []}}

	# ************************************************************************
	# Product List Functions
	# ************************************************************************

	def get_products_from_html(self):
		print("get_products_from_html()")
		products = self.wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'product-card .card-link'))
		)

		print(f"products found: {len(products)}")
		detail_urls = [product.get_attribute("href") for product in products]
		return '', detail_urls

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
			return image.get('src', '')

		except Exception as e:
			print(f"Error extracting image from viewModel.assets: {str(e)}")

		return ''






