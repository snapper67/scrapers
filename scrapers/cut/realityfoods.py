import json
from .dry import CutScraper


class RealityFoodsScraper(CutScraper):
    """Scraper for Reality Foods on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/realityfoods/'

    # Values to change
    BASE_URL = "https://realityfoods.cutanddry.com/catalog/realityfoods?verifiedVendorId=412964895&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://realityfoods.cutanddry.com"
    VENDOR_URL_NAME = 'realityfoods'
    VERIFIED_VENDOR_ID = 412964895

    # This the name of the vendor
    VENDOR_NAME = "Reality Foods"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "uncategorised",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "574412967",
          "name": "Uncategorised",
          "sortIndex": "0",
          "visibleOnHeader": false,
          "visibleOnSidebar": false
        },
        "productCount": 3,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574412968",
              "name": "Uncategorised",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fruits and vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4e7b628e3b7c7bfd723e61d572032f49.jpg",
          "id": "574412969",
          "name": "Fruits and Vegetables",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 303,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 43,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574428108",
              "name": "Tomatoes",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 41,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574428109",
              "name": "Olives",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 68,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574428110",
              "name": "Jarred Vegetables",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 72,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574428111",
              "name": "Dry/Canned Vegetables",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 54,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574428112",
              "name": "Canned Fruits",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 25,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574428113",
              "name": "Dried Fruits",
              "sortIndex": 7
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dairy, cheese, eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9cf0184939c8f839239810c008843b47.jpg",
          "id": "574412972",
          "name": "Dairy, Cheese, Eggs",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 296,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 194,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574433361",
              "name": "Cheese",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 102,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574433362",
              "name": "Dairy",
              "sortIndex": 4
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/844e1c158b1f351264fe63c573770129.jpg",
          "id": "574412974",
          "name": "Pasta",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 145,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574436080",
              "name": "Pasta Divella",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 28,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574436081",
              "name": "Pasta Dececco",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 107,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574436082",
              "name": "Other Pasta",
              "sortIndex": 6
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "grains and nuts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/7202b3d86f6fd62e9dc1857405e58434.jpg",
          "id": "574412977",
          "name": "Grains and Nuts",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 143,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 93,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574432072",
              "name": "Flour",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574432073",
              "name": "Rice",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 26,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574432074",
              "name": "Nuts",
              "sortIndex": 7
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "bakery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bc2cb8c8482a8c2b49fe8c65df8df0e3.jpg",
          "id": "574412979",
          "name": "Bakery",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 387,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 32,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574439998",
              "name": "Sugar",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 142,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574439999",
              "name": "Baking Products",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 64,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574440001",
              "name": "Baked Goods",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 81,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574440002",
              "name": "Chocolate/Candies",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 68,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574440003",
              "name": "Snacks",
              "sortIndex": 10
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "oils, vinegars, wines",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/257c9994407653f7eb3b9de4a10514c5.jpg",
          "id": "574412983",
          "name": "Oils, Vinegars, Wines",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 87,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 48,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574430575",
              "name": "Oils",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 29,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574430576",
              "name": "Vinegars",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574430577",
              "name": "Wines",
              "sortIndex": 9
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "condiments",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6a3ef1c5c98776eb7a3654f02add756d.jpg",
          "id": "574412999",
          "name": "Condiments",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 263,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574445918",
              "name": "Mustard",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574445919",
              "name": "Ketchup",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574445920",
              "name": "Dressings",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 144,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574445921",
              "name": "Sauces/Pasta",
              "sortIndex": 11
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 66,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574445922",
              "name": "Jams/Spreads",
              "sortIndex": 12
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "seasonings",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/905f0c040dc48506417575580ecf52ed.jpg",
          "id": "574413156",
          "name": "Seasonings",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 196,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 25,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574446560",
              "name": "Salt",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 171,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574446561",
              "name": "Spices/Seeds",
              "sortIndex": 3
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "frozen goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bfdfcfe0b4215e58d7ad24a0de0f1769.jpg",
          "id": "574413222",
          "name": "Frozen Goods",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 168,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 168,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574443991",
              "name": "Frozen Products",
              "sortIndex": 2
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9f18e2d587f66b2555bbb2f643736dfd.jpg",
          "id": "574413311",
          "name": "Supplies",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 588,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 41,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574452124",
              "name": "Bar Supplies",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 143,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574452126",
              "name": "Cleaning Supplies",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 67,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574452127",
              "name": "Wrap Supplies",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 41,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574452128",
              "name": "Paper Products",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 67,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574452129",
              "name": "Paper/Plastic Bags",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574452130",
              "name": "Pizza Boxes",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574452131",
              "name": "Doilies/Cake Boxes",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 113,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574452132",
              "name": "Take-Out Containers",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 17,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574452133",
              "name": "Cutlery",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 76,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574452134",
              "name": "Plastic/Paper Cups",
              "sortIndex": 11
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "meats",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b9925c3904784448e041bd0bbe23886f.jpg",
          "id": "574413340",
          "name": "Meats",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 114,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 27,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574448152",
              "name": "Canned Seafood",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 87,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574448153",
              "name": "Deli Meats",
              "sortIndex": 3
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "bases + soup juices",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bbd5bba81ec555a7c1a1a818f5db2a36.jpg",
          "id": "574413356",
          "name": "Bases + Soup Juices",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 20,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 20,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574436905",
              "name": "Soup Bases/Mixes",
              "sortIndex": 2
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "beverages",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f487efd49fe5fe861c460a3933147533.jpg",
          "id": "574413366",
          "name": "Beverages",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 291,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 73,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574442291",
              "name": "Juices",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 95,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574442292",
              "name": "Drinks/Pop",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574442293",
              "name": "Water - Natural",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 30,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574442294",
              "name": "Water Carb",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 47,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574442295",
              "name": "Coffee/Tea",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 33,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "574442296",
              "name": "Bar Mixes",
              "sortIndex": 8
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
