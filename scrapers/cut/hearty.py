import json
from .dry import CutScraper


class HeartyScraper(CutScraper):
    """Scraper for Hearty on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/hearty/'

    # Values to change
    BASE_URL = "https://hearty.cutanddry.com/catalog/hearty?verifiedVendorId=292768592&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://hearty.cutanddry.com"
    VENDOR_URL_NAME = 'hearty'
    VERIFIED_VENDOR_ID = 292768592

    # This the name of the vendor
    VENDOR_NAME = "Hearty"

    # Categories will be fetched dynamically
    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fruit",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6fdc1c05e8f80315349a1c35730ec152.jpg",
          "id": "339719766",
          "name": "Fruit",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 16,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850793",
              "name": "Apples",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850794",
              "name": "Cherries, Berries, and More",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850795",
              "name": "Citrus",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850796",
              "name": "Melons",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850798",
              "name": "Stone Fruit",
              "sortIndex": 6
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "vegetables/produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/466ed8b504c07ab7decf20f80c9e384d.jpg",
          "id": "339719976",
          "name": "Vegetables/Produce",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 69,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850816",
              "name": "Beans and Peas",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850817",
              "name": "Carrots",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850818",
              "name": "Corn",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850819",
              "name": "Cucumbers",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850820",
              "name": "Greens",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850821",
              "name": "Herbs",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850822",
              "name": "Lettuce and Salad",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 28,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850823",
              "name": "Microgreens",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850825",
              "name": "Onions and Garlic",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850826",
              "name": "Peppers",
              "sortIndex": 11
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850827",
              "name": "Potatoes",
              "sortIndex": 12
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850828",
              "name": "Roots",
              "sortIndex": 13
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850829",
              "name": "Squash",
              "sortIndex": 14
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850830",
              "name": "Tomatoes and Tomatillos",
              "sortIndex": 15
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850831",
              "name": "Vegetables",
              "sortIndex": 16
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385478331",
              "name": "Miscellaneous",
              "sortIndex": 17
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "meat/plant based proteins",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fe58f5272a194e4b79a7fbefb612dc0b.jpg",
          "id": "339719997",
          "name": "Meat/Plant Based Proteins",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 12,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850838",
              "name": "Beef",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850841",
              "name": "Tempeh",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850842",
              "name": "Tofu",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "384763095",
              "name": "Other Proteins",
              "sortIndex": 7
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "eggs/dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/629b38bf99da9bf713b8fd641ef50d5d.jpg",
          "id": "339720010",
          "name": "Eggs/Dairy",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 2,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341850872",
              "name": "Eggs",
              "sortIndex": 3
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "grains/legumes",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f4b7c744dcd7e7ec122a86bbe1424ac3.jpg",
          "id": "339720038",
          "name": "Grains/Legumes",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 12,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341851087",
              "name": "Beans",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341851090",
              "name": "Grains",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385478498",
              "name": "Miscellaneous",
              "sortIndex": 5
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "value added",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/59312155e619f8363f113ae5887bd847.jpg",
          "id": "339720091",
          "name": "Value Added",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 36,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341851232",
              "name": "Jams",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "341851236",
              "name": "Tortilla Chips",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "376371116",
              "name": "Tortillas",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "376371119",
              "name": "Coffee",
              "sortIndex": 11
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "376371121",
              "name": "Cookies",
              "sortIndex": 13
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "384853775",
              "name": "Miscellaneous",
              "sortIndex": 14
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385478790",
              "name": "Ice Cream",
              "sortIndex": 15
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "food box",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/83ae81559fad58230efeee68378eb195.jpg",
          "id": "339720111",
          "name": "Food Box",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 2,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "340089759",
              "name": "Food Box",
              "sortIndex": 1
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