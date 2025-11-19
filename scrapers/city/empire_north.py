import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from scrapers.city.hive import HiveScraper

"""
	Empire 360
	Type: Standard shop website
	Method: 
		Get Categories: Scape Navigation
		Get Products: Scape Product List
		Get Product Manual Scrape and json data from html
	Issues:
		The embedded json data does not have all the information needed to create a product. Data like 
		sku and description are not included in the json data.
"""

class EmpireNorthScraper(HiveScraper):
	# /1240/edit_note/1711/
	CRM_ID = 1240
	CRM_NOTE_ID = 1711
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/empire_north/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = 'https://empire360.com'
	VENDOR_NAME = 'Empire North'
	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "name": "Wine",
        "id": 2,
        "url": "https://empire360.com/shop/?type=Wine",
        "subcategories": [
          {
            "name": "By Style",
            "url": "",
            "subcategories": [
              {
                "name": "Red",
                "url": "https://empire360.com/shop/?subtype=red"
              },
              {
                "name": "White",
                "url": "https://empire360.com/shop/?subtype=white"
              },
              {
                "name": "Ros\u00e9 & Blush",
                "url": "https://empire360.com/shop/?subtype=rose"
              },
              {
                "name": "Champagne & Sparkling",
                "url": "https://empire360.com/shop/?subtype=sparkling"
              },
              {
                "name": "Dessert & Port",
                "url": "https://empire360.com/shop/?subtype=dessert&subtype=port"
              },
              {
                "name": "Other Wines",
                "url": "https://empire360.com/shop/?category=other_wine&title=Other+Wine"
              }
            ]
          },
          {
            "name": "By Varietal",
            "url": "",
            "subcategories": [
              {
                "name": "Cabernet Sauvignon",
                "url": "https://empire360.com/shop/?category=cabernet_sauvignon_name&title=Cabernet%20Sauvignon"
              },
              {
                "name": "Chardonnay",
                "url": "https://empire360.com/shop/?category=chardonnay_name&title=Chardonnay"
              },
              {
                "name": "Sauvignon Blanc",
                "url": "https://empire360.com/shop/?category=sauvignon_blanc_name&title=Sauvignon%20Blanc"
              },
              {
                "name": "Red Blends",
                "url": "https://empire360.com/shop/?varietal=red+blend"
              },
              {
                "name": "Pinot Noir",
                "url": "https://empire360.com/shop/?category=pinot_noir_name&title=Pinot%20Noir"
              },
              {
                "name": "Pinot Grigio",
                "url": "https://empire360.com/shop/?category=pinot_grigio_name&title=Pinot%20Grigio"
              },
              {
                "name": "Rose",
                "url": "https://empire360.com/shop/?varietal=rose"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "France",
                "url": "https://empire360.com/shop/?type=wine&country=france"
              },
              {
                "name": "Italy",
                "url": "https://empire360.com/shop/?type=wine&country=italy"
              },
              {
                "name": "Spain",
                "url": "https://empire360.com/shop/?type=wine&country=spain"
              },
              {
                "name": "Germany",
                "url": "https://empire360.com/shop/?type=wine&country=germany"
              },
              {
                "name": "Argentina",
                "url": "https://empire360.com/shop/?type=wine&country=argentina"
              },
              {
                "name": "United States",
                "url": "https://empire360.com/shop/?type=wine&country=united%20states"
              },
              {
                "name": "New Zealand",
                "url": "https://empire360.com/shop/?type=wine&country=new%20zealand"
              }
            ]
          },
          {
            "name": "By Region",
            "url": "",
            "subcategories": [
              {
                "name": "Bordeaux",
                "url": "https://empire360.com/shop/?type=wine®ion=bordeaux"
              },
              {
                "name": "Tuscany",
                "url": "https://empire360.com/shop/?type=wine®ion=tuscany"
              },
              {
                "name": "Rioja",
                "url": "https://empire360.com/shop/?type=wine®ion=rioja"
              },
              {
                "name": "Burgundy",
                "url": "https://empire360.com/shop/?type=wine®ion=burgundy"
              },
              {
                "name": "Napa Valley",
                "url": "https://empire360.com/shop/?type=wine®ion=napa%20valley"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://empire360.com/shop?group-id=62c447583deac5258b3f9c3d&title=New+Arrivals&type=Wine"
              },
              {
                "name": "Wine Combo Packs",
                "url": "https://empire360.com/shop/product-groups/wine-combo-packs"
              },
              {
                "name": "Cans",
                "url": "https://empire360.com/shop/product-groups/cans?type=Wine"
              },
              {
                "name": "Kegs",
                "url": "https://empire360.com/shop/product-groups/kegs"
              },
              {
                "name": "Farm License Wines",
                "url": "https://empire360.com/shop?ch-query=ny+made&type=Wine"
              },
              {
                "name": "Wine-Only License Products",
                "url": "https://empire360.com/shop/product-groups/wine-only-license-products"
              },
              {
                "name": "My Past Purchased Wine",
                "url": "https://empire360.com/shop/?type=Wine&customer_purchased_products=true"
              },
              {
                "name": "All Wine",
                "url": "https://empire360.com/shop/?type=wine"
              }
            ]
          }
        ]
      },
      {
        "name": "Spirits",
        "id": 3,
        "url": "https://empire360.com/shop/?type=Spirits",
        "subcategories": [
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "Vodka",
                "url": "https://empire360.com/shop/?subtype=vodka"
              },
              {
                "name": "Whiskey",
                "url": "https://empire360.com/shop/?subtype=whiskey"
              },
              {
                "name": "Sake",
                "url": "https://empire360.com/shop/?subtype=sake"
              },
              {
                "name": "Tequila",
                "url": "https://empire360.com/shop/?subtype=tequila"
              },
              {
                "name": "Rum",
                "url": "https://empire360.com/shop/?subtype=rum"
              },
              {
                "name": "Gin",
                "url": "https://empire360.com/shop/?subtype=gin"
              },
              {
                "name": "Brandy",
                "url": "https://empire360.com/shop/?subtype=brandy"
              },
              {
                "name": "Liqueur",
                "url": "https://empire360.com/shop/?subtype=liqueur"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "United States",
                "url": "https://empire360.com/shop/?type=spirits&country=united%20states"
              },
              {
                "name": "France",
                "url": "https://empire360.com/shop/?type=spirits&country=france"
              },
              {
                "name": "Ireland",
                "url": "https://empire360.com/shop/?type=spirits&country=ireland"
              },
              {
                "name": "Japan",
                "url": "https://empire360.com/shop/?type=spirits&country=japan"
              },
              {
                "name": "Italy",
                "url": "https://empire360.com/shop/?type=spirits&country=italy"
              },
              {
                "name": "Mexico",
                "url": "https://empire360.com/shop/?type=spirits&country=mexico"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://empire360.com/shop?group-id=62c447583deac5258b3f9c3d&title=New+Arrivals&type=Spirits"
              },
              {
                "name": "Staff Picks",
                "url": "https://empire360.com/shop/?category=spirits_staff_picks&title=Spirits%20Staff%20Picks"
              },
              {
                "name": "Spirits Combo Packs",
                "url": "https://empire360.com/shop/product-groups/spirits-combo-packs"
              },
              {
                "name": "Cans",
                "url": "https://empire360.com/shop/product-groups/cans?type=Spirits"
              },
              {
                "name": "Farm License Spirits",
                "url": "https://empire360.com/shop?ch-query=ny+made&type=Spirits"
              },
              {
                "name": "My Past Purchased Spirits",
                "url": "https://empire360.com/shop/?type=Spirits&customer_purchased_products=true"
              },
              {
                "name": "All Spirits",
                "url": "https://empire360.com/shop/?type=spirits"
              }
            ]
          }
        ]
      },
      {
        "name": "Shop By Brand",
        "id": 4,
        "url": "https://empire360.com/shop/?container-id=6194f35920459128ccff17cd&title=Shop+By+Brand",
        "subcategories": [
          {
            "name": "Shop Divisions",
            "url": "",
            "subcategories": [
              {
                "name": "Shop Freedom",
                "url": "https://empire360.com/pages/mhusa-north"
              }
            ]
          }
        ]
      },
      {
        "name": "Payments, Invoices & Orders",
        "id": 5,
        "url": "https://empire360.com/profile?section=payments&sub_section=invoices&Status=Open",
        "subcategories": [
          {
            "name": "Order History",
            "url": "",
            "subcategories": [
              {
                "name": "Past Orders",
                "url": "https://empire360.com/profile?section=order_history"
              },
              {
                "name": "My Past Purchased Items",
                "url": "https://empire360.com/shop/?customer_purchased_products=true"
              }
            ]
          },
          {
            "name": "Bill and Store",
            "url": "",
            "subcategories": [
              {
                "name": "Release Stored Items",
                "url": "https://empire360.com/shop?list_name=stored_items"
              },
              {
                "name": "How Do I? - Bill and Store",
                "url": "https://empire360.com/pages/billandstorehowdoi/"
              }
            ]
          },
          {
            "name": "Empire360 Invoices",
            "url": "",
            "subcategories": [
              {
                "name": "View & Pay Invoices",
                "url": "https://empire360.com/profile?section=payments&sub_section=invoices&Status=Open"
              },
              {
                "name": "View Payments",
                "url": "https://empire360.com/profile?section=payments&sub_section=payments+"
              },
              {
                "name": "Manage Bank Accounts",
                "url": "https://empire360.com/profile?section=payments&sub_section=banking"
              },
              {
                "name": "Pay On Account",
                "url": "https://empire360.com/checkout?payment-id=on-account-payment"
              },
              {
                "name": "Manage Auto Pay",
                "url": "https://empire360.com/profile?section=payments&sub_section=auto_pay"
              }
            ]
          },
          {
            "name": "Empire360 Bill Pay Help",
            "url": "",
            "subcategories": [
              {
                "name": "How Do I? - Bill Pay",
                "url": "https://cityhive-prod-cdn.cityhive.net/media_gallery/distributor/6064695850a0357d42357a6a/pdf/681ca06a9724d91dc0e3466e.pdf?1746706538"
              },
              {
                "name": "Start Bill Pay - FAQ",
                "url": "https://empire360.com/pages/startbillpay/"
              }
            ]
          }
        ]
      },
      {
        "name": "Customer Service",
        "id": 6,
        "url": "https://empire360.com/profile",
        "subcategories": [
          {
            "name": "PAYMENT",
            "url": "",
            "subcategories": [
              {
                "name": "Pay Online North",
                "url": "https://xprspay.ipayxepay.net/xprspay/emn/index.jsp"
              }
            ]
          },
          {
            "name": "GENERAL",
            "url": "",
            "subcategories": [
              {
                "name": "Customer Service Forms North",
                "url": "https://empirenorth.com/customers/customers-service/#service-form"
              },
              {
                "name": "Customer Service Forms Metro",
                "url": "https://csform.empiremerchants.com/"
              },
              {
                "name": "Policies & Updates North",
                "url": "https://empirenorth.com/customers/policies-announcements/#policy-docs"
              },
              {
                "name": "Policies & Updates Metro",
                "url": "https://www.empiremerchants.com/customers/policies-announcements/#policy-docs"
              },
              {
                "name": "Announcements North",
                "url": "https://empirenorth.com/customers/policies-announcements/#announce"
              },
              {
                "name": "Announcements Metro",
                "url": "https://www.empiremerchants.com/customers/policies-announcements/#announce"
              },
              {
                "name": "Become a Customer North",
                "url": "https://empirenorth.com/customers/new-customer/"
              },
              {
                "name": "Become a Customer Metro",
                "url": "https://www.empiremerchants.com/customers/new-customer/"
              }
            ]
          },
          {
            "name": "HOW-TO VIDEOS",
            "url": "",
            "subcategories": [
              {
                "name": "Overview",
                "url": "https://empire360.com/pages/how-to-videos#overview"
              },
              {
                "name": "Registration & Login",
                "url": "https://empire360.com/pages/how-to-videos#register"
              },
              {
                "name": "Pricing",
                "url": "https://empire360.com/pages/how-to-videos#pricing"
              },
              {
                "name": "Assortments",
                "url": "https://empire360.com/pages/how-to-videos#assortments"
              }
            ]
          },
          {
            "name": "QUICK GUIDES",
            "url": "",
            "subcategories": [
              {
                "name": "Register & Add Users",
                "url": "https://empire360.com/pages/register"
              },
              {
                "name": "Start Bill Pay - FAQ",
                "url": "https://empire360.com/pages/startbillpay/"
              },
              {
                "name": "Empire360 Bill & Store North",
                "url": "https://d3omj40jjfp5tk.cloudfront.net/media_gallery/distributor/60646c102949093d0fd0e97f/pdf/648a1c582a46592abac0b2bb.pdf?1686772824"
              },
              {
                "name": "How Do I? - Bill Pay",
                "url": "https://cityhive-prod-cdn.cityhive.net/media_gallery/distributor/6064695850a0357d42357a6a/pdf/681ca06a9724d91dc0e3466e.pdf?1746706538"
              },
              {
                "name": "Empire360 Bill & Store Metro",
                "url": "https://d3omj40jjfp5tk.cloudfront.net/media_gallery/distributor/60646c102949093d0fd0e97f/pdf/648a1c4f38f70547f1f739ab.pdf?1686772815"
              }
            ]
          }
        ]
      },
      {
        "name": "Monthly Pricing",
        "id": 7,
        "url": "https://empire360.com/#",
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
		self.bypass_cookie_consent("https://empire360.com/")
		self.switch_to_north()
		return

	def switch_to_north(self):
		print("switch_to_north()")
		try:
			button = self.wait.until(
				EC.presence_of_element_located((By.ID, 'store-picker-change-store'))
			)
			button.click()
			print("Changed Store")
		except Exception as e:
			print(f"Error: {e}")

