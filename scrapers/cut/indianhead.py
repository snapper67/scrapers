
import json
from scrapers.cut.dry import CutScraper


class IndianheadScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/indianhead/'

	# Values to change
	BASE_URL = "https://ifd.cutanddry.com/catalog/ShopIFD?verifiedVendorId=320572326&categoryId=1&page=1"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "339133131",
          "baseName": "bakery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4bd05d162548e1c8c41925b6cc2bb077.jpg",
          "name": "Bakery",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 862,
        "subcategories": [
          {
            "subcategory": {
              "id": "339134187",
              "name": "Cakes, Desserts and Pies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 79,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134359",
              "name": "Donuts and Pastries",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 107,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134224",
              "name": "Bread",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 99,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134249",
              "name": "Buns, Rolls and Pretzels",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 128,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133132",
              "name": "Bagels, Biscuits and English Muffins",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 49,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339135161",
              "name": "Tortillas and Taco Shells",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 38,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134276",
              "name": "Cookies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 107,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134619",
              "name": "Waffles, French Toast and Pancakes",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 56,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134246",
              "name": "Granola Bars, Muffins, Snack Bread and Bars",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 150,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339135000",
              "name": "Pizza Crusts",
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
          "id": "339133173",
          "baseName": "cleaning supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b593774c961338854f50ca09454ab1c6.jpg",
          "name": "Cleaning Supplies",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 217,
        "subcategories": [
          {
            "subcategory": {
              "id": "339137558",
              "name": "Sponges, Pads and Clothes",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 30,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339150073",
              "name": "Laundry Chemicals",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 1,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133420",
              "name": "Janitorial",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 58,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133174",
              "name": "Dispenser and Machine Chemicals",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 71,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339137694",
              "name": "Manual Chemicals",
              "sortIndex": 0,
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
          "id": "339134565",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/81f796ac987c4135a56457ae29f98354.jpg",
          "name": "Dairy",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 368,
        "subcategories": [
          {
            "subcategory": {
              "id": "339136350",
              "name": "Cheese",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 166,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134566",
              "name": "Milk and Creamers",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 80,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339141047",
              "name": "Ice Cream/Yogurt Mixes",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 21,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134598",
              "name": "Eggs and Egg Substitutes",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 37,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339141679",
              "name": "Yogurt and Sour Cream",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 33,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134580",
              "name": "Butter and Margarine",
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
          "id": "339133738",
          "baseName": "deli",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f160b88d64ff0957ed306f6ad3a5cb01.jpg",
          "name": "Deli",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 86,
        "subcategories": [
          {
            "subcategory": {
              "id": "339133739",
              "name": "Salads and Sides",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 50,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133742",
              "name": "Dips, Sauces and Spreads",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 15,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339140494",
              "name": "Snack Items",
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
          "id": "339133923",
          "baseName": "dietary",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/dcb6209c26d214ad401d8dea9eb5969c.jpg",
          "name": "Dietary",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 54,
        "subcategories": [
          {
            "subcategory": {
              "id": "339133924",
              "name": "Entrees",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 54,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "339133168",
          "baseName": "disposables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d0d6dc25454b8791b3d5648e9919b2d6.jpg",
          "name": "Disposables",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 603,
        "subcategories": [
          {
            "subcategory": {
              "id": "339137144",
              "name": "Bags, Films, Foils, Baking/Deli Paper and Can Liners",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 141,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133402",
              "name": "Paper Goods",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 105,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339137526",
              "name": "Cutlery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 35,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339137160",
              "name": "Serving Trays, Containers, and Take-out",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 98,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133360",
              "name": "Drinkware",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 86,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133169",
              "name": "Straws and Table Coverings",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 34,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339137247",
              "name": "Dinnerware",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 30,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339135033",
              "name": "Pizza Supplies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 18,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133410",
              "name": "Wearables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 32,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339137110",
              "name": "Portion and Souffle Cups",
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
          "id": "339133105",
          "baseName": "equipment/supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6d7719864eff830fdb06127d102804a2.jpg",
          "name": "Equipment/Supplies",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 781,
        "subcategories": [
          {
            "subcategory": {
              "id": "339133191",
              "name": "Dinnerware",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 45,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133198",
              "name": "Serving and Flatware",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 108,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133236",
              "name": "Tabletop and Dining Room Supplies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 60,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133139",
              "name": "Kitchenware",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 152,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339138002",
              "name": "Bar Supplies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133214",
              "name": "Catering Supplies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 34,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133233",
              "name": "Equipment",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 59,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133106",
              "name": "Glassware",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 38,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133310",
              "name": "Cookware",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 64,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133348",
              "name": "Food Storage Containers",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 71,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133203",
              "name": "Smallware and Cutlery",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 82,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133339",
              "name": "Apparel and Linens",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 16,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133303",
              "name": "Steam Table Pans",
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
          "id": "339133155",
          "baseName": "fish/seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/4513b99871b72ca1e7796c013d25bcd8.jpg",
          "name": "Fish/Seafood",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 253,
        "subcategories": [
          {
            "subcategory": {
              "id": "339133156",
              "name": "Fish",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 135,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134751",
              "name": "Seafood",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 118,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "339133144",
          "baseName": "frozen foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/54267df47151ddfdbcb79813b69268be.jpg",
          "name": "Frozen Foods",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 722,
        "subcategories": [
          {
            "subcategory": {
              "id": "339134484",
              "name": "Entrees and Sandwiches",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 175,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134644",
              "name": "Appetizers",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 140,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133145",
              "name": "Potato Products",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 123,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133148",
              "name": "Ice Cream, Novelties and Ice",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 141,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134239",
              "name": "Pizza Prepared",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 91,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339135240",
              "name": "Soup",
              "sortIndex": 0,
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
          "id": "339133111",
          "baseName": "fruits/vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/3c00ef4eb52265fda40db303082d30e1.jpg",
          "name": "Fruits/Vegetables",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 880,
        "subcategories": [
          {
            "subcategory": {
              "id": "339133115",
              "name": "Fruit",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 314,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133112",
              "name": "Vegetables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 541,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133549",
              "name": "Fresh Herbs",
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
          "id": "339133151",
          "baseName": "meat",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1a2d78017838e42ee659d510bef91a53.jpg",
          "name": "Meat",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1037,
        "subcategories": [
          {
            "subcategory": {
              "id": "339135123",
              "name": "Specialty Meats",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 77,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133159",
              "name": "Poultry",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 340,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133152",
              "name": "Beef",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 337,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134746",
              "name": "Pork",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 121,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134718",
              "name": "Bacon and Sausage",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 100,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134737",
              "name": "Bratwursts and Hotdogs",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 52,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134806",
              "name": "Pizza Toppings",
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
          "id": "339133118",
          "baseName": "pantry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/702cacafb2b7dd9dfc5a640cd9873d33.jpg",
          "name": "Pantry",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 2401,
        "subcategories": [
          {
            "subcategory": {
              "id": "339133119",
              "name": "Beverages and Beverage Mixes",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 413,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339136026",
              "name": "Snacks, Crackers and Pretzels",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 140,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339134571",
              "name": "Syrup, Jellies, Peanut Butter and Honey",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 107,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133162",
              "name": "Condiments",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 202,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133136",
              "name": "Oils, Shortening and Vinegar",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 50,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339135188",
              "name": "Dressings, Sauces and Salad Toppings",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 183,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133165",
              "name": "Baking, Breading, Cooking and Cake Mixes",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 234,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133122",
              "name": "Puddings, Gelatins and Fillings",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 98,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339136421",
              "name": "Cereal, Oatmeals and Pancake Mixes",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 140,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339135712",
              "name": "Gravy, Bases, Sauces and Cheese Sauces",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 146,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339136580",
              "name": "Seasonings and Spices",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 163,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133689",
              "name": "Canned Meats, Beans, Entrees and Prepared",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 125,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133453",
              "name": "Pickles, Mushrooms, Olives and Relishes",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 67,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339136585",
              "name": "Candy, Ice Cream Toppings and Cones",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 78,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339135182",
              "name": "Chips and Popcorn",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 107,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339133562",
              "name": "Dry Pasta, Rice and Beans",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 135,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "339136189",
              "name": "Soups and Broths",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 30,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'Indianhead Foodservice Distributor'
	VENDOR_URL_NAME = 'ShopIFD'
	VERIFIED_VENDOR_ID = 32057232

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY

