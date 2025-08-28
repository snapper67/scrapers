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

class PacificGourmetScraper(ShopifyScraper):

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/pacific_gourmet'

	BASE_URL = 'https://shop.pacgourmet.com/collections/savory'
	BASE_PRODUCT_URL = 'https://shop.pacgourmet.com/products/'
	VENDOR_NAME = 'Pacific Gourmet'

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "id": 1,
        "name": "SAVORY",
        "subcategories": [
          {
            "name": "FLOURS, GRAINS & LEGUMESCerealsBeansLentilsFlours & MealsGrainsSeedsPastaRice",
            "subcategories": [
              {
                "name": "Cereals",
                "url": "/collections/cereals"
              },
              {
                "name": "Beans",
                "url": "/collections/beans"
              },
              {
                "name": "Lentils",
                "url": "/collections/lentils"
              },
              {
                "name": "Flours & Meals",
                "url": "/collections/flours-meals"
              },
              {
                "name": "Grains",
                "url": "/collections/grains"
              },
              {
                "name": "Seeds",
                "url": "/collections/seeds-2"
              },
              {
                "name": "Pasta",
                "url": "/collections/pasta"
              },
              {
                "name": "Rice",
                "url": "/collections/rice"
              }
            ],
            "url": "/collections/flours-grains-legumes"
          },
          {
            "name": "MEATS & FISHCaviarCharcuterieEscargotsFoie GrasHamPate/TerrinesSeafoodStock & Sauce Bases",
            "subcategories": [
              {
                "name": "Caviar",
                "url": "/collections/caviar-1"
              },
              {
                "name": "Charcuterie",
                "url": "/collections/charcuterie"
              },
              {
                "name": "Escargots",
                "url": "/collections/escargots"
              },
              {
                "name": "Foie Gras",
                "url": "/collections/foie-gras"
              },
              {
                "name": "Ham",
                "url": "/collections/ham-1"
              },
              {
                "name": "Pate/Terrines",
                "url": "/collections/pate-terrines"
              },
              {
                "name": "Seafood",
                "url": "/collections/seafood"
              },
              {
                "name": "Stock & Sauce Bases",
                "url": "/collections/stock-sauce-bases"
              }
            ],
            "url": "/collections/meats-fish"
          },
          {
            "name": "MUSHROOMS & TRUFFLESMushroomsTruffles",
            "subcategories": [
              {
                "name": "Mushrooms",
                "url": "/collections/mushrooms-1"
              },
              {
                "name": "Truffles",
                "url": "/collections/truffles-1"
              }
            ],
            "url": "/collections/mushrooms-truffles"
          },
          {
            "name": "OILS & VINEGARSBalsamicVerjusVinegarsVinegar in BulkOlive Oil",
            "subcategories": [
              {
                "name": "Balsamic",
                "url": "/collections/balsamic"
              },
              {
                "name": "Verjus",
                "url": "/collections/verjus"
              },
              {
                "name": "Vinegars",
                "url": "/collections/vinegars"
              },
              {
                "name": "Vinegar in Bulk",
                "url": "/collections/vinegar-in-bulk"
              },
              {
                "name": "Olive Oil",
                "url": "/collections/olive-oil"
              }
            ],
            "url": "/collections/oils-vinegars"
          },
          {
            "name": "OLIVES, VEGETABLES & CONDIMENTSCondimentsMustardsOlives FreshPreserved OlivesPicklesCapersSoy SaucesSweet PeppersTomatoesVegetablesChestnuts",
            "subcategories": [
              {
                "name": "Condiments",
                "url": "/collections/condiments"
              },
              {
                "name": "Mustards",
                "url": "/collections/mustards"
              },
              {
                "name": "Olives Fresh",
                "url": "/collections/olives-fresh"
              },
              {
                "name": "Preserved Olives",
                "url": "/collections/preserved-olives"
              },
              {
                "name": "Pickles",
                "url": "/collections/pickles"
              },
              {
                "name": "Capers",
                "url": "/collections/capers"
              },
              {
                "name": "Soy Sauces",
                "url": "/collections/soy-sauces-1"
              },
              {
                "name": "Sweet Peppers",
                "url": "/collections/sweet-peppers"
              },
              {
                "name": "Tomatoes",
                "url": "/collections/tomatoes"
              },
              {
                "name": "Vegetables",
                "url": "/collections/vegetables"
              },
              {
                "name": "Chestnuts",
                "url": "/collections/chestnuts"
              }
            ],
            "url": "/collections/olives-vegetables-condiments"
          },
          {
            "name": "SPICES, SALTS & CHILIESChilies & Dried PeppersSaltsHerbs & SpicesTrufflesMushrooms",
            "subcategories": [
              {
                "name": "Chilies & Dried Peppers",
                "url": "/collections/chilies-dried-peppers"
              },
              {
                "name": "Salts",
                "url": "/collections/salts"
              },
              {
                "name": "Herbs & Spices",
                "url": "/collections/herbs-spices"
              },
              {
                "name": "Truffles",
                "url": "/collections/truffles-1"
              },
              {
                "name": "Mushrooms",
                "url": "/collections/mushrooms-1"
              }
            ],
            "url": "/collections/spices-salts-chilies"
          },
          {
            "name": "TEASTeas",
            "subcategories": [
              {
                "name": "Teas",
                "url": "/collections/teas"
              }
            ],
            "url": "/collections/teas"
          }
        ],
        "url": "/pages/savory-collection"
      },
      {
        "id": 2,
        "name": "PASTRY",
        "subcategories": [
          {
            "name": "BAKING SPECIALTIESBaking DecorBaking IngredientsMilkStabilizersSupplies",
            "subcategories": [
              {
                "name": "Baking Decor",
                "url": "/collections/baking-decor"
              },
              {
                "name": "Baking Ingredients",
                "url": "/collections/baking-ingredients"
              },
              {
                "name": "Milk",
                "url": "/collections/milk"
              },
              {
                "name": "Stabilizers",
                "url": "/collections/stabilizers"
              },
              {
                "name": "Supplies",
                "url": "/collections/supplies"
              }
            ],
            "url": "/collections/baking-specialties"
          },
          {
            "name": "CHOCOLATEBaking DropsBittersweetChocolate CupsChocolate DecorChocolate GlazeCocoa PowdersMilk ChocolateSemisweet ChocolateSpecialty ChocolateUnsweetenedWhite Chocolate",
            "subcategories": [
              {
                "name": "Baking Drops",
                "url": "/collections/baking-drops"
              },
              {
                "name": "Bittersweet",
                "url": "/collections/bittersweet"
              },
              {
                "name": "Chocolate Cups",
                "url": "/collections/chocolate-cups"
              },
              {
                "name": "Chocolate Decor",
                "url": "/collections/chocolate-decor"
              },
              {
                "name": "Chocolate Glaze",
                "url": "/collections/chocolate-glaze"
              },
              {
                "name": "Cocoa Powders",
                "url": "/collections/cocoa-powders"
              },
              {
                "name": "Milk Chocolate",
                "url": "/collections/milk-chocolate"
              },
              {
                "name": "Semisweet Chocolate",
                "url": "/collections/semisweet-chocolate"
              },
              {
                "name": "Specialty Chocolate",
                "url": "/collections/specialty-chocolate"
              },
              {
                "name": "Unsweetened",
                "url": "/collections/unsweetened"
              },
              {
                "name": "White Chocolate",
                "url": "/collections/white-chocolate"
              }
            ],
            "url": "/collections/chocolate"
          },
          {
            "name": "CONFECTIONS, DOUGHS & SHELLSConfectionsCrackers/CookiesPastriesShells & Doughs",
            "subcategories": [
              {
                "name": "Confections",
                "url": "/collections/confections-1"
              },
              {
                "name": "Crackers/Cookies",
                "url": "/collections/crackers-cookies"
              },
              {
                "name": "Pastries",
                "url": "/collections/pastries"
              },
              {
                "name": "Shells & Doughs",
                "url": "/collections/shells-doughs"
              }
            ],
            "url": "/collections/confections"
          },
          {
            "name": "FRUITCandied FruitCoconutCompoundsDried FruitFillingsFrozen BerriesFrozen PureeFruit JuicesFruits In SyrupGlazesJams & Preserves",
            "subcategories": [
              {
                "name": "Candied Fruit",
                "url": "/collections/candied-fruit"
              },
              {
                "name": "Coconut",
                "url": "/collections/coconut"
              },
              {
                "name": "Compounds",
                "url": "/collections/compounds"
              },
              {
                "name": "Dried Fruit",
                "url": "/collections/dried-fruit"
              },
              {
                "name": "Fillings",
                "url": "/collections/fillings"
              },
              {
                "name": "Frozen Berries",
                "url": "/collections/frozen-berries"
              },
              {
                "name": "Frozen Puree",
                "url": "/collections/frozen-puree"
              },
              {
                "name": "Fruit Juices",
                "url": "/collections/fruit-juices"
              },
              {
                "name": "Fruits In Syrup",
                "url": "/collections/fruits-in-syrup"
              },
              {
                "name": "Glazes",
                "url": "/collections/glazes"
              },
              {
                "name": "Jams & Preserves",
                "url": "/collections/jams-preserves"
              }
            ],
            "url": "/collections/fruit"
          },
          {
            "name": "NUTS & SEEDSNutsSeeds",
            "subcategories": [
              {
                "name": "Nuts",
                "url": "/collections/nuts-1"
              },
              {
                "name": "Seeds",
                "url": "/collections/seeds-2"
              }
            ],
            "url": "/collections/nuts"
          },
          {
            "name": "SYRUPS & SUGARSFlavoring SyrupsHoneySugarsSyrups/Molasses",
            "subcategories": [
              {
                "name": "Flavoring Syrups",
                "url": "/collections/flavoring-syrups"
              },
              {
                "name": "Honey",
                "url": "/collections/honey"
              },
              {
                "name": "Sugars",
                "url": "/collections/sugars"
              },
              {
                "name": "Syrups/Molasses",
                "url": "/collections/syrups-molasses"
              }
            ],
            "url": "/collections/syrups-sugars"
          },
          {
            "name": "VANILLA & FLAVORINGSPure Essential OilsFlavor/ExtractsFood ColorsVanilla",
            "subcategories": [
              {
                "name": "Pure Essential Oils",
                "url": "/collections/pure-essential-oils"
              },
              {
                "name": "Flavor/Extracts",
                "url": "/collections/flavor-extracts"
              },
              {
                "name": "Food Colors",
                "url": "/collections/food-colors"
              },
              {
                "name": "Vanilla",
                "url": "/collections/vanilla"
              }
            ],
            "url": "/collections/vanilla-flavorings"
          }
        ],
        "url": "/pages/pastry-collection"
      },
      {
        "id": 3,
        "name": "WORLD SPECIALTIES",
        "subcategories": [
          {
            "name": "Asian Noodles",
            "subcategories": [],
            "url": "/collections/asian-noodles"
          },
          {
            "name": "Asian Wraps",
            "subcategories": [],
            "url": "/collections/asian-wraps"
          },
          {
            "name": "Soy Sauces",
            "subcategories": [],
            "url": "/collections/soy-sauces-1"
          },
          {
            "name": "Chinese Ingredients",
            "subcategories": [],
            "url": "/collections/chinese-ingredients"
          },
          {
            "name": "Korean Ingredients",
            "subcategories": [],
            "url": "/collections/korean-ingredients"
          },
          {
            "name": "Japanese Ingredients",
            "subcategories": [],
            "url": "/collections/japanese-ingredients"
          },
          {
            "name": "Middle Eastern Ingredients",
            "subcategories": [],
            "url": "/collections/middle-eastern-ingredients"
          },
          {
            "name": "Indian Ingredients",
            "subcategories": [],
            "url": "/collections/indian-ingredients"
          },
          {
            "name": "Thai & Southeast Asian Ingredients",
            "subcategories": [],
            "url": "/collections/thai-southeast-asian-ingredients"
          }
        ],
        "url": "/collections/world-specialties"
      },
      {
        "id": 4,
        "name": "HOLIDAY INSPIRATION",
        "subcategories": [
          {
            "name": "Chocolate Vermicelli Topping: 2.5 lb",
            "subcategories": [],
            "url": "/products/chocolate-vermicelli-topping-2-5-lb"
          },
          {
            "name": "Candied Violet Petals: 6.5 oz",
            "subcategories": [],
            "url": "/products/candied-violet-petals-6-5-oz"
          },
          {
            "name": "Candied Rose Petals: 6.5 oz",
            "subcategories": [],
            "url": "/products/candied-rose-petals-6-5-oz"
          },
          {
            "name": "Rainbow Nonpareils Natures Color: 3.4 lb",
            "subcategories": [],
            "url": "/products/rainbow-nonpareils-natures-color-3-4-lb"
          },
          {
            "name": "Bright Orange Sprinkles Natures: 2.9 lb",
            "subcategories": [],
            "url": "/products/bright-orange-sprinkles-natures-2-9-lb"
          },
          {
            "name": "Bright Blue Sprinkles Natures Color: 2.9 lb",
            "subcategories": [],
            "url": "/products/bright-blue-sprinkles-natures-color-2-9-lb"
          },
          {
            "name": "Bright Red Sprinkles Natures Color: 2.9 lb",
            "subcategories": [],
            "url": "/products/bright-red-sprinkles-natures-color"
          },
          {
            "name": "Yellow Sprinkles Natures Color: 2.9 lb",
            "subcategories": [],
            "url": "/products/yellow-sprinkles-natures-color-2-9-lb"
          },
          {
            "name": "White Sprinkles Natures Color: 2.9 lb",
            "subcategories": [],
            "url": "/products/white-sprinkles-natures-color-2-9-lb"
          },
          {
            "name": "Fiesta Sprinkles Nature's Colors: 2.9 lb",
            "subcategories": [],
            "url": "/products/fiesta-sprinkles-natures-colors-2-9-lb"
          },
          {
            "name": "Peppermint Crunch Nature's Colors: 2.4 lb",
            "subcategories": [],
            "url": "/products/peppermint-crunch-natures-colors-2-4-lb"
          }
        ],
        "url": "/collections/pantry-essentials"
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
		return f"https://shop.pacgourmet.com{category['url']}"

	# ************************************************************************

	# 	Product Scraping Functions
	# ************************************************************************

	def get_product_details(self, url, row_spec=None):
		"""Get Product Details"""
		data = self.get_product_details_json( url, row_spec)
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
	def grab_products(self):

		products = self.wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-image > a'))
		)

		print(f"products found: {len(products)}")
		detail_urls = [product.get_attribute("href") for product in products]
		return '', detail_urls

	def build_categories_list(self):
		url = self.BASE_URL
		navigation = self.get_navigation_structure(url)
		# self.print_navigation_structure(navigation)
		return f"<div>{navigation}</div>"

	def get_navigation_dict(self, url: str, headers: Optional[Dict] = None) -> List[Dict[str, Any]]:
		"""
		Scrapes and parses the navigation structure from the Pacific Gourmet website.

		Args:
			url: The URL of the page containing the navigation menu
			headers:

		Returns:
			A list of dictionaries representing the navigation structure with categories and subcategories
		"""
		try:
			self.driver.get(url)
			time.sleep(3)  # Allow page to load

			# Get the page source and parse with BeautifulSoup
			soup = BeautifulSoup(self.driver.page_source, 'html.parser')

			# Find the main navigation menu
			nav = soup.find('nav', {'class': 'wsmenu'})
			if not nav:
				print("Navigation menu not found")
				return []

			# Initialize the categories list
			categories = []

			# Find all top-level menu items
			top_level_items = nav.select('ul.wsmenu-list > li.has-submenu')
			navigation = {'data': {'categories': []}}
			i = 0
			for item in top_level_items:
				i += 1
				# Extract category name and URL
				category_link = item.find('a')
				if not category_link:
					continue

				category_name = category_link.get_text(strip=True)
				category_url = category_link.get('href', '')

				# Skip if it's the contact page
				if 'contact' in category_name.lower():
					continue

				# Initialize category data
				category_data = {
					'name': category_name,
					'url': category_url,
					'id': i,
					'subcategories': []
				}

				# Find subcategories
				submenu = item.find('ul', class_='wsmenu-submenu')
				if submenu:
					subcategory_items = submenu.find_all('li', class_='has-submenu-sub')
					if len(subcategory_items) == 0:
						subcategory_items = submenu.find_all('li')
					for sub_item in subcategory_items:
						subcategory_link = sub_item.find('a')
						if not subcategory_link:
							continue

						subcategory_name = sub_item.get_text(strip=True).replace('›', '').strip()
						subcategory_url = subcategory_link.get('href', '')

						# Initialize subcategory data
						subcategory_data = {
							'name': subcategory_name,
							'url': subcategory_url,
							'subcategories': []
						}

						# Find sub-subcategories
						subsubmenu = sub_item.find('ul', class_='wsmenu-submenu-sub')
						if subsubmenu:
							subsubcategory_items = subsubmenu.find_all('li')

							for subsub_item in subsubcategory_items:
								subsub_link = subsub_item.find('a')
								if not subsub_link:
									continue

								subsub_name = subsub_link.get_text(strip=True)
								subsub_url = subsub_link.get('href', '')

								subcategory_data['subcategories'].append({
									'name': subsub_name,
									'url': subsub_url
								})

						category_data['subcategories'].append(subcategory_data)

				# categories.append(category_data)
				navigation['data']['categories'].append(category_data)

			return navigation

		except Exception as e:
			print(f"Error getting navigation structure: {e}")
			return []

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


