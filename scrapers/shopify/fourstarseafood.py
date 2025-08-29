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

class FourStarSeafoodScraper(ShopifyScraper):

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/four_star_seafood'

	BASE_URL = 'https://www.fourstarseafood.com/pages/wholesale'
	BASE_PRODUCT_URL = 'https://www.fourstarseafood.com/products/'
	VENDOR_NAME = 'Four Star Seafood'

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "id": 1,
        "name": "NEW ARRIVALSNEW ARRIVALS",
        "subcategories": [],
        "url": "/pages/new-arrivals"
      },
      {
        "id": 2,
        "name": "VALUES UNDER $15VALUES UNDER $15",
        "subcategories": [],
        "url": "/collections/under-15"
      },
      {
        "id": 3,
        "name": "SEAFOOD",
        "subcategories": [
          {
            "name": "FINFISH",
            "subcategories": [],
            "url": "/pages/seafood#shopify-section-fresh-seafood"
          },
          {
            "name": "SHELLFISH",
            "subcategories": [],
            "url": "/pages/seafood#shopify-section-shellfish"
          },
          {
            "name": "OYSTERS",
            "subcategories": [],
            "url": "/pages/seafood#shopify-section-oysters"
          },
          {
            "name": "CURED/CAVIAR",
            "subcategories": [],
            "url": "/pages/seafood#shopify-section-cured-caviar"
          },
          {
            "name": "FROZEN",
            "subcategories": [],
            "url": "/pages/seafood#shopify-section-frozen-seafood"
          }
        ],
        "url": "/pages/seafood"
      },
      {
        "id": 4,
        "name": "Meals & KitsMeals & Kits",
        "subcategories": [],
        "url": "/pages/prepared-meals#shopify-section-four-star-boxes-kits"
      },
      {
        "id": 5,
        "name": "MEAT",
        "subcategories": [
          {
            "name": "POULTRY",
            "subcategories": [],
            "url": "/pages/meat#shopify-section-poultry"
          },
          {
            "name": "BEEF",
            "subcategories": [],
            "url": "/pages/meat#shopify-section-beef"
          },
          {
            "name": "LAMB",
            "subcategories": [],
            "url": "/pages/meat#shopify-section-lamb"
          },
          {
            "name": "PORK",
            "subcategories": [],
            "url": "/pages/meat#shopify-section-pork"
          },
          {
            "name": "GAME",
            "subcategories": [],
            "url": "/pages/meat#shopify-section-game-other"
          },
          {
            "name": "CHARCUTERIE",
            "subcategories": [],
            "url": "/pages/meat#shopify-section-charcuterie"
          },
          {
            "name": "STOCKS",
            "subcategories": [],
            "url": "/pages/meat#shopify-section-stocks"
          }
        ],
        "url": "/pages/meat"
      },
      {
        "id": 6,
        "name": "PRODUCE",
        "subcategories": [
          {
            "name": "SEAWEEDS",
            "subcategories": [],
            "url": "/pages/produce#shopify-section-seaweed"
          },
          {
            "name": "MUSHROOMS",
            "subcategories": [],
            "url": "/pages/produce#shopify-section-mushrooms"
          },
          {
            "name": "FRUIT",
            "subcategories": [],
            "url": "/pages/produce#shopify-section-fruit"
          },
          {
            "name": "VEGETABLES",
            "subcategories": [],
            "url": "/pages/produce#shopify-section-vegetables"
          }
        ],
        "url": "/pages/produce"
      },
      {
        "id": 7,
        "name": "Featured Ingredients",
        "subcategories": [
          {
            "name": "Mancini Pasta",
            "subcategories": [],
            "url": "/pages/bakery#shopify-section-mancini-pasta"
          },
          {
            "name": "N25 Caviar",
            "subcategories": [],
            "url": "/pages/bakery#shopify-section-n25-caviar"
          },
          {
            "name": "Queens Market",
            "subcategories": [],
            "url": "/pages/bakery#shopify-section-queens-market"
          },
          {
            "name": "Cafe 13 88 Coffee",
            "subcategories": [],
            "url": "/collections/coffee-mr-espresso"
          }
        ],
        "url": "/pages/bakery"
      },
      {
        "id": 8,
        "name": "CHEF'S PROVISIONS",
        "subcategories": [
          {
            "name": "DAIRY",
            "subcategories": [
              {
                "name": "MILK & CREAM",
                "url": "/pages/dairy#shopify-section-milk-cream"
              },
              {
                "name": "BUTTER & EGGS",
                "url": "/pages/dairy#shopify-section-butter-eggs"
              },
              {
                "name": "CHEESE",
                "url": "/pages/dairy#shopify-section-cheese"
              }
            ],
            "url": "/pages/dairy"
          },
          {
            "name": "MILK & CREAM",
            "subcategories": [],
            "url": "/pages/dairy#shopify-section-milk-cream"
          },
          {
            "name": "BUTTER & EGGS",
            "subcategories": [],
            "url": "/pages/dairy#shopify-section-butter-eggs"
          },
          {
            "name": "CHEESE",
            "subcategories": [],
            "url": "/pages/dairy#shopify-section-cheese"
          },
          {
            "name": "ASIAN SPECIALTY",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-japanese"
          },
          {
            "name": "BUTTER & EGGS",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-butter-eggs"
          },
          {
            "name": "CHEESE",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-cheese"
          },
          {
            "name": "COFFEE & BEVERAGE",
            "subcategories": [],
            "url": "/collections/coffee-mr-espresso"
          },
          {
            "name": "Cochon Volant",
            "subcategories": [],
            "url": "/pages/prepared-meals#shopify-section-cochon-volant"
          },
          {
            "name": "GRAINS, RICE, & BEANS",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-grains-rice-beans"
          },
          {
            "name": "HONEY, JAMS, & MARMALADES",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-honey-jams-marmalades"
          },
          {
            "name": "MILK & CREAM",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-milk-cream"
          },
          {
            "name": "NUTS",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-nuts"
          },
          {
            "name": "OILS",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-oils"
          },
          {
            "name": "OLIVES & PRESERVED VEGETABLES",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-olives-preserved-vegetables"
          },
          {
            "name": "PASTA",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-pasta"
          },
          {
            "name": "SALT",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-salt"
          },
          {
            "name": "SAVORY CONDIMENTS",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-savory-condiments"
          },
          {
            "name": "SWEET CONDIMENTS",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-sweet-condiments"
          },
          {
            "name": "SNACKS & SWEETS",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-snacks-sweets"
          },
          {
            "name": "SPICES",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-spices"
          },
          {
            "name": "VINEGARS",
            "subcategories": [],
            "url": "/pages/pantry#shopify-section-vinegar"
          },
          {
            "name": "MILK & CREAM",
            "subcategories": [],
            "url": "/pages/dairy#shopify-section-milk-cream"
          },
          {
            "name": "BUTTER & EGGS",
            "subcategories": [],
            "url": "/pages/dairy#shopify-section-butter-eggs"
          },
          {
            "name": "CHEESE",
            "subcategories": [],
            "url": "/pages/dairy#shopify-section-cheese"
          }
        ],
        "url": "/pages/pantry"
      },
      {
        "id": 9,
        "name": "MORE",
        "subcategories": [
          {
            "name": "CHEF'S TOOLS",
            "subcategories": [],
            "url": "/collections/chefs-tools"
          },
          {
            "name": "BESTSELLERS",
            "subcategories": [],
            "url": "/pages/bestseller"
          },
          {
            "name": "DELIVERY & SHIPPING",
            "subcategories": [],
            "url": "/pages/delivery-and-shipping"
          },
          {
            "name": "BLOG",
            "subcategories": [],
            "url": "/blogs/blog"
          },
          {
            "name": "FAQ",
            "subcategories": [],
            "url": "/pages/faq"
          },
          {
            "name": "ABOUT US",
            "subcategories": [],
            "url": "/pages/four-star-about-us"
          },
          {
            "name": "CONTACT US",
            "subcategories": [],
            "url": "/pages/four-star-contact"
          },
          {
            "name": "WHOLESALE",
            "subcategories": [],
            "url": "/pages/wholesale"
          }
        ],
        "url": "#"
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
		return f"https://www.fourstarseafood.com{category['url']}"

	# ************************************************************************

	# 	Product Scraping Functions
	# ************************************************************************

	def get_product_details(self, url, row_spec=None):
		"""Get Product Details"""
		print("FourStarSeafoodScraper.get_product_details()")
		data = self.get_product_details_scrape( url, row_spec)
		print(data)
		row_spec = self.get_product_data(data.get('product', {}), row_spec)
		return row_spec

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

	# ************************************************************************
	def grab_products(self, start=None):

		if start:
			products = self.wait.until(
				EC.presence_of_all_elements_located((By.CSS_SELECTOR, f'#{start} a.ProductItem__ImageWrapper' ))
			)
		else:
			products = self.wait.until(
				EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.ProductItem__ImageWrapper'))
			)

		print(f"products found: {len(products)}")
		detail_urls = [product.get_attribute("href") for product in products]
		return '', detail_urls

	def build_categories_list(self):
		url = self.BASE_URL
		navigation = self.get_navigation_structure(url)
		# self.print_navigation_structure(navigation)
		return f"<div>{navigation}</div>"

	def get_navigation_dict(self, url: str, headers: Optional[Dict] = None) -> Dict[str, Any]:
		"""
		Scrapes and parses the navigation structure from the Four Star Seafood website.

		Args:
			url: The URL of the page containing the navigation menu
			headers: Optional headers for the request

		Returns:
			A dictionary containing the navigation structure with categories and subcategories
		"""
		try:
			self.driver.get(url)
			time.sleep(3)  # Allow page to load

			# Get the page source and parse with BeautifulSoup
			soup = BeautifulSoup(self.driver.page_source, 'html.parser')

			# Initialize the navigation structure
			navigation = {
				'data': {
					'categories': []
				}
			}

			# Find the main navigation menu
			nav = soup.find('nav', {'class': 'Header__MainNav'})
			if not nav:
				print("Navigation menu not found")
				return navigation

			# Find all top-level menu items
			top_level_items = nav.select('ul.HorizontalList > li.HorizontalList__Item')

			for i, item in enumerate(top_level_items, 1):
				# Extract category name and URL
				category_link = item.find('a', class_='Heading')
				if not category_link:
					continue

				category_name = category_link.get_text(strip=True).replace('&amp;', '&')
				category_url = category_link.get('href', '')

				# Skip if it's the home or contact page
				if any(x in category_name.lower() for x in ['home', 'contact']):
					continue

				# Initialize category data
				category_data = {
					'name': category_name,
					'url': category_url,
					'id': i,
					'subcategories': []
				}

				# Find subcategories
				submenu = item.find('div', class_='DropdownMenu')
				if submenu:
					subcategory_lists = submenu.find_all('ul', class_='Linklist')

					for sublist in subcategory_lists:
						subcategory_items = sublist.find_all('li', class_='Linklist__Item')

						for sub_item in subcategory_items:
							subcategory_link = sub_item.find('a', class_='Link')
							if not subcategory_link:
								continue

							subcategory_name = subcategory_link.get_text(strip=True).replace('&amp;', '&')
							subcategory_url = subcategory_link.get('href', '')

							# Initialize subcategory data
							subcategory_data = {
								'name': subcategory_name,
								'url': subcategory_url,
								'subcategories': []
							}

							# Check for sub-subcategories (third level)
							subsubmenu = sub_item.find('div', class_='DropdownMenu')
							if subsubmenu:
								subsubcategory_items = subsubmenu.find_all('li', class_='Linklist__Item')

								for subsub_item in subsubcategory_items:
									subsub_link = subsub_item.find('a', class_='Link')
									if not subsub_link:
										continue

									subsub_name = subsub_link.get_text(strip=True).replace('&amp;', '&')
									subsub_url = subsub_link.get('href', '')

									subcategory_data['subcategories'].append({
										'name': subsub_name,
										'url': subsub_url
									})

							# Only add if it's a direct child (not a sub-subcategory)
							if not subsubmenu or subsubmenu.find_parent('li') == sub_item:
								category_data['subcategories'].append(subcategory_data)

				navigation['data']['categories'].append(category_data)

			return navigation

		except Exception as e:
			print(f"Error getting navigation structure: {e}")
			return {'data': {'categories': []}}

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
						if url.split('#')[1]:
							html_line, detail_urls = self.grab_products(start=url.split('#')[1])
						else:
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
