
import json
from scrapers.cut.dry import CutScraper


class PrimizieNoCaScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/primizie_noca'

	# Values to change
	BASE_URL = "https://app.cutanddry.com/catalog/primizie?verifiedVendorId=1979177&categoryId=1&page=1"
	SUB_DOMAIN = "https://app.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "appetizers & entrees",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "46448481",
          "name": "Appetizers & Entrees",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 160,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "309630556",
              "name": "Meat & Charcuterie",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 54,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "212033677",
              "name": "Savory Bites",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 44,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "311210607",
              "name": "Vegetables & Sides",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 36,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "76593237",
              "name": "Ready Meals",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "321940139",
              "name": "Pizzas & Crusts",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "321940514",
              "name": "Beans_ Rice & Mushrooms",
              "sortIndex": null
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "bakery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "225907237",
          "name": "Bakery",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 145,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 67,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "285797911",
              "name": "Pastries & Croissants",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 59,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "76593207",
              "name": "Ready to Serve",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 19,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "46448517",
              "name": "Bread & Dough",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "beverages",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "211759261",
          "name": "Beverages",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 16,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "211952282",
              "name": "Coffee & Tea",
              "sortIndex": null
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "butter cheese & dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "309629324",
          "name": "Butter Cheese & Dairy",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 14,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 14,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "309629325",
              "name": "Butter & Dairy",
              "sortIndex": null
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "desserts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "46448464",
          "name": "Desserts",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 406,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 75,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "211952046",
              "name": "Pre-cut Cakes",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 82,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "321939592",
              "name": "Individual Desserts",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 49,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "212033670",
              "name": "Sweet Bites & Petits Fours",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 52,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "76593208",
              "name": "Cookies",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "211952162",
              "name": "Bars & Brownies",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 76,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "76593204",
              "name": "Gelato & Sorbetto",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "76593221",
              "name": "Individual Cakes",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "76593223",
              "name": "Glass Desserts",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 19,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "76593217",
              "name": "Whole Cakes & Strip Cakes",
              "sortIndex": null
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "pasta & ravioli",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "46448453",
          "name": "Pasta & Ravioli",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 67,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "76593225",
              "name": "Dry Pasta",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 51,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "211759262",
              "name": "Frozen Pasta",
              "sortIndex": null
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "savory ingredients",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "212033668",
          "name": "Savory Ingredients",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 58,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "309629748",
              "name": "Neutral Tart Shells",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "76593218",
              "name": "Condiments",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "311210735",
              "name": "Bases & Sauces",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "212033880",
              "name": "Oils & Vinegars",
              "sortIndex": null
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "sweet ingredients",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "212033678",
          "name": "Sweet Ingredients",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 137,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "214217533",
              "name": "Jams & Jellies",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 55,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "311186333",
              "name": "Fruit Purees",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 27,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "212033672",
              "name": "Toppings Fillings & Sugars",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 14,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "76593226",
              "name": "Individual Jams & Jellies",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "311210826",
              "name": "Frozen Fruit",
              "sortIndex": null
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "76593228",
              "name": "Sweet Tart Shells",
              "sortIndex": null
            }
          }
        ]
      }
    ]
  }
}

                    
		''')

	VENDOR_NAME = 'Primizie NoCa'
	VENDOR_URL_NAME = 'primizie'
	VERIFIED_VENDOR_ID = 1979177

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
		'url': 'https://app.cutanddry.com/catalog/primizieny?verifiedVendorId=50714839&categoryId=1&page=1',
		'search_term': 'Spices',
		'attempts': '40',
	}

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY
		self.options['base_url'] = self.BASE_URL
