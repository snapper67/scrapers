
import json
from scrapers.cut.dry import CutScraper


class ABScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/ab/'

	# Values to change
	BASE_URL = "https://app.cutanddry.com/catalog/aandb?verifiedVendorId=1861824&categoryId=1&categoryName=All+Items&page=1"
	SUB_DOMAIN = "https://app.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "110413879",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Dairy",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 85,
        "subcategories": [
          {
            "subcategory": {
              "id": "110413880",
              "name": "Dairy",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 85,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "110413923",
          "baseName": "operational",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Operational",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 347,
        "subcategories": [
          {
            "subcategory": {
              "id": "110413924",
              "name": "Operational",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 347,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "352689330",
          "baseName": "protein",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Protein",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 478,
        "subcategories": [
          {
            "subcategory": {
              "id": "352689331",
              "name": "Protein",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 478,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "352689332",
          "baseName": "syrups & mixers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Syrups & Mixers",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 181,
        "subcategories": [
          {
            "subcategory": {
              "id": "352689333",
              "name": "Syrups & Mixers",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 181,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "352689334",
          "baseName": "charcuterie",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Charcuterie",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 25,
        "subcategories": [
          {
            "subcategory": {
              "id": "352689335",
              "name": "Charcuterie",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 25,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "352689337",
          "baseName": "fruit & vegetable",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Fruit & Vegetable",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 375,
        "subcategories": [
          {
            "subcategory": {
              "id": "352689338",
              "name": "Fruit & Vegetable",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 375,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "352689339",
          "baseName": "cheese",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Cheese",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 257,
        "subcategories": [
          {
            "subcategory": {
              "id": "352689340",
              "name": "Cheese",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 257,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "352689341",
          "baseName": "sauce & dressing",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Sauce & Dressing",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 177,
        "subcategories": [
          {
            "subcategory": {
              "id": "352689342",
              "name": "Sauce & Dressing",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 177,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "352689374",
          "baseName": "bakery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Bakery",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 447,
        "subcategories": [
          {
            "subcategory": {
              "id": "352689375",
              "name": "Bakery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 447,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "352689398",
          "baseName": "nuts & snacks",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Nuts & Snacks",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 81,
        "subcategories": [
          {
            "subcategory": {
              "id": "352689399",
              "name": "Nuts & Snacks",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 81,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "352689452",
          "baseName": "oil & vinegar",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Oil & Vinegar",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 63,
        "subcategories": [
          {
            "subcategory": {
              "id": "352689453",
              "name": "Oil & Vinegar",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 63,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "352689498",
          "baseName": "beverages",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Beverages",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 128,
        "subcategories": [
          {
            "subcategory": {
              "id": "352689499",
              "name": "Beverages",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 128,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "352689540",
          "baseName": "spices",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Spices",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 315,
        "subcategories": [
          {
            "subcategory": {
              "id": "352689541",
              "name": "Spices",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 315,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "352689544",
          "baseName": "pasta & grains",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Pasta & Grains",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 92,
        "subcategories": [
          {
            "subcategory": {
              "id": "352689545",
              "name": "Pasta & Grains",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 92,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'A & B'
	VENDOR_URL_NAME = 'aandb'
	VERIFIED_VENDOR_ID = 1861824

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY
		self.options['base_url'] = self.BASE_URL
