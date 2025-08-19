import json
from .dry import CutScraper


class JordanPaigeScraper(CutScraper):
    """Scraper for Jordan Paige on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/jordanpaige/'

    # Values to change
    BASE_URL = "https://jordanpaige.cutanddry.com/catalog/jordanpaige?verifiedVendorId=178111284&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://jordanpaige.cutanddry.com"
    VENDOR_URL_NAME = 'jordanpaige'
    VERIFIED_VENDOR_ID = 178111284

    # This the name of the vendor
    VENDOR_NAME = "Jordan Paige"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "hors d oeuvres",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/748dfe225b31272b14a6a49a9808098c.jpg",
          "id": "305036417",
          "name": "Hors D Oeuvres",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 192,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 192,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "305036418",
              "name": "Hors D Oeuvres",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "desserts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/45588b9876c2c44af50ae328fca63546.jpg",
          "id": "228536554",
          "name": "Desserts",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 129,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 129,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536555",
              "name": "Desserts",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "icecream",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f589a70214bd0fe2b807be89a84cd926.jpg",
          "id": "228536561",
          "name": "Icecream",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 66,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 66,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536562",
              "name": "Icecream",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cheese & dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/31ddde732abf388d3eaca98750d165e1.jpg",
          "id": "228536552",
          "name": "Cheese & Dairy",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 140,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 140,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536553",
              "name": "Cheese & Dairy",
              "sortIndex": 0
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a31586bbe6edc6d7f6d8c4f056d2f5b4.jpg",
          "id": "228536540",
          "name": "Charcuterie",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 57,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 57,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536541",
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
          "baseName": "chocolate & baking & pastry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b24cf3d961ebe8aecce6a96c05c08568.jpg",
          "id": "228536544",
          "name": "Chocolate & Baking & Pastry",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 258,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 258,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536545",
              "name": "Chocolate & Baking & Pastry",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "pantry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/0b1d0b4c86b0c8a290f88923f3ad6b4c.jpg",
          "id": "228536534",
          "name": "Pantry",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 208,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 208,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536535",
              "name": "Pantry",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "oils & vinegars",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/09b207c5fb4aee3b0ceb2f05991203a5.jpg",
          "id": "228536550",
          "name": "Oils & Vinegars",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 41,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 41,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536551",
              "name": "Oils & Vinegars",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "bakery & breads",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9979b28ef46385a2988d8bd5c9751d9f.jpg",
          "id": "228536557",
          "name": "Bakery & Breads",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 214,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 214,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536558",
              "name": "Bakery & Breads",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "asian & ethnic specialty",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/087ecca7b9ae81f5a3d7af7ecd3264a3.jpg",
          "id": "228536536",
          "name": "Asian & Ethnic Specialty",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 119,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 119,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536537",
              "name": "Asian & Ethnic Specialty",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "nuts & fruits & vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/43d06985178b7c27a93aa77170f3fd35.jpg",
          "id": "228536548",
          "name": "Nuts & Fruits & Vegetables",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 136,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 136,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536549",
              "name": "Nuts & Fruits & Vegetables",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "grains & beans & flour",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fbaef35251428238a3c286b9f6167b8b.jpg",
          "id": "228536546",
          "name": "Grains & Beans & Flour",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 71,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 71,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536547",
              "name": "Grains & Beans & Flour",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "pasta",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e4d79a5e95032e5ab7e6881b7e21d98c.jpg",
          "id": "228536559",
          "name": "Pasta",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 43,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 43,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536560",
              "name": "Pasta",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "meat & poultry & seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/32baf3be47e79cb815fc9c71037cd6b6.jpg",
          "id": "228536542",
          "name": "Meat & Poultry & Seafood",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 95,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 95,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536543",
              "name": "Meat & Poultry & Seafood",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "supplies & beverages",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1b9d63b0f92b693812d9c3bbfc2bb6bd.jpg",
          "id": "228536532",
          "name": "Supplies & Beverages",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 94,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 94,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "228536533",
              "name": "Supplies & Beverages",
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