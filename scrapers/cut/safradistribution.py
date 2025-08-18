import json
from .dry import CutScraper


class SafraDistributionScraper(CutScraper):
    """Scraper for Safra Distribution on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/safradistribution/'

    # Values to change
    BASE_URL = "https://app.cutanddry.com/catalog/Safra%20Distribution/?categoryId=1&%3BverifiedVendorId=52007581&%3Bpage=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://app.cutanddry.com"
    VENDOR_URL_NAME = 'Safra%20Distribution'
    VERIFIED_VENDOR_ID = 52007581

    # This the name of the vendor
    VENDOR_NAME = "Safra Distribution"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "paper bags",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324752860",
          "name": "Paper Bags",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 24,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324755701",
              "name": "Paper Bags",
              "sortIndex": 1
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "foil & film",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324766492",
          "name": "Foil & Film",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 24,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324766493",
              "name": "Foil & Film",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "gloves",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324766976",
          "name": "Gloves",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 18,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324766977",
              "name": "Gloves",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "straws & stirrers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324767136",
          "name": "Straws & Stirrers",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 22,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324767137",
              "name": "Straws & Stirrers",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cutlery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324767257",
          "name": "Cutlery",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 32,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 32,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324767258",
              "name": "Cutlery",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "waxed paper",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324767385",
          "name": "Waxed Paper",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 27,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 27,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324767386",
              "name": "Waxed Paper",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "hot cups",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324767428",
          "name": "Hot Cups",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 22,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324767429",
              "name": "Hot Cups",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "janitorial",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324767504",
          "name": "Janitorial",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 60,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 60,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324767505",
              "name": "Janitorial",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "operational",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324767592",
          "name": "Operational",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 16,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324767593",
              "name": "Operational",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "napkins",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324767845",
          "name": "Napkins",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 10,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324767846",
              "name": "Napkins",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cold cups",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324768060",
          "name": "Cold Cups",
          "sortIndex": "12",
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
              "id": "324768061",
              "name": "Cold Cups",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "catering",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324768218",
          "name": "Catering",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 27,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 27,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324768219",
              "name": "Catering",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "food trays",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324768620",
          "name": "Food Trays",
          "sortIndex": "14",
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
              "id": "324768622",
              "name": "Food Trays",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "plastic bags",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324770710",
          "name": "Plastic Bags",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 4,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324770711",
              "name": "Plastic Bags",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "planet choice fiber",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324770794",
          "name": "Planet Choice Fiber",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 39,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 39,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324770795",
              "name": "Planet Choice Fiber",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "portion cups",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324770867",
          "name": "Portion Cups",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 24,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324770869",
              "name": "Portion Cups",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "paper soup containers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324770926",
          "name": "Paper Soup Containers",
          "sortIndex": "18",
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
              "id": "324770927",
              "name": "Paper Soup Containers",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "deli containers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324771113",
          "name": "Deli Containers",
          "sortIndex": "19",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 37,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 37,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324771114",
              "name": "Deli Containers",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "produce bags",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324772330",
          "name": "Produce Bags",
          "sortIndex": "20",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 6,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324772331",
              "name": "Produce Bags",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "hinged containers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324772904",
          "name": "Hinged Containers",
          "sortIndex": "21",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 27,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 27,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324772905",
              "name": "Hinged Containers",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cake box",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324773060",
          "name": "Cake Box",
          "sortIndex": "22",
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
              "id": "324773061",
              "name": "Cake Box",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dinnerware",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324773210",
          "name": "Dinnerware",
          "sortIndex": "24",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 9,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324773211",
              "name": "Dinnerware",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "folded containers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324773263",
          "name": "Folded Containers",
          "sortIndex": "25",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 7,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324773264",
              "name": "Folded Containers",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "microwaveable 2 piece",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324773354",
          "name": "Microwaveable 2 Piece",
          "sortIndex": "26",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 18,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324773355",
              "name": "Microwaveable 2 Piece",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "pizza boxes",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "324773450",
          "name": "Pizza Boxes",
          "sortIndex": "27",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 5,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "324773451",
              "name": "Pizza Boxes",
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
