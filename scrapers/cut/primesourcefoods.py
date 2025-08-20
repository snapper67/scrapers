import json
from .dry import CutScraper


class PrimeSourceFoodsScraper(CutScraper):
    """Scraper for Prime Source Foods on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/primesourcefoods/'

    # Values to change
    BASE_URL = "https://primesourcefoods.cutanddry.com/catalog/primesourcefoods?verifiedVendorId=430993089&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://primesourcefoods.cutanddry.com"
    VENDOR_URL_NAME = 'primesourcefoods'
    VERIFIED_VENDOR_ID = 430993089

    # This the name of the vendor
    VENDOR_NAME = "Prime Source Foods"

    # Categories will be fetched dynamically
    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "beef",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d2814686728834216fbcaa2f590a4866.jpg",
          "id": "434898295",
          "name": "Beef",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 431,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820051",
              "name": "Whole Tenders",
              "sortIndex": 273
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820057",
              "name": "Chuck Rolls",
              "sortIndex": 275
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820060",
              "name": "Thin Flap",
              "sortIndex": 276
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820065",
              "name": "Chuck Clods",
              "sortIndex": 277
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 31,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820068",
              "name": "Beef",
              "sortIndex": 278
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820088",
              "name": "Loins Tri-tips",
              "sortIndex": 279
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820149",
              "name": "Chuck Tenders",
              "sortIndex": 280
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820161",
              "name": "Chuck Clod Hearts",
              "sortIndex": 281
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820164",
              "name": "Chuck Flap",
              "sortIndex": 282
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820167",
              "name": "Short Ribs",
              "sortIndex": 283
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820178",
              "name": "Chucks Eye Rolls",
              "sortIndex": 284
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820182",
              "name": "Chuck Semi-boneless",
              "sortIndex": 285
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820191",
              "name": "Chuck Blades",
              "sortIndex": 286
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820197",
              "name": "Chuck Teres Major",
              "sortIndex": 287
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 17,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820240",
              "name": "Loin 0x1 Strip",
              "sortIndex": 288
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 14,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820245",
              "name": "Loins Top Butts",
              "sortIndex": 289
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820248",
              "name": "Loins - Culottes",
              "sortIndex": 290
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820256",
              "name": "Loins Short Loin",
              "sortIndex": 291
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820261",
              "name": "Thin Briskets",
              "sortIndex": 292
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820265",
              "name": "Loins 1x1 Strips",
              "sortIndex": 293
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820368",
              "name": "Loin Butt Tenders",
              "sortIndex": 295
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 27,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820492",
              "name": "Ribeye Bnls",
              "sortIndex": 296
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820502",
              "name": "Export Ribeye B/i",
              "sortIndex": 297
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820551",
              "name": "Peeled Knuckles",
              "sortIndex": 298
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 17,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820558",
              "name": "Inside Round",
              "sortIndex": 299
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820619",
              "name": "Bottom Flats",
              "sortIndex": 300
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820626",
              "name": "Eye-round",
              "sortIndex": 301
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820727",
              "name": "Heel Meat",
              "sortIndex": 303
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820793",
              "name": "Thin Brisket Flats",
              "sortIndex": 304
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820807",
              "name": "Thin Outside Skirt",
              "sortIndex": 306
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820847",
              "name": "Thin Hanging Tenders",
              "sortIndex": 308
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820858",
              "name": "Beef Trimmings",
              "sortIndex": 309
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820865",
              "name": "Chuck Shanks",
              "sortIndex": 310
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820877",
              "name": "Peeled Flap",
              "sortIndex": 311
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820889",
              "name": "Bones Fresh",
              "sortIndex": 312
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 79,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820920",
              "name": "Portion Steaks",
              "sortIndex": 313
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820924",
              "name": "Steak Tips",
              "sortIndex": 314
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820955",
              "name": "Patties",
              "sortIndex": 315
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820967",
              "name": "Beef Offals",
              "sortIndex": 316
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820975",
              "name": "Rib Roll",
              "sortIndex": 317
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820980",
              "name": "Beef Cubes",
              "sortIndex": 318
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821015",
              "name": "Tripe",
              "sortIndex": 319
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821029",
              "name": "Misc Beef",
              "sortIndex": 320
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822808",
              "name": "Shaved Steak",
              "sortIndex": 354
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499825571",
              "name": "Back Ribs",
              "sortIndex": 412
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499829310",
              "name": "Ribs Beef",
              "sortIndex": 428
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499829650",
              "name": "Peeled Butt Tender",
              "sortIndex": 432
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499829826",
              "name": "Finger Meat",
              "sortIndex": 433
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499829888",
              "name": "Bison",
              "sortIndex": 435
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499832285",
              "name": "Export Ribs",
              "sortIndex": 442
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "519139801",
              "name": "Loin Strips",
              "sortIndex": 443
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544743766",
              "name": "Value-added Steak",
              "sortIndex": 449
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "549695549",
              "name": "Thin Flank",
              "sortIndex": 480
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "549695761",
              "name": "Lifter Meat",
              "sortIndex": 482
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "555071039",
              "name": "Loin Tails",
              "sortIndex": 490
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 17,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "592503580",
              "name": "Ground Beef",
              "sortIndex": 502
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "other protein",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/ddcd203b814124309c354972f19dcdf2.jpg",
          "id": "434898300",
          "name": "Other Protein",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 3,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820017",
              "name": "Other Protein",
              "sortIndex": 270
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2efcaedc017d3675c7afa9f96e30fe12.jpg",
          "id": "434898305",
          "name": "Pork",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 72,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821157",
              "name": "Pork",
              "sortIndex": 326
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821328",
              "name": "Pork Chops",
              "sortIndex": 328
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821337",
              "name": "Bacon - Sliced",
              "sortIndex": 329
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821872",
              "name": "Bacon",
              "sortIndex": 336
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822513",
              "name": "Pork Other",
              "sortIndex": 346
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822879",
              "name": "Belly",
              "sortIndex": 357
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499826628",
              "name": "Ribs",
              "sortIndex": 414
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499826666",
              "name": "Ct Butt",
              "sortIndex": 415
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499827508",
              "name": "Boar",
              "sortIndex": 420
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499827773",
              "name": "Bones",
              "sortIndex": 421
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499828199",
              "name": "Loins",
              "sortIndex": 423
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499830414",
              "name": "Butt",
              "sortIndex": 439
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544743925",
              "name": "Picnic",
              "sortIndex": 450
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544743968",
              "name": "Offals",
              "sortIndex": 452
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544743988",
              "name": "Trimmings",
              "sortIndex": 453
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8e0f46b88a61445facd388e88b4f0a55.jpg",
          "id": "434898318",
          "name": "Poultry",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 185,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499819705",
              "name": "Chicken Thigh Meat",
              "sortIndex": 251
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499819708",
              "name": "Chicken Breast - Halves",
              "sortIndex": 252
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499819734",
              "name": "Pcr - Portion Chicken",
              "sortIndex": 255
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499819739",
              "name": "Chicken Leg Meat",
              "sortIndex": 256
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499819771",
              "name": "Chicken - Drumsticks",
              "sortIndex": 257
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 31,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499819777",
              "name": "Poultry",
              "sortIndex": 259
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499819780",
              "name": "Chicken Whole Fryer",
              "sortIndex": 260
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499819787",
              "name": "Chicken Giblets",
              "sortIndex": 261
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499819821",
              "name": "Chicken - Tenders",
              "sortIndex": 262
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499819898",
              "name": "Chicken Wings - Party",
              "sortIndex": 264
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499819903",
              "name": "Chicken Wings - Whole",
              "sortIndex": 265
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499819950",
              "name": "Chicken - Ground",
              "sortIndex": 266
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820011",
              "name": "Chicken - Rendered Fat",
              "sortIndex": 268
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820014",
              "name": "Chicken - Piece Meat",
              "sortIndex": 269
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499820048",
              "name": "Chicken - Bones",
              "sortIndex": 272
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821531",
              "name": "Turkey - Breast",
              "sortIndex": 330
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821545",
              "name": "Turkey - Whole",
              "sortIndex": 331
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821671",
              "name": "Turkey - Tenders",
              "sortIndex": 332
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499829856",
              "name": "Turkey Wings",
              "sortIndex": 434
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "519140044",
              "name": "Turkey Other",
              "sortIndex": 436
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544743755",
              "name": "Chicken Thighs",
              "sortIndex": 446
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 14,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544743756",
              "name": "Chicken Breast Whole",
              "sortIndex": 447
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544743758",
              "name": "Chicken Leg Quarters",
              "sortIndex": 448
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544744159",
              "name": "Chicken - Breaded Tenders",
              "sortIndex": 461
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "549695497",
              "name": "Chicken Breast - Split",
              "sortIndex": 479
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "592503354",
              "name": "Chicken - Wog",
              "sortIndex": 499
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "592503415",
              "name": "Chicken - Whole",
              "sortIndex": 500
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "592503446",
              "name": "Chicken Necks / Backs / Feet",
              "sortIndex": 501
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/10b131c779cafe53bec73368920909ab.jpg",
          "id": "434898322",
          "name": "Grocery - Cooler",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 11,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822633",
              "name": "Prepared Salads",
              "sortIndex": 350
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823348",
              "name": "Fresh Soup",
              "sortIndex": 374
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "592504175",
              "name": "Dips / Spreads / Dressings",
              "sortIndex": 504
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "prime cutting room",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9b3ebe36b87e465fa19487af12b98cc6.jpg",
          "id": "434898331",
          "name": "Prime Cutting Room",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 11,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822876",
              "name": "Prime Cutting Room",
              "sortIndex": 356
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/36601c9b5c4c070ba642074df4d0f8aa.jpg",
          "id": "434898355",
          "name": "Deli/processed & Cured Meats",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 64,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821922",
              "name": "Deli Meat Slicing Loaves",
              "sortIndex": 338
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822244",
              "name": "Hot Dogs",
              "sortIndex": 344
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822505",
              "name": "Sausage",
              "sortIndex": 346
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822406",
              "name": "Liverwurst / Knockwurst",
              "sortIndex": 346
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499827365",
              "name": "Deli Other",
              "sortIndex": 418
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "519140068",
              "name": "Deli/processed & Cured Meats",
              "sortIndex": 419
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e7d04758912753ba1438a867c593dcfe.jpg",
          "id": "434898411",
          "name": "Seafood",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 34,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822929",
              "name": "Shrimp - Cooked",
              "sortIndex": 360
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822939",
              "name": "Shrimp - Raw",
              "sortIndex": 361
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822946",
              "name": "Seafood",
              "sortIndex": 362
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822966",
              "name": "Fin Fish",
              "sortIndex": 365
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823064",
              "name": "Lobster",
              "sortIndex": 366
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823154",
              "name": "Other Seafood",
              "sortIndex": 367
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544744124",
              "name": "Crab",
              "sortIndex": 456
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544744137",
              "name": "Calamari & Octopus",
              "sortIndex": 457
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "592506141",
              "name": "Mussels / Clams / Oysters",
              "sortIndex": 508
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/c589c4ebef7e15cf63c020f138cfb9a1.jpg",
          "id": "434898462",
          "name": "Lamb & Veal",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 18,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821057",
              "name": "Frozen Lamb",
              "sortIndex": 321
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821086",
              "name": "Fresh Lamb",
              "sortIndex": 322
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821129",
              "name": "Frozen Veal",
              "sortIndex": 323
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "526662622",
              "name": "Fresh Veal",
              "sortIndex": 445
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/eeba2b4fb84d930c1c4e6ed2396c8daa.jpg",
          "id": "434898518",
          "name": "Chemicals",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 3,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499829201",
              "name": "Cleaning Supplies",
              "sortIndex": 427
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/281a512e66ba1dd615ee5f5bb171c710.jpg",
          "id": "434898525",
          "name": "Dairy & Eggs",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 22,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821926",
              "name": "Cheese - Processed Sliced",
              "sortIndex": 338
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821992",
              "name": "Cheese - Wheels",
              "sortIndex": 340
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499821997",
              "name": "Cream Cheese",
              "sortIndex": 341
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823305",
              "name": "Cultures/cottage Cheese",
              "sortIndex": 372
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499829999",
              "name": "Dairy & Eggs",
              "sortIndex": 437
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499830419",
              "name": "Yogurt",
              "sortIndex": 440
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499831017",
              "name": "Milk",
              "sortIndex": 441
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "592504202",
              "name": "Cheese - Shredded / Shaved / Crumble / Grated",
              "sortIndex": 505
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8353cec53f7a8fbd4f5ce23ead9722db.jpg",
          "id": "434898545",
          "name": "Grocery - Dry",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 52,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823245",
              "name": "Vegetables",
              "sortIndex": 368
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823907",
              "name": "Sauce - Bbq",
              "sortIndex": 380
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823944",
              "name": "Marinades / Dips",
              "sortIndex": 382
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823952",
              "name": "Condiments",
              "sortIndex": 383
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823956",
              "name": "Sauce - Asian",
              "sortIndex": 384
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823984",
              "name": "Dressing / Mayo",
              "sortIndex": 385
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824039",
              "name": "Baking Ingredients - Bulk",
              "sortIndex": 386
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824077",
              "name": "Fruit",
              "sortIndex": 388
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824144",
              "name": "Snacks/nuts",
              "sortIndex": 390
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824173",
              "name": "Pasta",
              "sortIndex": 391
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824192",
              "name": "Pickles",
              "sortIndex": 392
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824215",
              "name": "Rice",
              "sortIndex": 393
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824340",
              "name": "Syrups / Toppings",
              "sortIndex": 395
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824351",
              "name": "Ingredients",
              "sortIndex": 396
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499825829",
              "name": "Canned Tomato Product",
              "sortIndex": 413
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499826689",
              "name": "Spice / Seasoning",
              "sortIndex": 416
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499828302",
              "name": "Grocery - Dry",
              "sortIndex": 424
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499829955",
              "name": "Bases & Gravy",
              "sortIndex": 436
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544744158",
              "name": "Sauce - Other Shelf Stable",
              "sortIndex": 460
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544744299",
              "name": "Canned Beans",
              "sortIndex": 466
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "549695935",
              "name": "Cereal & Grains",
              "sortIndex": 484
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "592507543",
              "name": "Potatoes",
              "sortIndex": 517
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8faa6c197798cb6e6bd595b4629f1db7.jpg",
          "id": "434898792",
          "name": "Beverages",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 14,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499829349",
              "name": "Beverages",
              "sortIndex": 429
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499829470",
              "name": "Coffee & Tea",
              "sortIndex": 431
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "592507290",
              "name": "Juice Canned / Boxed / Bottled",
              "sortIndex": 516
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/41e2803124e5b86e9cfd3200a4ad38f4.jpg",
          "id": "434898827",
          "name": "Frozen Foods",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 43,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822522",
              "name": "Appetizers",
              "sortIndex": 347
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822733",
              "name": "Pasta",
              "sortIndex": 351
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822770",
              "name": "Entrees",
              "sortIndex": 353
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822815",
              "name": "Vegetables",
              "sortIndex": 355
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 19,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823302",
              "name": "Frozen Foods",
              "sortIndex": 371
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823521",
              "name": "French Fries",
              "sortIndex": 377
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "565824605",
              "name": "Sauces",
              "sortIndex": 496
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b8fb371eb766c94d4c9e4c5c22598431.jpg",
          "id": "434899997",
          "name": "Oil & Shortening",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 3,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822918",
              "name": "Lard Cubes",
              "sortIndex": 359
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823623",
              "name": "Oils",
              "sortIndex": 378
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/225d00acedceec92e3ddddc5fdd54861.jpg",
          "id": "434900065",
          "name": "Non-food/disposables",
          "sortIndex": "18",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 15,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824450",
              "name": "Bag - Paper To-go",
              "sortIndex": 398
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824539",
              "name": "Non-food/disposables",
              "sortIndex": 401
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824627",
              "name": "Food Pails",
              "sortIndex": 405
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824665",
              "name": "Foil / Film / Rolls / Wraps",
              "sortIndex": 407
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499825266",
              "name": "Container - Foam",
              "sortIndex": 410
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499829447",
              "name": "Pizza Boxes",
              "sortIndex": 430
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544744476",
              "name": "Trash Bags",
              "sortIndex": 470
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544744575",
              "name": "Food Storage - Deli",
              "sortIndex": 474
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6859b26f9fbf80b572e4f669f8bd1d3e.jpg",
          "id": "434900092",
          "name": "Fresh Produce",
          "sortIndex": "19",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 41,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 29,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823283",
              "name": "Vegetables",
              "sortIndex": 370
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824827",
              "name": "Fresh Produce",
              "sortIndex": 408
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499824901",
              "name": "Fruit",
              "sortIndex": 410
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "544744412",
              "name": "Fresh Herbs",
              "sortIndex": 469
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4681cab74e147859c3ae59fe214f87bb.jpg",
          "id": "436150323",
          "name": "Bakery & Desserts",
          "sortIndex": "20",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 11,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499822748",
              "name": "Cakes",
              "sortIndex": 352
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499823253",
              "name": "Pies",
              "sortIndex": 369
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499830030",
              "name": "Pastries",
              "sortIndex": 438
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499832413",
              "name": "Dough",
              "sortIndex": 443
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "592506603",
              "name": "Pizza Crusts & Dough",
              "sortIndex": 514
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
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1b3ec5238615a0aa8aa638841af65daa.jpg",
          "id": "519139096",
          "name": "Game",
          "sortIndex": "25",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 13,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "519139097",
              "name": "Duck/quail",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "519139130",
              "name": "Goat",
              "sortIndex": 2
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
