
import json
from scrapers.cut.dry import CutScraper


class ChefsKitchenScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/chefs_kitchen/'

	# Values to change
	BASE_URL = "https://ckfresh.cutanddry.com/catalog/ckfresh?verifiedVendorId=165144545&categoryId=1&page=1"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "247481472",
          "baseName": "smallwares + equipment",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/decaa3d17d9d02aea707fc169bab7a86.jpg",
          "name": "Smallwares + Equipment",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 291,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481473",
              "name": "Smallwares + Equipment",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 291,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "247481474",
          "baseName": "frozen",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1fc802236bb0af4781a409355a89fbbd.jpg",
          "name": "Frozen",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 408,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481475",
              "name": "Frozen",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 408,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "247481476",
          "baseName": "grocery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5404dc637d29a06800fb50524d301908.jpg",
          "name": "Grocery",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 2998,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481477",
              "name": "Grocery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2998,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "247481478",
          "baseName": "bakery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9979b28ef46385a2988d8bd5c9751d9f.jpg",
          "name": "Bakery",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 512,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481479",
              "name": "Bakery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 512,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "247481480",
          "baseName": "dairy + eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e7e8432d215f2484b3eee49ef8006e03.jpg",
          "name": "Dairy + Eggs",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 320,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481481",
              "name": "Dairy + Eggs",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 320,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "247481482",
          "baseName": "paper disposables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/619077ad0d86188a14f99ce1bb7add0f.jpg",
          "name": "Paper Disposables",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 542,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481483",
              "name": "Paper Disposables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 542,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "247481484",
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
        "productCount": 438,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481485",
              "name": "Beverage",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 438,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "247481486",
          "baseName": "operational supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e878bd9fcf6cfddb7adf16a477a887e1.jpg",
          "name": "Operational Supplies",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 194,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481487",
              "name": "Operational Supplies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 194,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "247481488",
          "baseName": "janitorial",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d4c07da2b474b3f2ea581add9022d5fc.jpg",
          "name": "Janitorial",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 254,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481489",
              "name": "Janitorial",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 254,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "247481490",
          "baseName": "spices",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e2cb07423eec9fb2d0567cd93bdf0242.jpg",
          "name": "Spices",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 173,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481491",
              "name": "Spices",
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
          "id": "247481492",
          "baseName": "produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/eadb874d1c673816790852e904fa259b.jpg",
          "name": "Produce",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 250,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481493",
              "name": "Produce",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 250,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "247481494",
          "baseName": "meat + game",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bdba4214ac93a9bf35d1a16cfbf7be07.jpg",
          "name": "Meat + Game",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 152,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481495",
              "name": "Meat + Game",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 152,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "247481497",
          "baseName": "deli",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/09ff3639bc850c8d28a9c34a4a5978fe.jpg",
          "name": "Deli",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 54,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481498",
              "name": "Deli",
              "sortIndex": 0,
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
          "id": "247481499",
          "baseName": "poultry + fowl",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/38f0d7ec8ba175451d784f164c672073.jpg",
          "name": "Poultry + Fowl",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 29,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481500",
              "name": "Poultry + Fowl",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 29,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "247481501",
          "baseName": "other",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Other",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 24,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481502",
              "name": "Other",
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
          "id": "247481503",
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2c86b15ff62fd1aa98542d71bd4a22e9.jpg",
          "name": "Seafood",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 74,
        "subcategories": [
          {
            "subcategory": {
              "id": "247481504",
              "name": "Seafood",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 74,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = "Chef's Kitchen"
	VENDOR_URL_NAME = 'ckfresh?'
	VERIFIED_VENDOR_ID = 165144545

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY

