
import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.options import PageLoadStrategy
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire.utils import decode
from typing import List, Dict, Any, Optional

from scrapers.scraper import Scraper, SkuNotFound


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
		'timestamp': '',
		# Fields from Southern Glazier
		'extra_data_2': '',
		'vintage': '',
		'varietal': '',
		'appellation': '',
		'pack_size': '',
		'category': '',
		'subcategory': '',
		'bpc': '',
		'supplier': '',
		'producer': '',
		'region': '',
		'country_of_origin': '',
		'alcohol_proof': '',
		'alcohol_by_volume': '',
		'sub-type': '',
		'producer_description': '',
		'container_type': '',
		'closure_type': '',
		'units_per_case': '',
		'packs_per_case': '',
		'units_per_pack': '',
		'outer_pkg': '',
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
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}

	def get_category_ids(self):
		return self.CATEGORY_IDS

	def get_categories(self):
		return self.TAXONOMY

	def get_category_names(self):
		return self.CATEGORY_NAMES

	def get_category_urls(self):
		return self.CATEGORY_URLS

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

	def bypass_age_gate(self, url):
		try:
			self.driver.get(url)
			# time.sleep(2)
			modal = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '.modal-box div.verify-select div.form-select'))
			)
			select = self.driver.find_element(By.CSS_SELECTOR, '.modal-box select.verify-select-input')

			select.click()
			select = Select(select)
			select.select_by_value("91")
			self.driver.find_element(By.CSS_SELECTOR, '.modal-box .verify-trigger-yes').click()

			print("Bypassed age gate")
		except Exception as e:
			print(f"Error: {e}")

	def bypass_age_gate_home_page(self, url):
		print("bypass_age_gate_home_page()")
		try:
			self.driver.get(url)
			modal = self.wait.until(
				EC.visibility_of_element_located((By.CSS_SELECTOR, '#ageGatemodal'))
			)
			print(f"select: {modal}")
			select = modal.find_element(By.CSS_SELECTOR, '#stateSelect')
			print(f"select: {select}")
			# select.click()
			select = Select(select)
			print(f"select: {select}")
			select.select_by_value("91")
			# Yes button should be activated so click it
			modal.find_element(By.CSS_SELECTOR, '#ageGatemodal .verify-trigger-yes').click()

			print("Bypassed age gate")
		except Exception as e:
			print(f"Error: {e}")
			# time.sleep(200)

	def scraping_setup(self):
		"""Scrape products from the website"""
		print("scraping_setup()")
		self.bypass_age_gate_home_page("https://shop.sgproof.com/")
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
			image_url = self.driver.find_element(By.CSS_SELECTOR, 'img.product-viewer-image').get_attribute("src")
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

	def get_table_section(self, row_spec):
		# Scrape the section that contains the manufacturer information. It is in an unordered list
		print("get_table_section()")
		#product-info-table-container
		details = self.driver.find_element(By.CSS_SELECTOR, 'div.product-info-table-container')
		print(details)
		try:
			hidden_element = self.driver.find_element(By.CSS_SELECTOR, '.product-info-table-container div.product-info-hide')
			self.driver.execute_script("arguments[0].style.display = 'block';", hidden_element)
		except Exception as e:
			print(f"No hidden element: {type(e)}")
		try:
			rows = details.find_elements(By.CSS_SELECTOR, 'div.g-row')
			print(rows)
			for row in rows:
				key = row.find_element(By.CSS_SELECTOR, '.product-info-table-left').text.strip()
				key = key.lower().replace(' ', '_').replace('_(%)', '')
				print(key)
				value = row.find_element(By.CSS_SELECTOR, '.product-info-table-right').text.strip()
				if key in self.PRODUCT_DATA_SPEC.keys():
					row_spec[key] = value

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing table data: {type(e)}")
		return row_spec

	def get_variant_section(self, container, row_spec):
		# Scrape the section that contains the manufacturer information. It is in an unordered list
		print("get_variant_section()")
		hidden_element = self.driver.find_element(By.CSS_SELECTOR, 'div.item-variant-menu')
		self.driver.execute_script("arguments[0].style.display = 'block';", hidden_element)
		variant_info = container.find_element(By.CSS_SELECTOR, 'div.item-variant-menu-list')
		try:
			rows = variant_info.find_elements(By.CSS_SELECTOR, 'a.item-variant-list-menu-item')
			print(rows)
			for row in rows:
				row_dict = {}
				columns = row.find_elements(By.CSS_SELECTOR, 'div.item-variant')
				print(columns)
				for column in columns:
					key = column.find_element(By.CSS_SELECTOR, 'span.item-variant-list-mobile-header').text.strip()
					key = key.lower().replace(' ', '_').replace(':', '')
					print(f"key: {key}")
					value = column.find_element(By.CSS_SELECTOR, 'span.item-variant-list').text.strip()
					value = '' if value == '—' else value
					print(f"value: {value}")
					if key in self.PRODUCT_DATA_SPEC.keys() or key == 'item_id':
						row_dict.update({key: value})
				if row_dict['item_id'] == row_spec['sku']:
					for key, value in row_dict.items():
						if key in self.PRODUCT_DATA_SPEC.keys():
							row_spec[key] = value
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing variant data: {type(e)}")
		return row_spec

	def get_description(self, row_spec):
		print("get_description()")
		description = ''
		# product-info-about-container
		self.driver.execute_script("document.body.style.zoom = '20%'")
		try:
			producer_description = self.driver.find_element(By.CSS_SELECTOR, 'div.product-info-full').text.strip()
			if producer_description:
				row_spec["producer_description"]  = producer_description
		except Exception as e:
			print(f"⛔️️ Error processing product producer description: {type(e)}")

		# product-card-pdp-desc
		try:
			description = self.driver.find_element(By.CSS_SELECTOR, 'div.product-card-pdp-desc').text.strip()
			if description:
				row_spec["description"]  = description
		except Exception as e:
			print(f"⛔️️ Error processing product description: {type(e)}")
		print("processing product overview Complete...")
		return row_spec

	def get_additional_packages(self):
		"""
		Product have a dropsown selector for chosing different versions
		"""
		print("get_additional_packages()")
		package_list = []
		# Get item list from item-variant-menu-list
		variation_list = self.wait.until(
			EC.presence_of_element_located((By.CSS_SELECTOR, '.item-variant-menu-list'))
		)
		anchor_list = variation_list.find_elements(By.TAG_NAME, 'a')
		print(f"anchor_list: {anchor_list}")
		for anchor in anchor_list:
			href_value = anchor.get_attribute("href")
			print(f"href_value: {href_value}")
			package_list.append(href_value)

		print(f"anchor_list: {package_list}")
		return package_list

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
					if len(self.options['direct_category_to_process']) > 0 and self.options[
						'direct_category_to_process'] != url:
						print(f"Skipping category {category['name']} as it is not the direct category to process")
						continue
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
						print(f"Loading page...{url}")

						del self.driver.requests
						self.driver.get(url)
						print(f"URL Loaded")
						print(f"Page : {i}")
						continue_on = True
						filter_criteria = "southernglazerswinespiritsproduction78xh7hnm.org.coveo.com/rest/search"
						# request_filter2 = f"page={i}"
						# https://app.salsify.com/catalogs/api/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products?filter=%3D%27Product%20Category%27%3A%27Beer%27&page=1&per_page=36&product_identifier_collection_id=&query=
						try:
							request = self.driver.wait_for_request(filter_criteria, 50)
						except Exception as e:
							print(f"⛔️⛔️⛔️Request failed: {e}")
							html += f"<h2>{category_name} -> {class_['name']} -> {subclass['category']}</h2>"
							html += "<div>TIme Out </div>"
							break
						if request.response and filter_criteria in request.url:  # Filter for API requests
							print(f"URL: {request.url}")
							print(f"Status Code: {request.response.status_code}")
							print(f"Content Type: {request.response.headers.get('Content-Type')}")
							current_data = request.body.decode('utf-8')
							# print(f"current_data: {current_data}")
							payload = json.loads(current_data)
							if 'facets' in payload and payload['facets']:
								for facet in payload['facets']:
									if facet.get('field') == 'ec_prd_category':
										print(facet)
										print(f"Number of results: {payload['numberOfResults']}")
									if facet.get('field') == 'ec_prd_category' and (
											not facet.get('currentValues') or len(
										facet.get('currentValues', [])) == 0):
										print("This is not the request you are looking for")
										continue_on = False

							if continue_on:
								try:
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
											if len(detail_urls) < self.MAX_API_PRODUCTS:
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

	def process_details_from_html(self, url, follow_anchors=False, row_spec=None):
		print(f"process_details_from_html()")
		additional_packages = []
		del self.driver.requests
		self.driver.get(url)
		# product-viewer-box
		try:
			print("here")
			container = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '.marketplace-product-card'))
			)
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing process_details_from_html: {type(e)}")
			raise
		try:
			row_spec['content_url'] = self.driver.current_url
			print("here2")
			name = container.find_element(By.CSS_SELECTOR, 'div.product-card-title h3').text.strip()
			print(f"name: {name}")
			row_spec['name'] = name

			row_spec = self.get_description(row_spec)
			row_spec = self.get_table_section(row_spec)
			row_spec = self.get_first_image_url(row_spec)
			# page has a dropdown to select additional packages
			if follow_anchors:
				additional_packages = self.get_additional_packages()
			else:
				try:
					variant_info = container.find_element(By.CSS_SELECTOR, '.item-variant-select-text')
					sku = variant_info.find_element(By.CSS_SELECTOR, '[data-at-product-id]').text.strip()
					row_spec['sku'] = sku
					row_spec = self.get_variant_section(container, row_spec)
				except Exception as e:
					print(f"⛔️Error finding variant info: {type(e)}")
					raise SkuNotFound
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing process_details_from_html: {type(e)}")
		return row_spec, additional_packages

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
		print("processing product detail page")

		data = ''
		sku = row_spec['sku']
		url = f"https://shop.sgproof.com/sgws/en/usd/p/{sku}"
		row_spec['content_url'] = url
		# https://shop.sgproof.com/sgws/en/usd/p/{sku}
		print(f"Loading page...{url}")
		try:
			row_spec, additional_packages = self.process_details_from_html(url, row_spec=row_spec, follow_anchors=False)
			# self.write_product_to_csv(row_spec)
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing get_product_details: {type(e)}")
			raise

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