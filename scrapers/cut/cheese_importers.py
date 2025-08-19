import json
from .dry import CutScraper


class CheeseImportersScraper(CutScraper):
    """Scraper for Cheese Importers on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/cheese_importers/'

    # Values to change
    BASE_URL = "https://cheeseimporters.cutanddry.com/catalog/CheeseImporters?verifiedVendorId=130783764&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://cheeseimporters.cutanddry.com"
    VENDOR_URL_NAME = 'CheeseImporters'
    VERIFIED_VENDOR_ID = 130783764

    # This the name of the vendor
    VENDOR_NAME = "Cheese Importers"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "396169871",
          "baseName": "cheese",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/aed71f209b6f6ec1ba0e3655cd9d1c2f.jpg",
          "name": "Cheese",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 963,
        "subcategories": [
          {
            "subcategory": {
              "id": "396170093",
              "name": "Cheese Organic",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169933",
              "name": "Cheese Shredded",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 46,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169880",
              "name": "Cheese Usa Artisan",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 143,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169875",
              "name": "Cheese Colorado",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 55,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169913",
              "name": "Cheese Switzerland",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 52,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169922",
              "name": "Cheese Italy",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 139,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169908",
              "name": "Cheese Holland",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 72,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169882",
              "name": "Cheese France",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 82,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169888",
              "name": "Cheese U.k.",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 41,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169872",
              "name": "Cheese Spain",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 103,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169948",
              "name": "Cheese Exotic",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 9,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396170039",
              "name": "Cheese Portugal",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396170018",
              "name": "Cheese Mexico",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169961",
              "name": "Cheese Germany",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169877",
              "name": "Cheese Usa",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 123,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169944",
              "name": "Cheese Norway",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396170050",
              "name": "Cheese Greece",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396170043",
              "name": "Cheese Belgium",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169876",
              "name": "Cheese Australia",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396170013",
              "name": "Cheese Denmark",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 15,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169881",
              "name": "Cheese Pckgd Exact",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169937",
              "name": "Cheese Pckgd Randm",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "416818868",
              "name": "Cheese Austria",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477915282",
              "name": "Cheese Canada",
              "sortIndex": 55,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477987358",
              "name": "Cheese Grated Bulk",
              "sortIndex": 58,
              "__typename": "ProductSubcategory"
            },
            "productCount": 12,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477987426",
              "name": "Cheese Sliced Bulk",
              "sortIndex": 60,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "396169878",
          "baseName": "vegan and non dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/7be76bab9c6e895e75b5d67f0e95d5f9.jpg",
          "name": "Vegan And Non Dairy",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 5,
        "subcategories": [
          {
            "subcategory": {
              "id": "396169879",
              "name": "Vegan",
              "sortIndex": 0,
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
          "id": "396169883",
          "baseName": "olives & vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/7f5e46bbbf6c4a33f5472ae19665fcd8.jpg",
          "name": "Olives & Vegetables",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1,
        "subcategories": [
          {
            "subcategory": {
              "id": "526828972",
              "name": "Vegetables Bulk",
              "sortIndex": 71,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "396169910",
          "baseName": "crackers, chips & snacks",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/c7051701dcc6cf0115c8cfa7ea07b8a7.jpg",
          "name": "Crackers, Chips & Snacks",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 61,
        "subcategories": [
          {
            "subcategory": {
              "id": "396170016",
              "name": "Chips & Snacks",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 25,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396169911",
              "name": "Crackers",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 36,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "396169939",
          "baseName": "pasta",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1750825f9829711418d761544930edeb.jpg",
          "name": "Pasta",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 27,
        "subcategories": [
          {
            "subcategory": {
              "id": "396170095",
              "name": "Pasta Fresh Frz",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477987396",
              "name": "Pasta Retail",
              "sortIndex": 59,
              "__typename": "ProductSubcategory"
            },
            "productCount": 25,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "396169941",
          "baseName": "fish & seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/0850c8e13cca98ab0e33aa4f42b2de75.jpg",
          "name": "Fish & Seafood",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 18,
        "subcategories": [
          {
            "subcategory": {
              "id": "396169942",
              "name": "Seafood",
              "sortIndex": 0,
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
          "id": "396169952",
          "baseName": "beverage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/37cfb353c8e90f7468c301cd31ccb094.jpg",
          "name": "Beverage",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 40,
        "subcategories": [
          {
            "subcategory": {
              "id": "430842786",
              "name": "Beverages Rtl",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 38,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "430843506",
              "name": "Beverages Bulk",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "396169964",
          "baseName": "cheese accompaniments",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/705a6250dd9545b9470cec6edb069b16.jpg",
          "name": "Cheese Accompaniments",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1,
        "subcategories": [
          {
            "subcategory": {
              "id": "586869427",
              "name": "Condiments Rtl",
              "sortIndex": 74,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "396170045",
          "baseName": "fruit",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/236984859409f49d9b9e7169d6bed1ea.jpg",
          "name": "Fruit",
          "sortIndex": "18",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 33,
        "subcategories": [
          {
            "subcategory": {
              "id": "396170062",
              "name": "Dried Fruit",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 31,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "396170046",
              "name": "Fruit Preserved",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "430842605",
          "baseName": "bacon & sausage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b7620b9becdcad1557b1b86d28c53ad2.jpg",
          "name": "Bacon & Sausage",
          "sortIndex": "19",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 28,
        "subcategories": [
          {
            "subcategory": {
              "id": "430842606",
              "name": "Sausage",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 15,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "430842944",
              "name": "Bacon",
              "sortIndex": 5,
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
          "id": "430842947",
          "baseName": "bread & pastry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1baddfb461544d5cd5242683df9698d7.jpg",
          "name": "Bread & Pastry",
          "sortIndex": "20",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 11,
        "subcategories": [
          {
            "subcategory": {
              "id": "430842948",
              "name": "Bread",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477912908",
              "name": "Breads Gf",
              "sortIndex": 53,
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
          "id": "430843397",
          "baseName": "butter & dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/77754813646d133fad42c60e71b729f5.jpg",
          "name": "Butter & Dairy",
          "sortIndex": "21",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 28,
        "subcategories": [
          {
            "subcategory": {
              "id": "430843398",
              "name": "Butter Bulk",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "430899869",
              "name": "Butter Retail",
              "sortIndex": 11,
              "__typename": "ProductSubcategory"
            },
            "productCount": 24,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "430900146",
              "name": "Dairy Retail",
              "sortIndex": 12,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "430899808",
          "baseName": "cheese packaged retail",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5a677b2d5797daafd7557616a1f2a7d6.jpg",
          "name": "Cheese Packaged Retail",
          "sortIndex": "22",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 463,
        "subcategories": [
          {
            "subcategory": {
              "id": "430899809",
              "name": "Cheese Pckgd Exact",
              "sortIndex": 9,
              "__typename": "ProductSubcategory"
            },
            "productCount": 282,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "430899849",
              "name": "Cheese Grated Rtl",
              "sortIndex": 10,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "431028619",
              "name": "Cheese Pckgd Randm",
              "sortIndex": 14,
              "__typename": "ProductSubcategory"
            },
            "productCount": 156,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "431028620",
              "name": "Cheese Sliced Rtl",
              "sortIndex": 14,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "596929593",
              "name": "Cheese Shred Rtl",
              "sortIndex": 74,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "431028617",
          "baseName": "chocolate",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/91de6743624f496f7f0bb4f2ec412707.jpg",
          "name": "Chocolate",
          "sortIndex": "23",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 77,
        "subcategories": [
          {
            "subcategory": {
              "id": "431028618",
              "name": "Chocolate Rtl",
              "sortIndex": 13,
              "__typename": "ProductSubcategory"
            },
            "productCount": 59,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "431028817",
              "name": "Chocolate Bulk",
              "sortIndex": 15,
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
          "id": "431029627",
          "baseName": "condiments",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2db1d0a78ce458d2278a860e9188473e.jpg",
          "name": "Condiments",
          "sortIndex": "24",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 77,
        "subcategories": [
          {
            "subcategory": {
              "id": "431029628",
              "name": "Condiments Bulk",
              "sortIndex": 16,
              "__typename": "ProductSubcategory"
            },
            "productCount": 19,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "431303780",
              "name": "Condiments Rtl",
              "sortIndex": 18,
              "__typename": "ProductSubcategory"
            },
            "productCount": 58,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "431303708",
          "baseName": "desserts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/802c241a719321c8b9e328cb5c54c370.jpg",
          "name": "Desserts",
          "sortIndex": "25",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 35,
        "subcategories": [
          {
            "subcategory": {
              "id": "431303709",
              "name": "Cakes & Cheesecake",
              "sortIndex": 17,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "431305279",
              "name": "Waffles & Crepe",
              "sortIndex": 19,
              "__typename": "ProductSubcategory"
            },
            "productCount": 9,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "431305327",
              "name": "Cookies",
              "sortIndex": 20,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "578797882",
              "name": "Other Sweets",
              "sortIndex": 73,
              "__typename": "ProductSubcategory"
            },
            "productCount": 12,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "431362887",
          "baseName": "grains & flour",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/722aeb6c98ac99b55dbd5f64eb1b88cc.jpg",
          "name": "Grains & Flour",
          "sortIndex": "26",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 50,
        "subcategories": [
          {
            "subcategory": {
              "id": "431362888",
              "name": "Flour",
              "sortIndex": 20,
              "__typename": "ProductSubcategory"
            },
            "productCount": 24,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "435274265",
              "name": "Grains",
              "sortIndex": 32,
              "__typename": "ProductSubcategory"
            },
            "productCount": 26,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "431362944",
          "baseName": "fresh beef",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d39add21d070dd54310a9e5226483e3f.jpg",
          "name": "Fresh Beef",
          "sortIndex": "27",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 7,
        "subcategories": [
          {
            "subcategory": {
              "id": "431362945",
              "name": "Creekstone Beef",
              "sortIndex": 21,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "518176014",
              "name": "Brunson Beef",
              "sortIndex": 69,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "432333722",
          "baseName": "oils & vinegars",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d8fa13d3df4fa40a2e5716132fb2cd89.jpg",
          "name": "Oils & Vinegars",
          "sortIndex": "28",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 92,
        "subcategories": [
          {
            "subcategory": {
              "id": "435274632",
              "name": "Oils",
              "sortIndex": 40,
              "__typename": "ProductSubcategory"
            },
            "productCount": 37,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "435368135",
              "name": "Vinegars",
              "sortIndex": 44,
              "__typename": "ProductSubcategory"
            },
            "productCount": 55,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "435274236",
          "baseName": "meats cooked deli",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/93236565c9a160fb62f4176ece37c8cb.jpg",
          "name": "Meats Cooked Deli",
          "sortIndex": "29",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 37,
        "subcategories": [
          {
            "subcategory": {
              "id": "435274237",
              "name": "Meat Cooked",
              "sortIndex": 24,
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
          "id": "435274238",
          "baseName": "legumes",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4ed28d08bc1e6e78bf6ca4c84615b4f3.jpeg",
          "name": "Legumes",
          "sortIndex": "30",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 10,
        "subcategories": [
          {
            "subcategory": {
              "id": "435274239",
              "name": "Legumes",
              "sortIndex": 25,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "435274241",
          "baseName": "meat cured charcuterie",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bd003f741f4af0d4d30d751313fbbdb2.webp",
          "name": "Meat Cured Charcuterie",
          "sortIndex": "31",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 216,
        "subcategories": [
          {
            "subcategory": {
              "id": "435274260",
              "name": "Duck & Foie Gra",
              "sortIndex": 30,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "435274691",
              "name": "Pate & Rillette",
              "sortIndex": 41,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477987353",
              "name": "Meat Sliced",
              "sortIndex": 56,
              "__typename": "ProductSubcategory"
            },
            "productCount": 17,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477987356",
              "name": "Meat Domestic",
              "sortIndex": 57,
              "__typename": "ProductSubcategory"
            },
            "productCount": 45,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477987427",
              "name": "Meat Elevation",
              "sortIndex": 61,
              "__typename": "ProductSubcategory"
            },
            "productCount": 41,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477987429",
              "name": "Meat Imported",
              "sortIndex": 62,
              "__typename": "ProductSubcategory"
            },
            "productCount": 54,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477987432",
              "name": "Meat Biellese",
              "sortIndex": 63,
              "__typename": "ProductSubcategory"
            },
            "productCount": 20,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477987465",
              "name": "Meat River Bear",
              "sortIndex": 64,
              "__typename": "ProductSubcategory"
            },
            "productCount": 13,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477987557",
              "name": "Meat Porcelino",
              "sortIndex": 65,
              "__typename": "ProductSubcategory"
            },
            "productCount": 21,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "435274270",
          "baseName": "honey & honeycomb",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/7b7767e75e167932da7e949d38095ce2.jpg",
          "name": "Honey & Honeycomb",
          "sortIndex": "32",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 8,
        "subcategories": [
          {
            "subcategory": {
              "id": "435274271",
              "name": "Honey Bulk",
              "sortIndex": 34,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "435274576",
              "name": "Honey Retail",
              "sortIndex": 37,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "435274288",
          "baseName": "molecular",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4f41b1d7dd91af711eb4fe601e7bc654.jpg",
          "name": "Molecular",
          "sortIndex": "33",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 19,
        "subcategories": [
          {
            "subcategory": {
              "id": "435274289",
              "name": "Molecular",
              "sortIndex": 35,
              "__typename": "ProductSubcategory"
            },
            "productCount": 19,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "435274291",
          "baseName": "jams & mostarda",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fc92dbfe61e1e09fc42698b42b238a34.jpeg",
          "name": "Jams & Mostarda",
          "sortIndex": "34",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 49,
        "subcategories": [
          {
            "subcategory": {
              "id": "435274292",
              "name": "Jams Retail",
              "sortIndex": 36,
              "__typename": "ProductSubcategory"
            },
            "productCount": 33,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "435274591",
              "name": "Jams Bulk",
              "sortIndex": 38,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "435274640",
          "baseName": "nonfood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5c8d25b6a4317d31c4fe5786df9eea38.jpg",
          "name": "Nonfood",
          "sortIndex": "35",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 3,
        "subcategories": [
          {
            "subcategory": {
              "id": "435274641",
              "name": "Cheese Tools",
              "sortIndex": 40,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "435322595",
              "name": "Cookware",
              "sortIndex": 41,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "435322412",
          "baseName": "nuts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a7ed07b13686584d2b5b3a80a98a1e6d.jpg",
          "name": "Nuts",
          "sortIndex": "36",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 63,
        "subcategories": [
          {
            "subcategory": {
              "id": "435322413",
              "name": "Nuts Bulk",
              "sortIndex": 40,
              "__typename": "ProductSubcategory"
            },
            "productCount": 47,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "435322816",
              "name": "Nuts Retail",
              "sortIndex": 42,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "435368106",
          "baseName": "olives",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d9a1c8f96347fc57c7ef56be7d9ba7d7.jpg",
          "name": "Olives",
          "sortIndex": "37",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 76,
        "subcategories": [
          {
            "subcategory": {
              "id": "435368107",
              "name": "Olives Bulk",
              "sortIndex": 43,
              "__typename": "ProductSubcategory"
            },
            "productCount": 70,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "435368155",
              "name": "Olives Retail",
              "sortIndex": 44,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "435413442",
          "baseName": "soup & broth",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d9706f934d5a0d0056b0e8fb9da6da80.jpg",
          "name": "Soup & Broth",
          "sortIndex": "38",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 14,
        "subcategories": [
          {
            "subcategory": {
              "id": "435413443",
              "name": "Broth",
              "sortIndex": 43,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "435413806",
              "name": "Soup",
              "sortIndex": 46,
              "__typename": "ProductSubcategory"
            },
            "productCount": 9,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "435413458",
          "baseName": "spices & salts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/79bd4b400e84acfbd566b79c92014089.jpg",
          "name": "Spices & Salts",
          "sortIndex": "39",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 139,
        "subcategories": [
          {
            "subcategory": {
              "id": "435413459",
              "name": "Spices Bulk",
              "sortIndex": 44,
              "__typename": "ProductSubcategory"
            },
            "productCount": 108,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "436251687",
              "name": "Spices Retail",
              "sortIndex": 45,
              "__typename": "ProductSubcategory"
            },
            "productCount": 27,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "477988565",
              "name": "Salt",
              "sortIndex": 67,
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
          "id": "435413621",
          "baseName": "premade food frozen",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/59fad60f88e7ff05cc9f1119238b71d8.jpg",
          "name": "Premade Food Frozen",
          "sortIndex": "40",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 13,
        "subcategories": [
          {
            "subcategory": {
              "id": "435415847",
              "name": "Appetizer Frzn",
              "sortIndex": 48,
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
          "id": "436251710",
          "baseName": "vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/93fd05ec2e7a1b518560dcac635268bf.jpg",
          "name": "Vegetables",
          "sortIndex": "41",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 86,
        "subcategories": [
          {
            "subcategory": {
              "id": "436251711",
              "name": "Vegetables Bulk",
              "sortIndex": 46,
              "__typename": "ProductSubcategory"
            },
            "productCount": 58,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "438048106",
              "name": "Vegetables Rtl",
              "sortIndex": 48,
              "__typename": "ProductSubcategory"
            },
            "productCount": 28,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "436251844",
          "baseName": "vanilla",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/51a4d5e1fd8e4896f5def6c5634ef121.jpg",
          "name": "Vanilla",
          "sortIndex": "42",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 7,
        "subcategories": [
          {
            "subcategory": {
              "id": "436251845",
              "name": "Vanilla",
              "sortIndex": 47,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "459133414",
          "baseName": "colorado products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2027eb7a9be546a6e4b2a14d86c9c03d.jpg",
          "name": "Colorado Products",
          "sortIndex": "43",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 437,
        "subcategories": [
          {
            "subcategory": {
              "id": "459133415",
              "name": "Colorado Products",
              "sortIndex": 50,
              "__typename": "ProductSubcategory"
            },
            "productCount": 437,
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
