import json
from .dry import CutScraper


class WhatChefsWantSouthScraper(CutScraper):
    """Scraper for What Chefs Want - South on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/whatchefswant_south/'

    # Values to change
    BASE_URL = "https://whatchefswant.cutanddry.com/catalog/What%20Chefs%20Want%20-%20South?verifiedVendorId=240964740&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://whatchefswant.cutanddry.com"
    VENDOR_URL_NAME = 'What%20Chefs%20Want%20-%20South'
    VERIFIED_VENDOR_ID = 240964740

    # This the name of the vendor
    VENDOR_NAME = "What Chefs Want - South"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/87a0ad8ff49d42dccfc84c0d4d790292.jpg",
          "id": "289090334",
          "name": "Produce",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 1238,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 160,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090364",
              "name": "Fruits - Fresh",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 267,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090368",
              "name": "Sliced And Diced Fruits & Veg",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 85,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090370",
              "name": "Lettuces & Greens",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 316,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090378",
              "name": "Vegetables - Fresh",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 175,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090369",
              "name": "Microgreens & Flowers",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 49,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090443",
              "name": "Mushrooms - Fresh",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 42,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090439",
              "name": "Tomatoes",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090335",
              "name": "School Snacks",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 58,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090440",
              "name": "Potatoes",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 47,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090360",
              "name": "Herbs - Fresh",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 34,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090437",
              "name": "Onions",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090484",
              "name": "Chili Peppers - Dried",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "meat",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5e0ebcae581a397f06b21fd2c56c0ae5.jpg",
          "id": "289090381",
          "name": "Meat",
          "sortIndex": "1",
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
              "id": "289090382",
              "name": "Pork",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090410",
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
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/7b919ded4889b7bf4014fbcfe22c6c5f.jpg",
          "id": "289090273",
          "name": "Seafood",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 744,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 263,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090274",
              "name": "Seafood-frozen,can & Specialty",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 103,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090287",
              "name": "Fresh Shellfish",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 376,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090275",
              "name": "Fresh Fish",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "294014304",
              "name": "Alaska Boat Direct",
              "sortIndex": 1
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "gourmet",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/98fb48436473d54c9be18ee032f133b1.jpg",
          "id": "289090341",
          "name": "Gourmet",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 92,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090461",
              "name": "Grains",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090446",
              "name": "Cheeses",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090372",
              "name": "Canned & Jarred Items",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090463",
              "name": "Sauces, Bases & Spreads",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090389",
              "name": "Coffee Shop Products",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090408",
              "name": "Flour & Sugar",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090342",
              "name": "Spices, Salts & Dried Herbs",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090653",
              "name": "Olives",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 46,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090478",
              "name": "Pastas",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090392",
              "name": "Beans - Dried",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090464",
              "name": "Fruit - Dried",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090405",
              "name": "Onions",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "541736709",
              "name": "Seafood-frozen,can & Specialty",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "552033716",
              "name": "Fruits - Fresh",
              "sortIndex": 8
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "staples",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2b3a314e91e2097973be24acdaea9773.jpg",
          "id": "289090268",
          "name": "Staples",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 766,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 98,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090365",
              "name": "Frozen Products & Foods",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 35,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090345",
              "name": "Baking Ingredients",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 42,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090409",
              "name": "Snack Foods / Ready To Eat",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 126,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090272",
              "name": "Beverages & Juices",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 37,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090431",
              "name": "Oils & Vinegars",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090412",
              "name": "Desserts",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090636",
              "name": "Nuts",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090373",
              "name": "Asian Products",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 37,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090391",
              "name": "Spices, Salts & Dried Herbs",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 27,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090346",
              "name": "Jams, Honey & Syrups",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 19,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090269",
              "name": "Flour & Sugar",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 23,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090489",
              "name": "Dressings",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 51,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090363",
              "name": "Breads, Rolls & Pastry",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 115,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090390",
              "name": "Sauces, Bases & Spreads",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090475",
              "name": "Coffee Shop Products",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 75,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090393",
              "name": "Canned & Jarred Items",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 23,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090468",
              "name": "Grains",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090509",
              "name": "Frozen Puree Line",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090791",
              "name": "Food Preparation",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090513",
              "name": "Pastas",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090652",
              "name": "Olives",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090935",
              "name": "Appetizers",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090473",
              "name": "Dairy - Other",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090493",
              "name": "Fruit - Dried",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "371838750",
              "name": "Sliced And Diced Fruits & Veg",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "549238128",
              "name": "Onions",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "601479075",
              "name": "Seafood-frozen,can & Specialty",
              "sortIndex": 5
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dairy & cheeses",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/0c0fc4de954bfefd8dab74017381ca84.jpg",
          "id": "289090398",
          "name": "Dairy & Cheeses",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 428,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 52,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090424",
              "name": "Dairy - Other",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 318,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090399",
              "name": "Cheeses",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 36,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090422",
              "name": "Milk",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "289090423",
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
          "baseName": "to-go & kitchen essentials",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a3f1bc20dd66bd30917b39fcccda0ec1.jpg",
          "id": "289090270",
          "name": "To-go & Kitchen Essentials",
          "sortIndex": "6",
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
              "id": "496163562",
              "name": "Lettuces & Greens",
              "sortIndex": 4
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
