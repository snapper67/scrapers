
import json
from scrapers.cut.dry import CutScraper


class FoodAndPaperScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/food_paper/'

	# Values to change
	BASE_URL = "https://foodandpaper.cutanddry.com/catalog/foodandpaper?verifiedVendorId=1861972&categoryId=1&page=1"
	SUB_DOMAIN = "https://foodandpaper.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "543103482",
          "baseName": "beef, pork, lamb",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/61d049267e885dcbe285ca848a321979.jpg",
          "name": "Beef, Pork, Lamb",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 238,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103483",
              "name": "Beef (F)",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 86,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103484",
              "name": "Beef Wght",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 55,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103485",
              "name": "Game (F)",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103486",
              "name": "Pork (F)",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 69,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103487",
              "name": "Pork Wght",
              "sortIndex": 5,
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
          "id": "543103488",
          "baseName": "poultry, chicken, turkey",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4e4a75e8f003bfe7e7ce4c9e31f6de0b.jpg",
          "name": "Poultry, Chicken, Turkey",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 146,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103489",
              "name": "Poultry (F)",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 84,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103490",
              "name": "Poultry (R)",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 62,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "543103491",
          "baseName": "seafood, shrimp",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/219883ee5c54dbbe1dac6cac09d007a7.jpg",
          "name": "Seafood, Shrimp",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 71,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103492",
              "name": "Seafood (F)",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 71,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "543103493",
          "baseName": "produce, prepared salads",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/0962601e966fccd114954ea05945cf93.jpg",
          "name": "Produce, Prepared Salads",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 213,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103494",
              "name": "Frt/Veg (F)",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 47,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103495",
              "name": "Prep Salad",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 19,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103496",
              "name": "Produce",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 147,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "543103497",
          "baseName": "dairy, eggs, refrigerated",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9dca3f4049a91e7e0bd3c2a6032b15b8.jpg",
          "name": "Dairy, Eggs, Refrigerated",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 139,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103498",
              "name": "Asstd Refrg",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103499",
              "name": "Cheeses",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 85,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103500",
              "name": "Dairy Liq",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 44,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103501",
              "name": "Eggs",
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
          "id": "543103502",
          "baseName": "dry goods, packaging",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/31748d944e7832c8535e6dbe3f3e211b.jpg",
          "name": "Dry Goods, Packaging",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1368,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103503",
              "name": "Alum Foil",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 33,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103504",
              "name": "Alum Pans",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 88,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103506",
              "name": "Bag Glasine",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103507",
              "name": "Bag Paper",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 77,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103508",
              "name": "Bag Pizza",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103509",
              "name": "Bag Poly",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 37,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103510",
              "name": "Bag S.P.",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103511",
              "name": "Bakery Pads",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103512",
              "name": "Cake Boxes",
              "sortIndex": 9,
              "__typename": "ProductSubcategory"
            },
            "productCount": 24,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103513",
              "name": "Can Liners",
              "sortIndex": 10,
              "__typename": "ProductSubcategory"
            },
            "productCount": 38,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103515",
              "name": "Cont Foam",
              "sortIndex": 11,
              "__typename": "ProductSubcategory"
            },
            "productCount": 76,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103518",
              "name": "Cont Lids",
              "sortIndex": 12,
              "__typename": "ProductSubcategory"
            },
            "productCount": 45,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103519",
              "name": "Cont Paper",
              "sortIndex": 13,
              "__typename": "ProductSubcategory"
            },
            "productCount": 63,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103520",
              "name": "Cont Plstc",
              "sortIndex": 14,
              "__typename": "ProductSubcategory"
            },
            "productCount": 198,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103521",
              "name": "Cont S.P.",
              "sortIndex": 15,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103522",
              "name": "Cup Foam",
              "sortIndex": 16,
              "__typename": "ProductSubcategory"
            },
            "productCount": 21,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103523",
              "name": "Cup Lids",
              "sortIndex": 17,
              "__typename": "ProductSubcategory"
            },
            "productCount": 46,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103524",
              "name": "Cup Paper",
              "sortIndex": 18,
              "__typename": "ProductSubcategory"
            },
            "productCount": 18,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103525",
              "name": "Cup Plastic",
              "sortIndex": 19,
              "__typename": "ProductSubcategory"
            },
            "productCount": 65,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103526",
              "name": "Cup S.P.",
              "sortIndex": 20,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103527",
              "name": "Cutlery",
              "sortIndex": 21,
              "__typename": "ProductSubcategory"
            },
            "productCount": 54,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103528",
              "name": "Doilies",
              "sortIndex": 22,
              "__typename": "ProductSubcategory"
            },
            "productCount": 9,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103529",
              "name": "Film",
              "sortIndex": 23,
              "__typename": "ProductSubcategory"
            },
            "productCount": 15,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103530",
              "name": "Filters Etc",
              "sortIndex": 24,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103531",
              "name": "Foam Hinged",
              "sortIndex": 25,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103532",
              "name": "Folder S.P.",
              "sortIndex": 26,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103533",
              "name": "Food Trays",
              "sortIndex": 27,
              "__typename": "ProductSubcategory"
            },
            "productCount": 26,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103534",
              "name": "Guestchecks",
              "sortIndex": 28,
              "__typename": "ProductSubcategory"
            },
            "productCount": 24,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103535",
              "name": "Hats/Aprons",
              "sortIndex": 29,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103536",
              "name": "Nap Paper",
              "sortIndex": 30,
              "__typename": "ProductSubcategory"
            },
            "productCount": 34,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103538",
              "name": "Pan Lid Alm",
              "sortIndex": 32,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103539",
              "name": "Paper Wrap",
              "sortIndex": 33,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103540",
              "name": "Party Sup",
              "sortIndex": 34,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103541",
              "name": "Pizza Box",
              "sortIndex": 35,
              "__typename": "ProductSubcategory"
            },
            "productCount": 19,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103542",
              "name": "Pizza Circl",
              "sortIndex": 36,
              "__typename": "ProductSubcategory"
            },
            "productCount": 14,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103543",
              "name": "Pizza Supp",
              "sortIndex": 37,
              "__typename": "ProductSubcategory"
            },
            "productCount": 24,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103544",
              "name": "Plate Foam",
              "sortIndex": 38,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103545",
              "name": "Plate Paper",
              "sortIndex": 39,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103546",
              "name": "Plate Plstc",
              "sortIndex": 40,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103547",
              "name": "Plate S.P.",
              "sortIndex": 41,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103548",
              "name": "Rgstr Tape",
              "sortIndex": 42,
              "__typename": "ProductSubcategory"
            },
            "productCount": 26,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103549",
              "name": "Souffle Cup",
              "sortIndex": 43,
              "__typename": "ProductSubcategory"
            },
            "productCount": 26,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103550",
              "name": "Souffle Lid",
              "sortIndex": 44,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103551",
              "name": "Straws",
              "sortIndex": 45,
              "__typename": "ProductSubcategory"
            },
            "productCount": 33,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103552",
              "name": "Tablecovers",
              "sortIndex": 46,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103553",
              "name": "Tissue Bath",
              "sortIndex": 47,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103554",
              "name": "Towel Paper",
              "sortIndex": 48,
              "__typename": "ProductSubcategory"
            },
            "productCount": 19,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103555",
              "name": "Towel/Wipe",
              "sortIndex": 49,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103556",
              "name": "Wax Paper",
              "sortIndex": 50,
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
          "id": "543103558",
          "baseName": "grocery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/83fd7341dd4c11ed9c932b5ad2eab556.jpg",
          "name": "Grocery",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1022,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103559",
              "name": "Asst Cans",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103560",
              "name": "Bbq Sauce",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 37,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103561",
              "name": "Beans Dry",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103562",
              "name": "Cereals",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 19,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103563",
              "name": "Cherries",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103564",
              "name": "Dressings",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 103,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103565",
              "name": "Gravy Mix",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103566",
              "name": "Hot Sauce",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 28,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103567",
              "name": "Ketchup",
              "sortIndex": 9,
              "__typename": "ProductSubcategory"
            },
            "productCount": 20,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103568",
              "name": "Mustard",
              "sortIndex": 10,
              "__typename": "ProductSubcategory"
            },
            "productCount": 14,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103569",
              "name": "Oil/Shrtng",
              "sortIndex": 11,
              "__typename": "ProductSubcategory"
            },
            "productCount": 69,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103570",
              "name": "Olives",
              "sortIndex": 12,
              "__typename": "ProductSubcategory"
            },
            "productCount": 21,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103571",
              "name": "Pan Spray",
              "sortIndex": 13,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103572",
              "name": "Pasta Dry",
              "sortIndex": 14,
              "__typename": "ProductSubcategory"
            },
            "productCount": 61,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103573",
              "name": "Pc Dress",
              "sortIndex": 15,
              "__typename": "ProductSubcategory"
            },
            "productCount": 13,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103574",
              "name": "Pc Sauces",
              "sortIndex": 16,
              "__typename": "ProductSubcategory"
            },
            "productCount": 30,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103575",
              "name": "Peppers",
              "sortIndex": 17,
              "__typename": "ProductSubcategory"
            },
            "productCount": 38,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103577",
              "name": "Pickles",
              "sortIndex": 18,
              "__typename": "ProductSubcategory"
            },
            "productCount": 17,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103578",
              "name": "Pudding",
              "sortIndex": 19,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103579",
              "name": "Relish",
              "sortIndex": 20,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103580",
              "name": "Rice Etc",
              "sortIndex": 21,
              "__typename": "ProductSubcategory"
            },
            "productCount": 14,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103581",
              "name": "Sauce Asstd",
              "sortIndex": 22,
              "__typename": "ProductSubcategory"
            },
            "productCount": 110,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103582",
              "name": "Sauce S.P.",
              "sortIndex": 23,
              "__typename": "ProductSubcategory"
            },
            "productCount": 23,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103585",
              "name": "Snacks Etc",
              "sortIndex": 24,
              "__typename": "ProductSubcategory"
            },
            "productCount": 118,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103586",
              "name": "Soup Base",
              "sortIndex": 25,
              "__typename": "ProductSubcategory"
            },
            "productCount": 24,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103587",
              "name": "Soup Canned",
              "sortIndex": 26,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103588",
              "name": "Spreads",
              "sortIndex": 27,
              "__typename": "ProductSubcategory"
            },
            "productCount": 21,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103589",
              "name": "Tomato Prod",
              "sortIndex": 28,
              "__typename": "ProductSubcategory"
            },
            "productCount": 61,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103590",
              "name": "Veg Cans",
              "sortIndex": 29,
              "__typename": "ProductSubcategory"
            },
            "productCount": 96,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103591",
              "name": "Vinegar",
              "sortIndex": 30,
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
          "id": "543103592",
          "baseName": "appetizers, fries",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5d0195791f59d2e7047e204747747010.jpg",
          "name": "Appetizers, Fries",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 242,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103593",
              "name": "Appetizers",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 95,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103594",
              "name": "Fr Fries",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 53,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103595",
              "name": "Meat Subs",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103596",
              "name": "Misc Food",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 19,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103597",
              "name": "Pasta (F)",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 30,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103598",
              "name": "Soup Frozen",
              "sortIndex": 6,
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
          "id": "543103599",
          "baseName": "frozen desserts",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5d80485194ba9b9278b7d7102f1f0591.jpg",
          "name": "Frozen Desserts",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 110,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103600",
              "name": "Dessert (F)",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 65,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103601",
              "name": "Ic Toppings",
              "sortIndex": 2,
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
          "id": "543103602",
          "baseName": "kitchen supplies, equipment",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/7216732d343e625a5670db68d55c57a4.jpg",
          "name": "Kitchen Supplies, Equipment",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 391,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103603",
              "name": "Bar Supply",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103604",
              "name": "China Etc",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103605",
              "name": "Dispensers",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 41,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103606",
              "name": "Glassware",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103607",
              "name": "Kitchen Sup",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 198,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103608",
              "name": "Serve Supp",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 78,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103609",
              "name": "Stm Tbl Etc",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 29,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103610",
              "name": "Storagecont",
              "sortIndex": 8,
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
          "id": "543103612",
          "baseName": "operational supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/872da0ce75f6a4bc89949a9d0f2808b0.jpg",
          "name": "Operational Supplies",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 4,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103613",
              "name": "Charcoal",
              "sortIndex": 1,
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
          "id": "543103614",
          "baseName": "janitorial",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/027085e2e34eb8091abe0e833f389e4f.jpg",
          "name": "Janitorial",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 240,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103615",
              "name": "Clean Aero",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 20,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103616",
              "name": "Clean Chem",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 148,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103617",
              "name": "Clean Equip",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103618",
              "name": "Clean Wipes",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103620",
              "name": "Gloves",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 44,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103621",
              "name": "Mops Etc",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 14,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103622",
              "name": "Trash Cans",
              "sortIndex": 7,
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
          "id": "543103623",
          "baseName": "beverage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fdca2f1fa8872cc478db4172fd7c5fcf.jpg",
          "name": "Beverage",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 368,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103624",
              "name": "Bar Mix",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 14,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103625",
              "name": "Bev Mix",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103626",
              "name": "Beverages",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 67,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103627",
              "name": "Coffee",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103628",
              "name": "Dairy Dry",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103629",
              "name": "Extracts",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 15,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103630",
              "name": "Fruit Cans",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 45,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103631",
              "name": "Juices",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 32,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103632",
              "name": "Pop/Soda",
              "sortIndex": 9,
              "__typename": "ProductSubcategory"
            },
            "productCount": 49,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103633",
              "name": "Syrup&Bases",
              "sortIndex": 10,
              "__typename": "ProductSubcategory"
            },
            "productCount": 110,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103634",
              "name": "Tea",
              "sortIndex": 11,
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
          "id": "543103635",
          "baseName": "spices, seasonings",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fcc883dde64a1264647ae7e4c33b8326.jpg",
          "name": "Spices, Seasonings",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 329,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103636",
              "name": "Salt",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 22,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103637",
              "name": "Spice S.P.",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 12,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103638",
              "name": "Spice/Seasn",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 263,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103639",
              "name": "Sugars",
              "sortIndex": 4,
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
          "id": "543103640",
          "baseName": "bakery, nuts, seeds",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/13ff723148ea5b890a644cccc4394efa.jpg",
          "name": "Bakery, Nuts, Seeds",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 200,
        "subcategories": [
          {
            "subcategory": {
              "id": "543103641",
              "name": "Baking Prod",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 47,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103642",
              "name": "Bread (F)",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103643",
              "name": "Bread/Mix",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 33,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103644",
              "name": "Breadings",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 28,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103645",
              "name": "Buns (F)",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103646",
              "name": "Cake Mix",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103647",
              "name": "Flour",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 31,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103648",
              "name": "Nuts/Seeds",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 21,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103649",
              "name": "Tortillas",
              "sortIndex": 9,
              "__typename": "ProductSubcategory"
            },
            "productCount": 12,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "543103651",
              "name": "Yeast",
              "sortIndex": 10,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'Food and Paper'
	VENDOR_URL_NAME = 'foodandpaper'
	VERIFIED_VENDOR_ID = 1861972

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY
		self.options['base_url'] = self.BASE_URL
