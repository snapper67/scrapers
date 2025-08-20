import json
from .dry import CutScraper


class CityLineFoodsScraper(CutScraper):
    """Scraper for City Line Foods on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/citylinefoods/'

    # Values to change
    BASE_URL = "https://citylinefoods.cutanddry.com/catalog/citylinefoods?verifiedVendorId=1861897&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://citylinefoods.cutanddry.com"
    VENDOR_URL_NAME = 'citylinefoods'
    VERIFIED_VENDOR_ID = 1861897

    # This the name of the vendor
    VENDOR_NAME = "City Line Foods"

    # Categories will be fetched dynamically
    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "506469943",
          "name": "Seafood",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 455,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506469944",
              "name": "Seafood",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 74,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864533",
              "name": "Mussels / Clams / Oysters",
              "sortIndex": 16
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 51,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864535",
              "name": "Lobster",
              "sortIndex": 17
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 19,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864551",
              "name": "Value-added",
              "sortIndex": 18
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 153,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864553",
              "name": "Fin Fish",
              "sortIndex": 19
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 33,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864555",
              "name": "Crab",
              "sortIndex": 20
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864610",
              "name": "Other Seafood",
              "sortIndex": 22
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 26,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867699",
              "name": "Calamari & Octopus",
              "sortIndex": 147
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 72,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867737",
              "name": "Shrimp - Raw",
              "sortIndex": 149
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867950",
              "name": "Shrimp - Cooked",
              "sortIndex": 150
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "boxed beef/veal/pork",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "506470879",
          "name": "Boxed Beef/veal/pork",
          "sortIndex": "6",
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
              "id": "506470880",
              "name": "Boxed Beef/veal/pork",
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
          "iconUrl": null,
          "id": "506473311",
          "name": "Poultry",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 292,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 78,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "506473312",
              "name": "Poultry",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865730",
              "name": "Chicken - Wog",
              "sortIndex": 84
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868330",
              "name": "Chicken - Breaded Tenders",
              "sortIndex": 163
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868842",
              "name": "Chicken - Piece Meat",
              "sortIndex": 185
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 19,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868923",
              "name": "Chicken - Tenders",
              "sortIndex": 188
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870092",
              "name": "Turkey Other",
              "sortIndex": 197
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870156",
              "name": "Chicken Breast - Split",
              "sortIndex": 198
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870157",
              "name": "Chicken Whole Fryer",
              "sortIndex": 199
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870213",
              "name": "Chicken Thigh Meat",
              "sortIndex": 200
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870215",
              "name": "Chicken - Drumsticks",
              "sortIndex": 201
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870217",
              "name": "Chicken Wings - Party",
              "sortIndex": 202
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870223",
              "name": "Chicken Wings - Whole",
              "sortIndex": 203
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 74,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870225",
              "name": "Chicken Breast - Halves",
              "sortIndex": 204
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870228",
              "name": "Chicken Necks / Backs / Feet",
              "sortIndex": 205
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870265",
              "name": "Chicken Giblets",
              "sortIndex": 206
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870266",
              "name": "Chicken - Whole",
              "sortIndex": 207
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870296",
              "name": "Chicken Nuggets",
              "sortIndex": 209
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 31,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870537",
              "name": "Turkey - Breast",
              "sortIndex": 211
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870543",
              "name": "Turkey - Whole",
              "sortIndex": 212
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870559",
              "name": "Turkey - Thigh Meat",
              "sortIndex": 213
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870560",
              "name": "Turkey - Drumsticks",
              "sortIndex": 214
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "506474878",
          "name": "Produce",
          "sortIndex": "10",
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
              "id": "506474879",
              "name": "Produce",
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
          "iconUrl": null,
          "id": "530847225",
          "name": "Non-food/disposables",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 748,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 58,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530847226",
              "name": "Non-food/disposables",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864593",
              "name": "Food Storage - Micro",
              "sortIndex": 21
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 73,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865793",
              "name": "Equipment",
              "sortIndex": 89
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866089",
              "name": "Coffee Filters",
              "sortIndex": 98
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 55,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866090",
              "name": "Cups / Lids",
              "sortIndex": 99
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 45,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868114",
              "name": "Bag - Paper To-go",
              "sortIndex": 152
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 51,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868318",
              "name": "Food Storage - Other",
              "sortIndex": 161
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868329",
              "name": "Trash Bags",
              "sortIndex": 162
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 37,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868346",
              "name": "Foil / Film / Rolls / Wraps",
              "sortIndex": 164
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 40,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868349",
              "name": "Kitchen & Cutlery",
              "sortIndex": 165
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 33,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868424",
              "name": "Paper Towels / Tissue",
              "sortIndex": 166
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868425",
              "name": "Food Storage - Hinged",
              "sortIndex": 167
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868435",
              "name": "Container - Foam",
              "sortIndex": 168
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868441",
              "name": "Plates & Bowls - Other",
              "sortIndex": 169
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868465",
              "name": "Bag - Plastic To-go",
              "sortIndex": 170
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868474",
              "name": "Food Pails",
              "sortIndex": 171
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 29,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868477",
              "name": "Napkins / Table Top",
              "sortIndex": 172
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 32,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868481",
              "name": "Aprons / Bibs / Gloves / Headware",
              "sortIndex": 173
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 23,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868490",
              "name": "Food Storage - Deli",
              "sortIndex": 174
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 14,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868492",
              "name": "Plates - Paper",
              "sortIndex": 175
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868497",
              "name": "Aluminum Pans",
              "sortIndex": 176
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868504",
              "name": "Catering Supplies",
              "sortIndex": 177
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868507",
              "name": "Straws",
              "sortIndex": 178
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868735",
              "name": "Meat Pad",
              "sortIndex": 179
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 56,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868789",
              "name": "Pizza Boxes",
              "sortIndex": 182
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 48,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "541946709",
              "name": "Cleaning Supplies",
              "sortIndex": 302
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "grocery - dry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "530847279",
          "name": "Grocery - Dry",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 1571,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 36,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530847280",
              "name": "Grocery - Dry",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 207,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864611",
              "name": "Spice / Seasoning",
              "sortIndex": 23
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 45,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864633",
              "name": "Ingredients",
              "sortIndex": 25
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864647",
              "name": "Other",
              "sortIndex": 26
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 49,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864651",
              "name": "Syrups / Toppings",
              "sortIndex": 27
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864668",
              "name": "Baking Ingredients - Bulk",
              "sortIndex": 28
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 38,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864702",
              "name": "Cereal & Grains",
              "sortIndex": 30
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 34,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864705",
              "name": "Rice",
              "sortIndex": 31
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 26,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866109",
              "name": "Crackers/cookies",
              "sortIndex": 101
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 41,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866264",
              "name": "Sauce - Asian",
              "sortIndex": 108
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 117,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866266",
              "name": "Dressing / Mayo",
              "sortIndex": 109
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 80,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866277",
              "name": "Sauce - Other Shelf Stable",
              "sortIndex": 110
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 117,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866278",
              "name": "Condiments",
              "sortIndex": 111
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 45,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866430",
              "name": "Vinegar/cooking Wine",
              "sortIndex": 112
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 67,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866435",
              "name": "Canned Tomato Product",
              "sortIndex": 113
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 17,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866470",
              "name": "Olives",
              "sortIndex": 114
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 105,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866471",
              "name": "Vegetables",
              "sortIndex": 115
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866530",
              "name": "Pickles",
              "sortIndex": 116
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866580",
              "name": "Canned Seafood",
              "sortIndex": 120
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 17,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866582",
              "name": "Marinades / Dips",
              "sortIndex": 121
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 23,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866583",
              "name": "Sauce - Bbq",
              "sortIndex": 122
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 78,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866674",
              "name": "Bases & Gravy",
              "sortIndex": 125
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 120,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866725",
              "name": "Snacks/nuts",
              "sortIndex": 127
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867111",
              "name": "Sauce - Cheese",
              "sortIndex": 138
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867149",
              "name": "Peanut Butter",
              "sortIndex": 140
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 46,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867736",
              "name": "Fruit",
              "sortIndex": 148
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 38,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868229",
              "name": "Canned Beans",
              "sortIndex": 158
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868239",
              "name": "Canned Meat",
              "sortIndex": 159
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 124,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530871196",
              "name": "Pasta",
              "sortIndex": 222
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 26,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530871427",
              "name": "Sugar / Sugar Substitutes",
              "sortIndex": 223
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "541933318",
              "name": "Dips / Spreads / Dressings",
              "sortIndex": 300
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "bakery & desserts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "530847282",
          "name": "Bakery & Desserts",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 680,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 106,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864614",
              "name": "Bakery Ingredients / Mixes",
              "sortIndex": 24
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 58,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864697",
              "name": "Bread",
              "sortIndex": 29
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866122",
              "name": "Dough",
              "sortIndex": 102
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 43,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866123",
              "name": "Pastries",
              "sortIndex": 103
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 32,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866124",
              "name": "Pizza Crusts & Dough",
              "sortIndex": 104
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 55,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866144",
              "name": "Rolls / Buns",
              "sortIndex": 106
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 122,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866579",
              "name": "Cakes",
              "sortIndex": 119
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 45,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866681",
              "name": "Taco & Tortilla Shells",
              "sortIndex": 126
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 23,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866740",
              "name": "Dinner Rolls & Biscuits",
              "sortIndex": 128
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 86,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866777",
              "name": "Cookies / Brownies / Bars",
              "sortIndex": 129
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 25,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866779",
              "name": "Muffins",
              "sortIndex": 130
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 25,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866867",
              "name": "Bagels",
              "sortIndex": 131
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 20,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867311",
              "name": "Other Desserts",
              "sortIndex": 144
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 26,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867425",
              "name": "Pies",
              "sortIndex": 145
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867499",
              "name": "Croissants",
              "sortIndex": 146
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "grocery - cooler",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "530847360",
          "name": "Grocery - Cooler",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 225,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 94,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530847361",
              "name": "Grocery - Cooler",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 59,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866108",
              "name": "Dips / Spreads / Dressings",
              "sortIndex": 100
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866224",
              "name": "Fruit Cups / Salads",
              "sortIndex": 107
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 42,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866569",
              "name": "Prepared Salads",
              "sortIndex": 118
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867640",
              "name": "Snacks/nuts",
              "sortIndex": 147
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867579",
              "name": "Ingredients",
              "sortIndex": 147
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530871119",
              "name": "Fresh Soup",
              "sortIndex": 219
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530871666",
              "name": "Fresh Salsa",
              "sortIndex": 224
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "541934307",
              "name": "Dressing / Mayo",
              "sortIndex": 301
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "541940101",
              "name": "Pastries",
              "sortIndex": 302
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
          "iconUrl": null,
          "id": "530847387",
          "name": "Frozen Foods",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 741,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 21,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530847388",
              "name": "Frozen Foods",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864706",
              "name": "Entrees",
              "sortIndex": 32
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864710",
              "name": "Sauces",
              "sortIndex": 33
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 34,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864718",
              "name": "Desserts/pastries/baked Goods",
              "sortIndex": 34
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 19,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865538",
              "name": "Meat Alternatives",
              "sortIndex": 81
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865767",
              "name": "Value-added Steak",
              "sortIndex": 88
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 134,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866128",
              "name": "Appetizers",
              "sortIndex": 105
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 82,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866536",
              "name": "Vegetables",
              "sortIndex": 117
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866537",
              "name": "Potatoes",
              "sortIndex": 117
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866671",
              "name": "Dips",
              "sortIndex": 124
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 97,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867307",
              "name": "Ice Cream",
              "sortIndex": 144
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867408",
              "name": "Condiments",
              "sortIndex": 145
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 92,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867991",
              "name": "French Fries",
              "sortIndex": 151
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 46,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868067",
              "name": "Fruit",
              "sortIndex": 152
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 52,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530871120",
              "name": "Soup",
              "sortIndex": 220
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 85,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530871131",
              "name": "Pasta",
              "sortIndex": 221
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530871690",
              "name": "Onion Rings",
              "sortIndex": 225
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "541948257",
              "name": "Pizza Crusts & Dough",
              "sortIndex": 304
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "beef",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "530847390",
          "name": "Beef",
          "sortIndex": "18",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 715,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 89,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530847391",
              "name": "Beef",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 76,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864719",
              "name": "Ribeye Bnls",
              "sortIndex": 35
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864720",
              "name": "Inside Round",
              "sortIndex": 36
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 105,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864722",
              "name": "Loin Strips",
              "sortIndex": 38
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864723",
              "name": "Ribs Beef",
              "sortIndex": 39
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 35,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864725",
              "name": "Export Ribeye B/i",
              "sortIndex": 40
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864726",
              "name": "Beef Offals",
              "sortIndex": 41
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 38,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864733",
              "name": "Patties",
              "sortIndex": 42
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 29,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864737",
              "name": "Shaved Steak",
              "sortIndex": 43
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864744",
              "name": "Steak Tips",
              "sortIndex": 44
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 19,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864753",
              "name": "Thin Briskets",
              "sortIndex": 45
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864754",
              "name": "Bottom Flats",
              "sortIndex": 46
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864755",
              "name": "Thin Brisket Flats",
              "sortIndex": 47
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864756",
              "name": "Eye-round",
              "sortIndex": 48
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 40,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864792",
              "name": "Short Ribs",
              "sortIndex": 49
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864802",
              "name": "Thin Flap",
              "sortIndex": 50
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 89,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864805",
              "name": "Loin Peeled Tenders",
              "sortIndex": 51
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864810",
              "name": "Loin 1x1 Stirips B/i",
              "sortIndex": 52
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864811",
              "name": "Chuck Teres Major",
              "sortIndex": 53
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864812",
              "name": "Thin Outside Skirt",
              "sortIndex": 54
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864815",
              "name": "Whole Tenders",
              "sortIndex": 55
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864839",
              "name": "Loin 0x1 Strip",
              "sortIndex": 56
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864846",
              "name": "Chuck Clods",
              "sortIndex": 57
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864850",
              "name": "Loins - Culottes",
              "sortIndex": 58
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864862",
              "name": "Thin Inside Skirt",
              "sortIndex": 59
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864889",
              "name": "Loins Short Loin",
              "sortIndex": 60
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864914",
              "name": "Chuck Tenders",
              "sortIndex": 61
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864936",
              "name": "Loin Tails",
              "sortIndex": 63
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 35,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864949",
              "name": "Loins Top Butts",
              "sortIndex": 64
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530864952",
              "name": "Thin Hanging Tenders",
              "sortIndex": 65
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865059",
              "name": "Back Ribs",
              "sortIndex": 66
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865063",
              "name": "Bones Fresh",
              "sortIndex": 67
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865065",
              "name": "Thin Flank",
              "sortIndex": 68
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865066",
              "name": "Chuck Rolls",
              "sortIndex": 69
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865070",
              "name": "Peeled Knuckles",
              "sortIndex": 72
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865073",
              "name": "Beef Cubes",
              "sortIndex": 74
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865074",
              "name": "Flat Rounds",
              "sortIndex": 75
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865393",
              "name": "Ground Beef",
              "sortIndex": 78
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865523",
              "name": "Chuck Flap",
              "sortIndex": 80
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865754",
              "name": "Pork",
              "sortIndex": 86
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866139",
              "name": "Value-added Steak",
              "sortIndex": 106
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530869582",
              "name": "Tripe",
              "sortIndex": 192
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "541947148",
              "name": "Sausage",
              "sortIndex": 303
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "lamb & veal",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "530847980",
          "name": "Lamb & Veal",
          "sortIndex": "20",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 118,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530847982",
              "name": "Lamb & Veal",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 45,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865068",
              "name": "Fresh Lamb",
              "sortIndex": 70
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865728",
              "name": "Frozen Veal",
              "sortIndex": 82
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 58,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865729",
              "name": "Fresh Veal",
              "sortIndex": 83
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865731",
              "name": "Offals",
              "sortIndex": 85
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868224",
              "name": "Frozen Lamb",
              "sortIndex": 156
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "541933380",
              "name": "Spice / Seasoning",
              "sortIndex": 301
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "541948285",
              "name": "Ingredients",
              "sortIndex": 304
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "pork",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "530847986",
          "name": "Pork",
          "sortIndex": "21",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 213,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530847987",
              "name": "Pork",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865413",
              "name": "Boar",
              "sortIndex": 79
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868173",
              "name": "Whole Pig",
              "sortIndex": 153
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 23,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868174",
              "name": "Pork Other",
              "sortIndex": 154
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868175",
              "name": "Offals",
              "sortIndex": 155
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868225",
              "name": "Ribs",
              "sortIndex": 157
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 20,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868782",
              "name": "Loins",
              "sortIndex": 181
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 32,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868790",
              "name": "Pork Chops",
              "sortIndex": 183
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868794",
              "name": "Butt",
              "sortIndex": 184
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868846",
              "name": "Belly",
              "sortIndex": 186
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868915",
              "name": "Ground",
              "sortIndex": 187
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530869056",
              "name": "Bacon - Cooked",
              "sortIndex": 189
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530869064",
              "name": "Bacon - Sliced",
              "sortIndex": 190
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 26,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530869119",
              "name": "Bacon",
              "sortIndex": 191
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 47,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530869656",
              "name": "Hams - Whole",
              "sortIndex": 193
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530869920",
              "name": "Picnic",
              "sortIndex": 195
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870022",
              "name": "Pizza Topping",
              "sortIndex": 196
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "game",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "530848065",
          "name": "Game",
          "sortIndex": "22",
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
              "id": "530848066",
              "name": "Game",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865198",
              "name": "Bison",
              "sortIndex": 76
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865389",
              "name": "Elk",
              "sortIndex": 77
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530868219",
              "name": "Goat",
              "sortIndex": 155
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870501",
              "name": "Duck/quail",
              "sortIndex": 210
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
          "iconUrl": null,
          "id": "530848231",
          "name": "Beverages",
          "sortIndex": "23",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 378,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530848232",
              "name": "Beverages",
              "sortIndex": 11
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 46,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865794",
              "name": "Coffee & Tea",
              "sortIndex": 90
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 141,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865956",
              "name": "Syrups/mixes",
              "sortIndex": 91
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865819",
              "name": "Bison",
              "sortIndex": 91
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 20,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865957",
              "name": "Other Drinks",
              "sortIndex": 92
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 67,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865958",
              "name": "Juice Canned / Boxed / Bottled",
              "sortIndex": 93
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865980",
              "name": "Water",
              "sortIndex": 96
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 54,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865981",
              "name": "Soda",
              "sortIndex": 97
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "541932359",
              "name": "Milk",
              "sortIndex": 299
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dairy & eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "530848324",
          "name": "Dairy & Eggs",
          "sortIndex": "24",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 349,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 51,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530848325",
              "name": "Dairy & Eggs",
              "sortIndex": 12
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 25,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865968",
              "name": "Milk",
              "sortIndex": 94
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 29,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530865969",
              "name": "Dairy Alternative",
              "sortIndex": 95
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530866663",
              "name": "Butter / Spreads",
              "sortIndex": 123
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867090",
              "name": "Eggs & Egg Substitutes",
              "sortIndex": 132
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 61,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867091",
              "name": "Cheese - Shredded / Shaved / Crumble / Grated",
              "sortIndex": 133
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867092",
              "name": "Cheese - Wheels",
              "sortIndex": 134
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 26,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867104",
              "name": "Cultures/cottage Cheese",
              "sortIndex": 135
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 72,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867105",
              "name": "Cheese - Processed Sliced",
              "sortIndex": 136
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867109",
              "name": "Cheese Loaf",
              "sortIndex": 137
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867142",
              "name": "Cheese - Spreadable",
              "sortIndex": 139
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867241",
              "name": "Cream Cheese",
              "sortIndex": 141
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867249",
              "name": "Yogurt",
              "sortIndex": 142
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530867250",
              "name": "Sour Cream",
              "sortIndex": 143
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "oil & shortening",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "530849779",
          "name": "Oil & Shortening",
          "sortIndex": "25",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 82,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530849780",
              "name": "Oil & Shortening",
              "sortIndex": 13
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 77,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870693",
              "name": "Oils",
              "sortIndex": 217
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530870715",
              "name": "Pan Sprays",
              "sortIndex": 218
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "541939709",
              "name": "Lard Cubes",
              "sortIndex": 301
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "chemicals",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "530851460",
          "name": "Chemicals",
          "sortIndex": "26",
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
              "id": "530868743",
              "name": "Cleaning Supplies",
              "sortIndex": 180
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fresh produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "530855038",
          "name": "Fresh Produce",
          "sortIndex": "27",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 399,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 318,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530871592",
              "name": "Vegetables",
              "sortIndex": 224
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530871716",
              "name": "Fresh Juice",
              "sortIndex": 226
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 80,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "530871718",
              "name": "Fruit",
              "sortIndex": 227
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "seafood (e)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535013559",
          "name": "Seafood (e)",
          "sortIndex": "57",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 147,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 147,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535013560",
              "name": "Seafood (e)",
              "sortIndex": 285
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "non - foods (e)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535013566",
          "name": "Non - Foods (e)",
          "sortIndex": "58",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 71,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 71,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535013567",
              "name": "Non - Foods (e)",
              "sortIndex": 286
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "product w/ equipt. (e)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535013765",
          "name": "Product W/ Equipt. (e)",
          "sortIndex": "59",
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
              "id": "535013766",
              "name": "Product W/ Equipt. (e)",
              "sortIndex": 287
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "grocery (e)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535013770",
          "name": "Grocery (e)",
          "sortIndex": "60",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 122,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 122,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535013771",
              "name": "Grocery (e)",
              "sortIndex": 288
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "frozen other (e)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535013949",
          "name": "Frozen Other (e)",
          "sortIndex": "61",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 130,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 130,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535013950",
              "name": "Frozen Other (e)",
              "sortIndex": 289
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "other meat (e)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535013993",
          "name": "Other Meat (e)",
          "sortIndex": "62",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 109,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 109,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535013994",
              "name": "Other Meat (e)",
              "sortIndex": 290
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "boxed beef/veal/pork (e)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535013995",
          "name": "Boxed Beef/veal/pork (e)",
          "sortIndex": "63",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 61,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 61,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535013996",
              "name": "Boxed Beef/veal/pork (e)",
              "sortIndex": 291
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "deli/processed & cured meats",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535013999",
          "name": "Deli/processed & Cured Meats",
          "sortIndex": "64",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 244,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 75,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535014000",
              "name": "Deli Meat Slicing Loaves",
              "sortIndex": 292
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535015185",
              "name": "Deli Other",
              "sortIndex": 295
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 33,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535018458",
              "name": "Hot Dogs",
              "sortIndex": 298
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535020512",
              "name": "Kielbasa & Brats",
              "sortIndex": 299
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 114,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535019466",
              "name": "Sausage",
              "sortIndex": 299
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535020350",
              "name": "Liverwurst / Knockwurst",
              "sortIndex": 299
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fabricated meat (e)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535014047",
          "name": "Fabricated Meat (e)",
          "sortIndex": "65",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 24,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535014048",
              "name": "Fabricated Meat (e)",
              "sortIndex": 293
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "poultry (e)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535015166",
          "name": "Poultry (e)",
          "sortIndex": "66",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 47,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 47,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535015167",
              "name": "Poultry (e)",
              "sortIndex": 294
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "produce (e)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535015481",
          "name": "Produce (e)",
          "sortIndex": "67",
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
              "id": "535015482",
              "name": "Produce (e)",
              "sortIndex": 295
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dairy (e)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535016050",
          "name": "Dairy (e)",
          "sortIndex": "68",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 13,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535016051",
              "name": "Dairy (e)",
              "sortIndex": 296
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "ice cream (e)",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "535016282",
          "name": "Ice Cream (e)",
          "sortIndex": "69",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 13,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "535016283",
              "name": "Ice Cream (e)",
              "sortIndex": 297
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
