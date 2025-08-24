import json
from .dry import CutScraper


class WhatChefsWantCentralScraper(CutScraper):
    """Scraper for What Chefs Want - South on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/whatchefswant_central/'

    # Values to change
    BASE_URL = "https://whatchefswant.cutanddry.com/catalog/What%20Chefs%20Want%20-%20Central?verifiedVendorId=341183528&categoryId=1&categoryName=All+Items&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://whatchefswant.cutanddry.com"
    VENDOR_URL_NAME = 'What%20Chefs%20Want%20-%20Central'
    VERIFIED_VENDOR_ID = 341183528

    # This the name of the vendor
    VENDOR_NAME = "What Chefs Want - Central"

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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1c32bef60a3bbc800dc4d371a763c502.jpg",
          "id": "342230593",
          "name": "Produce",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 1211,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 121,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230594",
              "name": "Fruits - Fresh",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 247,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230658",
              "name": "Sliced And Diced Fruits & Veg",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230673",
              "name": "School Snacks",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 257,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231063",
              "name": "Vegetables - Fresh",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 31,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232128",
              "name": "Onions",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 112,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342233102",
              "name": "Do Not Order On Web  Off Price",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 181,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342233173",
              "name": "Microgreens & Flowers",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 80,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342233260",
              "name": "Lettuces & Greens",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 47,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342233469",
              "name": "Mushrooms - Fresh",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 37,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342234737",
              "name": "Herbs - Fresh",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 48,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342234980",
              "name": "Potatoes",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 41,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342235242",
              "name": "Tomatoes",
              "sortIndex": 12
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "559131861",
              "name": "Frozen Products & Foods",
              "sortIndex": 17
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d17b2444578fb3fd0768a7b6637d9461.jpg",
          "id": "342228980",
          "name": "Meat",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 1270,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 239,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342228981",
              "name": "Pork",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 543,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342228991",
              "name": "Beef",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342229714",
              "name": "Gourmet-cured Meat&specialty",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 130,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231626",
              "name": "Do Not Order On Web  Off Price",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 42,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231696",
              "name": "Meat - Deli, Foods, General",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232049",
              "name": "Plant-based Meats",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 44,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232108",
              "name": "Meat - Exotic",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 164,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232137",
              "name": "Poultry",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 43,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342236833",
              "name": "Lamb",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 37,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342238640",
              "name": "Marksbury Farm",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 17,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342238775",
              "name": "Veal",
              "sortIndex": 10
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fc8728a095bb0ef8e161e651642d5ed7.jpg",
          "id": "342229004",
          "name": "Seafood",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 644,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 278,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342229005",
              "name": "Fresh Fish",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 296,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342229010",
              "name": "Seafood-frozen,can & Specialty",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342229110",
              "name": "Alaska Boat Direct",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 46,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342229511",
              "name": "Fresh Shellfish",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 21,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "345584557",
              "name": "Do Not Order On Web  Off Price",
              "sortIndex": 4
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6103bd55d7ebc0bc42157f5180c7ff8e.jpg",
          "id": "342229811",
          "name": "Gourmet",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 1882,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342229812",
              "name": "Seafood-frozen,can & Specialty",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 48,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230535",
              "name": "Baking Ingredients",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 49,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230599",
              "name": "Appetizers",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 158,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230682",
              "name": "Asian Products",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 134,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230700",
              "name": "Canned & Jarred Items",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 46,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230999",
              "name": "Spices, Salts & Dried Herbs",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 148,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231042",
              "name": "Oils & Vinegars",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 78,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231074",
              "name": "Pastas",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 99,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231205",
              "name": "Do Not Order On Web  Off Price",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 80,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231227",
              "name": "Chocolates",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231290",
              "name": "Molecular Gastronomy",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 41,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231301",
              "name": "Flour & Sugar",
              "sortIndex": 11
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 91,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231308",
              "name": "Breads, Rolls & Pastry",
              "sortIndex": 12
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 143,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231408",
              "name": "Coffee Shop Products",
              "sortIndex": 13
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 94,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231418",
              "name": "Jams, Honey & Syrups",
              "sortIndex": 14
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 58,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231429",
              "name": "Sauces, Bases & Spreads",
              "sortIndex": 15
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 35,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231508",
              "name": "Beans - Dried",
              "sortIndex": 16
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 20,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231749",
              "name": "Plant-based Meats",
              "sortIndex": 17
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 35,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232018",
              "name": "Beverages & Juices",
              "sortIndex": 18
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232125",
              "name": "Onions",
              "sortIndex": 19
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 42,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232266",
              "name": "Desserts",
              "sortIndex": 20
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 21,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232306",
              "name": "Frozen Products & Foods",
              "sortIndex": 21
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 53,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342233168",
              "name": "Snack Foods / Ready To Eat",
              "sortIndex": 23
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342233441",
              "name": "Cheeses",
              "sortIndex": 24
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 49,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342233831",
              "name": "Nuts",
              "sortIndex": 25
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 78,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342234245",
              "name": "Grains",
              "sortIndex": 26
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342234252",
              "name": "Chili Peppers - Dried",
              "sortIndex": 27
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 85,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342234480",
              "name": "Gourmet-cured Meat&specialty",
              "sortIndex": 28
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 29,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342235469",
              "name": "Fruit - Dried",
              "sortIndex": 29
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342235529",
              "name": "Mushrooms - Dried",
              "sortIndex": 30
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342236069",
              "name": "Eggs",
              "sortIndex": 31
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 69,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342238635",
              "name": "Frozen Puree Line",
              "sortIndex": 32
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342239395",
              "name": "Meat - Exotic",
              "sortIndex": 33
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342240224",
              "name": "Meat - Deli, Foods, General",
              "sortIndex": 34
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 35,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342249039",
              "name": "Olives",
              "sortIndex": 35
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a7f00776fbc2468726e1c9fac43497c8.jpg",
          "id": "342230540",
          "name": "Staples",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 1328,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 148,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230541",
              "name": "Beverages & Juices",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 243,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230556",
              "name": "Spices, Salts & Dried Herbs",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 36,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230559",
              "name": "Baking Ingredients",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 21,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230564",
              "name": "Jams, Honey & Syrups",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 83,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230571",
              "name": "Breads, Rolls & Pastry",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 78,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230584",
              "name": "Frozen Products & Foods",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 54,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230646",
              "name": "Snack Foods / Ready To Eat",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230723",
              "name": "Asian Products",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231197",
              "name": "Chocolates",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 204,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231200",
              "name": "Do Not Order On Web  Off Price",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 70,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231210",
              "name": "Flour & Sugar",
              "sortIndex": 11
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231380",
              "name": "Desserts",
              "sortIndex": 12
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 118,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231411",
              "name": "Sauces, Bases & Spreads",
              "sortIndex": 13
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 87,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231547",
              "name": "Canned & Jarred Items",
              "sortIndex": 14
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 31,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231901",
              "name": "Coffee Shop Products",
              "sortIndex": 16
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232052",
              "name": "Plant-based Meats",
              "sortIndex": 17
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232554",
              "name": "Appetizers",
              "sortIndex": 18
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 40,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232894",
              "name": "Oils & Vinegars",
              "sortIndex": 20
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342233689",
              "name": "Cheeses",
              "sortIndex": 21
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342234776",
              "name": "Fruit - Dried",
              "sortIndex": 22
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342234792",
              "name": "Dairy - Other",
              "sortIndex": 23
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342236199",
              "name": "Frozen Puree Line",
              "sortIndex": 24
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 26,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342236359",
              "name": "Dressings",
              "sortIndex": 25
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 28,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342236436",
              "name": "Grains",
              "sortIndex": 26
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342239406",
              "name": "Meat - Deli, Foods, General",
              "sortIndex": 29
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342239552",
              "name": "Gourmet-cured Meat&specialty",
              "sortIndex": 30
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342248884",
              "name": "Nuts",
              "sortIndex": 31
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342249034",
              "name": "Olives",
              "sortIndex": 32
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342249502",
              "name": "Pastas",
              "sortIndex": 33
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342250845",
              "name": "Food Preparation",
              "sortIndex": 34
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "371838777",
              "name": "Sliced And Diced Fruits & Veg",
              "sortIndex": 35
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "449643607",
              "name": "Beef",
              "sortIndex": 36
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "472820235",
              "name": "Seafood-frozen,can & Specialty",
              "sortIndex": 37
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d06f5fb374ab5dd83d5659a876cf4eb7.jpg",
          "id": "342228994",
          "name": "Dairy & Cheeses",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 642,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 47,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342228995",
              "name": "Milk",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 449,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342229504",
              "name": "Cheeses",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 60,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232568",
              "name": "Dairy - Other",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 40,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342233466",
              "name": "Do Not Order On Web  Off Price",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342235042",
              "name": "Butter",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342236072",
              "name": "Eggs",
              "sortIndex": 5
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a59213625012bf37ae99d9febb3c0cb8.jpg",
          "id": "342228985",
          "name": "To-go & Kitchen Essentials",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 465,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342228986",
              "name": "Smallwares",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 94,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342229576",
              "name": "Carryout Containers",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 21,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230278",
              "name": "Plates & Trays",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 40,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230691",
              "name": "Catering Supplies",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230776",
              "name": "Cutlery And Utensils",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 84,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230781",
              "name": "Food Preparation",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231169",
              "name": "Carryout Bags",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342234789",
              "name": "Coffee Shop Products",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 50,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342234797",
              "name": "Cups, Lids, Straws",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 53,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342235217",
              "name": "Janitorial Supplies",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342235280",
              "name": "Custom & Proprietary Items",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342235632",
              "name": "Towels, Napkins, Tissue, Wipes",
              "sortIndex": 11
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342235798",
              "name": "Supply",
              "sortIndex": 13
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342249365",
              "name": "Front Of House",
              "sortIndex": 14
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 39,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "345584765",
              "name": "Do Not Order On Web  Off Price",
              "sortIndex": 15
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "exclude from catalog grouping",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6af4d733e4640210418c9b6ecc342cda.jpg",
          "id": "342228974",
          "name": "Exclude From Catalog Grouping",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 210,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 156,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342228975",
              "name": "Do Not Order On Web  Off Price",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342230984",
              "name": "Asian Products",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231268",
              "name": "Baking Ingredients",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342231273",
              "name": "Snack Foods / Ready To Eat",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342232273",
              "name": "Breads, Rolls & Pastry",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342233028",
              "name": "Beverages & Juices",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342233612",
              "name": "Cheeses",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342235524",
              "name": "Beef",
              "sortIndex": 12
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342235789",
              "name": "In House Packaging",
              "sortIndex": 13
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342236485",
              "name": "Vegetables - Fresh",
              "sortIndex": 15
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342237281",
              "name": "Appetizers",
              "sortIndex": 16
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342237408",
              "name": "Sauces, Bases & Spreads",
              "sortIndex": 17
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342237469",
              "name": "Coffee Shop Products",
              "sortIndex": 18
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342237714",
              "name": "Plant-based Meats",
              "sortIndex": 19
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342238302",
              "name": "Spices, Salts & Dried Herbs",
              "sortIndex": 20
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342239269",
              "name": "Gourmet-cured Meat&specialty",
              "sortIndex": 21
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342249270",
              "name": "Frozen Products & Foods",
              "sortIndex": 22
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342249333",
              "name": "Desserts",
              "sortIndex": 23
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342251756",
              "name": "Grains",
              "sortIndex": 28
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342252240",
              "name": "Carryout Containers",
              "sortIndex": 30
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "342253263",
              "name": "Plates & Trays",
              "sortIndex": 31
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "432235452",
              "name": "Meat - Exotic",
              "sortIndex": 36
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "459335242",
              "name": "Mushrooms - Fresh",
              "sortIndex": 37
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
