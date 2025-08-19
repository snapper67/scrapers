
import json
from scrapers.cut.dry import CutScraper


class SardilliScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/sardilli'

	# Values to change
	BASE_URL = "https://app.cutanddry.com/catalog/sardilli?verifiedVendorId=369151799&categoryId=1&categoryName=All+Items&page=1"
	SUB_DOMAIN = "https://app.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "476813170",
          "baseName": "vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/38851c46a95dec40e98e46b684cc5fb3.jpg",
          "name": "Vegetables",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 416,
        "subcategories": [
          {
            "subcategory": {
              "id": "476813172",
              "name": "Tomato",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 26,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813177",
              "name": "Anise",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813187",
              "name": "Artichoke",
              "sortIndex": 8,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813188",
              "name": "Greens",
              "sortIndex": 9,
              "__typename": "ProductSubcategory"
            },
            "productCount": 15,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813189",
              "name": "Asparagus",
              "sortIndex": 10,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813194",
              "name": "Beans",
              "sortIndex": 15,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813196",
              "name": "Beets",
              "sortIndex": 16,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813197",
              "name": "Smartcuts",
              "sortIndex": 17,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813200",
              "name": "Bok Choy",
              "sortIndex": 19,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813201",
              "name": "Broccoli",
              "sortIndex": 20,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813204",
              "name": "Brussel Sprt",
              "sortIndex": 22,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813207",
              "name": "Cabbage",
              "sortIndex": 24,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813209",
              "name": "Carrots",
              "sortIndex": 26,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813211",
              "name": "Cauliflower",
              "sortIndex": 28,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813213",
              "name": "Celery",
              "sortIndex": 30,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813253",
              "name": "Peppers",
              "sortIndex": 35,
              "__typename": "ProductSubcategory"
            },
            "productCount": 32,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813255",
              "name": "Corn",
              "sortIndex": 37,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813259",
              "name": "Cucumbers",
              "sortIndex": 40,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813264",
              "name": "Eggplant",
              "sortIndex": 44,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813265",
              "name": "Endive",
              "sortIndex": 45,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813266",
              "name": "Vegetables",
              "sortIndex": 46,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813269",
              "name": "Flowers",
              "sortIndex": 49,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813272",
              "name": "Frisse",
              "sortIndex": 51,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813275",
              "name": "Root",
              "sortIndex": 53,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813274",
              "name": "Garlic",
              "sortIndex": 53,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813281",
              "name": "Herbs",
              "sortIndex": 58,
              "__typename": "ProductSubcategory"
            },
            "productCount": 28,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813285",
              "name": "Jicama",
              "sortIndex": 61,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813292",
              "name": "Leeks",
              "sortIndex": 65,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813291",
              "name": "Leaves",
              "sortIndex": 65,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813296",
              "name": "Lettuce",
              "sortIndex": 69,
              "__typename": "ProductSubcategory"
            },
            "productCount": 32,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813297",
              "name": "Micro",
              "sortIndex": 70,
              "__typename": "ProductSubcategory"
            },
            "productCount": 23,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813307",
              "name": "Mushrooms",
              "sortIndex": 78,
              "__typename": "ProductSubcategory"
            },
            "productCount": 18,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813311",
              "name": "Onions",
              "sortIndex": 81,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813316",
              "name": "Parsnips",
              "sortIndex": 85,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813317",
              "name": "Parsley",
              "sortIndex": 86,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813320",
              "name": "Peas",
              "sortIndex": 89,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813325",
              "name": "Pickles",
              "sortIndex": 94,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813328",
              "name": "Potatoes",
              "sortIndex": 97,
              "__typename": "ProductSubcategory"
            },
            "productCount": 39,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813330",
              "name": "Radish",
              "sortIndex": 99,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813332",
              "name": "Radicchio",
              "sortIndex": 101,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813334",
              "name": "Rhubarb",
              "sortIndex": 103,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813339",
              "name": "Scallions",
              "sortIndex": 107,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813342",
              "name": "Shallots",
              "sortIndex": 109,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813343",
              "name": "Cress",
              "sortIndex": 110,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813344",
              "name": "Spinach",
              "sortIndex": 111,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813345",
              "name": "Sprouts",
              "sortIndex": 112,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813346",
              "name": "Squash",
              "sortIndex": 113,
              "__typename": "ProductSubcategory"
            },
            "productCount": 22,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813348",
              "name": "Tofu",
              "sortIndex": 115,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813350",
              "name": "Tomatillo",
              "sortIndex": 117,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813351",
              "name": "Turnips",
              "sortIndex": 118,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813353",
              "name": "Watercress",
              "sortIndex": 120,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "509740818",
              "name": "Okra",
              "sortIndex": 132,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "530496557",
              "name": "Palms",
              "sortIndex": 135,
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
          "id": "476813174",
          "baseName": "grocery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a4a171f120b0ced167b153167fceeae7.jpg",
          "name": "Grocery",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 195,
        "subcategories": [
          {
            "subcategory": {
              "id": "476813175",
              "name": "Spice",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 62,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813176",
              "name": "Grocery",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 20,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813180",
              "name": "Dried Fruit",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 20,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813191",
              "name": "Salads",
              "sortIndex": 12,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813193",
              "name": "Dried Beans",
              "sortIndex": 14,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813199",
              "name": "Dried Grains",
              "sortIndex": 18,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813252",
              "name": "Dried Chili",
              "sortIndex": 34,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813257",
              "name": "Couscous",
              "sortIndex": 38,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813260",
              "name": "Dates",
              "sortIndex": 41,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813270",
              "name": "Flour",
              "sortIndex": 50,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813273",
              "name": "Garlic",
              "sortIndex": 52,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813276",
              "name": "Ginger",
              "sortIndex": 54,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813277",
              "name": "Rice",
              "sortIndex": 55,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813282",
              "name": "Honey",
              "sortIndex": 59,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813284",
              "name": "Horseradish",
              "sortIndex": 60,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813287",
              "name": "Cabbage",
              "sortIndex": 62,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813290",
              "name": "Leaves",
              "sortIndex": 64,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813295",
              "name": "Lentils",
              "sortIndex": 68,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813303",
              "name": "Meat",
              "sortIndex": 75,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813308",
              "name": "Mushrooms",
              "sortIndex": 79,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813310",
              "name": "Nuts",
              "sortIndex": 80,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813318",
              "name": "Paste",
              "sortIndex": 87,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813322",
              "name": "Dried Veg",
              "sortIndex": 91,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813323",
              "name": "Peppers",
              "sortIndex": 92,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813333",
              "name": "Raisins",
              "sortIndex": 102,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813341",
              "name": "Seeds",
              "sortIndex": 108,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813347",
              "name": "Syrup",
              "sortIndex": 114,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813349",
              "name": "Tomato",
              "sortIndex": 116,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813352",
              "name": "Vinegar",
              "sortIndex": 119,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813354",
              "name": "Yeast",
              "sortIndex": 121,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "497911035",
              "name": "Olives",
              "sortIndex": 128,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "497911046",
              "name": "Chili",
              "sortIndex": 129,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "505811774",
              "name": "Oil",
              "sortIndex": 130,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "541054079",
              "name": "Beans",
              "sortIndex": 136,
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
          "id": "476813178",
          "baseName": "beverage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/73b93dbd48c361cc16e0857df8c9ff89.jpg",
          "name": "Beverage",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 28,
        "subcategories": [
          {
            "subcategory": {
              "id": "476813179",
              "name": "Juice",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 26,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813306",
              "name": "Milk",
              "sortIndex": 78,
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
          "id": "476813181",
          "baseName": "fruit",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/7e825188724ec101f14d2de6d9a0320e.jpg",
          "name": "Fruit",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 131,
        "subcategories": [
          {
            "subcategory": {
              "id": "476813182",
              "name": "Apples",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 34,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813190",
              "name": "Avocado",
              "sortIndex": 11,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813192",
              "name": "Bananas",
              "sortIndex": 13,
              "__typename": "ProductSubcategory"
            },
            "productCount": 12,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813198",
              "name": "Berries",
              "sortIndex": 17,
              "__typename": "ProductSubcategory"
            },
            "productCount": 10,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813261",
              "name": "Dragon",
              "sortIndex": 42,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813268",
              "name": "Figs",
              "sortIndex": 48,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813278",
              "name": "Grapes",
              "sortIndex": 56,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813279",
              "name": "Grapefruit",
              "sortIndex": 57,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813288",
              "name": "Kiwifruit",
              "sortIndex": 62,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813289",
              "name": "Kumquats",
              "sortIndex": 63,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813293",
              "name": "Lemons",
              "sortIndex": 66,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813300",
              "name": "Limes",
              "sortIndex": 72,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813301",
              "name": "Mangoes",
              "sortIndex": 73,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813304",
              "name": "Melons",
              "sortIndex": 76,
              "__typename": "ProductSubcategory"
            },
            "productCount": 9,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813313",
              "name": "Oranges",
              "sortIndex": 83,
              "__typename": "ProductSubcategory"
            },
            "productCount": 8,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813315",
              "name": "Papaya",
              "sortIndex": 84,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813319",
              "name": "Pears",
              "sortIndex": 88,
              "__typename": "ProductSubcategory"
            },
            "productCount": 4,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813321",
              "name": "Peaches",
              "sortIndex": 90,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813326",
              "name": "Pineapple",
              "sortIndex": 95,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813327",
              "name": "Pomegranate",
              "sortIndex": 96,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813335",
              "name": "Root",
              "sortIndex": 104,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "480603981",
              "name": "Guava",
              "sortIndex": 123,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "481474948",
              "name": "Starfruit",
              "sortIndex": 124,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "481627162",
              "name": "Coconuts",
              "sortIndex": 125,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "509739419",
              "name": "Cherries",
              "sortIndex": 131,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "510348737",
              "name": "Apricot",
              "sortIndex": 133,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "510349617",
              "name": "Nectarine",
              "sortIndex": 134,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "575399732",
              "name": "Plums",
              "sortIndex": 137,
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
          "id": "476813185",
          "baseName": "precut",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1bea937d8354460699904a504f944ef7.jpg",
          "name": "Precut",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 238,
        "subcategories": [
          {
            "subcategory": {
              "id": "476813186",
              "name": "Smartcuts",
              "sortIndex": 7,
              "__typename": "ProductSubcategory"
            },
            "productCount": 195,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813202",
              "name": "Broccoli",
              "sortIndex": 21,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813208",
              "name": "Cabbage",
              "sortIndex": 25,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813210",
              "name": "Carrots",
              "sortIndex": 27,
              "__typename": "ProductSubcategory"
            },
            "productCount": 7,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813212",
              "name": "Cauliflower",
              "sortIndex": 29,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813214",
              "name": "Celery",
              "sortIndex": 31,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813298",
              "name": "Lettuce",
              "sortIndex": 71,
              "__typename": "ProductSubcategory"
            },
            "productCount": 6,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813312",
              "name": "Onions",
              "sortIndex": 82,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813329",
              "name": "Potatoes",
              "sortIndex": 98,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813337",
              "name": "Salads",
              "sortIndex": 105,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "497910951",
              "name": "Grapefruit",
              "sortIndex": 128,
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
          "id": "476813205",
          "baseName": "butter",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/883460dec082b592bb0592a78184f10f.jpg",
          "name": "Butter",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 6,
        "subcategories": [
          {
            "subcategory": {
              "id": "476813206",
              "name": "Butter",
              "sortIndex": 23,
              "__typename": "ProductSubcategory"
            },
            "productCount": 5,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813302",
              "name": "Margarine",
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
          "id": "476813215",
          "baseName": "cheese",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a1700adc4ec0d733c387416bbca2df83.jpg",
          "name": "Cheese",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 96,
        "subcategories": [
          {
            "subcategory": {
              "id": "476813216",
              "name": "Cheese",
              "sortIndex": 32,
              "__typename": "ProductSubcategory"
            },
            "productCount": 96,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "476813242",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a5bf61067d45473b409bf61a05c14460.jpg",
          "name": "Dairy",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 53,
        "subcategories": [
          {
            "subcategory": {
              "id": "476813243",
              "name": "Cheese",
              "sortIndex": 33,
              "__typename": "ProductSubcategory"
            },
            "productCount": 2,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813258",
              "name": "Cream",
              "sortIndex": 39,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813305",
              "name": "Milk",
              "sortIndex": 77,
              "__typename": "ProductSubcategory"
            },
            "productCount": 25,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "476813355",
              "name": "Yogurt",
              "sortIndex": 122,
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
          "id": "476813262",
          "baseName": "eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/09a0e9b1b7339b3661835526162adb70.jpg",
          "name": "Eggs",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 3,
        "subcategories": [
          {
            "subcategory": {
              "id": "476813263",
              "name": "Eggs",
              "sortIndex": 43,
              "__typename": "ProductSubcategory"
            },
            "productCount": 3,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'Sardilli'
	VENDOR_URL_NAME = 'sardilli'
	VERIFIED_VENDOR_ID = 369151799

	DEFAULT_OPTIONS = {
		'get_categories': False,
		'scrape_products': False,
		'process_csv': False,
		'reprocess_csv': False,
		'dedupe_csv': False,
		'count_csv': False,
		'process_extra': False,
		'search_requests': False,
		'test_products': 20000,
		'max_products': 99,
		'csv_start_row': 0,
		'category_to_process': 0,
		'test_categories': 100,
		'chosen_category': '10001',  # Default to Meat
		'url_output_file': '',
		'data_output_file': '',
		'home_directory': DEFAULT_DIRECTORY,
		'url': 'https://app.cutanddry.com/catalog/sardilli?verifiedVendorId=369151799&categoryId=1&page=1',
		'search_term': 'Spices',
		'attempts': '40',
	}

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY
		self.options['base_url'] = self.BASE_URL
