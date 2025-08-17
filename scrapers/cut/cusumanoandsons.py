import json
from .dry import CutScraper


class CusumanoAndSonsScraper(CutScraper):
    """Scraper for Cusumano & Sons on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/cusumanoandsons/'

    # Values to change
    BASE_URL = "https://cusumanoandsons.cutanddry.com/catalog/cusumanoandsons?verifiedVendorId=224897147&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://cusumanoandsons.cutanddry.com"
    VENDOR_URL_NAME = 'cusumanoandsons'
    VERIFIED_VENDOR_ID = 224897147

    # This the name of the vendor
    VENDOR_NAME = "Cusumano & Sons"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "542026108",
          "baseName": "fruit",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/75cf99e324f9beab3d19237be3b1f2f5.jpg",
          "name": "Fruit",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 78,
        "subcategories": [
          {
            "subcategory": {
              "id": "542026109",
              "name": "Fruit",
              "sortIndex": 38,
              "__typename": "ProductSubcategory"
            },
            "productCount": 78,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "542560812",
          "baseName": "vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d107463e096189a9cce4d04546bdd3e3.jpg",
          "name": "Vegetables",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 156,
        "subcategories": [
          {
            "subcategory": {
              "id": "542560813",
              "name": "Vegetables",
              "sortIndex": 38,
              "__typename": "ProductSubcategory"
            },
            "productCount": 156,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "540757309",
          "baseName": "fresh seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5a71db4db6fade526fde8aa602dd8c73.jpg",
          "name": "Fresh Seafood",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 252,
        "subcategories": [
          {
            "subcategory": {
              "id": "540757310",
              "name": "Fresh Seafood",
              "sortIndex": 41,
              "__typename": "ProductSubcategory"
            },
            "productCount": 252,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "540756915",
          "baseName": "beef",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e695ec9dff9cc9e6440a87a45af54f37.jpg",
          "name": "Beef",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 293,
        "subcategories": [
          {
            "subcategory": {
              "id": "540756916",
              "name": "Beef",
              "sortIndex": 36,
              "__typename": "ProductSubcategory"
            },
            "productCount": 293,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "540756911",
          "baseName": "pork",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f876aa6bf6a9174f0358a1221fbdb37c.jpg",
          "name": "Pork",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 159,
        "subcategories": [
          {
            "subcategory": {
              "id": "540756913",
              "name": "Pork",
              "sortIndex": 35,
              "__typename": "ProductSubcategory"
            },
            "productCount": 159,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "540756987",
          "baseName": "poultry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/12192a09d411203e7158cbd0babc72dc.jpg",
          "name": "Poultry",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 91,
        "subcategories": [
          {
            "subcategory": {
              "id": "540756988",
              "name": "Poultry",
              "sortIndex": 39,
              "__typename": "ProductSubcategory"
            },
            "productCount": 91,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "541483491",
          "baseName": "cheese",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e47141719dda1ba9c0f9e0428f09925e.jpg",
          "name": "Cheese",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 370,
        "subcategories": [
          {
            "subcategory": {
              "id": "541483492",
              "name": "Cheese",
              "sortIndex": 35,
              "__typename": "ProductSubcategory"
            },
            "productCount": 370,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "539313384",
          "baseName": "frozen seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bf0613eb96ee7bf99f86ebb8ea2f7496.jpg",
          "name": "Frozen Seafood",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 232,
        "subcategories": [
          {
            "subcategory": {
              "id": "539313388",
              "name": "Frozen Seafood",
              "sortIndex": 35,
              "__typename": "ProductSubcategory"
            },
            "productCount": 232,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "542024479",
          "baseName": "bread buns pastries",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/c17fd520558d256288abd3cfc7abda7b.jpg",
          "name": "Bread Buns Pastries",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 115,
        "subcategories": [
          {
            "subcategory": {
              "id": "542024480",
              "name": "Bread Buns Pastries",
              "sortIndex": 35,
              "__typename": "ProductSubcategory"
            },
            "productCount": 115,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "540756969",
          "baseName": "local meat",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5005c35e94ce00eeac9728d64a52d5fe.jpg",
          "name": "Local Meat",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 180,
        "subcategories": [
          {
            "subcategory": {
              "id": "540756970",
              "name": "Local Meat",
              "sortIndex": 38,
              "__typename": "ProductSubcategory"
            },
            "productCount": 180,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "540756918",
          "baseName": "deli meats",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/354887f3539f996127ca936be5179b94.jpg",
          "name": "Deli Meats",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 127,
        "subcategories": [
          {
            "subcategory": {
              "id": "540756919",
              "name": "Deli Meats",
              "sortIndex": 37,
              "__typename": "ProductSubcategory"
            },
            "productCount": 127,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "540757306",
          "baseName": "spices",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e25bc03dd5b3e603a7bb1b538c1f25de.jpg",
          "name": "Spices",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 271,
        "subcategories": [
          {
            "subcategory": {
              "id": "540757307",
              "name": "Spices",
              "sortIndex": 40,
              "__typename": "ProductSubcategory"
            },
            "productCount": 271,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "459122144",
          "baseName": "other food items",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/3f579284e84ab37016c46263148fdf87.jpg",
          "name": "Other Food Items",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 233,
        "subcategories": [
          {
            "subcategory": {
              "id": "517314972",
              "name": "Other Food Items",
              "sortIndex": 32,
              "__typename": "ProductSubcategory"
            },
            "productCount": 233,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "539925725",
          "baseName": "exotic meats",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2a22c50a83bd815a797ddac01c9039ab.jpg",
          "name": "Exotic Meats",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 37,
        "subcategories": [
          {
            "subcategory": {
              "id": "539925726",
              "name": "Exotic Meats",
              "sortIndex": 34,
              "__typename": "ProductSubcategory"
            },
            "productCount": 37,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "542560666",
          "baseName": "pre cut produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9cb42d64d446b6e5d9bb15043286db63.jpg",
          "name": "Pre Cut Produce",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 65,
        "subcategories": [
          {
            "subcategory": {
              "id": "542560667",
              "name": "Pre Cut Produce",
              "sortIndex": 37,
              "__typename": "ProductSubcategory"
            },
            "productCount": 65,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "539314542",
          "baseName": "fresh herbs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e6daf6e8a76cc68576ebc713eff16aa5.jpg",
          "name": "Fresh Herbs",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 18,
        "subcategories": [
          {
            "subcategory": {
              "id": "539314543",
              "name": "Fresh Herbs",
              "sortIndex": 36,
              "__typename": "ProductSubcategory"
            },
            "productCount": 18,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "542024851",
          "baseName": "flour sugar grains",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8b72de0696779c8a2e63f6e797b0ddcf.jpg",
          "name": "Flour Sugar Grains",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 169,
        "subcategories": [
          {
            "subcategory": {
              "id": "542024852",
              "name": "Flour Sugar Grains",
              "sortIndex": 37,
              "__typename": "ProductSubcategory"
            },
            "productCount": 169,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "459122225",
          "baseName": "kitchen supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/89effc4638e97c1a462839274fe4358e.jpg",
          "name": "Kitchen Supplies",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 46,
        "subcategories": [
          {
            "subcategory": {
              "id": "470068458",
              "name": "Kitchen Supplies",
              "sortIndex": 30,
              "__typename": "ProductSubcategory"
            },
            "productCount": 46,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "542024836",
          "baseName": "dairy and eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b7ba8451b05f48a538e75ba03057768a.jpg",
          "name": "Dairy And Eggs",
          "sortIndex": "18",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 45,
        "subcategories": [
          {
            "subcategory": {
              "id": "542024837",
              "name": "Dairy And Eggs",
              "sortIndex": 36,
              "__typename": "ProductSubcategory"
            },
            "productCount": 45,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "539312972",
          "baseName": "lamb",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8d556c76998c26249cd34db485e04565.jpg",
          "name": "Lamb",
          "sortIndex": "20",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 27,
        "subcategories": [
          {
            "subcategory": {
              "id": "539312973",
              "name": "Lamb",
              "sortIndex": 34,
              "__typename": "ProductSubcategory"
            },
            "productCount": 27,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "539312893",
          "baseName": "veal",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/177adc1df77ca4682c9340cdf2c39c68.jpg",
          "name": "Veal",
          "sortIndex": "21",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 17,
        "subcategories": [
          {
            "subcategory": {
              "id": "539312894",
              "name": "Veal",
              "sortIndex": 33,
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
          "id": "459122134",
          "baseName": "misc",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/34f899fa8f305e36eaca1f74d5193d8b.webp",
          "name": "Misc",
          "sortIndex": "22",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 5,
        "subcategories": [
          {
            "subcategory": {
              "id": "459122135",
              "name": "Misc",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "459122147",
          "baseName": "produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/75cf99e324f9beab3d19237be3b1f2f5.jpg",
          "name": "Produce",
          "sortIndex": "23",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 4,
        "subcategories": [
          {
            "subcategory": {
              "id": "459122148",
              "name": "Fruit",
              "sortIndex": 14,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "459122178",
              "name": "Vegetables",
              "sortIndex": 22,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
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
