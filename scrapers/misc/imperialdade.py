import json
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.options import PageLoadStrategy
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire.utils import decode
from typing import List, Dict, Any, Optional

from scrapers.scraper import Scraper, SkuNotFound

"""
	Imperial Dade
	Type: Standard shop website
	Page with sub categories
	Method: 
		Get Categories: 
		Get Product:
		Get Product:
"""


class ImperialDadeScraper(Scraper):
	# /3269/edit_note/1630/
	CRM_ID = 3269
	CRM_NOTE_ID = 1630
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = 'Ready'

	DISTRIBUTOR_PRODUCT_DATA_SPEC = {
		'recommendations': '',
		'product_type': '',
		'food_product_type': '',
		'product_category': '',
		'unspsc': '',
		'upc-12': '',
	}

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/imperial_dade/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = 'https://www.imperialdade.com/catalog/foodservice?cid=WCL1001'
	VENDOR_NAME = 'Imperial Dade'
	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "name": "Bakery Supplies",
        "id": 1,
        "url": "https://www.imperialdade.com/catalog/foodservice/bakery-supplies?cid=WCL2001"
      },
      {
        "name": "Bottles, Jars & Lids",
        "id": 2,
        "url": "https://www.imperialdade.com/catalog/foodservice/bottles-jars-lids?cid=WCL2003"
      },
      {
        "name": "Disposable Take-Out Containers & Servingware",
        "id": 3,
        "url": "https://www.imperialdade.com/catalog/foodservice/disposable-take-out-containers-servingware?cid=WCL2009"
      },
      {
        "name": "Food",
        "id": 4,
        "url": "https://www.imperialdade.com/catalog/foodservice/food?cid=WCL2013"
      },
      {
        "name": "Food Storage & Transport",
        "id": 5,
        "url": "https://www.imperialdade.com/catalog/foodservice/food-storage-transport?cid=WCL2017"
      },
      {
        "name": "Foodservice Bags",
        "id": 6,
        "url": "https://www.imperialdade.com/catalog/foodservice/foodservice-bags?cid=WCL2014"
      },
      {
        "name": "Foodservice Packaging Supplies",
        "id": 7,
        "url": "https://www.imperialdade.com/catalog/foodservice/foodservice-packaging-supplies?cid=WCL2015"
      },
      {
        "name": "Foodservice Safety",
        "id": 8,
        "url": "https://www.imperialdade.com/catalog/foodservice/foodservice-safety?cid=WCL2016"
      },
      {
        "name": "Napkins & Napkin Dispensers",
        "id": 9,
        "url": "https://www.imperialdade.com/catalog/foodservice/napkins-napkin-dispensers?cid=WCL2024"
      },
      {
        "name": "Restaurant Furniture",
        "id": 10,
        "url": "https://www.imperialdade.com/catalog/foodservice/restaurant-furniture?cid=WCL2032"
      },
      {
        "name": "Restaurant Kitchen Equipment",
        "id": 11,
        "url": "https://www.imperialdade.com/catalog/foodservice/restaurant-kitchen-equipment?cid=WCL2033"
      },
      {
        "name": "Skewers, Toothpicks & Markers",
        "id": 12,
        "url": "https://www.imperialdade.com/catalog/foodservice/skewers-toothpicks-markers?cid=WCL2036"
      },
      {
        "name": "Smallwares",
        "id": 13,
        "url": "https://www.imperialdade.com/catalog/foodservice/smallwares?cid=WCL2038"
      },
      {
        "name": "Straws & Drink Stirrers",
        "id": 14,
        "url": "https://www.imperialdade.com/catalog/foodservice/straws-drink-stirrers?cid=WCL2039"
      }
    ]
  }
}
	''')
	TAXONOMY = [
				  {
				    "name": "Beer",
				    "count": "1",
					"number": "1",
				    "classes": [
				      {
				        "name": "Malt Beverage",
				        "count": "1",
				        "subclasses": [
				          {
				            "category": "Malt Beverage-Other",
				            "count": "1"
				          }
				        ]
				      }
				    ]
				  },
				  {
				    "name": "Miscellaneous",
				    "count": "150",
				    "number": "2",
				    "classes": [
				      {
				        "name": "Drinkware",
				        "count": "149",
				        "subclasses": [
				          {
				            "category": "Wine Glass",
				            "count": "84"
				          },
				          {
				            "category": "Rocks Glass",
				            "count": "4"
				          },
				          {
				            "category": "Drinkware-Other",
				            "count": "15"
				          },
				          {
				            "category": "High Ball Glass",
				            "count": "4"
				          },
				          {
				            "category": "Cocktail Glass",
				            "count": "7"
				          },
				          {
				            "category": "Flute",
				            "count": "11"
				          },
				          {
				            "category": "Beer Glass",
				            "count": "2"
				          },
				          {
				            "category": "Wine Decanter",
				            "count": "18"
				          }
				        ]
				      },
				      {
				        "name": "Keg & Draft System",
				        "count": "1",
				        "subclasses": [
				          {
				            "category": "Empty Wine Keg",
				            "count": "1"
				          }
				        ]
				      }
				    ]
				  },
				  {
				    "name": "Non-Alcoholic Beverages",
				    "count": "1",
				    "number": "3",
				    "classes": [
				      {
				        "name": "Cocktail Mixers",
				        "count": "1",
				        "subclasses": [
				          {
				            "category": "Bloody Mary Mix",
				            "count": "1"
				          }
				        ]
				      }
				    ]
				  },
				  {
				    "name": "Sake",
				    "count": "140",
				    "number": "4",
				    "classes": [
				      {
				        "name": "Fortified Sake",
				        "count": "16",
				        "subclasses": [
				          {
				            "category": "Daiginjo Nigori Sake",
				            "count": "2"
				          },
				          {
				            "category": "Daiginjo Sake",
				            "count": "4"
				          },
				          {
				            "category": "Futsuu Shu Sake",
				            "count": "4"
				          },
				          {
				            "category": "Ginjo Sake",
				            "count": "2"
				          },
				          {
				            "category": "Honjozo Sake",
				            "count": "4"
				          }
				        ]
				      },
				      {
				        "name": "Mixed Package-Sake",
				        "count": "2",
				        "subclasses": [
				          {
				            "category": "Mixed Package-Sake",
				            "count": "2"
				          }
				        ]
				      },
				      {
				        "name": "Pure Rice Sake",
				        "count": "110",
				        "subclasses": [
				          {
				            "category": "Junmai Daiginjo Sake",
				            "count": "25"
				          },
				          {
				            "category": "Junmai Ginjo Nigori Sake",
				            "count": "6"
				          },
				          {
				            "category": "Junmai Ginjo Sake",
				            "count": "28"
				          },
				          {
				            "category": "Junmai Nigori Sake",
				            "count": "6"
				          },
				          {
				            "category": "Junmai Sake",
				            "count": "45"
				          }
				        ]
				      },
				      {
				        "name": "Sake-Other",
				        "count": "12",
				        "subclasses": [
				          {
				            "category": "Flavored Sake",
				            "count": "6"
				          },
				          {
				            "category": "Sake-Other",
				            "count": "3"
				          },
				          {
				            "category": "Sparkling Sake",
				            "count": "3"
				          }
				        ]
				      }
				    ]
				  },
				  {
				    "name": "Spirits",
				    "count": "5117",
					"number": "5",
				    "classes": [
				      {
				        "name": "Tequila & Agave Spirits",
				        "count": "666",
				        "subclasses": [
				          {
				            "category": "Agave Spirit-Other",
				            "count": "8"
				          },
				          {
				            "category": "Flavored Tequila",
				            "count": "22"
				          },
				          {
				            "category": "Mezcal",
				            "count": "121"
				          },
				          {
				            "category": "Mixed Package-Tequila & Agave Spirits",
				            "count": "1"
				          },
				          {
				            "category": "Sotol",
				            "count": "1"
				          },
				          {
				            "category": "Tequila",
				            "count": "513"
				          }
				        ]
				      },
				      {
				        "name": "Vodka",
				        "count": "785",
				        "subclasses": [
				          {
				            "category": "Flavored Vodka",
				            "count": "475"
				          },
				          {
				            "category": "Vodka",
				            "count": "300"
				          },
				          {
				            "category": "Vodka Specialty",
				            "count": "10"
				          }
				        ]
				      },
				      {
				        "name": "Whiskey-American",
				        "count": "746",
				        "subclasses": [
				          {
				            "category": "Straight Bourbon",
				            "count": "279"
				          },
				          {
				            "category": "Straight Rye Whiskey",
				            "count": "84"
				          },
				          {
				            "category": "Flavored Whiskey-American",
				            "count": "150"
				          },
				          {
				            "category": "Bourbon",
				            "count": "32"
				          },
				          {
				            "category": "Blended American Whiskey",
				            "count": "68"
				          },
				          {
				            "category": "Rye Whiskey",
				            "count": "41"
				          },
				          {
				            "category": "Blended Bourbon",
				            "count": "18"
				          },
				          {
				            "category": "Corn Whiskey",
				            "count": "10"
				          }
				        ]
				      },
				      {
				        "name": "Liqueur",
				        "count": "722",
				        "subclasses": [
				          {
				            "category": "Aperitif",
				            "count": "18"
				          },
				          {
				            "category": "Liqueur-Other",
				            "count": "45"
				          },
				          {
				            "category": "Cream Liqueur",
				            "count": "69"
				          },
				          {
				            "category": "Fruit Liqueur",
				            "count": "86"
				          },
				          {
				            "category": "Coffee Liqueur",
				            "count": "40"
				          },
				          {
				            "category": "Floral Liqueur",
				            "count": "5"
				          },
				          {
				            "category": "Brandy Liqueur",
				            "count": "36"
				          },
				          {
				            "category": "Herbal Liqueur",
				            "count": "24"
				          }
				        ]
				      },
				      {
				        "name": "Whisky-Scotch",
				        "count": "421",
				        "subclasses": [
				          {
				            "category": "Blended Malt Scotch",
				            "count": "6"
				          },
				          {
				            "category": "Blended Scotch",
				            "count": "126"
				          },
				          {
				            "category": "Flavored Whisky-Scotch",
				            "count": "3"
				          },
				          {
				            "category": "Single Grain Scotch",
				            "count": "2"
				          },
				          {
				            "category": "Single Malt Scotch",
				            "count": "284"
				          }
				        ]
				      },
				      {
				        "name": "Rum",
				        "count": "448",
				        "subclasses": [
				          {
				            "category": "Light Rum",
				            "count": "62"
				          },
				          {
				            "category": "Flavored Rum",
				            "count": "130"
				          },
				          {
				            "category": "Aged Rum",
				            "count": "99"
				          },
				          {
				            "category": "Gold Rum",
				            "count": "51"
				          },
				          {
				            "category": "Spiced Rum",
				            "count": "51"
				          },
				          {
				            "category": "Overproof Rum",
				            "count": "11"
				          },
				          {
				            "category": "Dark Rum",
				            "count": "33"
				          },
				          {
				            "category": "Rhum Agricole",
				            "count": "5"
				          }
				        ]
				      },
				      {
				        "name": "Whiskey-Irish",
				        "count": "108",
				        "subclasses": [
				          {
				            "category": "Blended Irish Whiskey",
				            "count": "45"
				          },
				          {
				            "category": "Flavored Whiskey-Irish",
				            "count": "1"
				          },
				          {
				            "category": "Single Grain Irish Whiskey",
				            "count": "3"
				          },
				          {
				            "category": "Single Malt Irish Whiskey",
				            "count": "23"
				          },
				          {
				            "category": "Single Pot Still Irish Whiskey",
				            "count": "36"
				          }
				        ]
				      },
				      {
				        "name": "Gin",
				        "count": "223",
				        "subclasses": [
				          {
				            "category": "Dry Gin",
				            "count": "103"
				          },
				          {
				            "category": "Flavored Gin",
				            "count": "38"
				          },
				          {
				            "category": "Genever",
				            "count": "3"
				          },
				          {
				            "category": "London Dry Gin",
				            "count": "77"
				          },
				          {
				            "category": "Old Tom Gin",
				            "count": "2"
				          }
				        ]
				      }
				    ]
				  },
				  {
				    "name": "Wine",
				    "count": "6117",
					"number": "6",
				    "classes": [
				      {
				        "name": "White Wine",
				        "count": "1669",
				        "subclasses": [
				          {
				            "category": "White Wine-Sauvignon Blanc",
				            "count": "271"
				          },
				          {
				            "category": "White Wine-Chardonnay",
				            "count": "684"
				          },
				          {
				            "category": "White Wine-Pinot Grigio/Pinot Gris",
				            "count": "173"
				          },
				          {
				            "category": "White Wine-Blend",
				            "count": "191"
				          },
				          {
				            "category": "White Wine-All Other Varietals",
				            "count": "171"
				          },
				          {
				            "category": "White Wine-Riesling",
				            "count": "100"
				          },
				          {
				            "category": "White Wine-Moscato",
				            "count": "31"
				          },
				          {
				            "category": "White Wine-Chenin Blanc",
				            "count": "30"
				          }
				        ]
				      },
				      {
				        "name": "Red Wine",
				        "count": "3058",
				        "subclasses": [
				          {
				            "category": "Red Wine-Cabernet Sauvignon",
				            "count": "668"
				          },
				          {
				            "category": "Red Wine-Blend",
				            "count": "704"
				          },
				          {
				            "category": "Red Wine-Pinot Noir",
				            "count": "753"
				          },
				          {
				            "category": "Red Wine-All Other Varietals",
				            "count": "345"
				          },
				          {
				            "category": "Red Wine-Sangiovese",
				            "count": "156"
				          },
				          {
				            "category": "Red Wine-Merlot",
				            "count": "133"
				          },
				          {
				            "category": "Red Wine-Syrah/Shiraz",
				            "count": "111"
				          },
				          {
				            "category": "Red Wine-Malbec",
				            "count": "61"
				          }
				        ]
				      },
				      {
				        "name": "Sparkling Wine",
				        "count": "666",
				        "subclasses": [
				          {
				            "category": "Sparkling Red Wine",
				            "count": "3"
				          },
				          {
				            "category": "Sparkling Rose Wine",
				            "count": "187"
				          },
				          {
				            "category": "Sparkling White Wine",
				            "count": "466"
				          },
				          {
				            "category": "Sparkling Wine-Other",
				            "count": "10"
				          }
				        ]
				      },
				      {
				        "name": "Rose Wine",
				        "count": "222",
				        "subclasses": [
				          {
				            "category": "Rose Wine-All Other Varietals",
				            "count": "16"
				          },
				          {
				            "category": "Rose Wine-Blend",
				            "count": "147"
				          },
				          {
				            "category": "Rose Wine-Grenache",
				            "count": "4"
				          },
				          {
				            "category": "Rose Wine-Moscato",
				            "count": "8"
				          },
				          {
				            "category": "Rose Wine-Pinot Noir",
				            "count": "27"
				          },
				          {
				            "category": "Rose Wine-Sangiovese",
				            "count": "3"
				          },
				          {
				            "category": "Rose Wine-Syrah",
				            "count": "2"
				          },
				          {
				            "category": "Rose Wine-Zinfandel",
				            "count": "15"
				          }
				        ]
				      },
				      {
				        "name": "Aromatized",
				        "count": "58",
				        "subclasses": [
				          {
				            "category": "Aperitif Wine",
				            "count": "11"
				          },
				          {
				            "category": "Vermouth",
				            "count": "47"
				          }
				        ]
				      },
				      {
				        "name": "Specialty",
				        "count": "209",
				        "subclasses": [
				          {
				            "category": "Cooking Wine",
				            "count": "3"
				          },
				          {
				            "category": "Flavored Wine",
				            "count": "61"
				          },
				          {
				            "category": "Plum Wine",
				            "count": "11"
				          },
				          {
				            "category": "Sangria",
				            "count": "22"
				          },
				          {
				            "category": "Wine Based Cocktail",
				            "count": "112"
				          }
				        ]
				      },
				      {
				        "name": "Fortified",
				        "count": "168",
				        "subclasses": [
				          {
				            "category": "Fortified-Other",
				            "count": "5"
				          },
				          {
				            "category": "Madeira",
				            "count": "4"
				          },
				          {
				            "category": "Marsala",
				            "count": "19"
				          },
				          {
				            "category": "Port",
				            "count": "94"
				          },
				          {
				            "category": "Sherry",
				            "count": "46"
				          }
				        ]
				      },
				      {
				        "name": "Sweet/Dessert Wine",
				        "count": "53",
				        "subclasses": [
				          {
				            "category": "Red Dessert Wine",
				            "count": "11"
				          },
				          {
				            "category": "Rose Dessert Wine",
				            "count": "1"
				          },
				          {
				            "category": "White Dessert Wine",
				            "count": "41"
				          }
				        ]
				      }
				    ]
				  }
				]
	CATEGORY_IDS = {}
	CATEGORY_NAMES = {}
	CATEGORY_URLS = {}
	# Category Names (can use category ID as key)
	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	DEFAULT_OPTIONS = {
		'get_categories': False,
		'scrape_products': False,
		'process_csv': False,
		'reprocess_csv': False,
		'dedupe_csv': False,
		'format_csv': False,
		'scan_csv': False,
		'count_csv': False,
		'process_extra': False,
		'search_requests': False,
		'test_products': 20000,
		'max_products': 99,
		'csv_start_row': 0,
		'category_to_process': 0,
		'test_categories': 100,
		'chosen_category': '10001',  # Default to Meat
		'url_output_file': '',
		'data_output_file': '',
		'home_directory': DEFAULT_DIRECTORY,
		'url': 'https://shop.sgproof.com/search',
		'search_term': 'Miscellaneous',
	}

	def __init__(self, options=None):
		super().__init__(options)
		self.PRODUCT_DATA_SPEC = self.BASE_PRODUCT_DATA_SPEC.copy()
		for spec in self.DISTRIBUTOR_PRODUCT_DATA_SPEC:
			self.PRODUCT_DATA_SPEC[spec] = ''
		print(self.PRODUCT_DATA_SPEC)

	def get_categories_from_site(self):
		"""
		Returns a list of category dictionaries with their details.

		Returns:
			list: A list of dictionaries, each containing 'id', 'name', 'url', and 'subcategories' of a category
		"""
		categories = []
		try:
			# Navigate to the main page if not already there
			if 'shop.imperialdade.com' not in self.driver.current_url:
				self.driver.get(self.BASE_URL)
				self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'nav[data-testid="category-nav"]')))

			# Find all top-level category elements
			category_elements = self.driver.find_elements(By.CSS_SELECTOR, 'nav[data-testid="category-nav"] > ul > li')

			for cat_element in category_elements:
				try:
					# Get category name and URL
					link = cat_element.find_element(By.TAG_NAME, 'a')
					category_name = link.text.strip()
					category_url = link.get_attribute('href')

					# Get category ID from URL or generate one
					category_id = category_url.split('/')[-1] if category_url else str(len(categories) + 1)

					# Store in class dictionaries
					self.CATEGORY_IDS[category_id] = category_name
					self.CATEGORY_NAMES[category_name] = category_id
					self.CATEGORY_URLS[category_id] = category_url

					# Get subcategories if they exist
					subcategories = []
					try:
						sub_elements = cat_element.find_elements(By.CSS_SELECTOR, 'ul > li > a')
						subcategories = [
							{
								'id': f"{category_id}_{i + 1}",
								'name': sub.text.strip(),
								'url': sub.get_attribute('href'),
								'subcategories': []
							}
							for i, sub in enumerate(sub_elements)
						]
					except Exception as e:
						print(f"Error getting subcategories for {category_name}: {e}")

					categories.append({
						'id': category_id,
						'name': category_name,
						'url': category_url,
						'subcategories': subcategories
					})

				except Exception as e:
					print(f"Error processing category element: {e}")
					continue

		except Exception as e:
			print(f"Error in get_categories: {e}")

		return categories

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

	def get_category_ids(self):
		return self.CATEGORY_IDS

	def get_category_names(self):
		return self.CATEGORY_NAMES

	def get_category_urls(self):
		return self.CATEGORY_URLS

	def scraping_setup(self):
		"""Scrape products from the website"""
		print("scraping_setup()")
		return

	# ************************************************************************
	# 	Product Scraping Functions
	# ************************************************************************

	def get_first_image_url(self, row_spec):
		"""
		Extract the first available image URL from the product API response.

		Args:
			response_data (dict): The parsed JSON response from the API

		Returns:
			str: URL of the first available image, or None if no image found
		"""
		print("get_first_image_url()")
		try:
			# product-viewer-image
			image_url = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="pdp-main-image-container-1"] img').get_attribute("src")
			if image_url:
				try:
					row_spec["image"] = image_url
					print("Image captured")
				except Exception as e:
					print(f"⛔️️ Error processing product overview from data: {e}")

		except Exception as e:
			print(f"Error extracting image from page: {str(e)}")

		return row_spec

	def get_product_data(self, data, row_spec):
		print("processing product data from response...")
		return row_spec

	def get_description(self, row_spec):
		print("get_description()")
		self.driver.execute_script("document.body.style.zoom = '20%'")
		try:
			description = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="romance-copy"]').text.strip()
			if description:
				row_spec["description"]  = description
		except NoSuchElementException as e:
			print(f"No Description found")
		except Exception as e:
			print(f"⛔️️ Error processing product description: {type(e)}")

		return row_spec

	# ************************************************************************
	# 	Core
	# ************************************************************************

	# Step One:
	def build_categories_list(self):
		# Run on all to get a category list then copy the list to CATEGORIES
		print(f"{self.__class__}->build_categories_list()")
		url = "https://www.imperialdade.com/catalog/foodservice?cid=WCL1001"
		self.driver.get(url)
		category_elements = self.wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='category-link']"))
		)
		print(f"Categories Found: {len(category_elements)}")
		# Initialize the navigation structure
		all_categories = {
			'data': {
				'categories': []
			}
		}
		i = 0
		for category in category_elements:
			i += 1
			category_name = category.find_element(By.TAG_NAME, 'p').text.strip()
			all_categories['data']['categories'].append({
				'name': category_name,
				'id': i,
				'url': category.get_attribute("href"),
			})

		return f"<div>{json.dumps(all_categories)}</div>"

	# Step Two: Get links to products
	def get_category_page(self, url, category_name, sub_category_name, sub_sub_category_name):
		print("get_category_page()")
		main_window = self.driver.current_window_handle
		html = ''
		total_products = 0
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

			while next_page:
				page_count += 1
				try:
					# Wait for page to load
					detail_urls = []
					if url in self.driver.current_url:
						print("Found products page")
						time.sleep(2)
						html_line, detail_urls = self.get_products_from_html()
					products_found_count = len(detail_urls)
					html += f"<div>Found {products_found_count} products for category {category_name} page {page_count}</div>"
					print(f"Found {products_found_count} products for category {category_name} page {page_count}")
					total_products += products_found_count
					# self.save_urls_to_csv(detail_urls, category_name, sub_category_name, sub_sub_category_name)

				except Exception as e:
					print(f"****************** ⛔️⛔️⛔️ Error getting details: {e}")
					html += f"<div>Name: {sub_category_name} (Error getting details)</div>"

				try:
					paging = self.wait.until(
						EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='pagination']"))
					)
					print("found paging area")
					button = paging.find_element(By.CSS_SELECTOR, "[aria-label='Next page']")
					self.driver.execute_script("arguments[0].scrollIntoView();", button)
					button.click()
					next_page = True
					print("go to next page")
				except Exception as e:
					next_page = False
					print(f"no next page  {e}")

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing category: {e}")

		html += f"<h2>Total products found: {total_products}</h2>"
		print(f"Total Products {total_products}")
		return detail_urls, html

	def get_products_from_html(self):
		print("get_products_from_html")
		products = self.wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='plp-card'"))
		)

		print(f"products found: {len(products)}")
		detail_urls = [product.find_element(By.CSS_SELECTOR,'a').get_attribute("href") for product in products]
		return '', detail_urls

	def build_products_list(self):
		"""Scrape products from the website - currently only a single category"""
		print("build_products_list()")
		html = ""
		all_urls = []
		categories = self.get_categories_from_site()
		# Use the options with fallback to module-level variables
		chosen_category = int(self.options.get('chosen_category', 0))

		if int(self.options['chosen_category']) == 0:
			categories = self.get_categories_from_site()
			print(f"All Categories ")
		else:
			for category in categories:
				print(f"category : {category.get('name', '')}")
				if int(category.get('id', '')) == chosen_category:
					categories = [category]  # Only process the chosen category
					print(f"Category found : {categories}")
					break
		url_output_file = self.options.get('url_output_file', '')

		# Wait for the page to be fully loaded
		print(f"Output File Name: {url_output_file}")
		for category in categories:
			category_name = category['name']
			print(f"category: {category_name}")
			url = category.get('url', '')
			print(f"Url: {url}")
			detail_urls, html = self.get_category_page(url, category_name, '', '')
			all_urls.extend(detail_urls)

		print(f"Total products found: {len(all_urls)}")
		return html

	@staticmethod
	def create_interceptor(max_api_products=MAX_API_PRODUCTS):
		def interceptor(request):
			# southernglazerswinespiritsproduction78xh7hnm.org.coveo.com/rest/search/v2
			if request.method == 'POST' and 'southernglazerswinespiritsproduction78xh7hnm.org.coveo.com/rest/search/v2' in request.url:
				print(f"👽👽👽Intercepting request: {request.url}")
				# Get the current POST data
				current_data = request.body.decode('utf-8')
				# print(f"Original POST data: {current_data}")

				try:
					payload = json.loads(current_data)
					if 'facets' in payload and payload['facets']:
						for facet in payload['facets']:
							if facet.get('field') == 'ec_prd_category' and (not facet.get('currentValues') or len(facet.get('currentValues', [])) == 0):
								print("Exiting interceptor: ec_prd_category has no current values")
								return
					# search = payload.get('search', {})
					print(f"Incoming number of results: {payload['numberOfResults']}")
					payload['numberOfResults'] = max_api_products  # Replace 'key_to_change' and 'new_value'
					request.body = json.dumps(payload).encode('utf-8')
					# Update the Content-Length header to reflect the new body size
					del request.headers['Content-Length']
					request.headers['Content-Length'] = str(len(request.body))
					# print(f"Modified POST data: {request.body.decode('utf-8')}")
				except json.JSONDecodeError:
					# Handle cases where the body is not JSON
					print("Request body is not JSON. Cannot modify in this example.")

		return interceptor

	# ************************************************************************
	# Functions for extracting product data
	# ************************************************************************

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
		print("Imperial Dade processing product detail page")

		data = ''
		sku = row_spec['sku']
		row_spec['sku'] = ''
		row_spec['id'] = sku
		row_spec['content_url'] = url
		print(f"Loading page...{url}")
		try:
			row_spec = self.process_details_from_html(url, row_spec=row_spec, follow_anchors=False)
			# self.write_product_to_csv(row_spec)
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing get_product_details: {type(e)}")
			raise
		# There is an api that returns json for related products
		try:
			row_spec = self.get_related_products(row_spec=row_spec)
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing get_product_details: {type(e)}")
			raise

		return row_spec

	def get_table_section(self, row_spec):
		# Scrape the section that contains the manufacturer information. It is in an unordered list
		print("get_table_section()")
		#product-info-table-container
		details = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='specifications-list']")
		print(details)
		# try:
		# 	hidden_element = self.driver.find_element(By.CSS_SELECTOR, '.product-info-table-container div.product-info-hide')
		# 	self.driver.execute_script("arguments[0].style.display = 'block';", hidden_element)
		# except Exception as e:
		# 	print(f"No hidden element: {type(e)}")
		try:
			rows = details.find_elements(By.CSS_SELECTOR, 'li')
			print(rows)
			for row in rows:
				key = row.find_element(By.CSS_SELECTOR, 'p.font-bold').text.strip()
				key = key.lower().replace(' ', '_').replace(':', '').replace('upc-14_(gtin)', 'gtin')
				print(key)
				value = row.find_element(By.CSS_SELECTOR, 'p.capitalize').text.strip()
				if key in self.PRODUCT_DATA_SPEC.keys():
					print(value)
					row_spec[key] = value

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing table data: {type(e)}")
		return row_spec

	def get_related_products(self, row_spec):
		print("get_related_products()")
		for request in self.driver.requests:
			if request.response and "recommendations/api/v1/products" in request.url and 'similar' in request.url:
				print(f"url: {request.url}")
				if 'application/json' in request.response.headers.get('Content-Type', ''):
					body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
					data = json.loads(body)
					row_spec['recommendations'] = json.dumps(data)
				else:
					print(f"Response Body (Text): {request.body}")

		return row_spec

	def process_details_from_html(self, url, follow_anchors=False, row_spec=None):
		print(f"process_details_from_html()")
		del self.driver.requests
		self.driver.get(url)
		try:
			container = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='product-detail-card']"))
			)
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing process_details_from_html: {type(e)}")
			raise
		try:
			row_spec['content_url'] = self.driver.current_url
			name = container.find_element(By.CSS_SELECTOR, 'article h1').text.strip()
			print(f"name: {name}")
			row_spec['name'] = name
			sku_elements = container.find_elements(By.CSS_SELECTOR, '[data-testid]')
			for element in sku_elements:
				content = element.text.strip()
				if 'SKU' in content:
					row_spec['sku'] = content.replace('SKU# ', '')
				if 'Mfr' in content:
					row_spec['manufacturer_sku'] = content.replace('Mfr# ', '')
			row_spec = self.get_description(row_spec)
			row_spec = self.get_table_section(row_spec)
			row_spec = self.get_first_image_url(row_spec)

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing process_details_from_html: {type(e)}")
		return row_spec

	# ************************************************************************
	# Category Extraction Functions
	# ************************************************************************
