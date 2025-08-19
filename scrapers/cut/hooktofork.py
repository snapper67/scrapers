import json
from .dry import CutScraper


class HookToForkScraper(CutScraper):
    """Scraper for Hook to Fork on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/hooktofork/'

    # Values to change
    BASE_URL = "https://hooktofork.cutanddry.com/catalog/hooktofork?verifiedVendorId=152922131&categoryId=1&page=1"
    
    # These values are pulled from the base URL
    SUB_DOMAIN = "https://hooktofork.cutanddry.com"
    VENDOR_URL_NAME = 'hooktofork'
    VERIFIED_VENDOR_ID = 152922131
    
    # This the name of the vendor
    VENDOR_NAME = "Hook to Fork"
    
    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dry goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f9fcc24f0a953a8b1287663e9ee68d07.jpg",
          "id": "365271059",
          "name": "Dry Goods",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 349,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 349,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "365271060",
              "name": "Dry Goods",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "meat + game",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b6b47229ad72db189affb43e775a82dc.jpg",
          "id": "365271061",
          "name": "Meat + Game",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 308,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 308,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "365271062",
              "name": "Meat + Game",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "poultry + fowl",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4808f6b6a8ad04fd6497a372e1c73a4e.jpg",
          "id": "365271064",
          "name": "Poultry + Fowl",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 86,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 86,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "365271065",
              "name": "Poultry + Fowl",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8b3f43cfab9852f85a908b932ac80aa8.jpg",
          "id": "365271066",
          "name": "Produce",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 61,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 61,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "365272721",
              "name": "Produce",
              "sortIndex": 1
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/98d355aefe70c8a2a69260ce9a356aeb.jpg",
          "id": "365271067",
          "name": "Seafood",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 728,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 728,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "609714816",
              "name": "Seafood",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "wild mushrooms & truffles",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/0b84b1ac22df3f513e8dc90d6dd7200a.jpg",
          "id": "365271069",
          "name": "Wild Mushrooms & Truffles",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 30,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 30,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "578386150",
              "name": "Wild Mushrooms & Truffles",
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