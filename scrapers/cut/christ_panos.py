
import json
from scrapers.cut.dry import CutScraper


class ChristPanosScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/christ_panos/'

	# Values to change
	BASE_URL = "https://panos.cutanddry.com/catalog/christpanos?verifiedVendorId=1861896&categoryId=1&page=1"
	SUB_DOMAIN = "https://panos.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "325524395",
          "baseName": "disposable",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/dcc4961b2ceabbb17c5a7d531b7b4de9.jpg",
          "name": "Disposable",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 633,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524396",
              "name": "Disposable",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 633,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524397",
          "baseName": "grocery frozen",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9ab39b04607a8e7a80438908d0301522.jpg",
          "name": "Grocery Frozen",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 239,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524398",
              "name": "Grocery Frozen",
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
          "id": "325524399",
          "baseName": "grocery dry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2ac74f022c3aeb162ef700723d96c1dd.jpg",
          "name": "Grocery Dry",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 734,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524400",
              "name": "Grocery Dry",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 734,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524401",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2dc3258a722e1b83904c77cbd5a2e0f9.jpg",
          "name": "Dairy",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 273,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524402",
              "name": "Dairy",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 273,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524403",
          "baseName": "canned dry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f9fcc24f0a953a8b1287663e9ee68d07.jpg",
          "name": "Canned Dry",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 158,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524404",
              "name": "Canned Dry",
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
          "id": "325524405",
          "baseName": "beverage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a47e953d88a0b383721ff541a01abfab.jpg",
          "name": "Beverage",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 189,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524406",
              "name": "Beverage",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 189,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524407",
          "baseName": "beef",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2cce55fe3cb874d93063df846d926357.jpg",
          "name": "Beef",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 270,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524408",
              "name": "Beef",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 270,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524409",
          "baseName": "condiment",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/90befd6af86efba767754cfdbbdd6715.jpg",
          "name": "Condiment",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 168,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524410",
              "name": "Condiment",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 168,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524411",
          "baseName": "frozen potatoes",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/56c587dce37ec72557c079c3c68f4669.jpg",
          "name": "Frozen Potatoes",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 121,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524412",
              "name": "Frozen Potatoes",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 121,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524434",
          "baseName": "appetizers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9f4b9f373ee5bf34240f41692a6c96a1.jpg",
          "name": "Appetizers",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 77,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524435",
              "name": "Appetizers",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 77,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524437",
          "baseName": "bread",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/096e567996291778bdd452e0521b6d16.jpg",
          "name": "Bread",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 76,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524438",
              "name": "Bread",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 76,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524439",
          "baseName": "produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/75bca6d94b911baaf7eb028d45d226b5.jpg",
          "name": "Produce",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 212,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524440",
              "name": "Produce",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 212,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524441",
          "baseName": "gyro",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/0749fb68431c3cb19379058c7f535706.jpg",
          "name": "Gyro",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 72,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524442",
              "name": "Gyro",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 72,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524444",
          "baseName": "grocery refrigerated",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b45e7f762ddb1c402037f52e9114d860.jpg",
          "name": "Grocery Refrigerated",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 84,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524445",
              "name": "Grocery Refrigerated",
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
          "id": "325524447",
          "baseName": "pork",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e1214734ee437aead91612889b512b4b.jpg",
          "name": "Pork",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 188,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524448",
              "name": "Pork",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 188,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524450",
          "baseName": "chemical, equipment & supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5a39f63781467b585a59af5d15e4f843.jpg",
          "name": "Chemical, Equipment & Supplies",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 172,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524451",
              "name": "Chemical, Equipment & Supplies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 172,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524452",
          "baseName": "poultry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4808f6b6a8ad04fd6497a372e1c73a4e.jpg",
          "name": "Poultry",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 173,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524453",
              "name": "Poultry",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 173,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325524460",
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/98d355aefe70c8a2a69260ce9a356aeb.jpg",
          "name": "Seafood",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 96,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524461",
              "name": "Seafood",
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
          "id": "325524640",
          "baseName": "vegetarian",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6c73f2d00f1ea9277c53b11939395725.jpg",
          "name": "Vegetarian",
          "sortIndex": "18",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 13,
        "subcategories": [
          {
            "subcategory": {
              "id": "325524641",
              "name": "Vegetarian",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 13,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "325526733",
          "baseName": "warehouse & operations",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/85d0b5379661cef3c39b96643ec62d42.webp",
          "name": "Warehouse & Operations",
          "sortIndex": "19",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1,
        "subcategories": [
          {
            "subcategory": {
              "id": "325526734",
              "name": "Warehouse & Operations",
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
          "id": "325526757",
          "baseName": "oil & shortening",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/346657e0054725f6552ad141a5a219f7.jpg",
          "name": "Oil & Shortening",
          "sortIndex": "20",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 41,
        "subcategories": [
          {
            "subcategory": {
              "id": "325526758",
              "name": "Oil & Shortening",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 41,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'Christ Panos'
	VENDOR_URL_NAME = 'christpanos'
	VERIFIED_VENDOR_ID = 1861896

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY

