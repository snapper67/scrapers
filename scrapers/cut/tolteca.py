import json
from .dry import CutScraper


class ToltecaScraper(CutScraper):
    """Scraper for Tolteca on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/tolteca/'

    # Values to change
    BASE_URL = "https://tolteca.cutanddry.com/catalog/tolteca?verifiedVendorId=236164749&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://tolteca.cutanddry.com"
    VENDOR_URL_NAME = 'tolteca'
    VERIFIED_VENDOR_ID = 236164749

    # This the name of the vendor
    VENDOR_NAME = "Tolteca"

    CATEGORIES = json.loads('''
    {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fruits and vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f4ee44251dc33b47cd2667314a8c1e6e.jpg",
          "id": "286188753",
          "name": "Fruits And Vegetables",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 127,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 17,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188754",
              "name": "Canned Vegetables",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188870",
              "name": "Frozen Vegetables",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188871",
              "name": "Frozen Fruits",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 38,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188879",
              "name": "Vegetables",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188884",
              "name": "Canned Chiles",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188886",
              "name": "Fruits",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188889",
              "name": "Whole Tomatoes",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188890",
              "name": "Cut Tomatoes",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188892",
              "name": "Tomato Sauces",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188896",
              "name": "Canned Fruits",
              "sortIndex": 9
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "egg and egg products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/1cc7f4307188a69e6e605a76960cc6c5.jpg",
          "id": "286188909",
          "name": "Egg And Egg Products",
          "sortIndex": "2",
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
              "id": "286188910",
              "name": "Eggs",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "meat products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/824df47fdd037cc9ef0554af08ad6fc7.jpg",
          "id": "286188725",
          "name": "Meat Products",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 303,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188726",
              "name": "Fresh Processed Pork",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 64,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188794",
              "name": "Frozen Beef",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 47,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188795",
              "name": "Fresh Beef",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 33,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188796",
              "name": "Reduced Frozen Beef",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188802",
              "name": "Frozen Processed Beef",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188804",
              "name": "Frozen Processed Pork",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188837",
              "name": "Frozen Pork",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188839",
              "name": "Fresh Pork",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188843",
              "name": "Reduced Frozen Pork",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188851",
              "name": "Frozen Processed Chicken",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188853",
              "name": "Frozen Chicken",
              "sortIndex": 12
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188855",
              "name": "Frozen Specialty",
              "sortIndex": 13
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188857",
              "name": "Reduced Frozen Chicken",
              "sortIndex": 14
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188858",
              "name": "Fresh Chicken",
              "sortIndex": 15
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188861",
              "name": "Frozen Fish",
              "sortIndex": 16
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188862",
              "name": "Frozen Processed Fish",
              "sortIndex": 17
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 41,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188863",
              "name": "Frozen Shellfish",
              "sortIndex": 18
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188866",
              "name": "Frozen Seafood",
              "sortIndex": 19
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "milk products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/2e615c3a9a822ad35d2ebffb1d48df9d.jpg",
          "id": "286188720",
          "name": "Milk Products",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 61,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188721",
              "name": "Fresh Milk",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188722",
              "name": "Canned Milk",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188723",
              "name": "Creams",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 42,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188724",
              "name": "Cheeses",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188729",
              "name": "Creamers",
              "sortIndex": 4
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "spices and seasoning",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/ba335840b0cd74bde22b2942c144a237.jpg",
          "id": "286188759",
          "name": "Spices And Seasoning",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 199,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188760",
              "name": "Dry Herbs",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188882",
              "name": "Fresh Herbs",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 49,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188885",
              "name": "Spices",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188887",
              "name": "Dry Chiles",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 38,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188888",
              "name": "Spice Mixes",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 27,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188895",
              "name": "Chile Sauces",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188898",
              "name": "Bouillons",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188899",
              "name": "Salt",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188900",
              "name": "Salad Dressings",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 20,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188901",
              "name": "Sauces",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188905",
              "name": "Vinegar",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "510285672",
              "name": "Spices And Seasoning",
              "sortIndex": 11
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "beverages and mixes",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/cdcbdb3b29ab403a2b5a2e07947612ce.webp",
          "id": "286188772",
          "name": "Beverages And Mixes",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 160,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188773",
              "name": "Soft Drink Syrups",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 34,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188774",
              "name": "Beverages",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188775",
              "name": "Juices",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188776",
              "name": "Teas And Coffees",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 49,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188777",
              "name": "Mixers",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188787",
              "name": "Powdered Mixes",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188788",
              "name": "Frozen Mixers",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188792",
              "name": "Concentrates",
              "sortIndex": 7
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dry goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a668ab5ce7f4be934205185ec37084c3.jpg",
          "id": "286188741",
          "name": "Dry Goods",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 40,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188742",
              "name": "Flour",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188747",
              "name": "Rice",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188748",
              "name": "Bread Crumbs",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188749",
              "name": "Breads",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188751",
              "name": "Canned Beans",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188752",
              "name": "Beans",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188755",
              "name": "Dry Goods",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188756",
              "name": "Saltines",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188761",
              "name": "Nuts",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188911",
              "name": "Pastas",
              "sortIndex": 9
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "oil and fat products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/b7ba8451b05f48a538e75ba03057768a.jpg",
          "id": "286188731",
          "name": "Oil And Fat Products",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 8,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188732",
              "name": "Vegetable Oils",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188734",
              "name": "Margarines",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188737",
              "name": "Lards",
              "sortIndex": 2
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "tortillas",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/182a98ea4ec4a32eee1c43d325138dde.jpg",
          "id": "286188702",
          "name": "Tortillas",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 54,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188703",
              "name": "Corn Chips",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 23,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188704",
              "name": "Corn Tortillas",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188714",
              "name": "Tostadas",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188718",
              "name": "Flour Tortillas",
              "sortIndex": 3
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "premade",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f1d10c378681ff1fb8cb9c5f1f0be423.jpg",
          "id": "286188715",
          "name": "Premade",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 40,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 14,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188716",
              "name": "Stuffed Bread",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188750",
              "name": "Breads And Doughs",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188767",
              "name": "Meals",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188872",
              "name": "For Fryer",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188939",
              "name": "Pizzas",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188947",
              "name": "Chips",
              "sortIndex": 5
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "sugar products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/de1271579eddba02ed1b3c130246dbe5.jpg",
          "id": "286188757",
          "name": "Sugar Products",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 65,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 27,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188758",
              "name": "Desserts",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188762",
              "name": "Sugar And Sweeteners",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188763",
              "name": "Honeys",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188764",
              "name": "Chocolates",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188765",
              "name": "Candy",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188770",
              "name": "Vanilla",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188771",
              "name": "Sweetened Fruits",
              "sortIndex": 6
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cleaning products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/865e20849a33d1b0601bc8c039c5e47a.jpg",
          "id": "286188948",
          "name": "Cleaning Products",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 42,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188949",
              "name": "Mixed Cleaners",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188950",
              "name": "Dish Detergents",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188951",
              "name": "Oven Cleaners",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188952",
              "name": "Machine Dish Detergents",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188957",
              "name": "Bleaches",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188958",
              "name": "Odor",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188959",
              "name": "Soap Hands",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188961",
              "name": "Cleaning Tools",
              "sortIndex": 8
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "catering",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/87e799166f31e296da766ff0d308fdb9.webp",
          "id": "286188940",
          "name": "Catering",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 16,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188941",
              "name": "Decorations",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "tableware",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/725fcb5662683eaac25efd8b63866cca.jpg",
          "id": "286188942",
          "name": "Tableware",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 35,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188943",
              "name": "Misc Table",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188944",
              "name": "Serveware",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188978",
              "name": "Table Plates",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189042",
              "name": "Silverware",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "558246411",
              "name": "Tableware",
              "sortIndex": 5
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "disposables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a768f196d25e90dedbadd42032cae634.jpg",
          "id": "286188955",
          "name": "Disposables",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 99,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188956",
              "name": "Straws",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 14,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188972",
              "name": "Paper Bags",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188974",
              "name": "Trash Bags",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188975",
              "name": "Plastic Bags",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188991",
              "name": "Paper Rolls",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188992",
              "name": "Film Rolls",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188993",
              "name": "Aluminum Rolls",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 7,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188995",
              "name": "Wax Paper",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188998",
              "name": "Aluminum Sheets",
              "sortIndex": 9
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 19,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188999",
              "name": "Napkins And Bands",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189004",
              "name": "Cutlery Kits",
              "sortIndex": 12
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189005",
              "name": "Toothpicks",
              "sortIndex": 13
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189007",
              "name": "Bev Trays",
              "sortIndex": 14
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "kitchen / bar",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5cd68080591a01766215721b0de897ab.jpg",
          "id": "286188968",
          "name": "Kitchen / Bar",
          "sortIndex": "19",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 22,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 20,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189006",
              "name": "Kitchen Tools",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189024",
              "name": "Pots",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189035",
              "name": "Kitchen Labels",
              "sortIndex": 3
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "containers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5a7a3e238ea29a52e4781155770a6697.jpg",
          "id": "286188970",
          "name": "Containers",
          "sortIndex": "20",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 104,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188971",
              "name": "Eco Containers",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188979",
              "name": "Plastic Containers",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 20,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188981",
              "name": "Foam Containers",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188982",
              "name": "Portion Containers",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188983",
              "name": "Foam Clamshells",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188985",
              "name": "Aluminum Containers",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188986",
              "name": "Plastic Lids",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 10,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188988",
              "name": "Plastic Cups",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188989",
              "name": "Foam Plates",
              "sortIndex": 8
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189002",
              "name": "Foam Cups",
              "sortIndex": 10
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 15,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189009",
              "name": "Portion Cups",
              "sortIndex": 12
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "apparel",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/eaecf1771266002579d6f3d6b493078c.jpg",
          "id": "286189036",
          "name": "Apparel",
          "sortIndex": "21",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 28,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189037",
              "name": "Gloves",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189038",
              "name": "Aprons",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189039",
              "name": "Ppe",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189040",
              "name": "Heat Resistence",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "611620067",
              "name": "Apparel",
              "sortIndex": 4
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dispensers",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9cd89a63a9252db1b663c9fe4d830912.jpg",
          "id": "286189048",
          "name": "Dispensers",
          "sortIndex": "22",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 8,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189049",
              "name": "Spray Bottles",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189058",
              "name": "Paper Dispensers",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 1,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189059",
              "name": "Soap Dispensers",
              "sortIndex": 2
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "office products",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/18fdfd6071fb84783f045742c2586899.jpg",
          "id": "286189055",
          "name": "Office Products",
          "sortIndex": "23",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 8,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189056",
              "name": "Paper Roll",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286189057",
              "name": "Guest Checks",
              "sortIndex": 1
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "obs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/0c0ffc952a3bf03058e361c11b766a24.jpg",
          "id": "286188705",
          "name": "Obs",
          "sortIndex": "26",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 14,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 14,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "286188706",
              "name": "Obs",
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
