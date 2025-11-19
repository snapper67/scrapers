import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from scrapers.city.hive import HiveScraper

"""
	Twin Liquors
	Type: Standard shop website
	Method: 
		Get Categories: Scape Navigation
		Get Products: Scape Product List
		Get Product Manual Scrape and json data from html
	Issues:
		The embedded json data does not have all the information needed to create a product. Data like 
		sku and description are not included in the json data.
"""

class TwinLiquorsScraper(HiveScraper):
	# 3286/edit_note/1726/
	CRM_ID = 3286
	CRM_NOTE_ID = 1726
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/twin_liquors/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = 'https://twinliquors.com/'
	VENDOR_NAME = 'Twin Liquors'
	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "name": "Our Deals",
        "id": 1,
        "url": "https://twinliquors.com/pages/deals",
        "subcategories": []
      },
      {
        "name": "Shop All",
        "id": 2,
        "url": "https://twinliquors.com/shop",
        "subcategories": []
      },
      {
        "name": "Wine",
        "id": 3,
        "url": "https://twinliquors.com/shop/?container-id=5fbe12cf2d83d407c47719c9&title=Shop%20Wine",
        "subcategories": [
          {
            "name": "By Style",
            "url": "",
            "subcategories": [
              {
                "name": "Red",
                "url": "https://twinliquors.com/shop/?subtype=red"
              },
              {
                "name": "White",
                "url": "https://twinliquors.com/shop/?subtype=white"
              },
              {
                "name": "Ros\u00e9 & Blush",
                "url": "https://twinliquors.com/shop/?subtype=rose"
              },
              {
                "name": "Champagne & Sparkling",
                "url": "https://twinliquors.com/shop/?subtype=sparkling"
              },
              {
                "name": "Dessert & Port",
                "url": "https://twinliquors.com/shop/?subtype=dessert&subtype=port"
              },
              {
                "name": "Other Wines",
                "url": "https://twinliquors.com/shop/?category=other_wine&title=Other+Wine"
              },
              {
                "name": "Non-Alcoholic",
                "url": "https://twinliquors.com/shop/product-groups/non-alcoholic-1?type=Wine"
              }
            ]
          },
          {
            "name": "By Varietal",
            "url": "",
            "subcategories": [
              {
                "name": "Cabernet Sauvignon",
                "url": "https://twinliquors.com/shop/?category=cabernet_sauvignon_name&title=Cabernet%20Sauvignon"
              },
              {
                "name": "Chardonnay",
                "url": "https://twinliquors.com/shop/?category=chardonnay_name&title=Chardonnay"
              },
              {
                "name": "Sauvignon Blanc",
                "url": "https://twinliquors.com/shop/?category=sauvignon_blanc_name&title=Sauvignon%20Blanc"
              },
              {
                "name": "Red Blends",
                "url": "https://twinliquors.com/shop/?type=wine&varietal=red+blend"
              },
              {
                "name": "Pinot Noir",
                "url": "https://twinliquors.com/shop/?category=pinot_noir_name&title=Pinot%20Noir"
              },
              {
                "name": "Pinot Grigio",
                "url": "https://twinliquors.com/shop/?category=pinot_grigio_name&title=Pinot%20Grigio"
              },
              {
                "name": "Rose",
                "url": "https://twinliquors.com/shop/?varietal=rose"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "France",
                "url": "https://twinliquors.com/shop/?type=wine&country=france"
              },
              {
                "name": "Italy",
                "url": "https://twinliquors.com/shop/?type=wine&country=italy"
              },
              {
                "name": "Spain",
                "url": "https://twinliquors.com/shop/?type=wine&country=spain"
              },
              {
                "name": "Germany",
                "url": "https://twinliquors.com/shop/?type=wine&country=germany"
              },
              {
                "name": "Argentina",
                "url": "https://twinliquors.com/shop/?type=wine&country=argentina"
              },
              {
                "name": "United States",
                "url": "https://twinliquors.com/shop/?type=wine&country=united%20states"
              },
              {
                "name": "New Zealand",
                "url": "https://twinliquors.com/shop/?type=wine&country=new%20zealand"
              }
            ]
          },
          {
            "name": "By Region",
            "url": "",
            "subcategories": [
              {
                "name": "Bordeaux",
                "url": "https://twinliquors.com/shop/?type=wine®ion=bordeaux"
              },
              {
                "name": "Tuscany",
                "url": "https://twinliquors.com/shop/?type=wine®ion=tuscany"
              },
              {
                "name": "Rioja",
                "url": "https://twinliquors.com/shop/?type=wine®ion=rioja"
              },
              {
                "name": "Burgundy",
                "url": "https://twinliquors.com/shop/?type=wine®ion=burgundy"
              },
              {
                "name": "Napa Valley",
                "url": "https://twinliquors.com/shop/?type=wine®ion=napa%20valley"
              }
            ]
          },
          {
            "name": "By Rating",
            "url": "",
            "subcategories": [
              {
                "name": "90+ Points Wine Advocate",
                "url": "https://twinliquors.com/product-groups/90-points-wine-advocate"
              },
              {
                "name": "90+ Points Wine Spectator",
                "url": "https://twinliquors.com/product-groups/90-points-wine-spectator"
              },
              {
                "name": "90+ Points Wine Enthusiast",
                "url": "https://twinliquors.com/product-groups/90-points-wine-enthusiast"
              },
              {
                "name": "90+ Points Vinous",
                "url": "https://twinliquors.com/product-groups/90-points-vinous"
              },
              {
                "name": "90+ Points James Suckling",
                "url": "https://twinliquors.com/product-groups/90-points-james-suckling"
              },
              {
                "name": "90+ Points Jeb Dunnuck",
                "url": "https://twinliquors.com/product-groups/90-points-jeb-dunnuck"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://twinliquors.com/shop/?category=wine_new_arrivals&title=Wine%20New%20Arrivals"
              },
              {
                "name": "On Sale",
                "url": "https://twinliquors.com/shop/?category=wine_on_sale&title=Wine%20On%20Sale"
              },
              {
                "name": "All Wine",
                "url": "https://twinliquors.com/shop/?type=wine"
              }
            ]
          }
        ]
      },
      {
        "name": "Spirits",
        "id": 4,
        "url": "https://twinliquors.com/shop/?container-id=5fbe14adf3e645405af2df97&title=Shop%20Spirits",
        "subcategories": [
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "Vodka",
                "url": "https://twinliquors.com/shop/?subtype=vodka"
              },
              {
                "name": "Tequila",
                "url": "https://twinliquors.com/shop/?subtype=tequila"
              },
              {
                "name": "Whiskey",
                "url": "https://twinliquors.com/shop/?subtype=whiskey"
              },
              {
                "name": "Ready to Drink",
                "url": "https://twinliquors.com/shop?category=all_spirits&category=all_spirits&category=ready_to_drink_cocktail&title=Ready+to+Drink"
              },
              {
                "name": "Rum",
                "url": "https://twinliquors.com/shop/?subtype=rum"
              },
              {
                "name": "Gin",
                "url": "https://twinliquors.com/shop/?subtype=gin"
              },
              {
                "name": "Sake",
                "url": "https://twinliquors.com/shop/?subtype=sake"
              },
              {
                "name": "Brandy",
                "url": "https://twinliquors.com/shop/?subtype=brandy"
              },
              {
                "name": "Liqueur",
                "url": "https://twinliquors.com/shop/?subtype=liqueur"
              },
              {
                "name": "Non-Alcoholic",
                "url": "https://twinliquors.com/shop/product-groups/non-alcoholic-1?type=Spirits"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "United States",
                "url": "https://twinliquors.com/shop/?type=spirits&country=united%20states"
              },
              {
                "name": "France",
                "url": "https://twinliquors.com/shop/?type=spirits&country=france"
              },
              {
                "name": "Ireland",
                "url": "https://twinliquors.com/shop/?type=spirits&country=ireland"
              },
              {
                "name": "Japan",
                "url": "https://twinliquors.com/shop/?type=spirits&country=japan"
              },
              {
                "name": "Italy",
                "url": "https://twinliquors.com/shop/?type=spirits&country=italy"
              },
              {
                "name": "Mexico",
                "url": "https://twinliquors.com/shop/?type=spirits&country=mexico"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://twinliquors.com/shop/?category=spirits_new_arrivals&title=Spirits%20New%20Arrivals"
              },
              {
                "name": "On Sale",
                "url": "https://twinliquors.com/shop/?category=spirits_on_sale&title=Spirits%20On%20Sale"
              },
              {
                "name": "All Spirits",
                "url": "https://twinliquors.com/shop/?type=spirits"
              }
            ]
          }
        ]
      },
      {
        "name": "Beer",
        "id": 5,
        "url": "https://twinliquors.com/shop/?container-id=5fbe11cea24d786c82b31f72&title=Shop%20Beer",
        "subcategories": [
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "IPA",
                "url": "https://twinliquors.com/shop/?category=ipa_basic_category&title=IPA"
              },
              {
                "name": "Hard Seltzer",
                "url": "https://twinliquors.com/shop/?category=seltzer_basic_category&title=Hard%20Seltzer"
              },
              {
                "name": "Ale",
                "url": "https://twinliquors.com/shop/?category=ale_beer&title=ale"
              },
              {
                "name": "Lager",
                "url": "https://twinliquors.com/shop/?category=lager_beer&title=lager"
              },
              {
                "name": "Pilsner",
                "url": "https://twinliquors.com/shop/?category=pilsner_basic_category&title=pilsner"
              },
              {
                "name": "Stout",
                "url": "https://twinliquors.com/shop/?category=stout_beer&title=stout"
              },
              {
                "name": "Non-Alcoholic",
                "url": "https://twinliquors.com/shop/product-groups/non-alcoholic-1?type=Beer"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://twinliquors.com/shop/?category=beer_new_arrivals&title=Beer%20New%20Arrivals"
              },
              {
                "name": "On Sale",
                "url": "https://twinliquors.com/shop/?category=beer_on_sale&title=Beer%20On%20Sale"
              },
              {
                "name": "All Beer",
                "url": "https://twinliquors.com/shop/?type=beer"
              }
            ]
          }
        ]
      },
      {
        "name": "Gifts",
        "id": 6,
        "url": "https://twinliquors.com/pages/gift-guide",
        "subcategories": [
          {
            "name": "Gift Wines",
            "url": "",
            "subcategories": [
              {
                "name": "Champagne & Sparkling",
                "url": "https://twinliquors.com/shop/?subtype=sparkling"
              },
              {
                "name": "Fine Red Wine",
                "url": "https://twinliquors.com/shop/?subtype=red&min_price=60&max_price=7265"
              },
              {
                "name": "Fine White Wine",
                "url": "https://twinliquors.com/shop/?subtype=white&min_price=60&max_price=7265"
              },
              {
                "name": "Festive Bottles",
                "url": "https://twinliquors.com/shop/product-groups/featured-festive-bottles"
              },
              {
                "name": "All Wines",
                "url": "https://twinliquors.com/shop/product-groups/wine-great-bottles-to-gift"
              }
            ]
          },
          {
            "name": "Gift Spirits",
            "url": "",
            "subcategories": [
              {
                "name": "Whiskey and Bourbon",
                "url": "https://twinliquors.com//shop/product-groups/holiday-whiskey-and-bourbon"
              },
              {
                "name": "Scotch",
                "url": "https://twinliquors.com/shop/product-groups/holiday-scotch"
              },
              {
                "name": "Tequila",
                "url": "https://twinliquors.com/shop/product-groups/holiday-tequila"
              },
              {
                "name": "Vodka",
                "url": "https://twinliquors.com/shop/product-groups/holiday-vodka"
              },
              {
                "name": "All Spirits",
                "url": "https://twinliquors.com/shop/product-groups/spirits-great-bottles-to-gift"
              }
            ]
          },
          {
            "name": "By Price",
            "url": "",
            "subcategories": [
              {
                "name": "Under $15",
                "url": "https://twinliquors.com/shop/product-groups/festive-gifts-under-15"
              },
              {
                "name": "$15-30",
                "url": "https://twinliquors.com/shop/product-groups/festive-gifts-15-30"
              },
              {
                "name": "$30-60",
                "url": "https://twinliquors.com/shop/product-groups/festive-gifts-30-60"
              },
              {
                "name": "$60-100",
                "url": "https://twinliquors.com/shop/product-groups/holiday-gifts-60-100"
              },
              {
                "name": "Over $100",
                "url": "https://twinliquors.com/shop/product-groups/festive-gifts-under-15-1"
              }
            ]
          },
          {
            "name": "Other Gifts",
            "url": "",
            "subcategories": [
              {
                "name": "Custom Gift Baskets",
                "url": "https://twinliquors.com/pages/custom-gift-baskets"
              },
              {
                "name": "Accessories",
                "url": "https://twinliquors.com/shop?show-search=true&type=Accessories"
              },
              {
                "name": "Gift Cards",
                "url": "https://giftcards.twinliquors.com/shop?show-search=true"
              }
            ]
          }
        ]
      },
      {
        "name": "Events",
        "id": 7,
        "url": "https://twinliquors.com/events",
        "subcategories": []
      },
      {
        "name": "Event Planning",
        "id": 8,
        "url": "https://twinliquors.com/#",
        "subcategories": [
          {
            "name": "Weddings/Parties",
            "url": "",
            "subcategories": [
              {
                "name": "Wedding Quote",
                "url": "https://twinliquors.com/pages/weddings"
              },
              {
                "name": "Party Quote",
                "url": "https://twinliquors.com/pages/party-planning"
              }
            ]
          },
          {
            "name": "Corporate Events",
            "url": "",
            "subcategories": [
              {
                "name": "Corporate Events",
                "url": "https://twinliquors.com/pages/corporate-events"
              },
              {
                "name": "Request An Event at Twin",
                "url": "https://twinliquors.com/pages/request-an-event"
              }
            ]
          },
          {
            "name": "Donation Request",
            "url": "",
            "subcategories": [
              {
                "name": "Donation Request Form",
                "url": "https://twinliquors.com/pages/donation-request"
              },
              {
                "name": "Twin Hearts",
                "url": "https://twinliquors.com/pages/hearts"
              }
            ]
          }
        ]
      },
      {
        "name": "Explore",
        "id": 9,
        "url": "https://twinliquors.com/#",
        "subcategories": [
          {
            "name": "Contact Us",
            "url": "",
            "subcategories": [
              {
                "name": "Contact Us",
                "url": "https://twinliquors.com/pages/contact"
              },
              {
                "name": "Join The Family",
                "url": "https://twinliquors.com/pages/join-the-family"
              }
            ]
          },
          {
            "name": "About Us",
            "url": "",
            "subcategories": [
              {
                "name": "Our History",
                "url": "https://twinliquors.com/pages/about-twin-liquors"
              },
              {
                "name": "Twin Hearts",
                "url": "https://twinliquors.com/pages/hearts"
              },
              {
                "name": "Pricing Philosophy",
                "url": "https://twinliquors.com/pages/pricing-philosophy-return-exchange-refund-policy"
              },
              {
                "name": "Locations",
                "url": "https://twinliquors.com/pages/store-locations"
              },
              {
                "name": "Marketplace Locations",
                "url": "https://twinliquors.com/pages/marketplace"
              },
              {
                "name": "Exchange & Refund Policy",
                "url": "https://twinliquors.com/pages/pricing-philosophy-return-exchange-refund-policy"
              }
            ]
          },
          {
            "name": "Learn",
            "url": "",
            "subcategories": [
              {
                "name": "Learn & Plan",
                "url": "https://twinliquors.com/pages/learn"
              },
              {
                "name": "Drink Calculator",
                "url": "https://twinliquors.com/pages/drink-calculator"
              },
              {
                "name": "Easy Guide to Wine",
                "url": "https://twinliquors.com/pages/easy-guide-to-wine"
              },
              {
                "name": "Twin Sourced Wine",
                "url": "https://twinliquors.com/pages/sourced-wine"
              }
            ]
          }
        ]
      },
      {
        "name": "Wholesale",
        "id": 10,
        "url": "https://twinliquors.com/pages/wholesale",
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

	def get_pack_size(self, row_spec):
		print("get_pack_size()")
		row_spec['size'] = f"{row_spec['pack_size'].get('quantity', '')} {row_spec['pack_size'].get('measure', '')}"
		row_spec['pack'] = row_spec['pack_size'].get('pack', '')

		print("processing product pack_size Complete...")
		return row_spec


