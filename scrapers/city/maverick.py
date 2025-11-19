import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from scrapers.city.hive import HiveScraper

"""
	Maverick
	Type: Standard shop website
	Method: 
		Get Categories: Scape Navigation
		Get Products: Scape Product List
		Get Product Manual Scrape and json data from html
	Issues:

"""

class MaverickBeverageScraper(HiveScraper):
	CRM_ID = 3510
	CRM_NOTE_ID = 1667
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = 'Ready'

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/maverick_beverages/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = 'https://shop.maverickbevil.com/'
	VENDOR_NAME = 'Maverick'
	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "name": "Wine",
        "id": 2,
        "url": "https://shop.maverickbevil.com/shop/?type=Wine",
        "subcategories": [
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "In Stock",
                "url": "https://shop.maverickbevil.com/shop/product-groups/in-stock-wine"
              },
              {
                "name": "Biodynamic",
                "url": "https://shop.maverickbevil.com/shop/product-groups/biodynamic"
              },
              {
                "name": "Organic",
                "url": "https://shop.maverickbevil.com/shop/product-groups/organic"
              },
              {
                "name": "Kosher",
                "url": "https://shop.maverickbevil.com/shop/product-groups/kosher"
              },
              {
                "name": "Cans",
                "url": "https://shop.maverickbevil.com/shop?ch-query=%27cans%27&order=name+asc"
              },
              {
                "name": "New Arrivals!",
                "url": "https://shop.maverickbevil.com/shop/product-groups/new-arrivals?order=name+asc&type=Wine"
              }
            ]
          },
          {
            "name": "By Importer",
            "url": "",
            "subcategories": [
              {
                "name": "Dreyfus, Ashby, & Co.",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine&supplier=DREYFUS+ASHBY+INC"
              },
              {
                "name": "Kermit Lynch",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine&supplier=KERMIT+LYNCH+WINE+MERCHANT"
              },
              {
                "name": "Louis/Dressner Selections",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine&supplier=LOUIS+DRESSNER+SELECTIONS"
              },
              {
                "name": "Michael Corso Selections",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine&supplier=MICHAEL+CORSO+SELECTIONS"
              },
              {
                "name": "Skurnik Wines & Spirits",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine&supplier=MICHAEL+SKURNIK+WINES+INC"
              },
              {
                "name": "Vias Imports",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine&supplier=VIAS+IMPORTS+LTD"
              }
            ]
          },
          {
            "name": "By Style",
            "url": "",
            "subcategories": [
              {
                "name": "Red",
                "url": "https://shop.maverickbevil.com/shop/?subtype=red"
              },
              {
                "name": "White",
                "url": "https://shop.maverickbevil.com/shop/?subtype=white"
              },
              {
                "name": "Ros\u00e9",
                "url": "https://shop.maverickbevil.com/shop/?subtype=rose"
              },
              {
                "name": "Sparkling",
                "url": "https://shop.maverickbevil.com/shop/?subtype=sparkling"
              },
              {
                "name": "Fortified",
                "url": "https://shop.maverickbevil.com/shop/?subtype=fortified"
              },
              {
                "name": "Non-alcoholic",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine&subtype=Non+Alcoholic"
              }
            ]
          },
          {
            "name": "By Region",
            "url": "",
            "subcategories": [
              {
                "name": "Beaujolais",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine®ion=Beaujolais"
              },
              {
                "name": "Burgundy",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine®ion=Burgundy"
              },
              {
                "name": "Bordeaux",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine®ion=Bordeaux"
              },
              {
                "name": "Champagne",
                "url": "https://shop.maverickbevil.com/shop/?region=Champagne&type=Wine"
              },
              {
                "name": "Mosel",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine®ion=Mosel"
              },
              {
                "name": "Napa Valley",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine®ion=Napa+Valley"
              }
            ]
          },
          {
            "name": "By Region Cont'd",
            "url": "",
            "subcategories": [
              {
                "name": "Piedmont",
                "url": "https://shop.maverickbevil.com/shop/?country=Italy®ion=Piedmont&type=Wine"
              },
              {
                "name": "Tuscany",
                "url": "https://shop.maverickbevil.com/shop/?type=wine®ion=tuscany"
              },
              {
                "name": "Rhone Valley",
                "url": "https://shop.maverickbevil.com/shop/?region=Rhone&type=Wine"
              },
              {
                "name": "Rioja",
                "url": "https://shop.maverickbevil.com/shop/?type=wine®ion=rioja"
              },
              {
                "name": "Willamette Valley",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine®ion=Willamette+Valley"
              },
              {
                "name": "Sicily",
                "url": "https://shop.maverickbevil.com/shop/?region=Sicily&type=Wine"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "United States",
                "url": "https://shop.maverickbevil.com/shop/?type=Wine&country=United+States"
              },
              {
                "name": "France",
                "url": "https://shop.maverickbevil.com/shop/?type=wine&country=france"
              },
              {
                "name": "Italy",
                "url": "https://shop.maverickbevil.com/shop/?type=wine&country=italy"
              },
              {
                "name": "Spain",
                "url": "https://shop.maverickbevil.com/shop/?type=wine&country=spain"
              },
              {
                "name": "Germany",
                "url": "https://shop.maverickbevil.com/shop/?type=wine&country=germany"
              },
              {
                "name": "Argentina",
                "url": "https://shop.maverickbevil.com/shop/?type=wine&country=argentina"
              }
            ]
          }
        ]
      },
      {
        "name": "Spirits",
        "id": 3,
        "url": "https://shop.maverickbevil.com/shop/product-groups/spirits",
        "subcategories": [
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "In-Stock",
                "url": "https://shop.maverickbevil.com/shop/product-groups/in-stock-spirits"
              },
              {
                "name": "750ml",
                "url": "https://shop.maverickbevil.com/shop/?category=all_explore&size=750ml&type=Spirits"
              },
              {
                "name": "1L",
                "url": "https://shop.maverickbevil.com/shop/?category=all_explore&size=1l&type=Spirits"
              },
              {
                "name": "New Arrivals!",
                "url": "https://shop.maverickbevil.com/shop/product-groups/new-arrivals?order=name+asc&type=Spirits"
              }
            ]
          },
          {
            "name": "By Importer",
            "url": "",
            "subcategories": [
              {
                "name": "De Maison Selections",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?supplier=DE+MAISON+SELECTIONS"
              },
              {
                "name": "Heavy Metl Imports",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?supplier=HEAVY+METL+PREMIUM+IMPORTS+LLC"
              },
              {
                "name": "Skurnik Wines & Spirits",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?supplier=MICHAEL+SKURNIK+WINES+INC"
              },
              {
                "name": "Spiribam",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?supplier=Park+Street+Imports+%2F+Spiribam"
              },
              {
                "name": "Tempus Fugit Spirits",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?supplier=PARK+ST+IMPORTS+-+TEMPUS+FUGIT+SPIRITS"
              }
            ]
          },
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "Mezcal",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?subtype=Mezcal"
              },
              {
                "name": "Liqueur",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?subtype=Liqueur"
              },
              {
                "name": "Brandy",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?subtype=Brandy"
              },
              {
                "name": "Vermouth",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?subtype=Vermouth"
              },
              {
                "name": "Rum",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?subtype=Rum"
              }
            ]
          },
          {
            "name": "By Type Cont'd",
            "url": "",
            "subcategories": [
              {
                "name": "Tequila",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?subtype=Tequila"
              },
              {
                "name": "Whiskey",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?subtype=Whiskey"
              },
              {
                "name": "Gin",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?subtype=Gin"
              },
              {
                "name": "Bitters",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?subtype=Bitters"
              },
              {
                "name": "Vodka",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?subtype=Vodka"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "Mexico",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?country=Mexico"
              },
              {
                "name": "United States",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?country=United+States"
              },
              {
                "name": "France",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?country=France"
              },
              {
                "name": "Italy",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?country=Italy"
              },
              {
                "name": "Spain",
                "url": "https://shop.maverickbevil.com/shop/product-groups/spirits?country=Spain"
              }
            ]
          }
        ]
      },
      {
        "name": "Sak\u00e9",
        "id": 4,
        "url": "https://shop.maverickbevil.com/shop/?category=all_explore&subtype=Sake",
        "subcategories": [
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "All Sak\u00e9",
                "url": "https://shop.maverickbevil.com/shop/?category=all_explore&subtype=Sake"
              },
              {
                "name": "720ml",
                "url": "https://shop.maverickbevil.com/shop/?category=all_explore&size=720ml&type=Spirits&subtype=Sake"
              },
              {
                "name": "300ml",
                "url": "https://shop.maverickbevil.com/shop/?category=all_explore&size=300ml&type=Spirits&subtype=Sake"
              },
              {
                "name": "Cans",
                "url": "https://shop.maverickbevil.com/shop/?category=all_explore&size=180ml&type=Spirits&subtype=Sake"
              }
            ]
          },
          {
            "name": "By Style",
            "url": "",
            "subcategories": [
              {
                "name": "Junmai Ginjo",
                "url": "https://shop.maverickbevil.com/shop?ch-query=junmai%20ginjo"
              },
              {
                "name": "Junmai Daiginjo",
                "url": "https://shop.maverickbevil.com/shop?ch-query=junmai%20daiginjo"
              },
              {
                "name": "Tokubetsu Junmai",
                "url": "https://shop.maverickbevil.com/shop?ch-query=tokubetsu%20junmai"
              },
              {
                "name": "Honjozo",
                "url": "https://shop.maverickbevil.com/shop?ch-query=honjozo"
              },
              {
                "name": "Nigori",
                "url": "https://shop.maverickbevil.com/shop?ch-query=nigori"
              }
            ]
          }
        ]
      },
      {
        "name": "Cider",
        "id": 5,
        "url": "https://shop.maverickbevil.com/shop/?subtype=Cider&order=name+asc",
        "subcategories": [
        {
	        "name": "Cider",
	        "id": 5,
	        "url": "https://shop.maverickbevil.com/shop/?subtype=Cider&order=name+asc",
	        "subcategories": []
	      }
	      ]
      },
      {
        "name": "No/Low Alc",
        "id": 6,
        "url": "https://shop.maverickbevil.com/shop?group-id=645cf8fa3aa1582dd265fc6f&title=No/low%20Alc",
        "subcategories": [
          {
            "name": "No/Low Alc",
            "url": "",
            "subcategories": [
              {
                "name": "Non-Alcoholic Wine",
                "url": "https://shop.maverickbevil.com/shop?ch-query=non-alcoholic&type=Wine"
              },
              {
                "name": "Non-Alcoholic Mixers",
                "url": "https://shop.maverickbevil.com/shop?ch-query=non-alcoholic&subtype=Mixers"
              },
              {
                "name": "Non-Alcoholic Spirits",
                "url": "https://shop.maverickbevil.com/shop?type=Spirits&subtype=Non+Alcoholic"
              },
              {
                "name": "Low Alcohol",
                "url": "https://shop.maverickbevil.com/shop?group-id=645cf8b5c903542aad913f88&title=Low%20Alc"
              }
            ]
          }
        ]
      },
      {
        "name": "Events",
        "id": 7,
        "url": "https://shop.maverickbevil.com/pages/upcoming-events",
        "subcategories": []
      },
      {
        "name": "Bill Pay, Invoices, & Orders",
        "id": 8,
        "url": "https://shop.maverickbevil.com/profile?section=payments&sub_section=invoices&Status=Open&sortParams=invoice_due_date+asc",
        "subcategories": [
          {
            "name": "ORDER HISTORY",
            "url": "",
            "subcategories": [
              {
                "name": "Past Orders",
                "url": "https://shop.maverickbevil.com/profile?section=order_history"
              },
              {
                "name": "Past Purchases",
                "url": "https://shop.maverickbevil.com/shop/?category=all_explore&category=all_explore&customer_purchased_products=true"
              }
            ]
          },
          {
            "name": "BILL PAY",
            "url": "",
            "subcategories": [
              {
                "name": "View & Pay Invoices",
                "url": "https://shop.maverickbevil.com/profile?section=payments&sub_section=invoices&Status=Open&sortParams=invoice_due_date+asc"
              },
              {
                "name": "Add Bank Account",
                "url": "https://shop.maverickbevil.com/profile?section=payments&sub_section=banking"
              },
              {
                "name": "View Payments",
                "url": "https://shop.maverickbevil.com/profile?section=payments&sub_section=payments+"
              }
            ]
          },
          {
            "name": "USER GUIDES",
            "url": "",
            "subcategories": [
              {
                "name": "How To - Pay Invoices",
                "url": "https://shop.maverickbevil.com/pages/bill-pay-guide"
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

	def get_distributor_specific(self, row_spec):
		"""
		Extract distributor-specific data for Maverick Beverage products.

		Args:
			row_spec (dict): Dictionary containing product data

		Returns:
			dict: Updated row_spec with distributor-specific fields
		"""
		try:
			# Get the product data from the row_spec
			data = row_spec.get('extra_data_2', {})
			if not data:
				return row_spec

			# Extract SKU - check multiple possible locations
			sku = None

			# First check the additional_properties at the root level
			if 'additional_properties' in data and 'SKU' in data['additional_properties']:
				sku = data['additional_properties']['SKU']
			# Then check within the first merchant's additional_properties
			elif 'merchants' in data and len(data['merchants']) > 0:
				merchant = data['merchants'][0]
				if 'additional_properties' in merchant and 'SKU' in merchant['additional_properties']:
					sku = merchant['additional_properties']['SKU']
				# Check within the product options if not found in merchant's additional_properties
				elif 'product_options' in merchant and len(merchant['product_options']) > 0:
					for option in merchant['product_options']:
						if 'additional_properties' in option and 'sku' in option['additional_properties']:
							sku = option['additional_properties']['sku']
							break

			# Update the row_spec with the found SKU
			if sku:
				row_spec['sku'] = sku
				print(f"Found SKU: {sku}")
			else:
				print("No SKU found in product data")

			return row_spec

		except Exception as e:
			print(f"Error in get_distributor_specific: {str(e)}")
			import traceback
			traceback.print_exc()
			return row_spec


