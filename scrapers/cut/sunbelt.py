
import json
from scrapers.cut.dry import CutScraper


class SunbeltScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/sunbelt/'

	# Values to change
	BASE_URL = "https://sunbelt.cutanddry.com/catalog/sunbelt?verifiedVendorId=27494043&categoryId=1&page=1"
	SUB_DOMAIN = "https://sunbelt.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "211426962",
          "baseName": "groceries",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8867d4468e0cb8d9ad365ec85168f821.jpg",
          "name": "Groceries",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 450,
        "subcategories": [
          {
            "subcategory": {
              "id": "211426963",
              "name": "Groceries",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 450,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "211426964",
          "baseName": "drinks & beverages",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bf50cce2bfa9b1247f2e18c8d834ce30.jpg",
          "name": "Drinks & Beverages",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 184,
        "subcategories": [
          {
            "subcategory": {
              "id": "211426965",
              "name": "Drinks & Beverages",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 184,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "211426966",
          "baseName": "frozen",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/41b7e2cb70b97a9ffd047bfdf0f1abaa.jpg",
          "name": "Frozen",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 476,
        "subcategories": [
          {
            "subcategory": {
              "id": "211426967",
              "name": "Frozen",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 476,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "211426968",
          "baseName": "snacks",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/3bf5c5dabff130b587a8e038b8be1606.webp",
          "name": "Snacks",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 103,
        "subcategories": [
          {
            "subcategory": {
              "id": "211426969",
              "name": "Snacks",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 103,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "211426970",
          "baseName": "others",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d475e403f011ccf58998eec376c0e506.jpg",
          "name": "Others",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 24,
        "subcategories": [
          {
            "subcategory": {
              "id": "211426971",
              "name": "Others",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 24,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "211426972",
          "baseName": "refrigerated",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/ed8feee9c3a179aed92db936ea6ea777.jpg",
          "name": "Refrigerated",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 130,
        "subcategories": [
          {
            "subcategory": {
              "id": "211426973",
              "name": "Refrigerated",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 130,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "211426974",
          "baseName": "herbs & supplements",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/76fc0beff1a2f5c9e4d8e632e93c1c4e.jpg",
          "name": "Herbs & Supplements",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 737,
        "subcategories": [
          {
            "subcategory": {
              "id": "211426975",
              "name": "Herbs & Supplements",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 737,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "211426980",
          "baseName": "bulk",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/84e8c1943bbc916c981e9637fd2ce99d.jpg",
          "name": "Bulk",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 169,
        "subcategories": [
          {
            "subcategory": {
              "id": "211426981",
              "name": "Bulk",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 169,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "211427318",
          "baseName": "disposable",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/535773279ab5dabdc2e216eb5e22eb75.jpg",
          "name": "Disposable",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 20,
        "subcategories": [
          {
            "subcategory": {
              "id": "211427319",
              "name": "Disposable",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 20,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'Sunbelt'
	VENDOR_URL_NAME = 'sunbelt'
	VERIFIED_VENDOR_ID = 27494043

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY

