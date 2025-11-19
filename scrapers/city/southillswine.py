import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from scrapers.city.hive import HiveScraper

"""
	South Hills Wine
	Type: Standard shop website
	Method: 
		Get Categories: Scape Navigation
		Get Products: Scape Product List
		Get Product Manual Scrape and json data from html
	Issues:
		The embedded json data does not have all the information needed to create a product. Data like 
		sku and description are not included in the json data.
"""

class ShortHillsWineScraper(HiveScraper):
	# 3302/edit_note/1729/
	CRM_ID = 3302
	CRM_NOTE_ID = 1729
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = 'Ready'

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/short_hill_wine/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = 'https://shorthillswine.com/'
	VENDOR_NAME = 'Short Hills Wine'
	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "name": "Shop All",
        "id": 2,
        "url": "https://shorthillswine.com/shop",
        "subcategories": [
          {
            "name": "Shop By Brand",
            "url": "",
            "subcategories": [
              {
                "name": "All Brands",
                "url": "https://shorthillswine.com/shop/?container-id=6194f35920459128ccff17cd&title=Shop+By+Brand"
              },
              {
                "name": "Wine Brands",
                "url": "https://shorthillswine.com/shop/?container-id=66e029d56a1c604675894512&title=Wine+Brands"
              },
              {
                "name": "Spirits Brands",
                "url": "https://shorthillswine.com/shop/?container-id=66e029eae1ecd0293828ce48&title=Spirits+Brands"
              },
              {
                "name": "Beer Brands",
                "url": "https://shorthillswine.com/shop/?container-id=66e029fee1ecd0294028e227&title=Beer+Brands"
              }
            ]
          },
          {
            "name": "Discover",
            "url": "",
            "subcategories": [
              {
                "name": "Our Deals",
                "url": "https://shorthillswine.com/pages/deals"
              }
            ]
          }
        ]
      },
      {
        "name": "Wine",
        "id": 3,
        "url": "https://shorthillswine.com/pages/shop-wine",
        "subcategories": [
          {
            "name": "By Style",
            "url": "",
            "subcategories": [
              {
                "name": "Red",
                "url": "https://shorthillswine.com/shop/?subtype=red"
              },
              {
                "name": "White",
                "url": "https://shorthillswine.com/shop/?subtype=white"
              },
              {
                "name": "Ros\u00e9 & Blush",
                "url": "https://shorthillswine.com/shop/?subtype=rose"
              },
              {
                "name": "Champagne & Sparkling",
                "url": "https://shorthillswine.com/shop/?subtype=sparkling"
              },
              {
                "name": "Dessert & Port",
                "url": "https://shorthillswine.com/shop/?subtype=dessert&subtype=port"
              },
              {
                "name": "Other Wines",
                "url": "https://shorthillswine.com/shop/?category=other_wine&title=Other+Wine"
              }
            ]
          },
          {
            "name": "By Varietal",
            "url": "",
            "subcategories": [
              {
                "name": "Cabernet Sauvignon",
                "url": "https://shorthillswine.com/shop/?category=cabernet_sauvignon_name&title=Cabernet%20Sauvignon"
              },
              {
                "name": "Chardonnay",
                "url": "https://shorthillswine.com/shop/?category=chardonnay_name&title=Chardonnay"
              },
              {
                "name": "Sauvignon Blanc",
                "url": "https://shorthillswine.com/shop/?category=sauvignon_blanc_name&title=Sauvignon%20Blanc"
              },
              {
                "name": "Red Blends",
                "url": "https://shorthillswine.com/shop/?type=wine&varietal=red+blend"
              },
              {
                "name": "Pinot Noir",
                "url": "https://shorthillswine.com/shop/?category=pinot_noir_name&title=Pinot%20Noir"
              },
              {
                "name": "Pinot Grigio",
                "url": "https://shorthillswine.com/shop/?category=pinot_grigio_name&title=Pinot%20Grigio"
              },
              {
                "name": "Rose",
                "url": "https://shorthillswine.com/shop/?varietal=rose"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "France",
                "url": "https://shorthillswine.com/shop/?type=wine&country=france"
              },
              {
                "name": "Italy",
                "url": "https://shorthillswine.com/shop/?type=wine&country=italy"
              },
              {
                "name": "Spain",
                "url": "https://shorthillswine.com/shop/?type=wine&country=spain"
              },
              {
                "name": "Germany",
                "url": "https://shorthillswine.com/shop/?type=wine&country=germany"
              },
              {
                "name": "Argentina",
                "url": "https://shorthillswine.com/shop/?type=wine&country=argentina"
              },
              {
                "name": "United States",
                "url": "https://shorthillswine.com/shop/?type=wine&country=united%20states"
              },
              {
                "name": "New Zealand",
                "url": "https://shorthillswine.com/shop/?type=wine&country=new%20zealand"
              }
            ]
          },
          {
            "name": "By Region",
            "url": "",
            "subcategories": [
              {
                "name": "Bordeaux",
                "url": "https://shorthillswine.com/shop/?type=wine®ion=bordeaux"
              },
              {
                "name": "Tuscany",
                "url": "https://shorthillswine.com/shop/?type=wine®ion=tuscany"
              },
              {
                "name": "Rioja",
                "url": "https://shorthillswine.com/shop/?type=wine®ion=rioja"
              },
              {
                "name": "Burgundy",
                "url": "https://shorthillswine.com/shop/?type=wine®ion=burgundy"
              },
              {
                "name": "Napa Valley",
                "url": "https://shorthillswine.com/shop/?type=wine®ion=napa%20valley"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://shorthillswine.com/shop/?category=wine_new_arrivals&title=Wine%20New%20Arrivals"
              },
              {
                "name": "Staff Picks",
                "url": "https://shorthillswine.com/shop/?category=wine_staff_picks&title=Wine%20Staff%20Picks"
              },
              {
                "name": "On Sale",
                "url": "https://shorthillswine.com/shop/?category=wine_on_sale&title=Wine%20On%20Sale"
              },
              {
                "name": "All Wine",
                "url": "https://shorthillswine.com/shop/?type=wine"
              },
              {
                "name": "Wine Brands",
                "url": "https://shorthillswine.com/shop/?container-id=66e029d56a1c604675894512&title=Wine+Brands"
              }
            ]
          }
        ]
      },
      {
        "name": "Spirits",
        "id": 4,
        "url": "https://shorthillswine.com/pages/shop-spirits",
        "subcategories": [
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "Vodka",
                "url": "https://shorthillswine.com/shop/?subtype=vodka"
              },
              {
                "name": "Whiskey",
                "url": "https://shorthillswine.com/shop/?subtype=whiskey"
              },
              {
                "name": "Sake",
                "url": "https://shorthillswine.com/shop/?subtype=sake"
              },
              {
                "name": "Tequila",
                "url": "https://shorthillswine.com/shop/?subtype=tequila"
              },
              {
                "name": "Rum",
                "url": "https://shorthillswine.com/shop/?subtype=rum"
              },
              {
                "name": "Gin",
                "url": "https://shorthillswine.com/shop/?subtype=gin"
              },
              {
                "name": "Brandy",
                "url": "https://shorthillswine.com/shop/?subtype=brandy"
              },
              {
                "name": "Liqueur",
                "url": "https://shorthillswine.com/shop/?subtype=liqueur"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "United States",
                "url": "https://shorthillswine.com/shop/?type=spirits&country=united%20states"
              },
              {
                "name": "France",
                "url": "https://shorthillswine.com/shop/?type=spirits&country=france"
              },
              {
                "name": "Ireland",
                "url": "https://shorthillswine.com/shop/?type=spirits&country=ireland"
              },
              {
                "name": "Japan",
                "url": "https://shorthillswine.com/shop/?type=spirits&country=japan"
              },
              {
                "name": "Italy",
                "url": "https://shorthillswine.com/shop/?type=spirits&country=italy"
              },
              {
                "name": "Mexico",
                "url": "https://shorthillswine.com/shop/?type=spirits&country=mexico"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://shorthillswine.com/shop/?category=spirits_new_arrivals&title=Spirits%20New%20Arrivals"
              },
              {
                "name": "Staff Picks",
                "url": "https://shorthillswine.com/shop/?category=spirits_staff_picks&title=Spirits%20Staff%20Picks"
              },
              {
                "name": "On Sale",
                "url": "https://shorthillswine.com/shop/?category=spirits_on_sale&title=Spirits%20On%20Sale"
              },
              {
                "name": "All Spirits",
                "url": "https://shorthillswine.com/shop/?type=spirits"
              },
              {
                "name": "Spirits Brands",
                "url": "https://shorthillswine.com/shop/?container-id=66e029eae1ecd0293828ce48&title=Spirits+Brands"
              }
            ]
          }
        ]
      },
      {
        "name": "Beer",
        "id": 5,
        "url": "https://shorthillswine.com/pages/shop-beer",
        "subcategories": [
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "IPA",
                "url": "https://shorthillswine.com/shop/?category=ipa_basic_category&title=IPA"
              },
              {
                "name": "Hard Seltzer",
                "url": "https://shorthillswine.com/shop/?category=seltzer_basic_category&title=Hard%20Seltzer"
              },
              {
                "name": "Ale",
                "url": "https://shorthillswine.com/shop/?category=ale_beer&title=ale"
              },
              {
                "name": "Lager",
                "url": "https://shorthillswine.com/shop/?category=lager_beer&title=lager"
              },
              {
                "name": "Pilsner",
                "url": "https://shorthillswine.com/shop/?category=pilsner_basic_category&title=pilsner"
              },
              {
                "name": "Stout",
                "url": "https://shorthillswine.com/shop/?category=stout_beer&title=stout"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://shorthillswine.com/shop/?category=beer_new_arrivals&title=Beer%20New%20Arrivals"
              },
              {
                "name": "Staff Picks",
                "url": "https://shorthillswine.com/shop/?category=beer_staff_picks&title=Beer%20Staff%20Picks"
              },
              {
                "name": "On Sale",
                "url": "https://shorthillswine.com/shop/?category=beer_on_sale&title=Beer%20On%20Sale"
              },
              {
                "name": "All Beer",
                "url": "https://shorthillswine.com/shop/?type=beer"
              },
              {
                "name": "Beer Brands",
                "url": "https://shorthillswine.com/shop/?container-id=66e029fee1ecd0294028e227&title=Beer+Brands"
              }
            ]
          }
        ]
      },
      {
        "name": "Staff Picks",
        "id": 6,
        "url": "https://shorthillswine.com/shop/?category=our_staff_picks&title=Staff%20Picks",
        "subcategories": []
      },
      {
        "name": "On Sale",
        "id": 7,
        "url": "https://shorthillswine.com/shop/?category=our_discount&title=On%20Sale",
        "subcategories": []
      },
      {
        "name": "Tasting & Events",
        "id": 8,
        "url": "https://shorthillswine.com/events",
        "subcategories": []
      },
      {
        "name": "Explore",
        "id": 9,
        "url": "https://shorthillswine.com/#",
        "subcategories": [
          {
            "name": "Store Info",
            "url": "",
            "subcategories": [
              {
                "name": "Location & Hours",
                "url": "https://shorthillswine.com/info"
              },
              {
                "name": "Notifications",
                "url": "https://shorthillswine.com/notifications"
              }
            ]
          },
          {
            "name": "My Account",
            "url": "",
            "subcategories": [
              {
                "name": "Order History",
                "url": "https://shorthillswine.com/order-history"
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


