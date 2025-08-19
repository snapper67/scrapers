import json
from .dry import CutScraper


class ValleyGoldScraper(CutScraper):
    """Scraper for Valley Gold on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/valleygold/'

    # Values to change
    BASE_URL = "https://valleygold.cutanddry.com/catalog/Valley%20Gold?verifiedVendorId=483829152&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://valleygold.cutanddry.com"
    VENDOR_URL_NAME = 'Valley%20Gold'
    VERIFIED_VENDOR_ID = 483829152

    # This the name of the vendor
    VENDOR_NAME = "Valley Gold"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "beef",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a099a87516660f84eb9d43470beb2974.jpg",
          "id": "506617612",
          "name": "Beef",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 77,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 19,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506617614",
              "name": "Premium Angus",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506617615",
              "name": "Premium Grinds",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 37,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506617616",
              "name": "Premium Wagyu",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506617617",
              "name": "Pre-Cut Steaks",
              "sortIndex": 4
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "charcuterie",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/81437b0a6f8d74b19bb130a24e2b7fb9.jpg",
          "id": "506618070",
          "name": "Charcuterie",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 9,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506618071",
              "name": "Charcuterie",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "deli",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1e164963ab4f8ba5b2db2377e3743cb1.jpg",
          "id": "506618486",
          "name": "Deli",
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
              "id": "506618487",
              "name": "Deli",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "game",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fcb9a477641949f08d3f226476d8fba9.jpg",
          "id": "506618596",
          "name": "Game",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 2,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506618598",
              "name": "Bison",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506618599",
              "name": "Venison",
              "sortIndex": 2
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "pork",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/62eea9e89d3a3ac5fd36d8cccb4887d7.jpg",
          "id": "506619402",
          "name": "Pork",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 40,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506619404",
              "name": "Nashvill Local Duroc",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 17,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506619405",
              "name": "Premium",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506619406",
              "name": "Bacon",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506619407",
              "name": "Ham",
              "sortIndex": 4
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "poultry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8cae37f48ee902865ef2b26f486b5c76.jpg",
          "id": "506619740",
          "name": "Poultry",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 9,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506619741",
              "name": "Poultry",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506619742",
              "name": "Chicken",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506619743",
              "name": "Duck",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506619744",
              "name": "Quail",
              "sortIndex": 3
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a60f085b2a979da3c3d857e2798d394b.jpg",
          "id": "506620015",
          "name": "Seafood",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 9,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506620017",
              "name": "Shellfish",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506620018",
              "name": "Finfish",
              "sortIndex": 2
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "smoked meats",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2232c7cf4a4aad9c6a7c386be6eeefe8.jpg",
          "id": "506620323",
          "name": "Smoked Meats",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 25,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506620325",
              "name": "Catering",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506620326",
              "name": "Sausage",
              "sortIndex": 2
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
