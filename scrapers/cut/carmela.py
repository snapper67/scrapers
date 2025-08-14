
import json
from scrapers.cut.dry import CutScraper


class CarmelaScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/carmela/'


	# Values to change
	BASE_URL = "https://app.cutanddry.com/catalog/carmela?verifiedVendorId=174874579&categoryId=1&page=1"
	SUB_DOMAIN = "https://app.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "219987189",
          "baseName": "dry grocery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5404dc637d29a06800fb50524d301908.jpg",
          "name": "Dry Grocery",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 3175,
        "subcategories": [
          {
            "subcategory": {
              "id": "219987190",
              "name": "Dry Grocery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3175,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "220182397",
          "baseName": "fresh herbs/produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1d4f5a7df3f5c262eeaa20c96bba84a0.jpg",
          "name": "Fresh Herbs/produce",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 11,
        "subcategories": [
          {
            "subcategory": {
              "id": "220182398",
              "name": "Fresh Herbs/produce",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "220182399",
          "baseName": "land based protein",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bdba4214ac93a9bf35d1a16cfbf7be07.jpg",
          "name": "Land Based Protein",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1687,
        "subcategories": [
          {
            "subcategory": {
              "id": "220182400",
              "name": "Land Based Protein",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1687,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "220182401",
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2c86b15ff62fd1aa98542d71bd4a22e9.jpg",
          "name": "Seafood",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1056,
        "subcategories": [
          {
            "subcategory": {
              "id": "220182402",
              "name": "Seafood",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1056,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "220182403",
          "baseName": "cheese",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/503e5f0cffd759fc1963a46dd6adb1f5.jpg",
          "name": "Cheese",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 715,
        "subcategories": [
          {
            "subcategory": {
              "id": "220182404",
              "name": "Cheese",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 715,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "220182405",
          "baseName": "deli",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/09ff3639bc850c8d28a9c34a4a5978fe.jpg",
          "name": "Deli",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 369,
        "subcategories": [
          {
            "subcategory": {
              "id": "220182406",
              "name": "Deli",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 369,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "220182407",
          "baseName": "frozen dessert",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5ffa0cee54f74109011cbd55e156108d.jpg",
          "name": "Frozen Dessert",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 170,
        "subcategories": [
          {
            "subcategory": {
              "id": "220182408",
              "name": "Frozen Dessert",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 170,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "220182409",
          "baseName": "beverage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2a4362a643dcf116294f19fcd185c6b5.jpg",
          "name": "Beverage",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 235,
        "subcategories": [
          {
            "subcategory": {
              "id": "220182410",
              "name": "Beverage",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 235,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "220182411",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/ff7766eca59f58a4ebaee1b0617f93d2.jpg",
          "name": "Dairy",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 35,
        "subcategories": [
          {
            "subcategory": {
              "id": "220182412",
              "name": "Dairy",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 35,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "220182414",
          "baseName": "coffee",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/12925d04fd2c48ca9711672f59fed5b0.jpg",
          "name": "Coffee",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 202,
        "subcategories": [
          {
            "subcategory": {
              "id": "220182415",
              "name": "Coffee",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 202,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "220182420",
          "baseName": "frozen bakery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9979b28ef46385a2988d8bd5c9751d9f.jpg",
          "name": "Frozen Bakery",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 252,
        "subcategories": [
          {
            "subcategory": {
              "id": "220182421",
              "name": "Frozen Bakery",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 252,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "220182422",
          "baseName": "chef source",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b65866364c50b6a31fa55d7356aa587d.jpg",
          "name": "Chef Source",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 2507,
        "subcategories": [
          {
            "subcategory": {
              "id": "220182423",
              "name": "Chef Source",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2507,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "220182428",
          "baseName": "frozen grocery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1fc802236bb0af4781a409355a89fbbd.jpg",
          "name": "Frozen Grocery",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 237,
        "subcategories": [
          {
            "subcategory": {
              "id": "220182429",
              "name": "Frozen Grocery",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 237,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "456485712",
          "baseName": "frozen",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Frozen",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 2,
        "subcategories": [
          {
            "subcategory": {
              "id": "456485713",
              "name": "Frozen",
              "sortIndex": 3,
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

	VENDOR_NAME = 'Carmela'
	VENDOR_URL_NAME = 'carmela'
	VENDOR_ID = 174874579
	VERIFIED_VENDOR_ID = 174874579

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY

