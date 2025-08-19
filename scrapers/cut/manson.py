
import json
from scrapers.cut.dry import CutScraper


class MansonScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/manson/'

	# Values to change
	BASE_URL = "https://manson.cutanddry.com/catalog/MansonProducts?verifiedVendorId=160779759&categoryId=1&page=1"
	SUB_DOMAIN = "https://manson.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "233831963",
          "baseName": "vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b6f3baa659ccaf0044ae7b3ce48b4874.jpg",
          "name": "Vegetables",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 268,
        "subcategories": [
          {
            "subcategory": {
              "id": "233831964",
              "name": "Vegetables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 268,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "233831968",
          "baseName": "fruits",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d6158381e2d184da7e7f23e025af95df.jpg",
          "name": "Fruits",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 96,
        "subcategories": [
          {
            "subcategory": {
              "id": "233831969",
              "name": "Fruits",
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
          "id": "233832289",
          "baseName": "processed items",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8eab994121b2562b1f465e36af566101.jpg",
          "name": "Processed Items",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 27,
        "subcategories": [
          {
            "subcategory": {
              "id": "233832290",
              "name": "Processed Items",
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
          "id": "233832550",
          "baseName": "miscellaneous",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/93ce38e467b14e5dc6e709a66d1169eb.jpg",
          "name": "Miscellaneous",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 16,
        "subcategories": [
          {
            "subcategory": {
              "id": "233832551",
              "name": "Miscellaneous",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "233832958",
          "baseName": "sprouts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/62fb47d4f13cfe0efb7ae204c0975f0c.jpg",
          "name": "Sprouts",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 10,
        "subcategories": [
          {
            "subcategory": {
              "id": "233832959",
              "name": "Sprouts",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "233833482",
          "baseName": "eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/11f83f399e08599a8d1eadfc4e24cfc8.webp",
          "name": "Eggs",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 11,
        "subcategories": [
          {
            "subcategory": {
              "id": "233833483",
              "name": "Eggs",
              "sortIndex": 0,
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
          "id": "233833616",
          "baseName": "mari's garden micros/flowers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/46a07f4c0614d5e63ce7cf91d3a8af61.jpg",
          "name": "Mari's Garden Micros/flowers",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 5,
        "subcategories": [
          {
            "subcategory": {
              "id": "233833617",
              "name": "Mari's Garden Micros/flowers",
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
          "id": "233833812",
          "baseName": "herbs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/974667ff6cfa217d90d0d52504377c71.jpg",
          "name": "Herbs",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 39,
        "subcategories": [
          {
            "subcategory": {
              "id": "233833813",
              "name": "Herbs",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 39,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "233834240",
          "baseName": "salads",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/cb681fbb18c47c0e7bd9979b5b4b8e41.jpg",
          "name": "Salads",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 13,
        "subcategories": [
          {
            "subcategory": {
              "id": "233834241",
              "name": "Salads",
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
          "id": "233834950",
          "baseName": "mushrooms",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e6f30e0ebb9674382e16322a7e6e3979.jpg",
          "name": "Mushrooms",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 26,
        "subcategories": [
          {
            "subcategory": {
              "id": "233834951",
              "name": "Mushrooms",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 26,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "233836925",
          "baseName": "tofu",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/7c71e18bd64c9c442a500ad034deb41b.jpg",
          "name": "Tofu",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 7,
        "subcategories": [
          {
            "subcategory": {
              "id": "233836926",
              "name": "Tofu",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "281434391",
          "baseName": "specialty items w/ lead times",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/01215b8129cfb2bacd938897cfaa686e.webp",
          "name": "Specialty Items W/ Lead Times",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 85,
        "subcategories": [
          {
            "subcategory": {
              "id": "281434392",
              "name": "Specialty Items W/ Lead Times",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 85,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'Manson Products'
	VENDOR_URL_NAME = 'MansonProducts'
	VERIFIED_VENDOR_ID = 160779759

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY
		self.options['base_url'] = self.BASE_URL
