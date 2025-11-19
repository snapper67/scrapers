import csv
import json
import os
import sys
import time
from operator import truediv
from urllib.parse import quote
from seleniumwire.utils import decode
from scrapers.cut.dry_market import DryMarketScraper
from scrapers.scraper import ProductNotFound


class AllStarSpecialtiesScraper(DryMarketScraper):
	# 1284/edit_note/1401/
	CRM_ID = 1284
	CRM_NOTE_ID = 1401
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/all_star_specialties/'

	# Values to change
	BASE_URL = "https://allstarspecialties.cutanddry.com/market/AllStar/448081160/448081149/quantities?verifiedVendorId=320450261&categoryId=1&page=1"
	SUB_DOMAIN = "https://allstarspecialties.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "baked goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/219503724e9f6ab6e22ffad97df2d55b.jpg",
          "id": "372855057",
          "name": "Baked Goods",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 132,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 23,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "372857059",
              "name": "Baked Goods",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 28,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412475061",
              "name": "Baking Batter & Mix",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 26,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412486838",
              "name": "Baking Supplies",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 21,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412486840",
              "name": "Cookies",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 18,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412486841",
              "name": "Cookie Dough",
              "sortIndex": 6
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412486842",
              "name": "Pie",
              "sortIndex": 7
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cakes",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/665be9562d6c9ed74e36d6e78639ba32.jpg",
          "id": "372855112",
          "name": "Cakes",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 42,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 42,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "372857017",
              "name": "Cakes",
              "sortIndex": 1
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "candy & snacks",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/bbe92e3bd8b9909a20bd1f49f2453744.jpg",
          "id": "372855116",
          "name": "Candy & Snacks",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 85,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 62,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "372857016",
              "name": "Candy",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 23,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412487576",
              "name": "Chips & Snacks",
              "sortIndex": 2
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "frozen drink mixes",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d16aa341f0f3da7b6aeb867fc22f8826.jpg",
          "id": "412490807",
          "name": "Frozen Drink Mixes",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 21,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 21,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412490808",
              "name": "Frozen Drink Mixes",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "ice cream tubs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/d5bf2a4180af03f02c24985cd34a1eaa.jpg",
          "id": "412491292",
          "name": "Ice Cream Tubs",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 65,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 43,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412491294",
              "name": "Ice Cream Tubs",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 11,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412491296",
              "name": "Haagen Dazs Tubs",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412491300",
              "name": "Mr. Green Tea",
              "sortIndex": 7
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 2,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412491301",
              "name": "Non Dairy Products",
              "sortIndex": 8
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "ice cream specialties",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f98eec941ba4622295c04d2f7e5721ce.jpg",
          "id": "412491642",
          "name": "Ice Cream Specialties",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 53,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412491645",
              "name": "Ice Cream Cake",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 21,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414359423",
              "name": "Ice Cream Tartufos",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 29,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414464530",
              "name": "Frozen Specialties",
              "sortIndex": 11
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "ice cream cones",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/21fe7c692a8680b196c610ad78d1c972.jpg",
          "id": "412491757",
          "name": "Ice Cream Cones",
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
              "id": "412491758",
              "name": "Ice Cream Cones",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "ice cream mix",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/a9c7be08394513a70cd64ab188bbc76b.jpg",
          "id": "412493184",
          "name": "Ice Cream Mix",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 17,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 13,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412493186",
              "name": "Ice Cream Mix",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 4,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414466362",
              "name": "Yogurt",
              "sortIndex": 15
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "ice cream novelties",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/f54c8bc885b201567f9deb8d873960fa.jpg",
          "id": "455442934",
          "name": "Ice Cream Novelties",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 80,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 80,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "455442935",
              "name": "Ice Cream Novelties",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "individual dessert",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/fa7eb85f0aad232b6d81e94455212d51.jpg",
          "id": "412493427",
          "name": "Individual Dessert",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 53,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 24,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412493428",
              "name": "Individual Dessert",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412493429",
              "name": "Individual Mini Dessert",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "611710637",
              "name": "Cake Pops",
              "sortIndex": 20
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "other items",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/c763ceb6135c546a1100568edb36c962.jpg",
          "id": "412493871",
          "name": "Other Items",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 77,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412493872",
              "name": "Spices & Seasoning",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412493873",
              "name": "Equipment",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 28,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414364378",
              "name": "Paper Goods",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414364379",
              "name": "Dry Ice",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 16,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414364380",
              "name": "Gloves",
              "sortIndex": 5
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "499771329",
              "name": "Cleaning Supplies",
              "sortIndex": 19
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fun foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/93026e949f6128e25c81de075d4ae110.jpg",
          "id": "412494720",
          "name": "Fun Foods",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 62,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 9,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412494724",
              "name": "Pretzel",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 6,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412494728",
              "name": "Donuts",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412494729",
              "name": "Candy Apples",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412494731",
              "name": "Sno Kones",
              "sortIndex": 4
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 14,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414466300",
              "name": "Churros & Fried Foods",
              "sortIndex": 13
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 3,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414466343",
              "name": "Pizza",
              "sortIndex": 14
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "private label",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/55313ec3cfccb31b5a48a28b4a3a6927.jpg",
          "id": "412494866",
          "name": "Private Label",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 53,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 28,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414365410",
              "name": "Pints",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414365411",
              "name": "Cookies",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414365412",
              "name": "Popcorn & Cotton Candy",
              "sortIndex": 3
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 5,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414365413",
              "name": "Novelties",
              "sortIndex": 4
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "toppings and syrups",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/01be1e4d1117e727d475312b903f2ca1.jpg",
          "id": "412495027",
          "name": "Toppings and Syrups",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 132,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 62,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412495028",
              "name": "Toppings",
              "sortIndex": 0
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 40,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412495029",
              "name": "Monin Puree & Syrups",
              "sortIndex": 1
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 8,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "412495030",
              "name": "Chocolate",
              "sortIndex": 2
            }
          },
          {
            "__typename": "subcategoryOption",
            "productCount": 22,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "414466167",
              "name": "Syrups & Sauces",
              "sortIndex": 12
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "gelato",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/8ccfdc7b615d2cc703153d8502cce3e8.jpg",
          "id": "498722208",
          "name": "Gelato",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 20,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 20,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "498722209",
              "name": "Gelato",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "sorbet & italian ice",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e9913c98a9035dbae819aa9810e2541c.jpg",
          "id": "498722496",
          "name": "Sorbet & Italian Ice",
          "sortIndex": "16",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 12,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 12,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "498722497",
              "name": "Sorbet & Italian Ice",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "popcorn",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/daf6c97f5f4bf115b36b3d54523d2599.jpg",
          "id": "498722721",
          "name": "Popcorn",
          "sortIndex": "17",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 37,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 37,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "498722722",
              "name": "Popcorn",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "cotton candy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/e24a45aeeb3cf8b904fdeff7de104589.jpg",
          "id": "498723197",
          "name": "Cotton Candy",
          "sortIndex": "18",
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
              "id": "498723198",
              "name": "Cotton Candy",
              "sortIndex": 0
            }
          }
        ]
      }
    ]
  }
}

                    
		''')

	VENDOR_NAME = 'All Star Specialties'
	VENDOR_URL_NAME = 'AllStar/448081160/448081149'
	VERIFIED_VENDOR_ID = 320450261

	def __init__(self, options=None):
		super().__init__(options)

