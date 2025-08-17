import json
from .dry import CutScraper


class Market406Scraper(CutScraper):
    """Scraper for 406 Market on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/market_406/'

    # Values to change
    BASE_URL = "https://app.cutanddry.com/catalog/406market?verifiedVendorId=51923907&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://app.cutanddry.com"
    VENDOR_URL_NAME = '406market'
    VERIFIED_VENDOR_ID = 51923907
    # This the name of the vendor
    VENDOR_NAME = "406 Market"
    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "156103875",
          "baseName": "beverages",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Beverages",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 12,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103876",
              "name": "Beverages",
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
          "id": "156103877",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Dairy",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 10,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103878",
              "name": "Dairy",
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
          "id": "156103879",
          "baseName": "local - beef grain finished",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Local - Beef Grain Finished",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 44,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103880",
              "name": "Local - Beef Grain Finished",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 44,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "156103883",
          "baseName": "local - beef grass fed",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Local - Beef Grass Fed",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 27,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103884",
              "name": "Local - Beef Grass Fed",
              "sortIndex": 0,
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
          "id": "156103887",
          "baseName": "local - dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Local - Dairy",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 29,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103888",
              "name": "Local - Dairy",
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
          "id": "156103891",
          "baseName": "local - charcuterie & jerky",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Local - Charcuterie & Jerky",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 43,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103892",
              "name": "Local - Charcuterie & Jerky",
              "sortIndex": 0,
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
          "id": "156103893",
          "baseName": "local - retail goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Local - Retail Goods",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 51,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103894",
              "name": "Local - Retail Goods",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 51,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "156103895",
          "baseName": "local - dry goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Local - Dry Goods",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 15,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103896",
              "name": "Local - Dry Goods",
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
          "id": "156103899",
          "baseName": "local - produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Local - Produce",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 35,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103900",
              "name": "Local - Produce",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 35,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "156103901",
          "baseName": "local - lamb",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Local - Lamb",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 17,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103902",
              "name": "Local - Lamb",
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
          "id": "156103905",
          "baseName": "local - pork",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Local - Pork",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 45,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103906",
              "name": "Local - Pork",
              "sortIndex": 0,
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
          "id": "156103907",
          "baseName": "local - poultry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Local - Poultry",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 2,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103908",
              "name": "Local - Poultry",
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
          "id": "156103909",
          "baseName": "specialty - produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Produce",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 77,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103910",
              "name": "Specialty - Produce",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 77,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "156103911",
          "baseName": "local - sausages",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Local - Sausages",
          "sortIndex": "18",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 25,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103912",
              "name": "Local - Sausages",
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
          "id": "156103917",
          "baseName": "specialty - beef",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Beef",
          "sortIndex": "21",
          "visibleOnHeader": false,
          "visibleOnSidebar": false,
          "__typename": "ProductCategory"
        },
        "productCount": 123,
        "subcategories": [
          {
            "subcategory": {
              "id": "389751732",
              "name": "Specialty - Beef",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 123,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "156103921",
          "baseName": "specialty - sausage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Sausage",
          "sortIndex": "23",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 23,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103922",
              "name": "Specialty - Sausage",
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
          "id": "156103925",
          "baseName": "specialty - beef wagyu japanese",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Beef Wagyu Japanese",
          "sortIndex": "25",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 15,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103926",
              "name": "Specialty - Beef Wagyu Japanese",
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
          "id": "156103929",
          "baseName": "specialty - canned and dry goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Canned and Dry Goods",
          "sortIndex": "27",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 32,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103930",
              "name": "Specialty - Canned and Dry Goods",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 32,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "156103931",
          "baseName": "specialty - charcuterie, pate', foie gras",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Charcuterie, Pate', Foie Gras",
          "sortIndex": "28",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 39,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103932",
              "name": "Specialty - Charcuterie, Pate', Foie Gras",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 39,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "156103935",
          "baseName": "specialty - dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Dairy",
          "sortIndex": "30",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 3,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103936",
              "name": "Specialty - Dairy",
              "sortIndex": 0,
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
          "id": "156103937",
          "baseName": "specialty - dry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Dry",
          "sortIndex": "31",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 10,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103938",
              "name": "Specialty - Dry",
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
          "id": "156103939",
          "baseName": "specialty - frozen",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Frozen",
          "sortIndex": "32",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 2,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103940",
              "name": "Specialty - Frozen",
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
          "id": "156103941",
          "baseName": "specialty - game meats",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Game Meats",
          "sortIndex": "33",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 61,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103942",
              "name": "Specialty - Game Meats",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 61,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "156103943",
          "baseName": "specialty - lamb",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Lamb",
          "sortIndex": "34",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 15,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103944",
              "name": "Specialty - Lamb",
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
          "id": "156103945",
          "baseName": "specialty - misc",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Misc",
          "sortIndex": "35",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 2,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103946",
              "name": "Specialty - Misc",
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
          "id": "156103949",
          "baseName": "specialty - pork - kurobuta pork",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Pork - Kurobuta Pork",
          "sortIndex": "37",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 8,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103950",
              "name": "Specialty - Pork - Kurobuta Pork",
              "sortIndex": 0,
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
          "id": "156103951",
          "baseName": "specialty - pork - roasting hogs - fresh",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Pork - Roasting Hogs - Fresh",
          "sortIndex": "38",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103952",
              "name": "Specialty - Pork - Roasting Hogs - Fresh",
              "sortIndex": 0,
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
          "id": "156103955",
          "baseName": "specialty - pork - wild boar",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Pork - Wild Boar",
          "sortIndex": "40",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 6,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103956",
              "name": "Specialty - Pork - Wild Boar",
              "sortIndex": 0,
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
          "id": "156103957",
          "baseName": "specialty - poultry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Poultry",
          "sortIndex": "41",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103958",
              "name": "Specialty - Poultry",
              "sortIndex": 0,
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
          "id": "156103959",
          "baseName": "specialty - poultry - chicken",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Poultry - Chicken",
          "sortIndex": "42",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103960",
              "name": "Specialty - Poultry - Chicken",
              "sortIndex": 0,
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
          "id": "156103969",
          "baseName": "specialty - retail goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Retail Goods",
          "sortIndex": "47",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 13,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103970",
              "name": "Specialty - Retail Goods",
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
          "id": "156103971",
          "baseName": "specialty - sausages",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Sausages",
          "sortIndex": "48",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103972",
              "name": "Specialty - Sausages",
              "sortIndex": 0,
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
          "id": "156103973",
          "baseName": "specialty - seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Seafood",
          "sortIndex": "49",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 6,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103974",
              "name": "Specialty - Seafood",
              "sortIndex": 0,
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
          "id": "156103977",
          "baseName": "specialty - truffles",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Truffles",
          "sortIndex": "51",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 4,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103978",
              "name": "Specialty - Truffles",
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
          "id": "156103979",
          "baseName": "specialty - veal bones",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Veal Bones",
          "sortIndex": "52",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103980",
              "name": "Specialty - Veal Bones",
              "sortIndex": 0,
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
          "id": "156103981",
          "baseName": "specialty - venison (red deer)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty - Venison (Red Deer)",
          "sortIndex": "53",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 26,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103982",
              "name": "Specialty - Venison (Red Deer)",
              "sortIndex": 0,
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
          "id": "156103989",
          "baseName": "specialty foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Specialty Foods",
          "sortIndex": "57",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 4,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103990",
              "name": "Specialty Foods",
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
          "id": "156103991",
          "baseName": "spices herbs dried goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Spices Herbs Dried Goods",
          "sortIndex": "58",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1,
        "subcategories": [
          {
            "subcategory": {
              "id": "156103992",
              "name": "Spices Herbs Dried Goods",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
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
