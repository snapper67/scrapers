import json
from .dry import CutScraper


class WhatChefsWantRockiesScraper(CutScraper):
    """Scraper for What Chefs Want - South on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/whatchefswant_rockies/'

    # Values to change
    BASE_URL = "https://whatchefswant.cutanddry.com/catalog/What%20Chefs%20Want%20-%20Rockies?verifiedVendorId=134452943&categoryId=1&categoryName=All+Items&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://whatchefswant.cutanddry.com"
    VENDOR_URL_NAME = 'What%20Chefs%20Want%20-%20Rockies'
    VERIFIED_VENDOR_ID = 134452943

    # This the name of the vendor
    VENDOR_NAME = "What Chefs Want - Rockies"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "meat",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/3537d174c44b5503cf72847aeafe5da0.jpg",
          "id": "164341073",
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
              "id": "164341074",
              "name": "Pork",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "403948258",
              "name": "Frozen Products & Foods",
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6f9d1d6cd6fcf5543a2e3adc7f9cd098.jpg",
          "id": "142821277",
          "name": "Seafood",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 3,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "145310897",
              "name": "Seafood-frozen,can & Specialty",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "517692541",
              "name": "Asian Products",
              "sortIndex": 2
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/76f579600f487a9d682b85136b1b82f5.jpg",
          "id": "142821287",
          "name": "Gourmet",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 54,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "142821579",
              "name": "Frozen Products & Foods",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "142821308",
              "name": "Canned & Jarred Items",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "145310991",
              "name": "Sauces, Bases & Spreads",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "142821509",
              "name": "Beverages & Juices",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "142821319",
              "name": "Coffee Shop Products",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "145310972",
              "name": "Jams, Honey & Syrups",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "142821317",
              "name": "Flour & Sugar",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 25,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "142821517",
              "name": "Pastas",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "145310971",
              "name": "Breads, Rolls & Pastry",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "142821429",
              "name": "Snack Foods / Ready To Eat",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "145310960",
              "name": "Seafood-frozen,can & Specialty",
              "sortIndex": 0
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/213c43cdd31edb2bb29462adf52ec5ea.jpg",
          "id": "164341076",
          "name": "Staples",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 625,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341093",
              "name": "Baking Ingredients",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 67,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341115",
              "name": "Snack Foods / Ready To Eat",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 50,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341103",
              "name": "Breads, Rolls & Pastry",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341094",
              "name": "Jams, Honey & Syrups",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 21,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341090",
              "name": "Flour & Sugar",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 29,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341142",
              "name": "Oils & Vinegars",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 57,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341231",
              "name": "Sauces, Bases & Spreads",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341263",
              "name": "Appetizers",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341086",
              "name": "Asian Products",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 43,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341077",
              "name": "Beverages & Juices",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 50,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341111",
              "name": "Frozen Products & Foods",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341345",
              "name": "Dressings",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341117",
              "name": "Coffee Shop Products",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 51,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341105",
              "name": "Canned & Jarred Items",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 175,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341139",
              "name": "Spices, Salts & Dried Herbs",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341342",
              "name": "Frozen Puree Line",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341125",
              "name": "Nuts",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341335",
              "name": "Pastas",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341326",
              "name": "Olives",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341141",
              "name": "Fruit - Dried",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "396224843",
              "name": "Plates & Trays",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341116",
              "name": "Desserts",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "164341104",
              "name": "Beans - Dried",
              "sortIndex": 0
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/00d4dc2976c04629467e97ec606a2523.jpg",
          "id": "142821324",
          "name": "Dairy & Cheeses",
          "sortIndex": "5",
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
              "id": "142821361",
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1ce653bb9970d7f3c515a9e865ab9f94.jpg",
          "id": "164341070",
          "name": "To-go & Kitchen Essentials",
          "sortIndex": "7",
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
              "id": "164341099",
              "name": "Food Preparation",
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
