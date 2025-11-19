import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from scrapers.city.hive import HiveScraper

"""
	Cellar 53
	Type: Standard shop website
	Method: 
		Get Categories: Scape Navigation
		Get Products: Scape Product List
		Get Product Manual Scrape and json data from html
	Issues:
		The embedded json data does not have all the information needed to create a product. Data like 
		sku and description are not included in the json data.
"""

class Cellar53Scraper(HiveScraper):
	# 3206/edit_note/1725/
	CRM_ID = 3206
	CRM_NOTE_ID = 1725
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/cellar_53/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = 'https://cellar53wine.com/'
	VENDOR_NAME = 'Cellar 53'
	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "name": "Shop All",
        "id": 2,
        "url": "https://cellar53wine.com/shop",
        "subcategories": []
      },
      {
        "name": "Wine",
        "id": 3,
        "url": "https://cellar53wine.com/pages/shop-wine",
        "subcategories": [
          {
            "name": "By Style",
            "url": "",
            "subcategories": [
              {
                "name": "Red",
                "url": "https://cellar53wine.com/shop/?subtype=red"
              },
              {
                "name": "White",
                "url": "https://cellar53wine.com/shop/?subtype=white"
              },
              {
                "name": "Ros\u00e9",
                "url": "https://cellar53wine.com/shop/?subtype=rose"
              },
              {
                "name": "Sparkling",
                "url": "https://cellar53wine.com/shop/?subtype=sparkling"
              },
              {
                "name": "Blend",
                "url": "https://cellar53wine.com/shop/?subtype=blend"
              },
              {
                "name": "Dessert",
                "url": "https://cellar53wine.com/shop/?subtype=dessert"
              },
              {
                "name": "Port",
                "url": "https://cellar53wine.com/shop/?subtype=port"
              }
            ]
          },
          {
            "name": "By Varietal",
            "url": "",
            "subcategories": [
              {
                "name": "Cabernet Sauvignon",
                "url": "https://cellar53wine.com/shop/?varietal=cabernet%20sauvignon"
              },
              {
                "name": "Merlot",
                "url": "https://cellar53wine.com/shop/?varietal=merlot"
              },
              {
                "name": "Pinot Grigio",
                "url": "https://cellar53wine.com/shop/?varietal=pinot%20grigio"
              },
              {
                "name": "Pinot Noir",
                "url": "https://cellar53wine.com/shop/?varietal=pinot%20noir"
              },
              {
                "name": "Shiraz/Syrah",
                "url": "https://cellar53wine.com/shop/?varietal=shiraz"
              },
              {
                "name": "Riesling",
                "url": "https://cellar53wine.com/shop/?varietal=riesling"
              },
              {
                "name": "Sauvignon Blanc",
                "url": "https://cellar53wine.com/shop/?varietal=sauvignon%20blanc"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "France",
                "url": "https://cellar53wine.com/shop/?ch-query=wine%20france"
              },
              {
                "name": "Italy",
                "url": "https://cellar53wine.com/shop/?ch-query=wine%20italy"
              },
              {
                "name": "Spain",
                "url": "https://cellar53wine.com/shop/?ch-query=wine%20spain"
              },
              {
                "name": "Germany",
                "url": "https://cellar53wine.com/shop/?ch-query=wine%20germany"
              },
              {
                "name": "Argentina",
                "url": "https://cellar53wine.com/shop/?ch-query=wine%20argentina"
              },
              {
                "name": "United States",
                "url": "https://cellar53wine.com/shop/?ch-query=wine%20united%20states"
              },
              {
                "name": "New Zealand",
                "url": "https://cellar53wine.com/shop/?ch-query=wine%20new%20zealand"
              }
            ]
          },
          {
            "name": "By Region",
            "url": "",
            "subcategories": [
              {
                "name": "Bordeaux",
                "url": "https://cellar53wine.com/shop/?region=bordeaux"
              },
              {
                "name": "Tuscany",
                "url": "https://cellar53wine.com/shop/?region=tuscany"
              },
              {
                "name": "Rioja",
                "url": "https://cellar53wine.com/shop/?region=rioja"
              },
              {
                "name": "Burgundy",
                "url": "https://cellar53wine.com/shop/?region=burgundy"
              },
              {
                "name": "Napa Valley",
                "url": "https://cellar53wine.com/shop/?region=napa%20valley"
              }
            ]
          }
        ]
      },
      {
        "name": "Spirits",
        "id": 4,
        "url": "https://cellar53wine.com/pages/shop-spirits",
        "subcategories": [
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "Vodka",
                "url": "https://cellar53wine.com/shop/?subtype=vodka"
              },
              {
                "name": "Whiskey",
                "url": "https://cellar53wine.com/shop/?subtype=whiskey"
              },
              {
                "name": "Sake",
                "url": "https://cellar53wine.com/shop/?subtype=sake"
              },
              {
                "name": "Tequila",
                "url": "https://cellar53wine.com/shop/?subtype=tequila"
              },
              {
                "name": "Rum",
                "url": "https://cellar53wine.com/shop/?subtype=rum"
              },
              {
                "name": "Gin",
                "url": "https://cellar53wine.com/shop/?subtype=gin"
              },
              {
                "name": "Brandy",
                "url": "https://cellar53wine.com/shop/?subtype=brandy"
              },
              {
                "name": "Liqueur",
                "url": "https://cellar53wine.com/shop/?subtype=liqueur"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "United States",
                "url": "https://cellar53wine.com/shop/?ch-query=spirits%20united%20states"
              },
              {
                "name": "France",
                "url": "https://cellar53wine.com/shop/?ch-query=spirits%20france"
              },
              {
                "name": "Ireland",
                "url": "https://cellar53wine.com/shop/?ch-query=spirits%20ireland"
              },
              {
                "name": "Japan",
                "url": "https://cellar53wine.com/shop/?ch-query=spirits%20japan"
              },
              {
                "name": "Italy",
                "url": "https://cellar53wine.com/shop/?ch-query=spirits%20italy"
              },
              {
                "name": "Mexico",
                "url": "https://cellar53wine.com/shop/?ch-query=spirits%20mexico"
              }
            ]
          }
        ]
      },
      {
        "name": "Staff Picks",
        "id": 5,
        "url": "https://cellar53wine.com/shop/?category=our_staff_picks",
        "subcategories": []
      },
      {
        "name": "Tasting & Events",
        "id": 6,
        "url": "https://cellar53wine.com/events",
        "subcategories": []
      },
      {
        "name": "Store Info",
        "id": 7,
        "url": "https://cellar53wine.com/info",
        "subcategories": [
          {
            "name": "Store Info",
            "url": "",
            "subcategories": [
              {
                "name": "Location & Hours",
                "url": "https://cellar53wine.com/info"
              },
              {
                "name": "Notifications",
                "url": "https://cellar53wine.com/notifications"
              }
            ]
          },
          {
            "name": "My Account",
            "url": "",
            "subcategories": [
              {
                "name": "Order History",
                "url": "https://cellar53wine.com/order-history"
              }
            ]
          }
        ]
      },
      {
        "name": "About Us",
        "id": 8,
        "url": "https://cellar53wine.com/pages/about-cellar-53-wine-and-spirits/",
        "subcategories": []
      },
      {
        "name": "Gift Cards",
        "id": 9,
        "url": "https://cellar53wine.com/buy-gift-cards",
        "subcategories": []
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


