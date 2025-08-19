import json
from .dry import CutScraper


class AllFreshSeafoodScraper(CutScraper):
    """Scraper for All Fresh Seafood on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/all_fresh_seafood/'

    # Values to change
    BASE_URL = "https://allfreshseafood.cutanddry.com/catalog/allfreshseafood?verifiedVendorId=232473144&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://allfreshseafood.cutanddry.com"
    VENDOR_URL_NAME = 'allfreshseafood'
    VERIFIED_VENDOR_ID = 232473144

    # This the name of the vendor
    VENDOR_NAME = "All Fresh Seafood"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "307419954",
          "baseName": "fresh fish",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8abbf686418e0814d1703d68c639c388.jpg",
          "name": "Fresh Fish",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 42,
        "subcategories": [
          {
            "subcategory": {
              "id": "307419955",
              "name": "Fresh Fish",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 42,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "307315118",
          "baseName": "quality meat",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a068c16516c7b97db5571cef9d07e1de.jpg",
          "name": "Quality Meat",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 26,
        "subcategories": [
          {
            "subcategory": {
              "id": "307315119",
              "name": "Quality Meat",
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
          "id": "307317273",
          "baseName": "caviar",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bbe96feba519427d733a8baed6168a0b.jpg",
          "name": "Caviar",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 10,
        "subcategories": [
          {
            "subcategory": {
              "id": "307321203",
              "name": "Caviar",
              "sortIndex": 1,
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
          "id": "307318977",
          "baseName": "smoked fish",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/c083f099322627b614e101da18544e27.webp",
          "name": "Smoked fish",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 6,
        "subcategories": [
          {
            "subcategory": {
              "id": "307322011",
              "name": "Smoked fish",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "307323963",
          "baseName": "shellfish",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d41f911204e543a20fcbf548b3ce2422.jpg",
          "name": "Shellfish",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 12,
        "subcategories": [
          {
            "subcategory": {
              "id": "307323964",
              "name": "Shellfish",
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
          "id": "307326240",
          "baseName": "lobster & crab",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f9184f01c0b793afab4bc89f7595fd42.jpg",
          "name": "Lobster & Crab",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 19,
        "subcategories": [
          {
            "subcategory": {
              "id": "307326241",
              "name": "Lobster & Crab",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 19,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "307328845",
          "baseName": "prepared food",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5b2a8fbd3bff5ebebf4df78f0cf2a403.jpg",
          "name": "Prepared food",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 23,
        "subcategories": [
          {
            "subcategory": {
              "id": "307330309",
              "name": "Prepared food",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 23,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "307338079",
          "baseName": "soups",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/262bd827e689007b37cb53ff4ded321c.jpg",
          "name": "Soups",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 5,
        "subcategories": [
          {
            "subcategory": {
              "id": "307338080",
              "name": "Soups",
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
          "id": "307339431",
          "baseName": "salads",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/906ea13389c09d7b93cc8ce1860927b3.jpg",
          "name": "Salads",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 8,
        "subcategories": [
          {
            "subcategory": {
              "id": "307339432",
              "name": "Salads",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "307340773",
          "baseName": "sauces",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b6f3c5039fd306ff1b1a32e75dcd6eae.webp",
          "name": "Sauces",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 12,
        "subcategories": [
          {
            "subcategory": {
              "id": "307340774",
              "name": "Sauces",
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
          "id": "307342474",
          "baseName": "dumplings",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/aba8d555af20e47ba6ac39d634f85eaa.jpg",
          "name": "Dumplings",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 8,
        "subcategories": [
          {
            "subcategory": {
              "id": "307342475",
              "name": "Dumplings",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
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
