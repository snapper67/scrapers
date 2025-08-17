import json
from .dry import CutScraper


class CrookBrosScraper(CutScraper):
    """Scraper for Crook & Co. on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/crookbros/'

    # Values to change
    BASE_URL = "https://crookbros.cutanddry.com/catalog/crookbros?verifiedVendorId=152915811&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://crookbros.cutanddry.com"
    VENDOR_URL_NAME = 'crookbros'
    VERIFIED_VENDOR_ID = 152915811

    # This the name of the vendor
    VENDOR_NAME = "Crook & Co."

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "234809193",
          "baseName": "west virginia grown",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fd5d21b4ff3c23aa24fdcdacd63a36e9.jpg",
          "name": "West Virginia Grown",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 25,
        "subcategories": [
          {
            "subcategory": {
              "id": "234809194",
              "name": "West Virginia Grown",
              "sortIndex": 0,
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
          "id": "420015659",
          "baseName": "beverage + juice + concentrate",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/0829b3a9a7bd6fde8b73c667122708ab.jpg",
          "name": "Beverage + Juice + Concentrate",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 43,
        "subcategories": [
          {
            "subcategory": {
              "id": "420015660",
              "name": "Beverage + Juice + Concentrate",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 43,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "234809166",
          "baseName": "bulk fruits",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9b0ad7325b65a37b8397fca1f183b61e.jpg",
          "name": "Bulk Fruits",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 164,
        "subcategories": [
          {
            "subcategory": {
              "id": "234809167",
              "name": "Bulk Fruits",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 164,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "234809172",
          "baseName": "bulk vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/16dc7b520c3694745090b6b265ade2ab.jpg",
          "name": "Bulk Vegetables",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 414,
        "subcategories": [
          {
            "subcategory": {
              "id": "234809173",
              "name": "Bulk Vegetables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 414,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "235278472",
          "baseName": "canned goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/178cc68305cbd9122e7e0e3c5b6b6cb4.jpg",
          "name": "Canned Goods",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 12,
        "subcategories": [
          {
            "subcategory": {
              "id": "235278473",
              "name": "Canned Goods",
              "sortIndex": 0,
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
          "id": "413352297",
          "baseName": "cheese + butter",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2fbc68d31ddc79676db2b68d10b94354.jpg",
          "name": "Cheese + Butter",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 82,
        "subcategories": [
          {
            "subcategory": {
              "id": "413352305",
              "name": "Cheese + Butter",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 82,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "235278454",
          "baseName": "cleaning supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/eac8c06ea2393860477c2262bc688092.jpg",
          "name": "Cleaning Supplies",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 11,
        "subcategories": [
          {
            "subcategory": {
              "id": "235278455",
              "name": "Cleaning Supplies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "222293248",
          "baseName": "dry goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/13ec542f04f714ea1b7c4ac18429c6cb.jpg",
          "name": "Dry Goods",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 41,
        "subcategories": [
          {
            "subcategory": {
              "id": "222293249",
              "name": "Dry Goods",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 41,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "381648648",
          "baseName": "fresh herbs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/ff9487004360921336786836e66e30f7.jpg",
          "name": "Fresh Herbs",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 49,
        "subcategories": [
          {
            "subcategory": {
              "id": "381648649",
              "name": "Fresh Herbs",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 49,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "419642447",
          "baseName": "frozen cakes & desserts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/46db906adbd1f8772c7c2fcabba7e748.jpg",
          "name": "Frozen Cakes & Desserts",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 6,
        "subcategories": [
          {
            "subcategory": {
              "id": "419642448",
              "name": "Frozen Cakes & Desserts",
              "sortIndex": 4,
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
          "id": "419642454",
          "baseName": "frozen vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5a3617ca7864e6f9bdfce031e1dbd2fe.jpg",
          "name": "Frozen Vegetables",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 5,
        "subcategories": [
          {
            "subcategory": {
              "id": "419642455",
              "name": "Frozen Vegetables",
              "sortIndex": 5,
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
          "id": "425562243",
          "baseName": "grab & go",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/3dc0c065d96bb845e26e831f8aba5bd1.jpg",
          "name": "Grab & Go",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 52,
        "subcategories": [
          {
            "subcategory": {
              "id": "425562244",
              "name": "Grab & Go",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 52,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "235278478",
          "baseName": "grains & flour",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/867dc5292501ac71dfa825e8377ef6ee.jpg",
          "name": "Grains & Flour",
          "sortIndex": "18",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 17,
        "subcategories": [
          {
            "subcategory": {
              "id": "235278479",
              "name": "Grains & Flour",
              "sortIndex": 0,
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
          "id": "235278460",
          "baseName": "kitchen supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d86713f7c793b861560d1f124e8dfe73.jpg",
          "name": "Kitchen Supplies",
          "sortIndex": "20",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 13,
        "subcategories": [
          {
            "subcategory": {
              "id": "235278461",
              "name": "Kitchen Supplies",
              "sortIndex": 0,
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
          "id": "235278395",
          "baseName": "meats & proteins",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/50c7530578a1e0ee40c51c59e8513f38.webp",
          "name": "Meats & Proteins",
          "sortIndex": "21",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 58,
        "subcategories": [
          {
            "subcategory": {
              "id": "235278396",
              "name": "Meats & Proteins",
              "sortIndex": 0,
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
          "id": "381648633",
          "baseName": "micro greens & flowers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d21ed348db70a2fdc501d9c65e6a671f.jpg",
          "name": "Micro Greens & Flowers",
          "sortIndex": "22",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 65,
        "subcategories": [
          {
            "subcategory": {
              "id": "381648634",
              "name": "Micro Greens & Flowers",
              "sortIndex": 0,
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
          "id": "413354596",
          "baseName": "milk + cream + eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8fa0c0ded81be9065186621096ed510b.jpg",
          "name": "Milk + Cream + Eggs",
          "sortIndex": "23",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 57,
        "subcategories": [
          {
            "subcategory": {
              "id": "413354597",
              "name": "Milk + Cream + Eggs",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 57,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "434329262",
          "baseName": "oil + vinegar + shortening",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2f88988248efff61f0ed76b2e7d6d75b.jpg",
          "name": "Oil + Vinegar + Shortening",
          "sortIndex": "25",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 13,
        "subcategories": [
          {
            "subcategory": {
              "id": "434329263",
              "name": "Oil + Vinegar + Shortening",
              "sortIndex": 8,
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
          "id": "217713007",
          "baseName": "oliverio italian style peppers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a5ac11b86ae413563b2a164ef66c52c9.jpg",
          "name": "Oliverio Italian Style Peppers",
          "sortIndex": "26",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 30,
        "subcategories": [
          {
            "subcategory": {
              "id": "217713008",
              "name": "Oliverio Italian Style Peppers",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 30,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "234809174",
          "baseName": "organic vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8201c60bfc7e96d76cc072a11f0b13e9.jpg",
          "name": "Organic Vegetables",
          "sortIndex": "27",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 15,
        "subcategories": [
          {
            "subcategory": {
              "id": "234809175",
              "name": "Organic Vegetables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 15,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "235278475",
          "baseName": "paper supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/342236f8cb0e61f46180fcdf36f50237.jpg",
          "name": "Paper Supplies",
          "sortIndex": "28",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 10,
        "subcategories": [
          {
            "subcategory": {
              "id": "235278476",
              "name": "Paper Supplies",
              "sortIndex": 0,
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
          "id": "234809164",
          "baseName": "pre-cuts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/edb1fdab42c39469865c2cbdd1b118d7.jpg",
          "name": "Pre-cuts",
          "sortIndex": "29",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 106,
        "subcategories": [
          {
            "subcategory": {
              "id": "234809165",
              "name": "Pre-cuts",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 106,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "234809213",
          "baseName": "retail salads",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/c95092cbf03e306d938a35c177892be2.jpg",
          "name": "Retail Salads",
          "sortIndex": "30",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 7,
        "subcategories": [
          {
            "subcategory": {
              "id": "234809214",
              "name": "Retail Salads",
              "sortIndex": 0,
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
          "id": "235278462",
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/0b39903f98476501a2ff5d9cada7f7d7.jpg",
          "name": "Seafood",
          "sortIndex": "31",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 20,
        "subcategories": [
          {
            "subcategory": {
              "id": "235278463",
              "name": "Seafood",
              "sortIndex": 0,
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
          "id": "234809199",
          "baseName": "seasonal",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/c8d014ce8b8791e82b06ee9eeb1d15f0.jpg",
          "name": "Seasonal",
          "sortIndex": "32",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 2,
        "subcategories": [
          {
            "subcategory": {
              "id": "234809200",
              "name": "Seasonal",
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
          "id": "239163365",
          "baseName": "snack pack fruit",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1e12586e6e2bb615e3b456f00cb304b1.jpg",
          "name": "Snack Pack Fruit",
          "sortIndex": "33",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 23,
        "subcategories": [
          {
            "subcategory": {
              "id": "239163366",
              "name": "Snack Pack Fruit",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 23,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "239163444",
          "baseName": "snack pack vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8fde9e581bf471463169f1dfbb270e47.jpg",
          "name": "Snack Pack Vegetables",
          "sortIndex": "34",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 31,
        "subcategories": [
          {
            "subcategory": {
              "id": "239163445",
              "name": "Snack Pack Vegetables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 31,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "235278451",
          "baseName": "sugar + spice + seasoning",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1cef310976c834438959232c64229d5e.jpg",
          "name": "Sugar + Spice + Seasoning",
          "sortIndex": "35",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 13,
        "subcategories": [
          {
            "subcategory": {
              "id": "235278452",
              "name": "Sugar + Spice + Seasoning",
              "sortIndex": 0,
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
          "id": "260934690",
          "baseName": "to-go supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/06a82510b70e56609b940062eae4356e.jpg",
          "name": "To-go Supplies",
          "sortIndex": "36",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 38,
        "subcategories": [
          {
            "subcategory": {
              "id": "260934691",
              "name": "To-go Supplies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 38,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "234809204",
          "baseName": "wet salads",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f28675f00a17b3db7efb2249942496a2.jpg",
          "name": "Wet Salads",
          "sortIndex": "37",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 4,
        "subcategories": [
          {
            "subcategory": {
              "id": "234809205",
              "name": "Wet Salads",
              "sortIndex": 0,
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
          "id": "496933966",
          "baseName": "catering supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/ee5aecf8ae7a3914d38e65afdaf3c6f5.jpg",
          "name": "Catering Supplies",
          "sortIndex": "230",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 4,
        "subcategories": [
          {
            "subcategory": {
              "id": "496933967",
              "name": "Catering Supplies",
              "sortIndex": 9,
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
          "id": "576231157",
          "baseName": "condiments + toppings",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Condiments + Toppings",
          "sortIndex": "231",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 31,
        "subcategories": [
          {
            "subcategory": {
              "id": "576231158",
              "name": "Condiments + Toppings",
              "sortIndex": 10,
              "__typename": "ProductSubcategory"
            },
            "productCount": 31,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "606650013",
          "baseName": "organic fruit",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Organic Fruit",
          "sortIndex": "232",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 8,
        "subcategories": [
          {
            "subcategory": {
              "id": "606650015",
              "name": "Organic Fruit",
              "sortIndex": 11,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
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
