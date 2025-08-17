import json
from .dry import CutScraper


class RareFoodsScraper(CutScraper):
    """Scraper for Rare Foods on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/rarefoods/'

    # Values to change
    BASE_URL = "https://rarefoods.cutanddry.com/catalog/rarefoods?verifiedVendorId=176591617&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://rarefoods.cutanddry.com"
    VENDOR_URL_NAME = 'rarefoods'
    VERIFIED_VENDOR_ID = 176591617

    # This the name of the vendor
    VENDOR_NAME = "Rare Foods"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "specialty",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d76e5028bc3e3f3396c1721f07fa36b5.jpg",
          "id": "237572496",
          "name": "Specialty",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 132,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 26,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "237572497",
              "name": "Specialty",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 49,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "428851442",
              "name": "Oils & Vinegars",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "428851443",
              "name": "Olives & Vegetables",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 44,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "428851444",
              "name": "Japanese Pantry",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "428851446",
              "name": "Spices",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "428851447",
              "name": "Flavorings",
              "sortIndex": 6
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/acc41beddb6c9ea4a2d3364b6a3e433c.jpg",
          "id": "237572499",
          "name": "Meats",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 104,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 26,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "378134538",
              "name": "Meats",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286281606",
              "name": "Japanese Wagyu",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 45,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286281731",
              "name": "American Wagyu",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286281732",
              "name": "Angus Beef",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 17,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286281733",
              "name": "Pork",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286281734",
              "name": "Poultry",
              "sortIndex": 5
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cheese",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f163fd8cfa566cf46d5521bf65d29d94.jpg",
          "id": "237572501",
          "name": "Cheese",
          "sortIndex": "2",
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
              "id": "237572502",
              "name": "Cheese",
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6a2a83fa4ad0d3fef8edd88e0637127b.jpg",
          "id": "237572503",
          "name": "Charcuterie",
          "sortIndex": "3",
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
              "id": "237572504",
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
          "baseName": "caviar & preserved seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b05d3c270c351e8b315c50aa57f4f5cd.jpg",
          "id": "237572508",
          "name": "Caviar & Preserved Seafood",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 23,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 23,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "237572509",
              "name": "Caviar & Preserved Seafood",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "seafood - fresh & frozen",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/213b6b1a55e506f4fe3b84845c8414ef.jpg",
          "id": "237572512",
          "name": "Seafood - Fresh & Frozen",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 14,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 14,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "237572513",
              "name": "Seafood - Fresh & Frozen",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "tea & beverage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9038f338aac4f53cc44e908239c7b201.jpg",
          "id": "237572516",
          "name": "Tea & Beverage",
          "sortIndex": "7",
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
              "id": "237572517",
              "name": "Tea & Beverage",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fresh truffles & mushrooms",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/49fc51bbb479475e6e3f1f5140fa514d.jpg",
          "id": "409319889",
          "name": "Fresh Truffles & Mushrooms",
          "sortIndex": "12",
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
              "id": "409319904",
              "name": "Fresh Truffles & Mushrooms",
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
