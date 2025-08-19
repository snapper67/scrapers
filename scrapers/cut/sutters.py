import json
from .dry import CutScraper


class SuttersScraper(CutScraper):
    """Scraper for Sutter's Food Group on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/sutters/'

    # Values to change
    BASE_URL = "https://sutters.cutanddry.com/catalog/suttersfoodgroup?verifiedVendorId=156080417&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://sutters.cutanddry.com"
    VENDOR_URL_NAME = 'suttersfoodgroup'
    VERIFIED_VENDOR_ID = 156080417

    # This the name of the vendor
    VENDOR_NAME = "Sutter's Food Group"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/3d0eae860a869de3d4033fed0179b9f7.jpg",
          "id": "178182092",
          "name": "Eggs",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 10,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "178182093",
              "name": "Eggs",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cheese",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/86acb3a008262c6dff27fde62bf23294.jpg",
          "id": "178182094",
          "name": "Cheese",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 68,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 68,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "178182095",
              "name": "Cheese",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "butter",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6f443f09a0d1cb10e2135b861c92ed4f.jpg",
          "id": "178182096",
          "name": "Butter",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 11,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "178182097",
              "name": "Butter",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fe05c26bda2295417ba303406089dc20.jpg",
          "id": "178182100",
          "name": "Dairy",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 38,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 38,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "178182101",
              "name": "Dairy",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "juice",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/74299c80281e2cabdab0473c63962476.jpg",
          "id": "178182102",
          "name": "Juice",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 21,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 21,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "178182103",
              "name": "Juice",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "soft serve mix",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/ecbd7d9537678516f0a14d9b8b84126f.jpg",
          "id": "178182104",
          "name": "Soft Serve Mix",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 14,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 14,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "178182105",
              "name": "Soft Serve Mix",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "frozen yogurt",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/0c83012332da3771a9fa40a35f4bc9fd.jpg",
          "id": "178182106",
          "name": "Frozen Yogurt",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 2,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "178182107",
              "name": "Frozen Yogurt",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "toppings",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5a97ecf95c217d11e8264b44a9ab9a5b.webp",
          "id": "178182108",
          "name": "Toppings",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 3,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "178182109",
              "name": "Toppings",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fruit",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4460259c30fa3abf4cc8a98a145fe4db.jpg",
          "id": "178182116",
          "name": "Fruit",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 2,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "178182117",
              "name": "Fruit",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cones",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6bed1a2a1e9e827edb34f5c66ee00432.jpg",
          "id": "178182118",
          "name": "Cones",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 2,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "178182119",
              "name": "Cones",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "paper goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4f62e015bbcd199270699fa815d16405.jpg",
          "id": "178182120",
          "name": "Paper Goods",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 7,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "178182121",
              "name": "Paper Goods",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "ice cream",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a4a4574313f5f2fc42657b82f83a303d.jpg",
          "id": "178182122",
          "name": "Ice Cream",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 92,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 92,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "178182123",
              "name": "Ice Cream",
              "sortIndex": 0
            }
          }
        ]
      }
    ]
  }
}
    ''')

    def __init__(self, options=None):
        super().__init__(options)
        self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
        self.options['home_directory'] = self.DEFAULT_DIRECTORY
        self.options['base_url'] = self.BASE_URL