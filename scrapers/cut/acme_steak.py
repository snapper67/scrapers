import json
from .dry import CutScraper


class AcmeSteakScraper(CutScraper):
    """Scraper for ACME Steak & Seafood on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/acme_steak/'

    # Values to change
    BASE_URL = "https://acmesteak.cutanddry.com/catalog/acmesteakandseafood?verifiedVendorId=176599551&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://acmesteak.cutanddry.com"
    VENDOR_URL_NAME = 'acmesteakandseafood'
    VERIFIED_VENDOR_ID = 176599551

    # This the name of the vendor
    VENDOR_NAME = "ACME Steak & Seafood"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "237893485",
          "baseName": "produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/eadb874d1c673816790852e904fa259b.jpg",
          "name": "Produce",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 273,
        "subcategories": [
          {
            "subcategory": {
              "id": "237893486",
              "name": "Produce",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 273,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237893494",
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2c86b15ff62fd1aa98542d71bd4a22e9.jpg",
          "name": "Seafood",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 240,
        "subcategories": [
          {
            "subcategory": {
              "id": "237893495",
              "name": "Seafood",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 240,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237893531",
          "baseName": "other",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a88571b7d64700810eff7547e93b80cd.jpg",
          "name": "Other",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 194,
        "subcategories": [
          {
            "subcategory": {
              "id": "237893533",
              "name": "Other",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 194,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237893638",
          "baseName": "grocery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/3396a044c50259d3beacc73fe2ccd6cc.jpg",
          "name": "Grocery",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1396,
        "subcategories": [
          {
            "subcategory": {
              "id": "237893639",
              "name": "Grocery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1396,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237893718",
          "baseName": "beverage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2a4362a643dcf116294f19fcd185c6b5.jpg",
          "name": "Beverage",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 219,
        "subcategories": [
          {
            "subcategory": {
              "id": "237893720",
              "name": "Beverage",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 219,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237893736",
          "baseName": "spices",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e2cb07423eec9fb2d0567cd93bdf0242.jpg",
          "name": "Spices",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 197,
        "subcategories": [
          {
            "subcategory": {
              "id": "237893737",
              "name": "Spices",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 197,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237893922",
          "baseName": "janitorial",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d4c07da2b474b3f2ea581add9022d5fc.jpg",
          "name": "Janitorial",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 144,
        "subcategories": [
          {
            "subcategory": {
              "id": "237893924",
              "name": "Janitorial",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 144,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237893951",
          "baseName": "meat + game",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bdba4214ac93a9bf35d1a16cfbf7be07.jpg",
          "name": "Meat + Game",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 671,
        "subcategories": [
          {
            "subcategory": {
              "id": "237893953",
              "name": "Meat + Game",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 671,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237894275",
          "baseName": "bakery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9979b28ef46385a2988d8bd5c9751d9f.jpg",
          "name": "Bakery",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 465,
        "subcategories": [
          {
            "subcategory": {
              "id": "237894276",
              "name": "Bakery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 465,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237894427",
          "baseName": "frozen desserts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5ffa0cee54f74109011cbd55e156108d.jpg",
          "name": "Frozen Desserts",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 24,
        "subcategories": [
          {
            "subcategory": {
              "id": "237894428",
              "name": "Frozen Desserts",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 24,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237894518",
          "baseName": "prepared foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b7707fba4d09054ad2512fbdfc11db0a.jpg",
          "name": "Prepared Foods",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 162,
        "subcategories": [
          {
            "subcategory": {
              "id": "237894520",
              "name": "Prepared Foods",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 162,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237894526",
          "baseName": "poultry + fowl",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/38f0d7ec8ba175451d784f164c672073.jpg",
          "name": "Poultry + Fowl",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 200,
        "subcategories": [
          {
            "subcategory": {
              "id": "237894527",
              "name": "Poultry + Fowl",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 200,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237894530",
          "baseName": "dairy + eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e7e8432d215f2484b3eee49ef8006e03.jpg",
          "name": "Dairy + Eggs",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 263,
        "subcategories": [
          {
            "subcategory": {
              "id": "237894531",
              "name": "Dairy + Eggs",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 263,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "237894533",
          "baseName": "dry goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5ac0a1b4c1918381073ee4cc7ff47dfd.jpg",
          "name": "Dry Goods",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 29,
        "subcategories": [
          {
            "subcategory": {
              "id": "237894534",
              "name": "Dry Goods",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 29,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "313014747",
          "baseName": "disposable supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Disposable Supplies",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 624,
        "subcategories": [
          {
            "subcategory": {
              "id": "313014748",
              "name": "Disposable Supplies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 624,
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
        self.options['base_url'] = self.BASE_URL