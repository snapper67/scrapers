import json
from .dry import CutScraper


class CreamCoScraper(CutScraper):
    """Scraper for CreamCo on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/creamco/'

    # Values to change
    BASE_URL = "https://app.cutanddry.com/catalog/creamco?verifiedVendorId=106701122&page=1&categoryId=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://app.cutanddry.com"
    VENDOR_URL_NAME = 'creamco'
    VERIFIED_VENDOR_ID = 106701122

    # This the name of the vendor
    VENDOR_NAME = "Cream Co Meats"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "181840095",
          "baseName": "beef",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d408e0233d322219a4ccae08d4fa18c0.jpg",
          "name": "Beef",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 189,
        "subcategories": [
          {
            "subcategory": {
              "id": "181840096",
              "name": "Beef",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 189,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "181840093",
          "baseName": "lamb",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/32261b426a16286e1eceb3ac7de793c7.jpg",
          "name": "Lamb",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 27,
        "subcategories": [
          {
            "subcategory": {
              "id": "181840094",
              "name": "Lamb",
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
          "id": "181840097",
          "baseName": "pork",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/14855e41bd163ab1f74bfe795364ee13.jpg",
          "name": "Pork",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 70,
        "subcategories": [
          {
            "subcategory": {
              "id": "181840098",
              "name": "Pork",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 70,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "181840099",
          "baseName": "chicken",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e7d0ce2423e03710275e40afe061fdda.jpg",
          "name": "Chicken",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 34,
        "subcategories": [
          {
            "subcategory": {
              "id": "181840100",
              "name": "Chicken",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 34,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "181840105",
          "baseName": "wagyu",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/16f044ec486a0bed4a3b90ebe1ffe20c.jpg",
          "name": "Wagyu",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 2,
        "subcategories": [
          {
            "subcategory": {
              "id": "181840106",
              "name": "Wagyu",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "182037447",
          "baseName": "turkey",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/286b9c129ba209203e64d4528c471294.jpg",
          "name": "Turkey",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 26,
        "subcategories": [
          {
            "subcategory": {
              "id": "182037547",
              "name": "Turkey",
              "sortIndex": 1,
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
          "id": "181840101",
          "baseName": "value added",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8f566dc1ec6355b231358f56d18367d6.jpg",
          "name": "Value Added",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 28,
        "subcategories": [
          {
            "subcategory": {
              "id": "181840102",
              "name": "Value Added",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 28,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "232337324",
          "baseName": "poultry + game",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fc025896029bdad0a3efcd62990a6c45.jpg",
          "name": "Poultry + Game",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 4,
        "subcategories": [
          {
            "subcategory": {
              "id": "232337325",
              "name": "Poultry + Game",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
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
