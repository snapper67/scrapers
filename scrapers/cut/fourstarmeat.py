import json
from .dry import CutScraper


class FourStarMeatScraper(CutScraper):
    """Scraper for Four Star Meat on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/fourstarmeat/'

    # Values to change
    BASE_URL = "https://fourstarmeat.cutanddry.com/catalog/fourstarmeat?verifiedVendorId=229262448&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://fourstarmeat.cutanddry.com"
    VENDOR_URL_NAME = 'fourstarmeat'
    VERIFIED_VENDOR_ID = 229262448

    # This the name of the vendor
    VENDOR_NAME = "Four Star Meat"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "339338261",
          "baseName": "fsm butcher shop",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/28efde6248fd24cf340c18f4d8d424c0.jpg",
          "name": "FSM Butcher Shop",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 109,
        "subcategories": [
          {
            "subcategory": {
              "id": "339922103",
              "name": "Specialty",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 21,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922106",
              "name": "Patties",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 37,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922112",
              "name": "Ground Beef",
              "sortIndex": 10,
              "__typename": "ProductSubcategory"
            },
            "productCount": 14,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922135",
              "name": "Chili Meat Coarse",
              "sortIndex": 11,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922137",
              "name": "Carne Asada",
              "sortIndex": 12,
              "__typename": "ProductSubcategory"
            },
            "productCount": 9,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922142",
              "name": "Ribeye",
              "sortIndex": 13,
              "__typename": "ProductSubcategory"
            },
            "productCount": 17,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "339338318",
          "baseName": "proteins",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2b57a37b499dc9061a0c4a4e5c81fcdb.jpg",
          "name": "Proteins",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 279,
        "subcategories": [
          {
            "subcategory": {
              "id": "339922108",
              "name": "Other/Alternative",
              "sortIndex": 17,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922109",
              "name": "Processed Beef",
              "sortIndex": 18,
              "__typename": "ProductSubcategory"
            },
            "productCount": 27,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922134",
              "name": "Processed Pork",
              "sortIndex": 19,
              "__typename": "ProductSubcategory"
            },
            "productCount": 58,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922136",
              "name": "Commodity Beef",
              "sortIndex": 20,
              "__typename": "ProductSubcategory"
            },
            "productCount": 46,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922138",
              "name": "Commodity Pork",
              "sortIndex": 21,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922218",
              "name": "Pastrami",
              "sortIndex": 22,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922220",
              "name": "Processed Chicken",
              "sortIndex": 23,
              "__typename": "ProductSubcategory"
            },
            "productCount": 30,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922232",
              "name": "Commodity Lamb/Goat",
              "sortIndex": 24,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922233",
              "name": "Processed Lamb/Goat",
              "sortIndex": 25,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922306",
              "name": "Chicken Wings",
              "sortIndex": 27,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922334",
              "name": "Turkey Breast",
              "sortIndex": 28,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922339",
              "name": "Commodity Poultry",
              "sortIndex": 29,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922340",
              "name": "Chicken Breast",
              "sortIndex": 30,
              "__typename": "ProductSubcategory"
            },
            "productCount": 26,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922345",
              "name": "Chicken Strips",
              "sortIndex": 31,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922350",
              "name": "Processed Seafood",
              "sortIndex": 32,
              "__typename": "ProductSubcategory"
            },
            "productCount": 40,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "264740265",
          "baseName": "fruits and vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f2277e61fd2bcb99f73a84e4e80f0cd3.jpg",
          "name": "Fruits and Vegetables",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 287,
        "subcategories": [
          {
            "subcategory": {
              "id": "264740266",
              "name": "Vegetables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 225,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "264740269",
              "name": "Fruit",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 62,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "264740223",
          "baseName": "french fries and hash browns",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/00c5832e8ca3f326c18c89f8fbc78675.jpg",
          "name": "French Fries and Hash Browns",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 37,
        "subcategories": [
          {
            "subcategory": {
              "id": "339922104",
              "name": "French Fry",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 24,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922105",
              "name": "Hash Brown",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 13,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "264740278",
          "baseName": "eggs and dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2ebb9818b2aa2bec2219fd365434f0d8.jpg",
          "name": "Eggs and Dairy",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 118,
        "subcategories": [
          {
            "subcategory": {
              "id": "264740289",
              "name": "Eggs Misc",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "264740290",
              "name": "Liquid Eggs",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "264740292",
              "name": "Creamers",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "264740293",
              "name": "Milk",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "264740295",
              "name": "Juice",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "264740296",
              "name": "Butter",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922247",
              "name": "Cheese",
              "sortIndex": 11,
              "__typename": "ProductSubcategory"
            },
            "productCount": 44,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922253",
              "name": "Yogurt",
              "sortIndex": 12,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922257",
              "name": "Ice Cream",
              "sortIndex": 13,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922259",
              "name": "Miscellaneous Dairy",
              "sortIndex": 14,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "480155832",
              "name": "Eggs in Shell",
              "sortIndex": 15,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "264740272",
          "baseName": "refrigerated foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e9b38986ec38e2cf30822093deb42c46.jpg",
          "name": "Refrigerated Foods",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 20,
        "subcategories": [
          {
            "subcategory": {
              "id": "339922234",
              "name": "Dressings/Sauces",
              "sortIndex": 1,
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
          "id": "264740219",
          "baseName": "frozen foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/ee6da456c55606ee7345cae051e2caa1.jpg",
          "name": "Frozen Foods",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 115,
        "subcategories": [
          {
            "subcategory": {
              "id": "339922102",
              "name": "Bakery",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 38,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922107",
              "name": "Specialty",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 22,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922139",
              "name": "Fruits/Vegetables",
              "sortIndex": 9,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922140",
              "name": "Ethnic",
              "sortIndex": 10,
              "__typename": "ProductSubcategory"
            },
            "productCount": 30,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922141",
              "name": "Appetizers",
              "sortIndex": 11,
              "__typename": "ProductSubcategory"
            },
            "productCount": 12,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922451",
              "name": "Dessert",
              "sortIndex": 13,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "264740217",
          "baseName": "dry grocery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/34ece17c5f12e9bf529da7f3a216671a.jpg",
          "name": "Dry Grocery",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 69,
        "subcategories": [
          {
            "subcategory": {
              "id": "339922101",
              "name": "Other",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922249",
              "name": "Mixes/Sauces/Spices",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 14,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922298",
              "name": "Oils/Shortenings",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 13,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922329",
              "name": "Beverages",
              "sortIndex": 9,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922355",
              "name": "Condiments",
              "sortIndex": 10,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339922432",
              "name": "Tortilla",
              "sortIndex": 11,
              "__typename": "ProductSubcategory"
            },
            "productCount": 9,
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
