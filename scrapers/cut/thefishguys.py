import json
from .dry import CutScraper


class TheFishGuysScraper(CutScraper):
    """Scraper for The Fish Guys on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/thefishguys/'

    # Values to change
    BASE_URL = "https://thefishguys.cutanddry.com/catalog/thefishguys?verifiedVendorId=103097510&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://thefishguys.cutanddry.com"
    VENDOR_URL_NAME = 'thefishguys'
    VERIFIED_VENDOR_ID = 103097510

    # This the name of the vendor
    VENDOR_NAME = "The Fish Guys"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "provisions",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/74d1a62b646a34b9b2f24147d1b360d8.jpg",
          "id": "205378316",
          "name": "Provisions",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 791,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 38,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "205378685",
              "name": "Provisions",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 46,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "292924652",
              "name": "Accompaniments",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 77,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "205382715",
              "name": "Bakery, Pastry & Chocolate",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 74,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "205382713",
              "name": "Charcuterie & Cured Meats",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 191,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "205382710",
              "name": "Cheese & Dairy",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 52,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "205382711",
              "name": "Oils & Vinegar",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 27,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "214176505",
              "name": "Olive/Pickled",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 56,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "205382718",
              "name": "Pasta & Grains",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 37,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "205382717",
              "name": "Preserves, Jams & Honey",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 83,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "205382714",
              "name": "Salts & Spices",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 56,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "205382712",
              "name": "Sauces, Syrups & Marinade",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "205382716",
              "name": "Specialty Seafood",
              "sortIndex": 11
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 35,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "214251830",
              "name": "Tomatoes & Produce",
              "sortIndex": 12
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "292924653",
              "name": "Truffles",
              "sortIndex": 13
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fresh seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Fresh+Seafood.png",
          "id": "113291680",
          "name": "Fresh Seafood",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 291,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 291,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "113291681",
              "name": "Fresh Seafood",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "frozen seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Frozen+Seafood.png",
          "id": "113291686",
          "name": "Frozen Seafood",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 238,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 238,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "113291687",
              "name": "Frozen Seafood",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "prepared seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Prepard+Seafood.png",
          "id": "113291691",
          "name": "Prepared Seafood",
          "sortIndex": "3",
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
              "id": "113291692",
              "name": "Prepared Seafood",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "beef",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Beef.png",
          "id": "112089444",
          "name": "Beef",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 522,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 522,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "113291739",
              "name": "Beef",
              "sortIndex": 1
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
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Pork.png",
          "id": "112089449",
          "name": "Pork",
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
              "id": "113291736",
              "name": "Pork",
              "sortIndex": 1
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
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Poultry.png",
          "id": "112089454",
          "name": "Poultry",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 151,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 151,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "113291733",
              "name": "Poultry",
              "sortIndex": 1
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "wild game",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Wild+Game.png",
          "id": "112089524",
          "name": "Wild Game",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 50,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 50,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "118972731",
              "name": "Wild Game",
              "sortIndex": 1
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "lamb/veal",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Lamb_Veal.png",
          "id": "113291674",
          "name": "Lamb/Veal",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 80,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 80,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "118972791",
              "name": "Lamb/Veal",
              "sortIndex": 1
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dry goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "246044134",
          "name": "Dry Goods",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 8,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "246044135",
              "name": "Duck",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "custom cut meats",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Custom+Cut+Meats.png",
          "id": "128833568",
          "name": "Custom Cut Meats",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 733,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 733,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "128833569",
              "name": "Custom Cut Meats",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cured meats",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Cured+meat.png",
          "id": "112089543",
          "name": "Cured Meats",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 83,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 83,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "118976640",
              "name": "Cured Meats",
              "sortIndex": 1
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "duck",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Duck.png",
          "id": "118972740",
          "name": "Duck",
          "sortIndex": "12",
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
              "id": "118972741",
              "name": "Duck",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "prepared foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Prepared+foods.png",
          "id": "112089532",
          "name": "Prepared Foods",
          "sortIndex": "13",
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
              "id": "113291727",
              "name": "Prepared Foods",
              "sortIndex": 1
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dry goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/103097510/Dry+goods.png",
          "id": "113291699",
          "name": "Dry Goods",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 29,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 29,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "113291700",
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
          "baseName": "sale",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/Sale_category.png",
          "id": "140078895",
          "name": "Sale",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 40,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 40,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "140078896",
              "name": "Sale",
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
