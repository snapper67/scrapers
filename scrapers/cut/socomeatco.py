import json
from .dry import CutScraper


class SoCoMeatCoScraper(CutScraper):
    """Scraper for SoCo Meat Co on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/socomeatco/'

    # Values to change
    BASE_URL = "https://socomeatco.cutanddry.com/catalog/socomeatco?verifiedVendorId=278970797&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://socomeatco.cutanddry.com"
    VENDOR_URL_NAME = 'socomeatco'
    VERIFIED_VENDOR_ID = 278970797

    # This the name of the vendor
    VENDOR_NAME = "SoCo Meat Co"

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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f46f8f75b387f24a6faaf26d7945e7af.jpg",
          "id": "287390561",
          "name": "Beef",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 98,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 98,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "287390562",
              "name": "Beef",
              "sortIndex": 0
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4158fa9234a07cfb7c405cd69ec83f9e.jpg",
          "id": "287391667",
          "name": "Pork",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 87,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 87,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "287391668",
              "name": "Pork",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "lamb",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/cb184ab85a9c0a560c6d8a065753c641.jpg",
          "id": "287392087",
          "name": "Lamb",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 35,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 35,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "287392088",
              "name": "Lamb",
              "sortIndex": 0
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/83a9adcdc2667eeb14e28e6ad59bf2f3.jpg",
          "id": "313439253",
          "name": "Poultry",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 48,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 48,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "313439254",
              "name": "Poultry",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "sausage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/afb2c0a4fca74dc3f53fe472651590be.jpg",
          "id": "316053781",
          "name": "Sausage",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 190,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 190,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "316053782",
              "name": "Sausage",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "smoked",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9bf9524520a0d46230774c1b38c126d8.jpg",
          "id": "287393092",
          "name": "Smoked",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 28,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 28,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "287393093",
              "name": "Smoked",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "grab & go",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b618fc83b497b8a777abe20adfa2ae5b.jpg",
          "id": "287393198",
          "name": "Grab & Go",
          "sortIndex": "7",
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
              "id": "294708182",
              "name": "Grab & Go",
              "sortIndex": 4
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "veal",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bc9b5173cc0de9610385735567d67d5b.jpg",
          "id": "389702517",
          "name": "Veal",
          "sortIndex": "9",
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
              "id": "389702518",
              "name": "Veal",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "turkey",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fa1c3c6492e77e83e8d4357830e426a0.jpg",
          "id": "310557837",
          "name": "Turkey",
          "sortIndex": "10",
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
              "id": "310557839",
              "name": "Turkey",
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
