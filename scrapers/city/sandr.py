import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from scrapers.city.hive import HiveScraper

"""
	S and R
	Type: Standard shop website
	Method: 
		Get Categories: Scape Navigation
		Get Products: Scape Product List
		Get Product Manual Scrape and json data from html
	Issues:
		The embedded json data does not have all the information needed to create a product. Data like 
		sku and description are not included in the json data.
"""

class SandRScraper(HiveScraper):
	# 3280/edit_note/1728/
	CRM_ID = 3280
	CRM_NOTE_ID = 1728
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

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
		'subsubcategory': '',
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
		'product_id': '',
		'option_id': '',
		'page_description': '',
		'page_image': '',
		'page_sku': '',
		'state': '',
	}

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/s_and_r/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = 'https://srliquors.com/'
	VENDOR_NAME = 'S & R Liquors'
	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "name": "Shop All",
        "id": 2,
        "url": "https://srliquors.com/shop",
        "subcategories": [
          {
            "name": "Shop By Brand",
            "url": "",
            "subcategories": [
              {
                "name": "All Brands",
                "url": "https://srliquors.com/shop/?container-id=6194f35920459128ccff17cd&title=Shop+By+Brand"
              },
              {
                "name": "Wine Brands",
                "url": "https://srliquors.com/shop/?container-id=66e029d56a1c604675894512&title=Wine+Brands"
              },
              {
                "name": "Spirits Brands",
                "url": "https://srliquors.com/shop/?container-id=66e029eae1ecd0293828ce48&title=Spirits+Brands"
              },
              {
                "name": "Beer Brands",
                "url": "https://srliquors.com/shop/?container-id=66e029fee1ecd0294028e227&title=Beer+Brands"
              }
            ]
          },
          {
            "name": "Discover",
            "url": "",
            "subcategories": [
              {
                "name": "Our Deals",
                "url": "https://srliquors.com/pages/deals"
              }
            ]
          }
        ]
      },
      {
        "name": "Wine",
        "id": 3,
        "url": "https://srliquors.com/pages/shop-wine",
        "subcategories": [
          {
            "name": "By Style",
            "url": "",
            "subcategories": [
              {
                "name": "Red",
                "url": "https://srliquors.com/shop/?subtype=red"
              },
              {
                "name": "White",
                "url": "https://srliquors.com/shop/?subtype=white"
              },
              {
                "name": "Ros\u00e9 & Blush",
                "url": "https://srliquors.com/shop/?subtype=rose"
              },
              {
                "name": "Champagne & Sparkling",
                "url": "https://srliquors.com/shop/?subtype=sparkling"
              },
              {
                "name": "Dessert & Port",
                "url": "https://srliquors.com/shop/?subtype=dessert&subtype=port"
              },
              {
                "name": "Other Wines",
                "url": "https://srliquors.com/shop/?category=other_wine&title=Other+Wine"
              }
            ]
          },
          {
            "name": "By Varietal",
            "url": "",
            "subcategories": [
              {
                "name": "Cabernet Sauvignon",
                "url": "https://srliquors.com/shop/?category=cabernet_sauvignon_name&title=Cabernet%20Sauvignon"
              },
              {
                "name": "Chardonnay",
                "url": "https://srliquors.com/shop/?category=chardonnay_name&title=Chardonnay"
              },
              {
                "name": "Sauvignon Blanc",
                "url": "https://srliquors.com/shop/?category=sauvignon_blanc_name&title=Sauvignon%20Blanc"
              },
              {
                "name": "Red Blends",
                "url": "https://srliquors.com/shop/?type=wine&varietal=red+blend"
              },
              {
                "name": "Pinot Noir",
                "url": "https://srliquors.com/shop/?category=pinot_noir_name&title=Pinot%20Noir"
              },
              {
                "name": "Pinot Grigio",
                "url": "https://srliquors.com/shop/?category=pinot_grigio_name&title=Pinot%20Grigio"
              },
              {
                "name": "Rose",
                "url": "https://srliquors.com/shop/?varietal=rose"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "France",
                "url": "https://srliquors.com/shop/?type=wine&country=france"
              },
              {
                "name": "Italy",
                "url": "https://srliquors.com/shop/?type=wine&country=italy"
              },
              {
                "name": "Spain",
                "url": "https://srliquors.com/shop/?type=wine&country=spain"
              },
              {
                "name": "Germany",
                "url": "https://srliquors.com/shop/?type=wine&country=germany"
              },
              {
                "name": "Argentina",
                "url": "https://srliquors.com/shop/?type=wine&country=argentina"
              },
              {
                "name": "United States",
                "url": "https://srliquors.com/shop/?type=wine&country=united%20states"
              },
              {
                "name": "New Zealand",
                "url": "https://srliquors.com/shop/?type=wine&country=new%20zealand"
              }
            ]
          },
          {
            "name": "By Region",
            "url": "",
            "subcategories": [
              {
                "name": "Bordeaux",
                "url": "https://srliquors.com/shop/?type=wine®ion=bordeaux"
              },
              {
                "name": "Tuscany",
                "url": "https://srliquors.com/shop/?type=wine®ion=tuscany"
              },
              {
                "name": "Rioja",
                "url": "https://srliquors.com/shop/?type=wine®ion=rioja"
              },
              {
                "name": "Burgundy",
                "url": "https://srliquors.com/shop/?type=wine®ion=burgundy"
              },
              {
                "name": "Napa Valley",
                "url": "https://srliquors.com/shop/?type=wine®ion=napa%20valley"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://srliquors.com/shop/?category=wine_new_arrivals&title=Wine%20New%20Arrivals"
              },
              {
                "name": "Staff Picks",
                "url": "https://srliquors.com/shop/?category=wine_staff_picks&title=Wine%20Staff%20Picks"
              },
              {
                "name": "On Sale",
                "url": "https://srliquors.com/shop/?category=wine_on_sale&title=Wine%20On%20Sale"
              },
              {
                "name": "All Wine",
                "url": "https://srliquors.com/shop/?type=wine"
              },
              {
                "name": "Wine Brands",
                "url": "https://srliquors.com/shop/?container-id=66e029d56a1c604675894512&title=Wine+Brands"
              }
            ]
          }
        ]
      },
      {
        "name": "Spirits",
        "id": 4,
        "url": "https://srliquors.com/pages/shop-spirits",
        "subcategories": [
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "Vodka",
                "url": "https://srliquors.com/shop/?subtype=vodka"
              },
              {
                "name": "Whiskey",
                "url": "https://srliquors.com/shop/?subtype=whiskey"
              },
              {
                "name": "Sake",
                "url": "https://srliquors.com/shop/?subtype=sake"
              },
              {
                "name": "Tequila",
                "url": "https://srliquors.com/shop/?subtype=tequila"
              },
              {
                "name": "Rum",
                "url": "https://srliquors.com/shop/?subtype=rum"
              },
              {
                "name": "Gin",
                "url": "https://srliquors.com/shop/?subtype=gin"
              },
              {
                "name": "Brandy",
                "url": "https://srliquors.com/shop/?subtype=brandy"
              },
              {
                "name": "Liqueur",
                "url": "https://srliquors.com/shop/?subtype=liqueur"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "United States",
                "url": "https://srliquors.com/shop/?type=spirits&country=united%20states"
              },
              {
                "name": "France",
                "url": "https://srliquors.com/shop/?type=spirits&country=france"
              },
              {
                "name": "Ireland",
                "url": "https://srliquors.com/shop/?type=spirits&country=ireland"
              },
              {
                "name": "Japan",
                "url": "https://srliquors.com/shop/?type=spirits&country=japan"
              },
              {
                "name": "Italy",
                "url": "https://srliquors.com/shop/?type=spirits&country=italy"
              },
              {
                "name": "Mexico",
                "url": "https://srliquors.com/shop/?type=spirits&country=mexico"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://srliquors.com/shop/?category=spirits_new_arrivals&title=Spirits%20New%20Arrivals"
              },
              {
                "name": "Staff Picks",
                "url": "https://srliquors.com/shop/?category=spirits_staff_picks&title=Spirits%20Staff%20Picks"
              },
              {
                "name": "On Sale",
                "url": "https://srliquors.com/shop/?category=spirits_on_sale&title=Spirits%20On%20Sale"
              },
              {
                "name": "All Spirits",
                "url": "https://srliquors.com/shop/?type=spirits"
              },
              {
                "name": "Spirits Brands",
                "url": "https://srliquors.com/shop/?container-id=66e029eae1ecd0293828ce48&title=Spirits+Brands"
              }
            ]
          }
        ]
      },
      {
        "name": "Beer",
        "id": 5,
        "url": "https://srliquors.com/pages/shop-beer",
        "subcategories": [
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "IPA",
                "url": "https://srliquors.com/shop/?category=ipa_basic_category&title=IPA"
              },
              {
                "name": "Hard Seltzer",
                "url": "https://srliquors.com/shop/?category=seltzer_basic_category&title=Hard%20Seltzer"
              },
              {
                "name": "Ale",
                "url": "https://srliquors.com/shop/?category=ale_beer&title=ale"
              },
              {
                "name": "Lager",
                "url": "https://srliquors.com/shop/?category=lager_beer&title=lager"
              },
              {
                "name": "Pilsner",
                "url": "https://srliquors.com/shop/?category=pilsner_basic_category&title=pilsner"
              },
              {
                "name": "Stout",
                "url": "https://srliquors.com/shop/?category=stout_beer&title=stout"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://srliquors.com/shop/?category=beer_new_arrivals&title=Beer%20New%20Arrivals"
              },
              {
                "name": "Staff Picks",
                "url": "https://srliquors.com/shop/?category=beer_staff_picks&title=Beer%20Staff%20Picks"
              },
              {
                "name": "On Sale",
                "url": "https://srliquors.com/shop/?category=beer_on_sale&title=Beer%20On%20Sale"
              },
              {
                "name": "All Beer",
                "url": "https://srliquors.com/shop/?type=beer"
              },
              {
                "name": "Beer Brands",
                "url": "https://srliquors.com/shop/?container-id=66e029fee1ecd0294028e227&title=Beer+Brands"
              }
            ]
          }
        ]
      },
      {
        "name": "Staff Picks",
        "id": 6,
        "url": "https://srliquors.com/shop/?category=our_staff_picks&title=Staff%20Picks",
        "subcategories": []
      },
      {
        "name": "On Sale",
        "id": 7,
        "url": "https://srliquors.com/shop/?category=our_discount&title=On%20Sale",
        "subcategories": []
      },
      {
        "name": "Tasting & Events",
        "id": 8,
        "url": "https://srliquors.com/events",
        "subcategories": []
      },
      {
        "name": "Explore",
        "id": 9,
        "url": "https://srliquors.com/#",
        "subcategories": [
          {
            "name": "Store Info",
            "url": "",
            "subcategories": [
              {
                "name": "Location & Hours",
                "url": "https://srliquors.com/info"
              },
              {
                "name": "Notifications",
                "url": "https://srliquors.com/notifications"
              }
            ]
          },
          {
            "name": "My Account",
            "url": "",
            "subcategories": [
              {
                "name": "Order History",
                "url": "https://srliquors.com/order-history"
              }
            ]
          }
        ]
      }
    ]
  }
}
                                                           
		''')

	def __init__(self, options=None):
		super().__init__(options)
		# There are only 2 navigation categories we want to process and we only want to process 1 sub category
		self.options['test_categories'] = 6

	def scraping_setup(self):
		"""Scrape products from the website"""
		print("scraping_setup()")
		# self.bypass_cookie_consent(self.BASE_URL)
		return


