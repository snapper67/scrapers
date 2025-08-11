
import json
from scrapers.cut.dry import CutScraper


class WagnerScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/wagner/'

	# Values to change
	BASE_URL = "https://wagner.cutanddry.com/catalog/wagner?verifiedVendorId=152858455&categoryId=1&page=1"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "222088640",
          "baseName": "beverage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9411282b3ceb7e329b85f7d40d25a25f.jpg",
          "name": "Beverage",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 777,
        "subcategories": [
          {
            "subcategory": {
              "id": "222088738",
              "name": "Juice",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 200,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222091871",
              "name": "Coffee",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 117,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222088790",
              "name": "Soft Drinks - Bottle/can",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 70,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222088648",
              "name": "Cocktail Mix- Passion Bay",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 32,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222088841",
              "name": "Tea",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 77,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222088758",
              "name": "Bib- Pvt Label Ftn Drinks",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 59,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222092738",
              "name": "Coffee Private Label",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 46,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222088818",
              "name": "Sports Drinks",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 23,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222088949",
              "name": "Bib - Fountain Drinks",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 14,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222088641",
              "name": "Cocktail Mixers",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 22,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222088846",
              "name": "Energy Drinks",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 15,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222106650",
              "name": "Bib - Frozen Drinks",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 19,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222088765",
              "name": "Water",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 38,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222088799",
              "name": "Bib-nat'l Brand Ftn Drink",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 33,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222091994",
              "name": "Cocoa",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 9,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "274457600",
              "name": "Tea Private Label",
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
          "id": "194836942",
          "baseName": "poultry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/deeeaa50d85b1f6393073ccdcc73e4c3.jpg",
          "name": "Poultry",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 173,
        "subcategories": [
          {
            "subcategory": {
              "id": "194836943",
              "name": "Chicken",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 133,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194837229",
              "name": "Duck",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 18,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194836971",
              "name": "Turkey",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 22,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "194831525",
          "baseName": "meats",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d0c9f08f55ad653236292c8d47881148.jpg",
          "name": "Meats",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 741,
        "subcategories": [
          {
            "subcategory": {
              "id": "194836999",
              "name": "Veal",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 28,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831527",
              "name": "Beef",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 466,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194836439",
              "name": "Pork",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 195,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194837031",
              "name": "Lamb",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 30,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194836802",
              "name": "Wild Game",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 22,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "194831491",
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/356402db3f0869502d5febd7d469a22c.jpg",
          "name": "Seafood",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 391,
        "subcategories": [
          {
            "subcategory": {
              "id": "194831492",
              "name": "Shellfish",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 196,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194832278",
              "name": "Finfish",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 176,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194836799",
              "name": "Specialty Seafood",
              "sortIndex": 0,
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
          "id": "194830804",
          "baseName": "produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f77c84d22f7ea2809320482302157e42.jpg",
          "name": "Produce",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 719,
        "subcategories": [
          {
            "subcategory": {
              "id": "194835126",
              "name": "Vegetables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 522,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830805",
              "name": "Fruits",
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
          "id": "194830817",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/500a08a6b110444940005444bff383f7.jpg",
          "name": "Dairy",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 403,
        "subcategories": [
          {
            "subcategory": {
              "id": "194831038",
              "name": "Dairy Frozen",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 66,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194836338",
              "name": "Cheese",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 196,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830818",
              "name": "Cultured Dairy",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 36,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194836313",
              "name": "Butter/margarine",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 24,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194836290",
              "name": "Eggs",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 30,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830821",
              "name": "Milk",
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
          "id": "168756161",
          "baseName": "frozen fruits & vegetable",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6ea3840f0e39f2ba54283b3bd336a0c3.jpg",
          "name": "Frozen Fruits & Vegetable",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 204,
        "subcategories": [
          {
            "subcategory": {
              "id": "194831662",
              "name": "Vegetables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 169,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194837246",
              "name": "Fruits",
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
          "id": "194831066",
          "baseName": "frozen and refr goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/aa90c0dd2a3466aeaade51858481c694.jpg",
          "name": "Frozen And Refr Goods",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1523,
        "subcategories": [
          {
            "subcategory": {
              "id": "194831547",
              "name": "Dressings",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 30,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831163",
              "name": "Appetizers Frz Or Refr",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 185,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831349",
              "name": "Pork & Processed Meats",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 133,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831067",
              "name": "Bakery Frozen",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 783,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194838322",
              "name": "Bib - Frozen Drinks",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 22,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194836461",
              "name": "Chicken Further Processed",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 43,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194832310",
              "name": "Pasta Frozen",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 63,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194836454",
              "name": "Turkey Further Processed",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 28,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831495",
              "name": "Sauces Bases & Gravies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 70,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831281",
              "name": "Pizza: Crust/dough",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 59,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831345",
              "name": "Entrees Frz Or Refr",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 79,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831481",
              "name": "Soups & Chili Refr",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 27,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194836387",
              "name": "Unassigned",
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
          "id": "194830808",
          "baseName": "dry-canned fr & veg",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a0abb8b821a90d4bc236dcb1a0f4e024.jpg",
          "name": "Dry-canned Fr & Veg",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 292,
        "subcategories": [
          {
            "subcategory": {
              "id": "194831422",
              "name": "Vegetables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 167,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830809",
              "name": "Fruits",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 125,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "194834632",
          "baseName": "shortenings and oils",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/da7860262fb728ade7f7696083a3710a.jpg",
          "name": "Shortenings And Oils",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 41,
        "subcategories": [
          {
            "subcategory": {
              "id": "194834633",
              "name": "Olive Oil",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194834731",
              "name": "Pan Coatings & Sprays",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194834666",
              "name": "Frying Oil",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194834653",
              "name": "Other: Oil/shortenings",
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
          "id": "168755495",
          "baseName": "dry groc, season & spices",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/0cf45464cb015e15e5d3a4e47b299c26.jpg",
          "name": "Dry Groc, Season & Spices",
          "sortIndex": "19",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1842,
        "subcategories": [
          {
            "subcategory": {
              "id": "194831415",
              "name": "Condiments",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 152,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831207",
              "name": "Spices & Seasoning",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 324,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831104",
              "name": "Snacks Shelf Stable",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 303,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831081",
              "name": "Sauces Bases & Gravies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 312,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831072",
              "name": "Bakery Mixes/ingredients",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 435,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "168755713",
              "name": "Meats & Soup Shelf Stable",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 59,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194832391",
              "name": "Cereal",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 51,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831545",
              "name": "Dressings",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 67,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831488",
              "name": "Pasta Shelf Stable",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 77,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831688",
              "name": "Vinegar & Cooking Wine",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 28,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194834427",
              "name": "Rice",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 21,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194831176",
              "name": "Unassigned",
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
          "id": "194828602",
          "baseName": "disposables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1b47ff15b8270d5f1309b5e7be02c4a8.jpg",
          "name": "Disposables",
          "sortIndex": "20",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1760,
        "subcategories": [
          {
            "subcategory": {
              "id": "194828890",
              "name": "Drinkware",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 323,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194828731",
              "name": "Other: Disposables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 88,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194828615",
              "name": "Containers & Lids",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 544,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830656",
              "name": "Napkin Towels & Tissue",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 124,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194828692",
              "name": "Can Liners & Storage Bags",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 166,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830933",
              "name": "Menu Covers",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 44,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194828603",
              "name": "Film Foil & Wraps",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 97,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830751",
              "name": "Placemats & Coasters",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 18,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830848",
              "name": "Gloves",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 29,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194828892",
              "name": "Dinnerware",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 116,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194828688",
              "name": "Table Covers",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 17,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194828899",
              "name": "Trays & Pans",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 81,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830513",
              "name": "Cutlery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 90,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830602",
              "name": "Toothpick/marker/skewer",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 22,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "483685641",
              "name": "Napkins",
              "sortIndex": 1,
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
          "id": "222086318",
          "baseName": "supplies and equipment",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b43d5bf64cb904406bffeff356ae1daf.jpg",
          "name": "Supplies And Equipment",
          "sortIndex": "22",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 3752,
        "subcategories": [
          {
            "subcategory": {
              "id": "222086319",
              "name": "Smallwares Equipment",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3314,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222087660",
              "name": "Miscellaneous Equipment",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 154,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "404870551",
              "name": "Salad Cups",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222088602",
              "name": "Beverage Equipment",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 121,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222090087",
              "name": "Food Warmers & Holding Eq",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 53,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "222088987",
              "name": "Cooking Equipment",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 19,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "407374746",
              "name": "Filters",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "407374741",
              "name": "Refrigeration Equipment",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "407374442",
              "name": "Dish Washing Equipment",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "407374504",
              "name": "Blenders",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "407374447",
              "name": "Cutlery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "407374440",
              "name": "Cleaners",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "596875439",
              "name": "Db Equipment",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 72,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "194829492",
          "baseName": "janitorial and chemical",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e4f1c868a73fb925e87cc48c2aa11d41.jpg",
          "name": "Janitorial And Chemical",
          "sortIndex": "24",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 379,
        "subcategories": [
          {
            "subcategory": {
              "id": "194829855",
              "name": "Cleaners",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 135,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194829844",
              "name": "Janitorial Equipment",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 136,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830082",
              "name": "Insecticide",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194829925",
              "name": "Odor Control",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830017",
              "name": "Hygiene/dispenser",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 56,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194829493",
              "name": "Warewash",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 14,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194835104",
              "name": "Dish And Laundry",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194830304",
              "name": "Unassigned",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "194829941",
              "name": "Laundry Chemicals",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'Wagner'
	VENDOR_URL_NAME = 'wagner'
	VERIFIED_VENDOR_ID = 152858455

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY

