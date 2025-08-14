
import json
from scrapers.cut.dry import CutScraper


class SouthwestTradersScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/southwest_traders/'

	# Values to change
	BASE_URL = "https://app.cutanddry.com/catalog/southwesttraders?verifiedVendorId=1862188&categoryId=1&page=1"
	SUB_DOMAIN = "https://app.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "29189192",
          "baseName": "additives & syrups",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Additives & Syrups",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 218,
        "subcategories": [
          {
            "subcategory": {
              "id": "29189193",
              "name": "Additives & Syrups",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 218,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29190351",
          "baseName": "bakery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Bakery",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 158,
        "subcategories": [
          {
            "subcategory": {
              "id": "29190352",
              "name": "Bakery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 158,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29192849",
          "baseName": "beverages",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Beverages",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 99,
        "subcategories": [
          {
            "subcategory": {
              "id": "29192850",
              "name": "Beverages",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 99,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29189220",
          "baseName": "boba",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Boba",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 81,
        "subcategories": [
          {
            "subcategory": {
              "id": "29189221",
              "name": "Boba",
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
          "id": "29189139",
          "baseName": "cones",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Cones",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 22,
        "subcategories": [
          {
            "subcategory": {
              "id": "29189140",
              "name": "Cones",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 22,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29192976",
          "baseName": "cleaning & janitorial",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Cleaning & Janitorial",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 98,
        "subcategories": [
          {
            "subcategory": {
              "id": "29194102",
              "name": "Cleaning & Janitorial",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 98,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29192935",
          "baseName": "cups, lids & containers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Cups, Lids & Containers",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 239,
        "subcategories": [
          {
            "subcategory": {
              "id": "29192936",
              "name": "Cups, Lids & Containers",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 239,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29192943",
          "baseName": "cutlery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Cutlery",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 46,
        "subcategories": [
          {
            "subcategory": {
              "id": "29192944",
              "name": "Cutlery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 46,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29190255",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Dairy",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 22,
        "subcategories": [
          {
            "subcategory": {
              "id": "29190256",
              "name": "Dairy",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 22,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29478619",
          "baseName": "dairy alternatives",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Dairy Alternatives",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 12,
        "subcategories": [
          {
            "subcategory": {
              "id": "29478620",
              "name": "Dairy Alternatives",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 12,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29192883",
          "baseName": "fruit & produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Fruit & Produce",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 84,
        "subcategories": [
          {
            "subcategory": {
              "id": "29192884",
              "name": "Fruit & Produce",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 84,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29192887",
          "baseName": "grocery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Grocery",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 96,
        "subcategories": [
          {
            "subcategory": {
              "id": "29192888",
              "name": "Grocery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 96,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29189112",
          "baseName": "ice cream hardpack",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Ice Cream Hardpack",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 309,
        "subcategories": [
          {
            "subcategory": {
              "id": "29189113",
              "name": "Ice Cream Hardpack",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 309,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29189203",
          "baseName": "juice concentrates",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Juice Concentrates",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 38,
        "subcategories": [
          {
            "subcategory": {
              "id": "29189204",
              "name": "Juice Concentrates",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 38,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29192901",
          "baseName": "novelties",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Novelties",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 129,
        "subcategories": [
          {
            "subcategory": {
              "id": "29192902",
              "name": "Novelties",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 129,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29192897",
          "baseName": "protein",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Protein",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 27,
        "subcategories": [
          {
            "subcategory": {
              "id": "29194034",
              "name": "Protein",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 27,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29192893",
          "baseName": "snacks",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Snacks",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 27,
        "subcategories": [
          {
            "subcategory": {
              "id": "29192894",
              "name": "Snacks",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 27,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29192939",
          "baseName": "straws",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Straws",
          "sortIndex": "18",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 9,
        "subcategories": [
          {
            "subcategory": {
              "id": "29192940",
              "name": "Straws",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 9,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29189198",
          "baseName": "smoothie mixes",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Smoothie Mixes",
          "sortIndex": "19",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 41,
        "subcategories": [
          {
            "subcategory": {
              "id": "29189199",
              "name": "Smoothie Mixes",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 41,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29189116",
          "baseName": "soft serve",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Soft Serve",
          "sortIndex": "20",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 231,
        "subcategories": [
          {
            "subcategory": {
              "id": "29189117",
              "name": "Soft Serve",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 231,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29189121",
          "baseName": "toppings",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Toppings",
          "sortIndex": "21",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 199,
        "subcategories": [
          {
            "subcategory": {
              "id": "29189122",
              "name": "Toppings",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 199,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "29192980",
          "baseName": "other supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Other Supplies",
          "sortIndex": "22",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 74,
        "subcategories": [
          {
            "subcategory": {
              "id": "29194136",
              "name": "Other Supplies",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 74,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120418324",
          "baseName": "beverage : drinks/ drink bases/drink mixes, other : cocktail mixes (frozen)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Beverage : Drinks/ Drink Bases/Drink Mixes, Other : Cocktail Mixes (Frozen)",
          "sortIndex": "23",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 2,
        "subcategories": [
          {
            "subcategory": {
              "id": "27904928",
              "name": "Beverage",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'Southwest Traders'
	VENDOR_URL_NAME = 'southwesttraders'
	VERIFIED_VENDOR_ID = 1862188

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY

