import csv
import json
import re
import requests
import time

from bs4 import BeautifulSoup
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumwire import webdriver as seleniumwire_webdriver
from seleniumwire.utils import decode

from scrapers.scraper import Scraper
from typing import List, Dict, Any, Optional

def get_category_facets(json_data):
	"""
	Extract and return all category facets from the provided JSON data.

	Args:
		json_data (dict): The parsed JSON data containing product information

	Returns:
		list: A list of category facet objects, each containing 'value' and 'numberOfResults'
	"""
	if not isinstance(json_data, dict) or 'facets' not in json_data:
		return []

	# Find the category facet
	category_facets = []
	for facet in json_data['facets']:
		if facet.get('facetId') == 'category' and 'values' in facet:
			category_facets = [
				{
					'category': item['value'],
					'count': item['numberOfResults'],
					'url': f"https://shop.sgproof.com/search?text=&f-category={item['value']}"
				}
				for item in facet['values']
			]
			break

	return category_facets

def format_filter(filter):
	# Replace spaces with '+'
	modified_string = filter.replace(" ", "+")

	# Replace '&' with '%26' in the already modified string
	final_string = modified_string.replace("&", "%26")
	return final_string

class SouthernGlazierScraper(Scraper):
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
		'pricingUnitOfMeasure': '',
	}

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/sg'

	BASE_URL = 'https://www.chefswarehouse.com'
	CATEGORIES = [{'category': 'Beer', 'count': 1, 'url': 'https://shop.sgproof.com/search?text=&f-category=Beer'},
	              {'category': 'Miscellaneous', 'count': 150, 'url': 'https://shop.sgproof.com/search?text=&f-category=Miscellaneous'},
	              {'category': 'Non-Alcoholic Beverages', 'count': 1, 'url': 'https://shop.sgproof.com/search?text=&f-category=Non-Alcoholic Beverages'},
	              {'category': 'Sake', 'count': 140, 'url': 'https://shop.sgproof.com/search?text=&f-category=Sake'},
	              {'category': 'Spirits', 'count': 5124, 'url': 'https://shop.sgproof.com/search?text=&f-category=Spirits'},
	              {'category': 'Wine', 'count': 6129, 'url': 'https://shop.sgproof.com/search?text=&f-category=Wine'}]
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
	CATEGORY_IDS = {
		"MEAT": 1,
		"SEAFOOD": 2,
		"CHEESE": 3,
		"OIL": 4,
		"BAKING": 5,
		"PANTRY": 6,
		"PRODUCE": 7,
		"FROZEN": 8,
		"BEVERAGE": 9,
		"SUPPLIES": 10,
		"DAIRY": 21,
	}
	# Category Names (can use category ID as key)
	CATEGORY_NAMES = {
		1: "Meat & Poultry",
		2: "Seafood",
		3: "cheese-and-charcuterie/",
		4: "oil-and-vinegar",
		5: "baking-and-pastry",
		6: "pantry-staples",
		7: "fresh-produce",
		8: "frozen-grocery",
		9: "beverages",
		10: "supplies",
		21: "dairy-and-eggs",
	}
	CATEGORY_URLS = {
		1: "meat-and-poultry",
		2: "Seafood",
		3: "cheese-and-charcuterie",
		4: "oil-and-vinegar",
		5: "baking-and-pastry",
		6: "pantry-staples",
		7: "fresh-produce",
		8: "frozen-grocery",
		9: "beverages",
		10: "supplies",
		21: "dairy-and-eggs",
	}
	URL_FILE_NAMES = {
		1: "meat_product_urls.csv",
		2: "seafood_product_urls.csv",
		3: "cheese_product_urls.csv",
		4: "oil_product_urls.csv",
		5: "bakery_product_urls.csv",
		6: "pantry_product_urls.csv",
		7: "produce_product_urls.csv",
		8: "frozen_product_urls.csv",
		9: "beverage_product_urls.csv",
		10: "supplies_product_urls.csv",
		21: "dairy_product_urls.csv",
	}
	DATA_FILE_NAMES = {
		1: "meat_product_data.csv",
		2: "seafood_product_data.csv",
		3: "cheese_product_data.csv",
		4: "oil_product_datas.csv",
		5: "bakery_product_data.csv",
		6: "pantry_product_data.csv",
		7: "produce_product_data.csv",
		8: "frozen_product_data.csv",
		9: "beverage_product_data.csv",
		10: "supplies_product_data.csv",
		21: "dairy_product_data.csv",
	}
	CHOSEN_CATEGORY = CATEGORY_IDS["DAIRY"]
	CATEGORY_NAME = CATEGORY_NAMES[CHOSEN_CATEGORY]
	URL_OUTPUT_FILE = URL_FILE_NAMES[CHOSEN_CATEGORY]
	DATA_OUTPUT_FILE = DATA_FILE_NAMES[CHOSEN_CATEGORY]
	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	DEFAULT_OPTIONS = {
		'get_categories': False,
		'scrape_products': False,
		'process_csv': False,
		'reprocess_csv': False,
		'dedupe_csv': False,
		'count_csv': False,
		'process_extra': False,
		'search_requests': False,
		'test_products': 20000,
		'max_products': 30,
		'csv_start_row': 0,
		'category_to_process': 0,
		'test_categories': 100,
		'chosen_category': '10001',  # Default to Meat
		'url_output_file': URL_OUTPUT_FILE,
		'data_output_file': DATA_OUTPUT_FILE,
		'home_directory': DEFAULT_DIRECTORY,
		'url': 'https://shop.sgproof.com/search',
		'search_term': 'Miscellaneous',
	}

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}

	def get_category_ids(self):
		return self.CATEGORY_IDS

	def get_categories(self):
		return self.TAXONOMY

	def get_category_names(self):
		return self.CATEGORY_NAMES

	def get_category_urls(self):
		return self.CATEGORY_URLS

	def bypass_age_gate(self, url):
		try:
			self.driver.get(url)
			# time.sleep(2)
			select = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '.modal-box div.verify-select div.form-select'))
			)
			select = self.driver.find_element(By.CSS_SELECTOR, '.modal-box select.verify-select-input')

			select.click()
			select = Select(select)
			# print(select.options)
			select.select_by_value("91")
			# select.select_by_visible_text("NY - Metro")
			# self.print_element(select)
			self.driver.find_element(By.CSS_SELECTOR, '.modal-box .verify-trigger-yes').click()
			# time.sleep(2)
			# self.driver.get(url)
			print("Bypassed age gate")
		except Exception as e:
			print(f"Error: {e}")

	def process_product_list_search_api(self, html, category, sub_category, url_output_file):
		# Build a list of product URLs
		detail_urls = []
		all_urls = []

		product_wrappers = self.wait.until(
			EC.presence_of_all_elements_located((By.CLASS_NAME, 'search-result-col'))
		)
		print(f"Found Product Wrapper: {len(product_wrappers)}")

		for request in self.driver.requests:
			#
			if request.response and "//search" in request.url:  # Filter for API requests
				print(f"URL: {request.url}")
				print(f"Status Code: {request.response.status_code}")
				print(f"Content Type: {request.response.headers.get('Content-Type')}")

				# Decode the response body (it's bytes by default)
				try:
					# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
					body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

					# If the body is JSON, parse it
					if 'application/json' in request.response.headers.get('Content-Type', ''):
						data = json.loads(body)
						# https://www.chefswarehouse.com/products/10303734/
						detail_urls = [f"https://www.chefswarehouse.com{product['url']}" for product in data['results']]
						print(f"== Number of products: {len(detail_urls)}")
						self.save_urls_to_csv(detail_urls, category, sub_category)
					else:
						print(f"Response Body (Text): {body}")
					all_urls.extend(detail_urls.url)

				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding response body: {e}")
		print(f"========= Number of products: {len(all_urls)}")
		del self.driver.requests
		return html, all_urls

	def process_subcategories(self):
		# Build a list of product URLs
		urls = []
		subcategories = ''
		category_name = ''

		sub_categories = self.wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.card__wrap'))
		)
		print(f"Found Category Wrapper: {len(sub_categories)}")
		category_url_part = str(self.options['category_url_part']) + "?expand"
		print(f"category_url_part: {category_url_part}")
		for request in self.driver.requests:
			#
			# https://www.chefswarehouse.com/products/meat-and-poultry/?expand=*&currentPageUrl=%252Fproducts%252Fmeat-and-poultry%252F&tz=America%252FNew_York&t=1753496336262
			if request.response and category_url_part in request.url:  # Filter for API requests
				print(f"URL: {request.url}")
				print(f"Status Code: {request.response.status_code}")
				print(f"Content Type: {request.response.headers.get('Content-Type')}")

				# Decode the response body (it's bytes by default)
				try:
					# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
					body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

					# If the body is JSON, parse it
					if 'application/json' in request.response.headers.get('Content-Type', ''):
						data = json.loads(body)
						# {
						# 	"name": "Foie Gras",
						# 	"imageUrl": "/siteassets/foie-gras_330.png",
						# 	"url": "/products/meat-and-poultry/foie-gras/"
						# },
						category_name = data.get('name', '')
						view_model = data.get('viewModel', {})
						subcategories = view_model.get('subCategories', [])
						urls = [category['url'] for category in subcategories]
						print(f"==== sub categories: {subcategories}")
					else:
						print(f"Response Body was not JSON:")

				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding response body: {e}")
		print(f"========= Number of sub categories: {len(urls)}")

		del self.driver.requests
		return subcategories, category_name

	# ************************************************************************

	# 	Product Scraping Functions
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
			view_model = response_data.get('viewModel', {})
			assets = view_model.get('assets', [])

			# If there are assets, get the first one's URL
			if assets and isinstance(assets, list) and len(assets) > 0:
				# Get the first asset and extract the URL
				first_asset = assets[0]
				if isinstance(first_asset, dict):
					return self.BASE_URL + first_asset.get('featuredSrc', '')

		except Exception as e:
			print(f"Error extracting image from viewModel.assets: {str(e)}")

		return ''

	def get_product_data(self, data, row_spec):
		print("processing product data from response...")
		# print(data)
		if data:
			try:
				row_spec["name"] = data.get("name", "")
				row_spec["brand"] = data.get("displayBrand", "")

				view_model = data.get('viewModel', {})
				row_spec["pack_size"] = view_model.get('size', {})

				row_spec["image"] = self.get_first_image_url(data)
				row_spec = self.get_classification(view_model, row_spec)
				row_spec = self.get_description(view_model, row_spec)
				row_spec = self.get_manufacturer(data, row_spec)
				row_spec = self.get_additional_info(data, row_spec)
				row_spec["extra_data_1"] = json.dumps(data)

			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing get_product_data Complete...")
		return row_spec

	def get_classification(self, product_data, row_spec):
		print("processing product classification...")
		if product_data:
			row_spec["level_1"] = product_data.get("category", "").get('text', '')
			row_spec["level_2"] = product_data.get("subcategory", "")
			row_spec["level_3"] = product_data.get("subsubcategory", "")
		return row_spec

	def get_manufacturer(self, data, row_spec):
		# Scrape the section that contains the manufacturer information. It is in an unordered list
		if data:
			try:
				row_spec["manufacturer_sku"] = data.get("manufacturerItemNumber", "")
				row_spec["manufacturer_name"] = data.get("manufacturerDisplayName", "")
			except Exception as e:
				print(f"⛔️⛔️⛔️Error processing manufacturer data: {e}")
		return row_spec

	def get_description(self, data, row_spec):
		print("processing product overview...")
		description = ''
		if data:
			try:
				row_spec["description"]  = data.get('description', description)
			except Exception as e:
				print(f"⛔️️ Error processing product overview from data: {e}")

		print("processing product overview Complete...")
		return row_spec

	def get_additional_info(self, data, row_spec):
		"""
		Processes the product additional data from the API response and stores it into `row_spec`.
		This function specifically handles the extra fields that are not present in the standard product spec .

		Args:
			data (dict): The API response containing the product additional data
			row_spec (dict): The dictionary containing the scraped product data

		Returns:
			dict: The updated `row_spec` with the additional data
		"""
		print("processing product additional data...")
		if data:
			try:
				view_model = data.get('viewModel', {})
				row_spec["pricingUnitOfMeasure"] = view_model.get("pricingUnitOfMeasure", "")
			except Exception as e:
				print(f"⛔️⛔️⛔️Error processing additional data: {e}")

		print("processing product additional data Complete...")
		return row_spec

	@staticmethod
	def create_interceptor(max_api_products=MAX_API_PRODUCTS):
		def interceptor(request):
			# southernglazerswinespiritsproduction78xh7hnm.org.coveo.com/rest/search/v2
			if request.method == 'POST' and 'southernglazerswinespiritsproduction78xh7hnm.org.coveo.com/rest/search/v2' in request.url:  # Replace 'your_target_url'
				print(f"👽👽👽Intercepting request: {request.url}")
				# Get the current POST data
				current_data = request.body.decode('utf-8')
				# print(f"Original POST data: {current_data}")

				# Modify the POST data
				# Example: change a value in a JSON payload
				try:
					payload = json.loads(current_data)
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

	def build_products_list(self):
		"""Scrape products from the website"""
		print(f"build_products_list()")
		self.bypass_age_gate(self.options['url'])
		self.driver.request_interceptor = self.create_interceptor()
		html = ''
		html_table = ''
		all_urls = []
		categories = []
		chosen_category = int(self.options.get('chosen_category', 0))
		test_categories = self.options.get('test_categories', 100)
		test_products = self.options.get('test_products', 0)
		category_count = 0
		if int(self.options['chosen_category']) == 0:
			categories = self.TAXONOMY
			print(f"All Categories ")
		else:
			for category in self.TAXONOMY:
				if int(category.get('number', '')) == chosen_category:
					categories = [category]  # Only process the chosen category
					print(f"Category found : {categories}")
					break
		del self.driver.requests
		for category in categories:
			category_count = category_count + 1
			category_filter_string = "&" + format_filter(f"f-category={category['name']}")
			if category_count > test_categories:
				break
			i = 0
			for  class_ in category.get('classes', []):
				class_filter_string = "&" + format_filter(f"f-class={class_['name']}")

				for subclass in class_.get('subclasses', []):
					subclass_filter_string = "&" + format_filter(f"f-subclass={subclass['category']}")

					if i > test_products:
						break
					url = f"https://shop.sgproof.com/search?text={category_filter_string}{class_filter_string}{subclass_filter_string}"

					still_looking = True
					while still_looking and i < self.options['max_products']:
						i = i + 1
						category_name = category.get('name', '')
						class_name = class_.get('name', '')
						subclass_name = subclass.get('category', '')
						self.options['url_output_file'] = category_name + "_product_urls.csv"
						print(f"category_name : {category_name}")
						print(f"class_name : {class_name}")
						print(f"subclass_name : {subclass_name}")
						del self.driver.requests
						self.driver.get(url)
						print(f"URL : {url}")
						print(f"Page : {i}")
						filter_criteria = "southernglazerswinespiritsproduction78xh7hnm.org.coveo.com/rest/search"
						# request_filter2 = f"page={i}"
						# https://app.salsify.com/catalogs/api/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products?filter=%3D%27Product%20Category%27%3A%27Beer%27&page=1&per_page=36&product_identifier_collection_id=&query=
						request = self.driver.wait_for_request(filter_criteria, 40)
						if request.response and filter_criteria in request.url:  # Filter for API requests
							print(f"URL: {request.url}")
							print(f"Status Code: {request.response.status_code}")
							print(f"Content Type: {request.response.headers.get('Content-Type')}")

							# Decode the response body (it's bytes by default)
							try:
								# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
								body = decode(request.response.body,
								              request.response.headers.get('Content-Encoding', 'identity'))

								# If the body is JSON, parse it
								if 'application/json' in request.response.headers.get('Content-Type', ''):
									data = json.loads(body)
									# https://app.salsify.com/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products/9258080
									if 'results' in data:
										detail_urls = [
											product['clickUri']
											for product in data['results']]
										print(f"== Number of products: {len(detail_urls)}")
										all_urls.extend(detail_urls)
										html += f"<h2>{category_name} -> {class_['name']} -> {subclass['category']}</h2>"
										html += "<div>Products found: " + str(len(detail_urls)) + "</div>"
										self.save_urls_to_csv(detail_urls, category_name, class_['name'], subclass['category'])
										print(f"=== Number of products: {len(detail_urls)}")
										# for url in detail_urls:
										# 	self.process_product(url, {})
										# 	time.sleep(1)
										if len(detail_urls) < 250:
											still_looking = False
										# still_looking = False
									else:
										print(f"Response products missing: {'products' in data} ")
										print(f"data: {data} ")

								else:
									print(f"Response Body (Text): ")
									print(f"Response not JSON  ")


							except Exception as e:
								print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

						# del self.driver.request_interceptor
						del self.driver.requests

					# html, detail_urls = self.process_product_list_search_api(html, category_name)

					time.sleep(3)

		html_table += "</tbody></table>"
		# html_table_to_csv(html_table)
		html += f"<h2>Total products found: {len(all_urls)}</h2>"
		html += html_table
		print(f"Total products found: {len(all_urls)}")
		return html

	def process_product(self, url, row_spec=None):
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print("processing product detail page")
		print(f"Loading page...{url}")

		data = ''
		sku = row_spec['sku']
		url = f"https://shop.sgproof.com/sgws/en/usd/p/{sku}"
		request_filter_escaped = sku + "/\?expand"
		request_filter = sku + "/?expand"
		# https://shop.sgproof.com/sgws/en/usd/p/{sku}
		self.driver.get(url)
		print(f"Sent Request")
		try:
			request = self.driver.wait_for_request(request_filter_escaped)
			if request.response and request_filter in request.url:  # Filter for API requests
				print(f"URL: {request.url}")
				print(f"Status Code: {request.response.status_code}")
				print(f"Content Type: {request.response.headers.get('Content-Type')}")

				# Decode the response body (it's bytes by default)
				try:
					# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
					body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

					# If the body is JSON, parse it
					if 'application/json' in request.response.headers.get('Content-Type', ''):
						data = json.loads(body)
					else:
						print(f"Response Body (Text): {body}")

				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

			# These use the data if available, then try to scrape from the page
			row_spec = self.get_product_data(data, row_spec)

		except Exception as e:
			print(f"⛔️⛔️⛔️Error waiting for request: {e}")

			# for request in self.driver.requests:
			# 	print(request.url)

		del self.driver.requests
		return row_spec

	def build_categories_list(self):
		# Run on all to get a category list then copy the list to CATEGORIES
		url = "https://shop.sgproof.com/search"
		categories = []
		all_categories = []
		classes = []
		all_classes = []
		subclasses = []
		all_subclasses = []
		self.bypass_age_gate(url)
		print(f"Loading page...{url}")
		del self.driver.requests
		self.driver.get(url)
		# time.sleep(5)
		filter_criteria = "southernglazerswinespiritsproduction78xh7hnm.org.coveo.com/rest/search"
		print(f"Filtering for {filter_criteria}")
		request = self.driver.wait_for_request(filter_criteria, 40)
		data = None
		if request.response and filter_criteria in request.url:  # Filter for API requests
			print(f"Found response :")
			try:
				body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

				# If the body is JSON, parse it
				if 'application/json' in request.response.headers.get('Content-Type', ''):
					data = json.loads(body)
				else:
					print(f"Response not JSON :")
			except Exception as e:
				print(f"⛔️⛔️⛔️Error decoding search response body: {e}")
		del self.driver.requests
		categories = self.get_navigation_categories(data)

		for category in categories:
			print(f"Starting Category: {category['name']}")
			category_filter_string = "&" + format_filter(f"f-category={category['name']}")
			url = f"https://shop.sgproof.com/search?text={category_filter_string}"
			print(f"Loading page...{url}")
			del self.driver.requests
			self.driver.get(url)
			request = self.driver.wait_for_request(filter_criteria, 40)
			data = None
			if request.response and filter_criteria in request.url:  # Filter for API requests
				print(f"Found response for category:")
				try:
					body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
					# If the body is JSON, parse it
					if 'application/json' in request.response.headers.get('Content-Type', ''):
						data = json.loads(body)
						print(f"Got data")
					else:
						print(f"Response not JSON :")
				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding search response body: {e}")
				if data:
					print(f"Got data grabbing classes")
					classes = self.get_navigation_classes(data)
					category['classes'] = classes
					all_classes.extend(classes)
					all_categories.append(category)
					for class_ in classes:
						print(f"Starting Class: {class_['name']}")
						class_filter_string = "&" + format_filter(f"f-class={class_['name']}")
						url = f"https://shop.sgproof.com/search?text={category_filter_string}{class_filter_string}"
						print(f"Loading class page...{url}")
						del self.driver.requests
						self.driver.get(url)
						request = self.driver.wait_for_request(filter_criteria, 40)
						data = None
						if request.response and filter_criteria in request.url:  # Filter for API requests
							print(f"Found response :")
							try:
								# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
								body = decode(request.response.body,
								              request.response.headers.get('Content-Encoding', 'identity'))

								# If the body is JSON, parse it
								if 'application/json' in request.response.headers.get('Content-Type', ''):
									data = json.loads(body)
								else:
									print(f"Response not JSON :")
							except Exception as e:
								print(f"⛔️⛔️⛔️Error decoding search response body: {e}")
							subclasses = self.get_navigation_subclasses(data)
							class_['subclasses'] = subclasses
							print(f"Got subclasses")
							print(subclasses)
							all_subclasses.extend(subclasses)
			print(f"finished category : {category['name']}")
			print(category)
		# subclasses = self.get_product_subclasses(data)
		print(f"")
		print(f"categories : {json.dumps(categories)}")
		del self.driver.requests

		return f"<div>{json.dumps(categories)}</div>"

	def get_navigation_categories(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
		"""
		Extract product categories from search response data.

		Args:
			data: Dictionary containing the search response data (already parsed JSON)

		Returns:
			List of dictionaries containing category information with 'id' and 'name' keys
		"""
		if not isinstance(data, dict) or 'facets' not in data:
			return []

		# Find the category facet
		category_facets = []
		for facet in data['facets']:
			if facet.get('facetId') == 'category' and 'values' in facet:
				category_facets = [
					{
						'name': item['value'],
						'count': str(item['numberOfResults']),
						"number": str(index + 1),
					}
					for index, item in facet['values']
				]
				break
		print(f"category_facets : {category_facets}")
		return category_facets

	def get_navigation_classes(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
		"""
		Extract product categories from search response data.

		Args:
			data: Dictionary containing the search response data (already parsed JSON)

		Returns:
			List of dictionaries containing category information with 'id' and 'name' keys
		"""
		if not isinstance(data, dict) or 'facets' not in data:
			print(f"facets not in data")
			print(data)
			return []

		# Find the category facet
		class_facets = []
		for facet in data['facets']:
			if facet.get('facetId') == 'class' and 'values' in facet:
				class_facets = [
					{
						'name': item['value'],
						'count': str(item['numberOfResults']),
					}
					for item in facet['values']
				]
				break
		print(f"class facets : {class_facets}")
		return class_facets

	def get_navigation_subclasses(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
		"""
		Extract product categories from search response data.

		Args:
			data: Dictionary containing the search response data (already parsed JSON)

		Returns:
			List of dictionaries containing category information with 'id' and 'name' keys
		"""
		if not isinstance(data, dict) or 'facets' not in data:
			return []

		# Find the category facet
		subclass_facets = []
		for facet in data['facets']:
			if facet.get('facetId') == 'subclass' and 'values' in facet:
				subclass_facets = [
					{
						'name': item['value'],
						'count': str(item['numberOfResults']),
					}
					for item in facet['values']
				]
				break
		print(f"subclass_facets : {subclass_facets}")
		return subclass_facets