
import json
from scrapers.cut.dry import CutScraper


class VitcoScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/vitco_foods/'

	# Values to change
	BASE_URL = "https://vitcofoods.cutanddry.com/catalog/vitcofoods?verifiedVendorId=1862236&categoryId=1&page=1"
	SUB_DOMAIN = "https://vitcofoods.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "243727957",
          "baseName": "groceries",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/Vitco/Groceries.png",
          "name": "GROCERIES",
          "sortIndex": "10",
          "visibleOnHeader": false,
          "visibleOnSidebar": false,
          "__typename": "ProductCategory"
        },
        "productCount": 2242,
        "subcategories": [
          {
            "subcategory": {
              "id": "243727958",
              "name": "CANNED VEGETABLES & BEANS",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 113,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243727961",
              "name": "CONDIMENTS",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 237,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243727963",
              "name": "SPICES & FLAVORINGS",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 371,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243727966",
              "name": "JUICES",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 26,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243727970",
              "name": "BEVERAGES",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 334,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243727975",
              "name": "SAUCES",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 194,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728013",
              "name": "DRIED GROCERIES",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 405,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728101",
              "name": "OIL & SHORTENING",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 66,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728206",
              "name": "CANNED TOMATO PRODUCTS",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 53,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728250",
              "name": "CANNED FISH & BEEF",
              "sortIndex": 9,
              "__typename": "ProductSubcategory"
            },
            "productCount": 21,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728280",
              "name": "FLOUR & MIXES",
              "sortIndex": 10,
              "__typename": "ProductSubcategory"
            },
            "productCount": 178,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728645",
              "name": "PASTAS",
              "sortIndex": 11,
              "__typename": "ProductSubcategory"
            },
            "productCount": 60,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728713",
              "name": "CANNED FRUIT",
              "sortIndex": 12,
              "__typename": "ProductSubcategory"
            },
            "productCount": 29,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728964",
              "name": "%22SYRUPS, TOPPINGS & DESERTS%22",
              "sortIndex": 13,
              "__typename": "ProductSubcategory"
            },
            "productCount": 59,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243729089",
              "name": "%22SYRUPS, TOPPINGS & DESSERTS%22",
              "sortIndex": 14,
              "__typename": "ProductSubcategory"
            },
            "productCount": 90,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243729728",
              "name": "SALAD DRESSINGS",
              "sortIndex": 15,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243731524",
              "name": "DRESSINGS",
              "sortIndex": 16,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243733499",
              "name": "POTATOES",
              "sortIndex": 17,
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
          "id": "243727971",
          "baseName": "frozen",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/Vitco/Frozen.jpg",
          "name": "FROZEN",
          "sortIndex": "11",
          "visibleOnHeader": false,
          "visibleOnSidebar": false,
          "__typename": "ProductCategory"
        },
        "productCount": 782,
        "subcategories": [
          {
            "subcategory": {
              "id": "243727972",
              "name": "POTATO PRODUCTS",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 121,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728008",
              "name": "BREADS",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 164,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728133",
              "name": "PORK-FROZEN",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 49,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728135",
              "name": "FROZEN FOODS",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 84,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728232",
              "name": "DESSERTS",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 97,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728667",
              "name": "FROZEN FRUITS & VEGETABLES",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 93,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728674",
              "name": "MEXICAN FOODS",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 46,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728976",
              "name": "CANNED/FROZEN SOUP",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 18,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243729043",
              "name": "APPETIZERS",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 67,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243729046",
              "name": "FROZEN ROLLS & BISCUITS",
              "sortIndex": 9,
              "__typename": "ProductSubcategory"
            },
            "productCount": 40,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243729565",
              "name": "SAUCES",
              "sortIndex": 10,
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
          "id": "243727977",
          "baseName": "dispenser beverages",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/Vitco/Beverages.jpg",
          "name": "DISPENSER BEVERAGES",
          "sortIndex": "12",
          "visibleOnHeader": false,
          "visibleOnSidebar": false,
          "__typename": "ProductCategory"
        },
        "productCount": 140,
        "subcategories": [
          {
            "subcategory": {
              "id": "243727978",
              "name": "DISPENSER BEVERAGES",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 140,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "243727981",
          "baseName": "miscellaneous",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/Vitco/Misc.jpg",
          "name": "MISCELLANEOUS",
          "sortIndex": "13",
          "visibleOnHeader": false,
          "visibleOnSidebar": false,
          "__typename": "ProductCategory"
        },
        "productCount": 707,
        "subcategories": [
          {
            "subcategory": {
              "id": "243727982",
              "name": "SMALLWARES",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 211,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728304",
              "name": "KITCHEN PRODUCTS",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 356,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728613",
              "name": "DISPENSERS",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 38,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243729137",
              "name": "MISC",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "411450723",
              "name": "F2F",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 94,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "243727984",
          "baseName": "protein",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/Vitco/Protein.jpeg",
          "name": "PROTEIN",
          "sortIndex": "14",
          "visibleOnHeader": false,
          "visibleOnSidebar": false,
          "__typename": "ProductCategory"
        },
        "productCount": 1271,
        "subcategories": [
          {
            "subcategory": {
              "id": "243727985",
              "name": "BEEF",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 404,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243727986",
              "name": "FROZEN SEAFOOD",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 34,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243727995",
              "name": "SEAFOOD",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 225,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728004",
              "name": "PORK",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 234,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728012",
              "name": "CHICKEN",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 196,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728016",
              "name": "LAMB",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 34,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728035",
              "name": "TURKEY",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 63,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728118",
              "name": "BOXED BEEF",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728191",
              "name": "POULTRY",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 51,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243729346",
              "name": "BEEF-FROZEN GROUND",
              "sortIndex": 9,
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
          "id": "243727989",
          "baseName": "processed meat",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/Vitco/Processed.jpg",
          "name": "PROCESSED MEAT",
          "sortIndex": "15",
          "visibleOnHeader": false,
          "visibleOnSidebar": false,
          "__typename": "ProductCategory"
        },
        "productCount": 313,
        "subcategories": [
          {
            "subcategory": {
              "id": "243727990",
              "name": "PROCESSED MEAT",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 120,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728028",
              "name": "PROCESSED PATTIES",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 34,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728032",
              "name": "S/O VITCO PRODUCTION",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 154,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728809",
              "name": "MISCELLANEOUS",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "479335896",
              "name": "RAW MATERIAL",
              "sortIndex": 4,
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
          "id": "243728010",
          "baseName": "disposables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/Vitco/Disposables.png",
          "name": "DISPOSABLES",
          "sortIndex": "16",
          "visibleOnHeader": false,
          "visibleOnSidebar": false,
          "__typename": "ProductCategory"
        },
        "productCount": 1334,
        "subcategories": [
          {
            "subcategory": {
              "id": "243728011",
              "name": "CUPS",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 123,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728024",
              "name": "PAPER PRODUCTS",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 301,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728080",
              "name": "DISPOSABLES",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 163,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728286",
              "name": "NAPKINS & PAPER TOWELS",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 57,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728301",
              "name": "BOWLS & CONTAINERS",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 267,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728360",
              "name": "LIDS",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 194,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728413",
              "name": "PLATES",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 27,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728454",
              "name": "BAGS PLASTIC/POLY",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 76,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243729503",
              "name": "SPOONS",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 31,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243729799",
              "name": "FOOD TRAYS",
              "sortIndex": 9,
              "__typename": "ProductSubcategory"
            },
            "productCount": 39,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243730195",
              "name": "FORKS",
              "sortIndex": 10,
              "__typename": "ProductSubcategory"
            },
            "productCount": 18,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243730196",
              "name": "KNIVES",
              "sortIndex": 11,
              "__typename": "ProductSubcategory"
            },
            "productCount": 23,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243730579",
              "name": "BATH & FACIAL TISSUE",
              "sortIndex": 12,
              "__typename": "ProductSubcategory"
            },
            "productCount": 14,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243733021",
              "name": "DOILIES",
              "sortIndex": 13,
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
          "id": "243728020",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/Vitco/Dairy.png",
          "name": "DAIRY",
          "sortIndex": "17",
          "visibleOnHeader": false,
          "visibleOnSidebar": false,
          "__typename": "ProductCategory"
        },
        "productCount": 434,
        "subcategories": [
          {
            "subcategory": {
              "id": "243728021",
              "name": "CHEESE/DAIRY",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 217,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728252",
              "name": "DAIRY",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 217,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "243728169",
          "baseName": "janitorial",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/Vitco/Janitorial.png",
          "name": "JANITORIAL",
          "sortIndex": "18",
          "visibleOnHeader": false,
          "visibleOnSidebar": false,
          "__typename": "ProductCategory"
        },
        "productCount": 363,
        "subcategories": [
          {
            "subcategory": {
              "id": "243728170",
              "name": "CHEMICALS",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 203,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728335",
              "name": "CLEANING PRODUCTS",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 107,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728341",
              "name": "JANITORIAL",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 53,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "243728219",
          "baseName": "refrigerated",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/Vitco/Refrigarated.jpg",
          "name": "REFRIGERATED",
          "sortIndex": "19",
          "visibleOnHeader": false,
          "visibleOnSidebar": false,
          "__typename": "ProductCategory"
        },
        "productCount": 331,
        "subcategories": [
          {
            "subcategory": {
              "id": "243728220",
              "name": "DRESSING",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 88,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728253",
              "name": "DESSERTS",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 111,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728421",
              "name": "BASES",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 69,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243728903",
              "name": "MEXICAN FOOD",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 43,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243729441",
              "name": "BEVERAGES",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 18,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "243729996",
              "name": "CONDIMENTS",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "420256855",
              "name": "POTATO PRODUCTS",
              "sortIndex": 6,
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
          "id": "243729215",
          "baseName": "produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/Vitco/Produce.jpeg",
          "name": "PRODUCE",
          "sortIndex": "20",
          "visibleOnHeader": false,
          "visibleOnSidebar": false,
          "__typename": "ProductCategory"
        },
        "productCount": 568,
        "subcategories": [
          {
            "subcategory": {
              "id": "243729216",
              "name": "PRODUCE",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 568,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'Vitco Foods'
	VENDOR_URL_NAME = 'vitcofoods'
	VERIFIED_VENDOR_ID = 1862236

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY

