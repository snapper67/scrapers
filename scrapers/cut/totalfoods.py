import json
from .dry import CutScraper


class TotalFoodsScraper(CutScraper):
    """Scraper for Total Foods on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/totalfoods/'

    # Values to change
    BASE_URL = "https://totalfoods.cutanddry.com/catalog/totalfoods?verifiedVendorId=385655757&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://totalfoods.cutanddry.com"
    VENDOR_URL_NAME = 'totalfoods'
    VERIFIED_VENDOR_ID = 385655757

    # This the name of the vendor
    VENDOR_NAME = "Total Foods"

    # Categories will be fetched dynamically
    CATEGORIES = json.loads('''
        {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "candy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/ca7692db1cc588a970965092791b2b20.webp",
          "id": "385748922",
          "name": "Candy",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 164,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385748993",
              "name": "King Size",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 55,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385748994",
              "name": "Peg Pack",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385748995",
              "name": "Share Size",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 36,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385748996",
              "name": "Standard Bar",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 25,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473520920",
              "name": "Candy",
              "sortIndex": 22
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339216",
              "name": "Stand Up Pouch",
              "sortIndex": 164
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477342556",
              "name": "K12 Approved",
              "sortIndex": 165
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477343635",
              "name": "Gum/mints",
              "sortIndex": 166
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477345025",
              "name": "Non Upc (fda)",
              "sortIndex": 167
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477349150",
              "name": "Halls",
              "sortIndex": 169
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cold beverages / energy drinks",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/444fe1a41d359485fb68e93a3205dec9.jpg",
          "id": "385749080",
          "name": "Cold Beverages / Energy Drinks",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 289,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749184",
              "name": "11.5 Oz",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749185",
              "name": "17.7 Oz",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 44,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749186",
              "name": "20 Oz",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 60,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749187",
              "name": "Energy Drink",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749188",
              "name": "Steaz",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749189",
              "name": "V8 Cans",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749190",
              "name": "V8 Splash Pet",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 62,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473521102",
              "name": "Cold Beverages / Energy Drinks",
              "sortIndex": 42
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 27,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473521976",
              "name": "Cans",
              "sortIndex": 102
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473523566",
              "name": "Snapple",
              "sortIndex": 140
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477338356",
              "name": "Water",
              "sortIndex": 197
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477338426",
              "name": "Energy Water",
              "sortIndex": 198
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477338732",
              "name": "Liquid Death",
              "sortIndex": 199
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339044",
              "name": "Sport Drinks",
              "sortIndex": 200
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339140",
              "name": "Powder",
              "sortIndex": 201
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477342133",
              "name": "12 Oz",
              "sortIndex": 204
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477342864",
              "name": "14 Oz Pet",
              "sortIndex": 206
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477343621",
              "name": "Bubbl'r",
              "sortIndex": 208
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477343859",
              "name": "Mixers",
              "sortIndex": 210
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477346699",
              "name": "Lacroix",
              "sortIndex": 214
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477347510",
              "name": "16.9 Oz",
              "sortIndex": 216
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477347645",
              "name": "Fairlife Milk",
              "sortIndex": 218
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477350328",
              "name": "Sprecher",
              "sortIndex": 221
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477351864",
              "name": "Variety Pack",
              "sortIndex": 223
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477351885",
              "name": "Sparkling Ice Starburst",
              "sortIndex": 224
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499540335",
              "name": "Probiotic Water",
              "sortIndex": 226
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "frozen foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/00c4e0e7be6deac3313196daa2378946.jpg",
          "id": "385749224",
          "name": "Frozen Foods",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 256,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 104,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749436",
              "name": "Frozen Foods",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749437",
              "name": "Deli Express Xxl Sandwiches",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749439",
              "name": "Market Sandwich Wraps",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749440",
              "name": "Pierre",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749441",
              "name": "San Luis Breakfast Burritos",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749442",
              "name": "Sandwiches",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473523108",
              "name": "Cookie",
              "sortIndex": 125
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473523647",
              "name": "Donuts",
              "sortIndex": 143
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473524672",
              "name": "Red Baron",
              "sortIndex": 165
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473524761",
              "name": "Cloverhill",
              "sortIndex": 170
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473526190",
              "name": "Micro Market Retail",
              "sortIndex": 194
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473526181",
              "name": "Honey Buns",
              "sortIndex": 194
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473526186",
              "name": "Misc Snack Cakes",
              "sortIndex": 194
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477338113",
              "name": "Triangles",
              "sortIndex": 195
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477338684",
              "name": "Subs",
              "sortIndex": 197
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477338872",
              "name": "Heat & Eat",
              "sortIndex": 198
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339496",
              "name": "Twin Sandwiches",
              "sortIndex": 199
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339523",
              "name": "Fast Choice",
              "sortIndex": 200
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339539",
              "name": "Big Az",
              "sortIndex": 201
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477343052",
              "name": "Wraps",
              "sortIndex": 203
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477344140",
              "name": "Breakfast",
              "sortIndex": 204
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477344527",
              "name": "Market Sandwich Premium Sandwiches",
              "sortIndex": 205
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477344618",
              "name": "Market Sandwich Artisan Style",
              "sortIndex": 206
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477345011",
              "name": "Market Sandwich Mega Wedges",
              "sortIndex": 207
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477345018",
              "name": "Market Sandwich Small Wedges",
              "sortIndex": 208
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477345194",
              "name": "Deli Express Htg Breakfast Sandwiches",
              "sortIndex": 209
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477345400",
              "name": "San Luis",
              "sortIndex": 210
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477345574",
              "name": "Deli Express Small Wedge Sandwiches",
              "sortIndex": 212
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477345579",
              "name": "Market Sandwich Subs",
              "sortIndex": 213
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477345590",
              "name": "Deli Express",
              "sortIndex": 214
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477349261",
              "name": "Tony's",
              "sortIndex": 216
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477349796",
              "name": "Snack Cakes",
              "sortIndex": 217
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477349801",
              "name": "Gem Donuts",
              "sortIndex": 218
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477350333",
              "name": "Deli Express Mega Wedge Sandwiches",
              "sortIndex": 219
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477350435",
              "name": "Deli Express Classic Sandwiches",
              "sortIndex": 220
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477350930",
              "name": "Deli Express Sub Sandwiches",
              "sortIndex": 221
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477352234",
              "name": "Creme Filled Snack Cakes",
              "sortIndex": 222
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477352265",
              "name": "Fruit Pies",
              "sortIndex": 225
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "hot beverages & accompaniments",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8c9edb506c0147aee1b0e7269585a33e.jpg",
          "id": "385749462",
          "name": "Hot Beverages & Accompaniments",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 334,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749598",
              "name": "Creamer Canisters",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749600",
              "name": "Decaffeinated Teas",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749602",
              "name": "Hot Chocolate",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749603",
              "name": "Liquid Creamer Pumps",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749604",
              "name": "Steep Cafe Teas",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749605",
              "name": "Steep Organic Teas",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749606",
              "name": "Traditional & Flavored Teas",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749607",
              "name": "Traditional Teas",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 89,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473520923",
              "name": "Hot Beverages & Accompaniments",
              "sortIndex": 23
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473525819",
              "name": "Aroma Valley",
              "sortIndex": 184
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 49,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477338086",
              "name": "Ground Coffee",
              "sortIndex": 189
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477338121",
              "name": "Benefits Tea",
              "sortIndex": 190
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 37,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477338723",
              "name": "Creamer Sugar",
              "sortIndex": 191
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339058",
              "name": "Whole Bean Coffee",
              "sortIndex": 192
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339075",
              "name": "Cups/lids",
              "sortIndex": 193
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339155",
              "name": "Speciality Brand & Dove",
              "sortIndex": 194
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 20,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339799",
              "name": "Cappuccino",
              "sortIndex": 195
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477340033",
              "name": "Topping",
              "sortIndex": 196
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477340338",
              "name": "Herbal Teas-caffeine Free",
              "sortIndex": 197
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477341414",
              "name": "K Cups",
              "sortIndex": 198
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477341481",
              "name": "Serenade Mix",
              "sortIndex": 199
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477341995",
              "name": "Liquid Coffee",
              "sortIndex": 200
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 17,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477347348",
              "name": "Flavia Brand",
              "sortIndex": 201
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477347366",
              "name": "Bright Tea Co. Brand",
              "sortIndex": 202
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477347412",
              "name": "Starbucks Brand",
              "sortIndex": 204
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477352209",
              "name": "Latte & Frappe",
              "sortIndex": 206
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "hot foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6c02270a2f6f57c05ee4c2f81d532a11.jpg",
          "id": "385749669",
          "name": "Hot Foods",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 31,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749671",
              "name": "Soup",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473521909",
              "name": "Hot Foods",
              "sortIndex": 99
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339148",
              "name": "Microwaveable Bowls",
              "sortIndex": 101
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "refrigerated products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2e31a204ef045a8d2e1ef0d6a534b058.jpg",
          "id": "385749695",
          "name": "Refrigerated Products",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 33,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 27,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749696",
              "name": "Refrigerated Products",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385749697",
              "name": "Dips",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477338714",
              "name": "Balanced Breaks",
              "sortIndex": 112
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477342250",
              "name": "Creamer Sugar",
              "sortIndex": 113
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "snacks",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b4173cee91f296983c50efef349aeac3.avif",
          "id": "385750125",
          "name": "Snacks",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 415,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750126",
              "name": "50 Count",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 17,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750127",
              "name": "Bars",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750128",
              "name": "Bulk",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750129",
              "name": "Cereal",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750130",
              "name": "Clif Bar",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750132",
              "name": "Combos",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750133",
              "name": "Concession",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 31,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750134",
              "name": "Cookie",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 14,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750135",
              "name": "Crackers",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750136",
              "name": "Dips",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750137",
              "name": "K12 Approved",
              "sortIndex": 11
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 107,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750138",
              "name": "Large Single Serve",
              "sortIndex": 12
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750140",
              "name": "Nuts",
              "sortIndex": 14
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750141",
              "name": "Peg Pack",
              "sortIndex": 15
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750142",
              "name": "Poptarts",
              "sortIndex": 16
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750143",
              "name": "Pringles",
              "sortIndex": 17
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750144",
              "name": "Rice Krispie Treats",
              "sortIndex": 18
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750145",
              "name": "Single Serve",
              "sortIndex": 19
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 65,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "385750146",
              "name": "Xvl",
              "sortIndex": 20
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 69,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473520990",
              "name": "Snacks",
              "sortIndex": 31
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 25,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477338948",
              "name": "Meat Sticks/jerky",
              "sortIndex": 165
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477340422",
              "name": "Lance",
              "sortIndex": 166
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "condiments / miscellaneous",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/7c0457928ed42dac040fc89d651dfd9b.jpg",
          "id": "473521090",
          "name": "Condiments / Miscellaneous",
          "sortIndex": "13",
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
              "id": "473521091",
              "name": "Crackers",
              "sortIndex": 41
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473521427",
              "name": "Condiments / Miscellaneous",
              "sortIndex": 68
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339255",
              "name": "Condiments",
              "sortIndex": 69
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "non foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/c8d93bfdc3f758828ad106fdfc0d4d17.jpg",
          "id": "473521515",
          "name": "Non Foods",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 239,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473521516",
              "name": "Napkins",
              "sortIndex": 75
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473521642",
              "name": "Plates",
              "sortIndex": 85
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473521763",
              "name": "Non Foods",
              "sortIndex": 90
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 20,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473521768",
              "name": "Cutlery",
              "sortIndex": 91
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473522479",
              "name": "Paper Products",
              "sortIndex": 110
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473524943",
              "name": "Gloves",
              "sortIndex": 175
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 60,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477339054",
              "name": "Cups",
              "sortIndex": 181
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477340002",
              "name": "Bulk",
              "sortIndex": 182
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 45,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477340571",
              "name": "Packing/containers",
              "sortIndex": 183
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477340649",
              "name": "Container W/lid",
              "sortIndex": 184
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477340716",
              "name": "Deli Bags",
              "sortIndex": 185
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477340723",
              "name": "Hot Cup Sleeve",
              "sortIndex": 186
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 19,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477340738",
              "name": "Lids",
              "sortIndex": 187
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477341123",
              "name": "Filters",
              "sortIndex": 188
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477341321",
              "name": "Bowls",
              "sortIndex": 189
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477341449",
              "name": "Stir Sticks",
              "sortIndex": 190
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477341833",
              "name": "Container",
              "sortIndex": 191
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477350368",
              "name": "Can Liner",
              "sortIndex": 194
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "boxes",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9d45270f9dbf572e7f7c19b6dfb37ce1.jpg",
          "id": "473523075",
          "name": "Boxes",
          "sortIndex": "19",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 33,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 31,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "473523076",
              "name": "Boxes",
              "sortIndex": 123
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "547560675",
              "name": "Share Size",
              "sortIndex": 228
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cups/lids",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/41c1cb85e39b35083cf30f4a35837e0e.jpg",
          "id": "477352603",
          "name": "Cups/lids",
          "sortIndex": "24",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 1,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "477352604",
              "name": "Cups/lids",
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
        self.options['base_url'] = self.BASE_URL
