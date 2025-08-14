
import json
from scrapers.cut.dry import CutScraper


class MapleValeScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/maple_vale/'


	# Values to change
	BASE_URL = "https://maplevale.cutanddry.com/catalog/maplevale?verifiedVendorId=106423628&categoryId=1&page=1"
	SUB_DOMAIN = "https://maplevale.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "120035269",
          "baseName": "steaks",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Steaks.png",
          "name": "Steaks",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 473,
        "subcategories": [
          {
            "subcategory": {
              "id": "120043907",
              "name": "Steaks",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 473,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120035281",
          "baseName": "specialty items",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Specialty Items.png",
          "name": "Specialty Items",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 772,
        "subcategories": [
          {
            "subcategory": {
              "id": "120043913",
              "name": "Specialty Items",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 772,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120035378",
          "baseName": "poultry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Poultry.png",
          "name": "Poultry",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 387,
        "subcategories": [
          {
            "subcategory": {
              "id": "120043969",
              "name": "Poultry",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 387,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120035401",
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Seafood.png",
          "name": "Seafood",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 249,
        "subcategories": [
          {
            "subcategory": {
              "id": "120044182",
              "name": "Seafood",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 249,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120035503",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Dairy.png",
          "name": "Dairy",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 650,
        "subcategories": [
          {
            "subcategory": {
              "id": "120044193",
              "name": "Dairy",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 650,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120035542",
          "baseName": "produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Produce.png",
          "name": "Produce",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 312,
        "subcategories": [
          {
            "subcategory": {
              "id": "120044287",
              "name": "Produce",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 312,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120035548",
          "baseName": "beverages",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Beverages.png",
          "name": "Beverages",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 165,
        "subcategories": [
          {
            "subcategory": {
              "id": "120044290",
              "name": "Beverages",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 165,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120035903",
          "baseName": "disposables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Disposable.png",
          "name": "Disposables",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 810,
        "subcategories": [
          {
            "subcategory": {
              "id": "120044550",
              "name": "Disposables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 810,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120043908",
          "baseName": "meat",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Meat.png",
          "name": "Meat",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 913,
        "subcategories": [
          {
            "subcategory": {
              "id": "120043909",
              "name": "Meat",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 913,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120043979",
          "baseName": "frozen foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Frozen+Foods.png",
          "name": "Frozen Foods",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1078,
        "subcategories": [
          {
            "subcategory": {
              "id": "120043981",
              "name": "Frozen Foods",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1078,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120044179",
          "baseName": "pantry essentials",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Pantry+Essentials.png",
          "name": "Pantry Essentials",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 823,
        "subcategories": [
          {
            "subcategory": {
              "id": "120044180",
              "name": "Pantry Essentials",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 823,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120044190",
          "baseName": "grocery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Grocery.png",
          "name": "Grocery",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1957,
        "subcategories": [
          {
            "subcategory": {
              "id": "120044191",
              "name": "Grocery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1957,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120044196",
          "baseName": "kitchen utensils",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Kitchen+Utensils.png",
          "name": "Kitchen Utensils",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 482,
        "subcategories": [
          {
            "subcategory": {
              "id": "120044197",
              "name": "Kitchen Utensils",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 482,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120044211",
          "baseName": "bakery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Bakery.png",
          "name": "Bakery",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 906,
        "subcategories": [
          {
            "subcategory": {
              "id": "120044212",
              "name": "Bakery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 906,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "120035271",
          "baseName": "other",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/106423628/Other.png",
          "name": "Other",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 936,
        "subcategories": [
          {
            "subcategory": {
              "id": "120044183",
              "name": "Other",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 936,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'Maple Vale'
	VENDOR_URL_NAME = 'maplevale'
	VERIFIED_VENDOR_ID = 106423628



	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY

