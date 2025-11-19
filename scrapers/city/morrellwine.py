import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from scrapers.city.hive import HiveScraper

"""
	Morrell Wine
	Type: Standard shop website
	Method: 
		Get Categories: Scape Navigation
		Get Products: Scape Product List
		Get Product Manual Scrape and json data from html
	Issues:
		The embedded json data does not have all the information needed to create a product. Data like 
		sku and description are not included in the json data.
"""

class MorrellWineScraper(HiveScraper):
	# 3207/edit_note/1546/
	CRM_ID = 3207
	CRM_NOTE_ID = 1546
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/morrell/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = 'https://morrellwine.com/'
	VENDOR_NAME = 'Morrell Wine'
	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "name": "Wines",
        "id": 1,
        "url": "https://morrellwine.com/pages/shop-wine",
        "subcategories": [
          {
            "name": "By Style",
            "url": "",
            "subcategories": [
              {
                "name": "Champagne / Sparkling",
                "url": "https://morrellwine.com/shop/?subtype=sparkling"
              },
              {
                "name": "White",
                "url": "https://morrellwine.com/shop/?subtype=white"
              },
              {
                "name": "Red",
                "url": "https://morrellwine.com/shop/?subtype=red"
              },
              {
                "name": "Port",
                "url": "https://morrellwine.com/shop/?subtype=port"
              },
              {
                "name": "Dessert",
                "url": "https://morrellwine.com/shop/?subtype=dessert"
              },
              {
                "name": "Rose / Blush",
                "url": "https://morrellwine.com/shop/?subtype=rose"
              }
            ]
          },
          {
            "name": "By Varietal",
            "url": "",
            "subcategories": [
              {
                "name": "Cabernet Sauvignon",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=cabernet+sauvignon"
              },
              {
                "name": "Pinot Noir",
                "url": "https://morrellwine.com/shop/?category=pinot_noir_name&title=Pinot%20Noir"
              },
              {
                "name": "Syrah",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=syrah"
              },
              {
                "name": "Bordeaux Blends",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=bordeaux+blends"
              },
              {
                "name": "Red Blends",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=red+blend"
              },
              {
                "name": "Merlot",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=merlot"
              },
              {
                "name": "Grenache",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=grenache"
              },
              {
                "name": "Tempranillo",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=tempranillo"
              },
              {
                "name": "Chardonnay",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=chardonnay"
              },
              {
                "name": "Sauvignon Blanc",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=sauvignon+blanc"
              },
              {
                "name": "Pinot Grigio",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=pinot+grigio"
              },
              {
                "name": "Riesling",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=riesling"
              },
              {
                "name": "Rose",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=rose"
              },
              {
                "name": "Petite Sirah",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=petite+sirah"
              },
              {
                "name": "Shiraz",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=shiraz"
              },
              {
                "name": "Zinfandel",
                "url": "https://morrellwine.com/shop/?type=wine&varietal=zinfandel"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "Argentina",
                "url": "https://morrellwine.com/shop/?type=wine&country=argentina"
              },
              {
                "name": "Australia",
                "url": "https://morrellwine.com/shop/?type=wine&country=australia"
              },
              {
                "name": "Chile",
                "url": "https://morrellwine.com/shop/?type=wine&country=chile"
              },
              {
                "name": "France",
                "url": "https://morrellwine.com/shop/?type=wine&country=france"
              },
              {
                "name": "Germany",
                "url": "https://morrellwine.com/shop/?type=wine&country=germany"
              },
              {
                "name": "Italy",
                "url": "https://morrellwine.com/shop/?type=wine&country=italy"
              },
              {
                "name": "Israel",
                "url": "https://morrellwine.com/shop/?type=wine&country=israel"
              },
              {
                "name": "Mexico",
                "url": "https://morrellwine.com/shop/?type=wine&country=mexico"
              },
              {
                "name": "New Zealand",
                "url": "https://morrellwine.com/shop/?type=wine&country=new%20zealand"
              },
              {
                "name": "Portugal",
                "url": "https://morrellwine.com/shop/?type=wine&country=portugal"
              },
              {
                "name": "South Africa",
                "url": "https://morrellwine.com/shop/?type=wine&country=south+africa"
              },
              {
                "name": "Spain",
                "url": "https://morrellwine.com/shop/?type=wine&country=spain"
              },
              {
                "name": "United States",
                "url": "https://morrellwine.com/shop/?type=wine&country=united%20states"
              }
            ]
          },
          {
            "name": "By Region",
            "url": "",
            "subcategories": [
              {
                "name": "Bordeaux",
                "url": "https://morrellwine.com/shop/?type=wine®ion=bordeaux"
              },
              {
                "name": "Burgundy",
                "url": "https://morrellwine.com/shop/?type=wine®ion=burgundy"
              },
              {
                "name": "Napa Valley",
                "url": "https://morrellwine.com/shop/?type=wine®ion=napa+valley"
              },
              {
                "name": "Champagne",
                "url": "https://morrellwine.com/shop/?type=wine®ion=champagne"
              },
              {
                "name": "Tuscany",
                "url": "https://morrellwine.com/shop/?type=wine®ion=tuscany"
              },
              {
                "name": "Piedmont",
                "url": "https://morrellwine.com/shop/?type=wine®ion=piedmont"
              },
              {
                "name": "Sicily",
                "url": "https://morrellwine.com/shop/?type=wine®ion=sicily"
              },
              {
                "name": "Alsace",
                "url": "https://morrellwine.com/shop/?type=wine®ion=alsace"
              },
              {
                "name": "Loire Valley",
                "url": "https://morrellwine.com/shop/?type=wine®ion=loire+valley"
              },
              {
                "name": "Marlborough",
                "url": "https://morrellwine.com/shop/?type=wine®ion=marlborough"
              },
              {
                "name": "Mendoza",
                "url": "https://morrellwine.com/shop/?type=wine®ion=mendoza"
              },
              {
                "name": "Rioja",
                "url": "https://morrellwine.com/shop/?type=wine®ion=rioja"
              },
              {
                "name": "Sonoma Valley",
                "url": "https://morrellwine.com/shop/?type=wine®ion=sonoma+valley"
              },
              {
                "name": "Trentino-Alto Adige",
                "url": "https://morrellwine.com/shop/?type=wine®ion=trentino+alto+adige"
              },
              {
                "name": "Columbia Valley",
                "url": "https://morrellwine.com/shop/?type=wine®ion=columbia+valley"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "All Wine",
                "url": "https://morrellwine.com/shop/?type=wine"
              },
              {
                "name": "Ready To Drink Wines",
                "url": "https://morrellwine.com/shop/product-groups/ready-to-drink-wines"
              },
              {
                "name": "New Arrivals",
                "url": "https://morrellwine.com/shop/?category=wine_new_arrivals&title=Wine%20New%20Arrivals"
              },
              {
                "name": "On Sale",
                "url": "https://morrellwine.com/shop/?category=wine_on_sale&title=Wine%20On%20Sale"
              }
            ]
          }
        ]
      },
      {
        "name": "Spirits",
        "id": 2,
        "url": "https://morrellwine.com/pages/shop-spirits",
        "subcategories": [
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "Bourbon",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=bourbon"
              },
              {
                "name": "Brandy",
                "url": "https://morrellwine.com/shop/?subtype=brandy"
              },
              {
                "name": "Cognac",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=cognac"
              },
              {
                "name": "Cocktail",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=cocktail"
              },
              {
                "name": "Gin",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=gin"
              },
              {
                "name": "Liqueur",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=liqueur"
              },
              {
                "name": "Mezcal",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=mezcal"
              },
              {
                "name": "Other Liquors",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=other+liquors"
              },
              {
                "name": "Rum",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=rum"
              },
              {
                "name": "Rye Whiskey",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=rye"
              },
              {
                "name": "Single Malt",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=single%20malt"
              },
              {
                "name": "Scotch",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=scotch"
              },
              {
                "name": "Soju",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=soju"
              },
              {
                "name": "Tequila",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=tequila"
              },
              {
                "name": "Vermouth",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=vermouth"
              },
              {
                "name": "Vodka",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=vodka"
              },
              {
                "name": "Whiskey",
                "url": "https://morrellwine.com/shop/?type=spirits&subtype=whiskey"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "Australia",
                "url": "https://morrellwine.com/shop/?type=spirits&country=australia"
              },
              {
                "name": "Canada",
                "url": "https://morrellwine.com/shop/?type=spirits&country=canada"
              },
              {
                "name": "England",
                "url": "https://morrellwine.com/shop/?type=spirits&country=england"
              },
              {
                "name": "France",
                "url": "https://morrellwine.com/shop/?type=spirits&country=france"
              },
              {
                "name": "Ireland",
                "url": "https://morrellwine.com/shop/?type=spirits&country=ireland"
              },
              {
                "name": "Italy",
                "url": "https://morrellwine.com/shop/?type=spirits&country=italy"
              },
              {
                "name": "Japan",
                "url": "https://morrellwine.com/shop/?type=spirits&country=japan"
              },
              {
                "name": "Mexico",
                "url": "https://morrellwine.com/shop/?type=spirits&country=mexico"
              },
              {
                "name": "Netherlands",
                "url": "https://morrellwine.com/shop/?type=spirits&country=netherlands"
              },
              {
                "name": "Poland",
                "url": "https://morrellwine.com/shop/?type=spirits&country=poland"
              },
              {
                "name": "Russia",
                "url": "https://morrellwine.com/shop/?type=spirits&country=russia"
              },
              {
                "name": "Scotland",
                "url": "https://morrellwine.com/shop/?type=spirits&country=scotland"
              },
              {
                "name": "United Kingdom",
                "url": "https://morrellwine.com/shop/?type=spirits&country=united+kingdom"
              },
              {
                "name": "United States",
                "url": "https://morrellwine.com/shop/?type=spirits&country=united+states"
              }
            ]
          },
          {
            "name": "By State",
            "url": "",
            "subcategories": [
              {
                "name": "California",
                "url": "https://morrellwine.com/shop/?type=spirits&state=california"
              },
              {
                "name": "Connecticut",
                "url": "https://morrellwine.com/shop/?type=spirits&state=connecticut"
              },
              {
                "name": "Florida",
                "url": "https://morrellwine.com/shop/?type=spirits&state=florida"
              },
              {
                "name": "Illinois",
                "url": "https://morrellwine.com/shop/?type=spirits&state=illinois"
              },
              {
                "name": "Indiana",
                "url": "https://morrellwine.com/shop/?type=spirits&state=indiana"
              },
              {
                "name": "Kentucky",
                "url": "https://morrellwine.com/shop/?type=spirits&state=kentucky"
              },
              {
                "name": "Maine",
                "url": "https://morrellwine.com/shop/?type=spirits&state=maine"
              },
              {
                "name": "Maryland",
                "url": "https://morrellwine.com/shop/?type=spirits&state=maryland"
              },
              {
                "name": "Minnesota",
                "url": "https://morrellwine.com/shop/?type=spirits&state=minnesota"
              },
              {
                "name": "Missouri",
                "url": "https://morrellwine.com/shop/?type=spirits&state=missouri"
              },
              {
                "name": "New Jersey",
                "url": "https://morrellwine.com/shop/?type=spirits&state=new+jersey"
              },
              {
                "name": "New York",
                "url": "https://morrellwine.com/shop/?type=spirits&state=new+york"
              },
              {
                "name": "Oregon",
                "url": "https://morrellwine.com/shop/?type=spirits&state=Oregon"
              },
              {
                "name": "Pennsylvania",
                "url": "https://morrellwine.com/shop/?type=spirits&state=pennsylvania"
              },
              {
                "name": "Tennessee",
                "url": "https://morrellwine.com/shop/?type=spirits&state=tennessee"
              },
              {
                "name": "Texas",
                "url": "https://morrellwine.com/shop/?type=spirits&state=texas"
              },
              {
                "name": "Vermont",
                "url": "https://morrellwine.com/shop/?type=spirits&state=vermont"
              },
              {
                "name": "Virginia",
                "url": "https://morrellwine.com/shop/?type=spirits&state=virginia"
              },
              {
                "name": "Washington",
                "url": "https://morrellwine.com/shop/?type=spirits&state=washington"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://morrellwine.com/shop/?category=spirits_new_arrivals&title=Spirits%20New%20Arrivals"
              },
              {
                "name": "On Sale",
                "url": "https://morrellwine.com/shop/?category=spirits_on_sale&title=Spirits%20On%20Sale"
              },
              {
                "name": "All Spirits",
                "url": "https://morrellwine.com/shop/?type=spirits"
              }
            ]
          }
        ]
      },
      {
        "name": "Tasting & Events",
        "id": 3,
        "url": "https://morrellwine.com/events",
        "subcategories": []
      },
      {
        "name": "Explore",
        "id": 4,
        "url": "https://morrellwine.com/#",
        "subcategories": [
          {
            "name": "Store Info",
            "url": "",
            "subcategories": [
              {
                "name": "Location & Hours",
                "url": "https://morrellwine.com/info"
              },
              {
                "name": "Notifications",
                "url": "https://morrellwine.com/notifications"
              }
            ]
          }
        ]
      },
      {
        "name": "My Account",
        "id": 5,
        "url": "https://morrellwine.com/profile?section=order_history",
        "subcategories": []
      },
      {
        "name": "Vintage Wine Warehouse Storage",
        "id": 6,
        "url": "https://vintagewinewarehouse.com/",
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


