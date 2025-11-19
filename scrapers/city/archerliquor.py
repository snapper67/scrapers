import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from scrapers.city.hive import HiveScraper

"""
	Archer Liquors
	Type: Standard shop website
	Method: 
		Get Categories: Scape Navigation
		Get Products: Scape Product List
		Get Product Manual Scrape and json data from html
	Issues:
		Categories manually edited to remove non products
"""


class ArcherLiquorScraper(HiveScraper):
	CRM_ID = 3359
	CRM_NOTE_ID = 1663
	CRM_PRICE_TYPE = 'Retail'
	CRM_STATUS_OVERRIDE = ''

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/archer_liquor/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = 'https://archerliquors.com/'
	VENDOR_NAME = 'Archer Liquor'
	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "name": "Wine",
        "id": 3,
        "url": "https://archerliquors.com/pages/shop-wine",
        "subcategories": [
          {
            "name": "By Style",
            "url": "",
            "subcategories": [
              {
                "name": "Red",
                "url": "https://archerliquors.com/shop/?subtype=red"
              },
              {
                "name": "White",
                "url": "https://archerliquors.com/shop/?subtype=white"
              },
              {
                "name": "Rose & Blush",
                "url": "https://archerliquors.com/shop/?subtype=rose"
              },
              {
                "name": "Champagne & Sparkling",
                "url": "https://archerliquors.com/shop/?subtype=sparkling"
              },
              {
                "name": "Dessert & Port",
                "url": "https://archerliquors.com/shop/?subtype=dessert&subtype=port"
              },
              {
                "name": "Other Wines",
                "url": "https://archerliquors.com/shop/?category=other_wine&title=Other+Wine"
              }
            ]
          },
          {
            "name": "By Varietal",
            "url": "",
            "subcategories": [
              {
                "name": "Cabernet Sauvignon",
                "url": "https://archerliquors.com/shop/?category=cabernet_sauvignon_name&title=Cabernet%20Sauvignon"
              },
              {
                "name": "Chardonnay",
                "url": "https://archerliquors.com/shop/?category=chardonnay_name&title=Chardonnay"
              },
              {
                "name": "Sauvignon Blanc",
                "url": "https://archerliquors.com/shop/?category=sauvignon_blanc_name&title=Sauvignon%20Blanc"
              },
              {
                "name": "Red Blends",
                "url": "https://archerliquors.com/shop/?type=wine&varietal=red+blend"
              },
              {
                "name": "Pinot Noir",
                "url": "https://archerliquors.com/shop/?category=pinot_noir_name&title=Pinot%20Noir"
              },
              {
                "name": "Pinot Grigio",
                "url": "https://archerliquors.com/shop/?category=pinot_grigio_name&title=Pinot%20Grigio"
              },
              {
                "name": "Rose",
                "url": "https://archerliquors.com/shop/?varietal=rose"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "France",
                "url": "https://archerliquors.com/shop/?type=wine&country=france"
              },
              {
                "name": "Italy",
                "url": "https://archerliquors.com/shop/?type=wine&country=italy"
              },
              {
                "name": "Spain",
                "url": "https://archerliquors.com/shop/?type=wine&country=spain"
              },
              {
                "name": "Germany",
                "url": "https://archerliquors.com/shop/?type=wine&country=germany"
              },
              {
                "name": "Argentina",
                "url": "https://archerliquors.com/shop/?type=wine&country=argentina"
              },
              {
                "name": "United States",
                "url": "https://archerliquors.com/shop/?type=wine&country=united%20states"
              },
              {
                "name": "New Zealand",
                "url": "https://archerliquors.com/shop/?type=wine&country=new%20zealand"
              }
            ]
          },
          {
            "name": "By Region",
            "url": "",
            "subcategories": [
              {
                "name": "Bordeaux",
                "url": "https://archerliquors.com/shop/?type=wine®ion=bordeaux"
              },
              {
                "name": "Tuscany",
                "url": "https://archerliquors.com/shop/?type=wine®ion=tuscany"
              },
              {
                "name": "Rioja",
                "url": "https://archerliquors.com/shop/?type=wine®ion=rioja"
              },
              {
                "name": "Burgundy",
                "url": "https://archerliquors.com/shop/?type=wine®ion=burgundy"
              },
              {
                "name": "Napa Valley",
                "url": "https://archerliquors.com/shop/?type=wine®ion=napa%20valley"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://archerliquors.com/shop/?category=wine_new_arrivals&title=Wine%20New%20Arrivals"
              },
              {
                "name": "Staff Picks",
                "url": "https://archerliquors.com/shop/?category=wine_staff_picks&title=Wine%20Staff%20Picks"
              },
              {
                "name": "On Sale",
                "url": "https://archerliquors.com/shop/?category=wine_on_sale&title=Wine%20On%20Sale"
              },
              {
                "name": "All Wine",
                "url": "https://archerliquors.com/shop/?type=wine"
              },
              {
                "name": "Wine Brands",
                "url": "https://archerliquors.com/shop/?container-id=66e029d56a1c604675894512&title=Wine+Brands"
              }
            ]
          }
        ]
      },
      {
        "name": "Spirits",
        "id": 4,
        "url": "https://archerliquors.com/pages/shop-spirits",
        "subcategories": [
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "Vodka",
                "url": "https://archerliquors.com/shop/?subtype=vodka"
              },
              {
                "name": "Whiskey",
                "url": "https://archerliquors.com/shop/?subtype=whiskey"
              },
              {
                "name": "Sake",
                "url": "https://archerliquors.com/shop/?subtype=sake"
              },
              {
                "name": "Tequila",
                "url": "https://archerliquors.com/shop/?subtype=tequila"
              },
              {
                "name": "Rum",
                "url": "https://archerliquors.com/shop/?subtype=rum"
              },
              {
                "name": "Gin",
                "url": "https://archerliquors.com/shop/?subtype=gin"
              },
              {
                "name": "Brandy",
                "url": "https://archerliquors.com/shop/?subtype=brandy"
              },
              {
                "name": "Liqueur",
                "url": "https://archerliquors.com/shop/?subtype=liqueur"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "United States",
                "url": "https://archerliquors.com/shop/?type=spirits&country=united%20states"
              },
              {
                "name": "France",
                "url": "https://archerliquors.com/shop/?type=spirits&country=france"
              },
              {
                "name": "Ireland",
                "url": "https://archerliquors.com/shop/?type=spirits&country=ireland"
              },
              {
                "name": "Japan",
                "url": "https://archerliquors.com/shop/?type=spirits&country=japan"
              },
              {
                "name": "Italy",
                "url": "https://archerliquors.com/shop/?type=spirits&country=italy"
              },
              {
                "name": "Mexico",
                "url": "https://archerliquors.com/shop/?type=spirits&country=mexico"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://archerliquors.com/shop/?category=spirits_new_arrivals&title=Spirits%20New%20Arrivals"
              },
              {
                "name": "Staff Picks",
                "url": "https://archerliquors.com/shop/?category=spirits_staff_picks&title=Spirits%20Staff%20Picks"
              },
              {
                "name": "On Sale",
                "url": "https://archerliquors.com/shop/?category=spirits_on_sale&title=Spirits%20On%20Sale"
              },
              {
                "name": "All Spirits",
                "url": "https://archerliquors.com/shop/?type=spirits"
              },
              {
                "name": "Spirits Brands",
                "url": "https://archerliquors.com/shop/?container-id=66e029eae1ecd0293828ce48&title=Spirits+Brands"
              },
              {
                "name": "Gift Sets",
                "url": "https://archerliquors.com/product-groups/gift-sets"
              }
            ]
          }
        ]
      },
      {
        "name": "Beer",
        "id": 5,
        "url": "https://archerliquors.com/pages/shop-beer",
        "subcategories": [
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "Oktoberfest",
                "url": "https://archerliquors.com/product-groups/oktoberfest"
              },
              {
                "name": "IPA",
                "url": "https://archerliquors.com/shop/?category=ipa_basic_category&title=IPA"
              },
              {
                "name": "Hazy IPAs",
                "url": "https://archerliquors.com/product-group?product-group-id=651712594aa6072ca173eaa4"
              },
              {
                "name": "Hard Seltzer",
                "url": "https://archerliquors.com/shop/?category=seltzer_basic_category&title=Hard%20Seltzer"
              },
              {
                "name": "Ale",
                "url": "https://archerliquors.com/shop/?category=ale_beer&title=ale"
              },
              {
                "name": "Lager",
                "url": "https://archerliquors.com/shop/?category=lager_beer&title=lager"
              },
              {
                "name": "Pilsner",
                "url": "https://archerliquors.com/shop/?category=pilsner_basic_category&title=pilsner"
              },
              {
                "name": "Stout",
                "url": "https://archerliquors.com/shop/?category=stout_beer&title=stout"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "the Fresh Report",
                "url": "https://archerliquors.com/product-groups/the-fresh-report"
              },
              {
                "name": "Local Craft",
                "url": "https://archerliquors.com/product-groups/local-craft-beers"
              },
              {
                "name": "All Beer",
                "url": "https://archerliquors.com/shop/?type=beer"
              },
              {
                "name": "Staff Picks",
                "url": "https://archerliquors.com/shop/?category=beer_staff_picks&title=Beer%20Staff%20Picks"
              },
              {
                "name": "On Sale",
                "url": "https://archerliquors.com/shop/?category=beer_on_sale&title=Beer%20On%20Sale"
              },
              {
                "name": "Kegs",
                "url": "https://archerliquors.com/product-groups/kegs-available"
              }
            ]
          }
        ]
      },
      {
        "name": "Staff Picks",
        "id": 6,
        "url": "https://archerliquors.com/shop/?category=our_staff_picks&title=Staff%20Picks",
        "subcategories": []
      },
      {
        "name": "Explore",
        "id": 7,
        "url": "https://archerliquors.com/#",
        "subcategories": [
          {
            "name": "Store Info",
            "url": "",
            "subcategories": [
              {
                "name": "Location & Hours",
                "url": "https://archerliquors.com/info"
              },
              {
                "name": "Notifications",
                "url": "https://archerliquors.com/notifications"
              }
            ]
          },
          {
            "name": "My Account",
            "url": "",
            "subcategories": [
              {
                "name": "Order History",
                "url": "https://archerliquors.com/order-history"
              }
            ]
          },
          {
            "name": "More",
            "url": "",
            "subcategories": [
              {
                "name": "Drink Calculator",
                "url": "https://archerliquors.com/drink-calculator"
              },
              {
                "name": "Homebrewing",
                "url": "https://archerliquors.com/product-group?product-group-id=651c14a42d0c732b8eb5508a"
              },
              {
                "name": "Staff Picks",
                "url": "https://archerliquors.com/shop/?category=our_staff_picks&title=Staff%20Picks"
              },
              {
                "name": "Gift Cards",
                "url": "https://archerliquors.com/buy-gift-cards"
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


