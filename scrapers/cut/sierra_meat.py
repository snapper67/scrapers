
import json
from scrapers.cut.dry import CutScraper


class SierraMeatScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/sierra_meat/'

	# Values to change
	BASE_URL = "https://app.cutanddry.com/catalog/sierra%20meat%20&%20seafood?verifiedVendorId=21262898&categoryId=1&page=1"
	SUB_DOMAIN = "https://app.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "99349143",
          "baseName": "freezer specials",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Freezer Specials",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 67,
        "subcategories": [
          {
            "subcategory": {
              "id": "99349144",
              "name": "Freezer Specials",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 67,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "27904996",
          "baseName": "beef",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Beef",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 923,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904997",
              "name": "Beef",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 923,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "27904988",
          "baseName": "poultry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Poultry",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 95,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904989",
              "name": "Poultry",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 95,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "27904990",
          "baseName": "pork",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Pork",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 233,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904991",
              "name": "Pork",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 233,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "27904968",
          "baseName": "lamb & goat",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Lamb & Goat",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 69,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904969",
              "name": "Lamb & Goat",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 69,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "27904970",
          "baseName": "game",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Game",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 310,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904971",
              "name": "Game",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 310,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "27904966",
          "baseName": "veal",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Veal",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 21,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904967",
              "name": "Veal",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 21,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "27904973",
          "baseName": "charcuterie & sausage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Charcuterie & Sausage",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 122,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904974",
              "name": "Charcuterie & Sausage",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 122,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "27904961",
          "baseName": "other meat",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Other Meat",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 2,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904963",
              "name": "Other Meat",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "27904981",
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Seafood",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 300,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904982",
              "name": "Seafood",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 300,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "27904975",
          "baseName": "dry goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Dry Goods",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904976",
              "name": "Dry Goods",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "27904964",
          "baseName": "pantry & prepared",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Pantry & Prepared",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 21,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904965",
              "name": "Pantry & Prepared",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 21,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "27904979",
          "baseName": "vegetables & herbs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Vegetables & Herbs",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 5,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904980",
              "name": "Vegetables & Herbs",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "28579543",
          "baseName": "sushi",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Sushi",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 10,
        "subcategories": [
          {
            "subcategory": {
              "id": "28689278",
              "name": "Sushi",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'Sierra Meat & Seafood'
	VENDOR_URL_NAME = 'sierra%20meat%20&%20seafood'
	VERIFIED_VENDOR_ID = 21262898

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY

