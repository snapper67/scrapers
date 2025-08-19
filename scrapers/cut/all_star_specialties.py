
import json
from scrapers.cut.dry import CutScraper


class AllStarSpecialtiesScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/all_star_specialties/'

	# Values to change
	BASE_URL = "https://allstarspecialties.cutanddry.com/market/AllStar/448081160/448081149/quantities?verifiedVendorId=320450261&categoryId=1&page=1"
	SUB_DOMAIN = "https://allstarspecialties.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "412165389",
          "baseName": "fruits",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/55422488ffee9910aee2e8b19f21706f.jpg",
          "name": "Fruits",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 400,
        "subcategories": [
          {
            "subcategory": {
              "id": "412165489",
              "name": "Conventional Fruits",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 336,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "412165490",
              "name": "Organic Fruits",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 63,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "412249822",
              "name": "Others",
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
          "id": "412165486",
          "baseName": "vegetables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/114abbbbeeea28ca919156319f9d8e6c.jpg",
          "name": "Vegetables",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 687,
        "subcategories": [
          {
            "subcategory": {
              "id": "412258980",
              "name": "Conventional Vegetables",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 517,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "412165488",
              "name": "Organic Vegetables",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 170,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "412165511",
          "baseName": "herbs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/02b8fa2152214dead65a8a62e7dcfe12.jpg",
          "name": "Herbs",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 90,
        "subcategories": [
          {
            "subcategory": {
              "id": "412165512",
              "name": "Herbs",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 90,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "412165584",
          "baseName": "bakery, breads, & tortillas",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5c4c97404eadb6c4b870e2a24f005ab7.jpg",
          "name": "Bakery, Breads, & Tortillas",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 17,
        "subcategories": [
          {
            "subcategory": {
              "id": "412165585",
              "name": "Bakery, Breads, & Tortillas",
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
          "id": "412165623",
          "baseName": "beverages & juices",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a2a2c0c8f6cb566b41d8f998e5aed0e4.jpg",
          "name": "Beverages & Juices",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 54,
        "subcategories": [
          {
            "subcategory": {
              "id": "412165624",
              "name": "Beverages & Juices",
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
          "id": "412165627",
          "baseName": "condiments & sauces",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6e42eab28246e675e45ed9e897b4b0bc.jpg",
          "name": "Condiments & Sauces",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 60,
        "subcategories": [
          {
            "subcategory": {
              "id": "412165628",
              "name": "Condiments & Sauces",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 60,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "412165643",
          "baseName": "cheese, dairy & eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/96768152ab944faa2eeac5c5a3ef2b17.jpg",
          "name": "Cheese, Dairy & Eggs",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 104,
        "subcategories": [
          {
            "subcategory": {
              "id": "412165644",
              "name": "Cheese, Dairy & Eggs",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 104,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "412165692",
          "baseName": "dry goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/6a7cb9ae2cf3fd9b18b6ff98976dbc35.jpg",
          "name": "Dry Goods",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 172,
        "subcategories": [
          {
            "subcategory": {
              "id": "412165693",
              "name": "Beans, Grains, Legumes & Rice",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 14,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "412165694",
              "name": "Canned Goods",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 31,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "412165695",
              "name": "Oil & Vinegar",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 24,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "412165696",
              "name": "Noodles & Pasta",
              "sortIndex": 3,
              "__typename": "ProductSubcategory"
            },
            "productCount": 11,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "412165697",
              "name": "Flour, Salt & Sugar",
              "sortIndex": 4,
              "__typename": "ProductSubcategory"
            },
            "productCount": 13,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "412165698",
              "name": "Spices & Seasonings",
              "sortIndex": 5,
              "__typename": "ProductSubcategory"
            },
            "productCount": 79,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "412166028",
          "baseName": "frozen foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/5afa6801143bd01c6a0c0d88de45a2ca.jpg",
          "name": "Frozen Foods",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 145,
        "subcategories": [
          {
            "subcategory": {
              "id": "412166029",
              "name": "Frozen Foods",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 145,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "412166042",
          "baseName": "grocery items",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fe587ef4a91b7d682ff49e402e71c35f.jpg",
          "name": "Grocery Items",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 20,
        "subcategories": [
          {
            "subcategory": {
              "id": "412166043",
              "name": "Grocery Items",
              "sortIndex": 0,
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
          "id": "412166072",
          "baseName": "protein",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/9bdf7430c44ab1227a5d4bcda759e996.jpg",
          "name": "Protein",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 51,
        "subcategories": [
          {
            "subcategory": {
              "id": "412166073",
              "name": "Protein",
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
          "id": "412165882",
          "baseName": "restaurant supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f160c02bb6f34490719582ffa8df209b.jpg",
          "name": "Restaurant Supplies",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 159,
        "subcategories": [
          {
            "subcategory": {
              "id": "412165883",
              "name": "Food Storage & Packaging Supplies",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 18,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "412165884",
              "name": "Paper Products & Disposables",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 122,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "412165885",
              "name": "Cleaning Supplies",
              "sortIndex": 2,
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
          "id": "412165943",
          "baseName": "value-add",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/eb06abc595c604eb4d105ecc07e2005a.jpg",
          "name": "Value-Add",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 482,
        "subcategories": [
          {
            "subcategory": {
              "id": "412165944",
              "name": "Fresh Cut Produce",
              "sortIndex": 0,
              "__typename": "ProductSubcategory"
            },
            "productCount": 106,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "412165945",
              "name": "Retail Value-Add",
              "sortIndex": 1,
              "__typename": "ProductSubcategory"
            },
            "productCount": 342,
            "__typename": "subcategoryOption"
          },
          {
            "subcategory": {
              "id": "412165946",
              "name": "Retail Supplies",
              "sortIndex": 2,
              "__typename": "ProductSubcategory"
            },
            "productCount": 34,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "412249667",
          "baseName": "others",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d8d4e2c24f2434a9dcdf1555fc6fbbd4.jpg",
          "name": "Others",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 79,
        "subcategories": [
          {
            "subcategory": {
              "id": "412249668",
              "name": "Others",
              "sortIndex": 6,
              "__typename": "ProductSubcategory"
            },
            "productCount": 79,
            "__typename": "subcategoryOption"
          }
        ],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'All Star Specialties'
	VENDOR_URL_NAME = 'CarusoProduceInc'
	VERIFIED_VENDOR_ID = 320450261

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY
		self.options['base_url'] = self.BASE_URL
