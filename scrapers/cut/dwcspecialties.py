import json
from .dry import CutScraper


class DWCSpecialtiesScraper(CutScraper):
    """Scraper for DWC Specialties on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/dwcspecialties/'

    # Values to change
    BASE_URL = "https://dwcspecialties.cutanddry.com/catalog/dwcspecialties?verifiedVendorId=214281348&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://dwcspecialties.cutanddry.com"
    VENDOR_URL_NAME = 'dwcspecialties'
    VERIFIED_VENDOR_ID = 214281348

    # This the name of the vendor
    VENDOR_NAME = "DWC Specialties"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "228536828",
          "baseName": "bakery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fc87cc0526cff6dbe415accbdc2854bf.jpg",
          "name": "Bakery",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 113,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536829",
              "name": "Bakery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 113,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "228536830",
          "baseName": "beverages",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/622063cb96e1f64c12b2975dd785f2a7.jpg",
          "name": "Beverages",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 60,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536831",
              "name": "Beverages",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 60,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "228536817",
          "baseName": "blended mixes",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/185d5c026dfb5abfcff9b3f77d5bde08.jpg",
          "name": "Blended Mixes",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 124,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536818",
              "name": "Blended Mixes",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 124,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "228536819",
          "baseName": "cafe supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5d072799fdadfdcffdafb15e6c847b31.jpg",
          "name": "Cafe Supplies",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 147,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536820",
              "name": "Cafe Supplies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 147,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "228536837",
          "baseName": "disposables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/ebb798f3370b1e0e34f6d6c938ac6922.jpg",
          "name": "Disposables",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 199,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536838",
              "name": "Disposables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 199,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "228536835",
          "baseName": "energy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f8e0ea8c81555606cbbd1c478669c951.jpg",
          "name": "Energy",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 64,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536836",
              "name": "Energy",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 64,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "228536822",
          "baseName": "food service",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/45f78871bdcf6573f426f375013539e0.jpg",
          "name": "Food Service",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 165,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536823",
              "name": "Food Service",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 165,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "228536824",
          "baseName": "ingredients",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/ef15e7ff87b7eea96a75cadd5afb1678.jpg",
          "name": "Ingredients",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 35,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536825",
              "name": "Ingredients",
              "sortIndex": 0,
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
          "id": "228536842",
          "baseName": "nondairy milk",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/df69c3be2619890553d45b5c2ad6ae87.jpg",
          "name": "Nondairy Milk",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 20,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536843",
              "name": "Nondairy Milk",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 20,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "228536826",
          "baseName": "packaging",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/326de237451479ffc9beeb1afbe07683.jpg",
          "name": "Packaging",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 120,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536827",
              "name": "Packaging",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 120,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "228536839",
          "baseName": "sauce & powders",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5b095ebb63f2054c0ae41ed53a3113b9.jpg",
          "name": "Sauce & Powders",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 52,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536840",
              "name": "Sauce & Powders",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 52,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "228536815",
          "baseName": "syrups",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e1c0c7d60a8e823877357978f7520002.jpg",
          "name": "Syrups",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 371,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536816",
              "name": "Syrups",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 371,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "228536832",
          "baseName": "tea",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a626066e2054db2ff8b7697b3d0517a6.jpg",
          "name": "Tea",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 127,
        "subcategories": [
          {
            "subcategory": {
              "id": "228536833",
              "name": "Tea",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 127,
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
