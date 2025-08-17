import json
from .dry import CutScraper


class SavalFoodserviceScraper(CutScraper):
    """Scraper for Saval Foodservice on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/savalfoodservice/'

    # Values to change
    BASE_URL = "https://savalfoodservice.cutanddry.com/catalog/Saval%20Foodservice?verifiedVendorId=1862167&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://savalfoodservice.cutanddry.com"
    VENDOR_URL_NAME = 'savalfoodservice'
    VERIFIED_VENDOR_ID = 1862167

    # This the name of the vendor
    VENDOR_NAME = "Saval Foodservice"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "apptzr hors d'oeuvre",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/3caef0fafd5a415ddc38186e7ee3168a.jpg",
          "id": "213803724",
          "name": "Apptzr Hors D'oeuvre",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 118,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 118,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213803725",
              "name": "Apptzr Hors D'oeuvre",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "bakery products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6ad8b93cac8cb33d199e0fb84fea5aca.jpg",
          "id": "213803452",
          "name": "Bakery Products",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 783,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 783,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213803453",
              "name": "Bakery Products",
              "sortIndex": 0
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a91c8a6cb8fae4c31b13b7fb756adc2c.jpg",
          "id": "213804625",
          "name": "Beverages",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 368,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 368,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213804626",
              "name": "Beverages",
              "sortIndex": 0
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9160d48820cdbb62815896db7b4e6924.jpg",
          "id": "213803876",
          "name": "Cheese",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 295,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 295,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213803877",
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
          "baseName": "cleaning supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/56d575ca6c23e66a7408a955ed502071.jpg",
          "id": "213803514",
          "name": "Cleaning Supplies",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 246,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 246,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213803515",
              "name": "Cleaning Supplies",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/116a3998ef1502b3a9f92b5555cef4af.jpg",
          "id": "213805210",
          "name": "Dairy",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 153,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 153,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213805211",
              "name": "Dairy",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dress mayo vngr wine",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bd5f6ce7b62e6a5ebef89f1f30d32b3d.jpg",
          "id": "213803664",
          "name": "Dress Mayo Vngr Wine",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 142,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 142,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213803665",
              "name": "Dress Mayo Vngr Wine",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "deli meats",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/cc2e6721d897aec6c7b0300edc5b12d1.jpg",
          "id": "213808436",
          "name": "Deli Meats",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 144,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 144,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213808437",
              "name": "Deli Meats",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "equipment & supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d8f1d338b71c16305a7910a2779deccd.jpg",
          "id": "213803523",
          "name": "Equipment & Supplies",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 398,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 398,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213803524",
              "name": "Equipment & Supplies",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "ice cream",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/60c5b5be4804cc2f2221a5bf3f8e758c.jpg",
          "id": "213819119",
          "name": "Ice Cream",
          "sortIndex": "10",
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
              "id": "213819121",
              "name": "Ice Cream",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "ingredients",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/687900eda0939aaf93588dd7f4b75fa4.jpg",
          "id": "213803459",
          "name": "Ingredients",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 884,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 884,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213803460",
              "name": "Ingredients",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "meat fresh",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/984566e08361937d85f2a7e88be80558.jpg",
          "id": "213803786",
          "name": "Meat Fresh",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 301,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 301,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213803787",
              "name": "Meat Fresh",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "meats custom cut",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/3e7ed2a4364589981239c4fe554db376.jpg",
          "id": "213804288",
          "name": "Meats Custom Cut",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 380,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 380,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213804289",
              "name": "Meats Custom Cut",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "meats processed",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/53708baa6b6c2b83b47a8699ff68d522.jpg",
          "id": "213803758",
          "name": "Meats Processed",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 113,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 113,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213803759",
              "name": "Meats Processed",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "non-food/disposables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b9dd2383259c8b66527a4e709ed64f0d.jpg",
          "id": "271091305",
          "name": "Non-food/disposables",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 1355,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 1355,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "271091306",
              "name": "Non-food/disposables",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "not-in-use-on-host",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/60a5965a2b3d3a1308b650028039d71a.jpg",
          "id": "270413738",
          "name": "Not-in-use-on-host",
          "sortIndex": "16",
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
              "id": "270413739",
              "name": "Not-in-use-on-host",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "pasta cereal rice",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9942156d49e7438202c484980c652c3a.jpg",
          "id": "213803728",
          "name": "Pasta Cereal Rice",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 257,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 257,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213803729",
              "name": "Pasta Cereal Rice",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "pickles peppers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/ce6d974b96850adf4bb4385283950715.jpg",
          "id": "213805684",
          "name": "Pickles Peppers",
          "sortIndex": "18",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 150,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 150,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213805685",
              "name": "Pickles Peppers",
              "sortIndex": 0
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5a63ed3caa40932e136f05ea3dc8adb0.jpg",
          "id": "213804831",
          "name": "Poultry",
          "sortIndex": "19",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 144,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 144,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213804835",
              "name": "Poultry",
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/17f2d8349fde808d8b21bce6482ce48d.jpg",
          "id": "213803622",
          "name": "Prepared Foods",
          "sortIndex": "20",
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
              "id": "213803623",
              "name": "Prepared Foods",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "produce fresh",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/3ac45fbdc0e0e4ba893b0869893ee8b9.jpg",
          "id": "213805325",
          "name": "Produce Fresh",
          "sortIndex": "21",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 613,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 613,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213805326",
              "name": "Produce Fresh",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "sausage & franks",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/be836bb06f0c224342b09480eb7f2daf.jpg",
          "id": "213803790",
          "name": "Sausage & Franks",
          "sortIndex": "22",
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
              "id": "213803791",
              "name": "Sausage & Franks",
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1e78f4fdbca0d325721a3378b645d322.jpg",
          "id": "213804442",
          "name": "Seafood",
          "sortIndex": "23",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 279,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 279,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213804443",
              "name": "Seafood",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "shortening oils",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/90f7f64d02cc934611b808d199f89b46.jpg",
          "id": "213805214",
          "name": "Shortening Oils",
          "sortIndex": "24",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 56,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 56,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213805215",
              "name": "Shortening Oils",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "snacks candy mints",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5cd3bc292fc7ba72e828350f2d51b6cf.jpg",
          "id": "213803636",
          "name": "Snacks Candy Mints",
          "sortIndex": "25",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 273,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 273,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "213803637",
              "name": "Snacks Candy Mints",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "soup base gravy cond",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "479636925",
          "name": "Soup Base Gravy Cond",
          "sortIndex": "92",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 519,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 519,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "479636926",
              "name": "Soup Base Gravy Cond",
              "sortIndex": 1
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fruit veg can frozen",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "483515044",
          "name": "Fruit Veg Can Frozen",
          "sortIndex": "94",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 376,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 376,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "483515045",
              "name": "Fruit Veg Can Frozen",
              "sortIndex": 3
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
