import json
from .dry import CutScraper


class MisterProduceScraper(CutScraper):
    """Scraper for Mister Produce on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/misterproduce/'

    # Values to change
    BASE_URL = "https://misterproduce.cutanddry.com/catalog/misterproduce?verifiedVendorId=286181355&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://misterproduce.cutanddry.com"
    VENDOR_URL_NAME = 'misterproduce'
    VERIFIED_VENDOR_ID = 286181355

    # This the name of the vendor
    VENDOR_NAME = "Mister Produce"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "prepared veg",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/afd55fff40baffae75fa4573b2b1f1c8.jpg",
          "id": "346124635",
          "name": "Prepared Veg",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 163,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 163,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "346124636",
              "name": "Prepared Veg",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fresh veg",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1dc5e5c7b912fd2d8e4b7f6d7fef579e.jpg",
          "id": "346167397",
          "name": "Fresh Veg",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 254,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 254,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "346167398",
              "name": "Fresh Veg",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "herbs & garnishes",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bbcb850a1e99e40886b8106e28727d65.jpg",
          "id": "346167399",
          "name": "Herbs & Garnishes",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 75,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 75,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "346167400",
              "name": "Herbs & Garnishes",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "miscellaneous products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2bf3044d8c21d7614febcd1fda75ea5a.jpg",
          "id": "346167404",
          "name": "Miscellaneous Products",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 13,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "346167405",
              "name": "Miscellaneous Products",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fresh fruit",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8ed58fb008b6d896f589170d961c2fbd.jpg",
          "id": "346167417",
          "name": "Fresh Fruit",
          "sortIndex": "4",
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
              "id": "346167418",
              "name": "Fresh Fruit",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "juice products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/41cb4fdf1ba41f7266f29e3ce250e5f6.jpg",
          "id": "346167419",
          "name": "Juice Products",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 24,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "346167420",
              "name": "Juice Products",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "prepared fruits",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/82a050a9a832715b5d4e85d2a5d8a394.jpg",
          "id": "346167436",
          "name": "Prepared Fruits",
          "sortIndex": "7",
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
              "id": "346167437",
              "name": "Prepared Fruits",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dried fruit & nuts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/69c7c3d2e5a46d28ed1d4ddbf0a124ab.jpg",
          "id": "346167515",
          "name": "Dried Fruit & Nuts",
          "sortIndex": "8",
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
              "id": "346167516",
              "name": "Dried Fruit & Nuts",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "puree herbs in oil",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/83576497c4a1314148be9a0f44f28a57.jpg",
          "id": "346167569",
          "name": "Puree Herbs in Oil",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 1,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "346167570",
              "name": "Puree Herbs in Oil",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "french fries",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/132bb0b393d13a406754dd090eebaec2.jpg",
          "id": "346167572",
          "name": "French Fries",
          "sortIndex": "10",
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
              "id": "346167573",
              "name": "French Fries",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "frozen products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fe9321f053e3f77feb347bc701c8fc91.jpg",
          "id": "346167574",
          "name": "Frozen Products",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 26,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 26,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "346167575",
              "name": "Frozen Products",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fresh pasta",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/628f8ab305cdaed97cceff784e385d21.jpg",
          "id": "346167576",
          "name": "Fresh Pasta",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 6,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "346167577",
              "name": "Fresh Pasta",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "mushrooms",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1afafc891c0011edc5440a6177a342cc.jpg",
          "id": "415585405",
          "name": "Mushrooms",
          "sortIndex": "21",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 13,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "415585406",
              "name": "Mushrooms",
              "sortIndex": 10
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dairy items",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4c12eba6ceda78c9bab5cd84d1da94ec.jpg",
          "id": "431083590",
          "name": "Dairy Items",
          "sortIndex": "22",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 85,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 85,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "431083591",
              "name": "Dairy Items",
              "sortIndex": 11
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
