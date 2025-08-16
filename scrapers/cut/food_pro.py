
import json
from scrapers.cut.dry import CutScraper


class FoodProScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/food_pro/'

	# Values to change
	BASE_URL = "https://app.cutanddry.com/catalog/foodpro?verifiedVendorId=152922267&categoryId=1&page=1"
	SUB_DOMAIN = "https://app.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "188308987",
          "baseName": "eggs & dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/86acb3a008262c6dff27fde62bf23294.jpg",
          "name": "Eggs & Dairy",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 601,
        "subcategories": [
          {
            "subcategory": {
              "id": "188308988",
              "name": "Butter & Margarine",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 31,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188309003",
              "name": "Cheese",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 247,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188309029",
              "name": "Cream & Creamers",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 41,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188309030",
              "name": "Dairy Alternatives",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 54,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188309010",
              "name": "Eggs",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 39,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188309046",
              "name": "Ice Cream & Shakes",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 93,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188309069",
              "name": "Milk",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 39,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188309101",
              "name": "Sour Cream",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188309042",
              "name": "Yogurt",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 54,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "188308968",
          "baseName": "fruits & vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/16a29b61e19e0512d1fcf76038b03f41.jpg",
          "name": "Fruits & Vegetables",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1141,
        "subcategories": [
          {
            "subcategory": {
              "id": "188308998",
              "name": "Canned Fruit",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 133,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188309043",
              "name": "Canned Vegetables",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 129,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188309102",
              "name": "Fresh Fruit",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 172,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188308969",
              "name": "Fresh Vegetables",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 551,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188309019",
              "name": "Frozen Fruit",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 41,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188308992",
              "name": "Frozen Vegetables",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 114,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "188309359",
              "name": "Sides",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = "Food Pro"
	VENDOR_URL_NAME = 'foodpro'
	VERIFIED_VENDOR_ID = 152922267

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY

