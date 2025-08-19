
import json
from scrapers.cut.dry import CutScraper


class CooksCompanyScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/cooks_company/'

	# Values to change
	BASE_URL = "https://app.cutanddry.com/catalog/cooks?verifiedVendorId=1897602&categoryId=1&page=1"
	SUB_DOMAIN = "https://app.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "65310545",
          "baseName": "herbs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Herbs",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 104,
        "subcategories": [
          {
            "subcategory": {
              "id": "65310546",
              "name": "Herbs",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 104,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "65310550",
          "baseName": "greens",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Greens",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 128,
        "subcategories": [
          {
            "subcategory": {
              "id": "65310551",
              "name": "Greens",
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
          "id": "65310556",
          "baseName": "vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Vegetables",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 324,
        "subcategories": [
          {
            "subcategory": {
              "id": "65310557",
              "name": "Vegetables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 324,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "65310563",
          "baseName": "fruit",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Fruit",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 197,
        "subcategories": [
          {
            "subcategory": {
              "id": "65310682",
              "name": "Fruit",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 197,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "65310569",
          "baseName": "dairy + eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Dairy + Eggs",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 145,
        "subcategories": [
          {
            "subcategory": {
              "id": "65310570",
              "name": "Dairy + Eggs",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 145,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "65310581",
          "baseName": "grocery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Grocery",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 288,
        "subcategories": [
          {
            "subcategory": {
              "id": "65310582",
              "name": "Grocery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 288,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "65310585",
          "baseName": "frozen",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Frozen",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 81,
        "subcategories": [
          {
            "subcategory": {
              "id": "65310603",
              "name": "Frozen",
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
          "id": "65310606",
          "baseName": "pre-cut",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Pre-Cut",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 19,
        "subcategories": [
          {
            "subcategory": {
              "id": "65310613",
              "name": "Pre-Cut",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 19,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "61928620",
          "baseName": "other",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Other",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 145,
        "subcategories": [
          {
            "subcategory": {
              "id": "61928621",
              "name": "Other",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 145,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'Cooks Company'
	VENDOR_URL_NAME = 'cooks'
	VERIFIED_VENDOR_ID = 1897602

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY
		self.options['base_url'] = self.BASE_URL
