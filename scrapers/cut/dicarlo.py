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


class DiCarloScraper(DryMarketScraper):
	# /1391/edit_note/1703/
	CRM_ID = 1391
	CRM_NOTE_ID = 1703
	CRM_PRICE_TYPE = 'Retail'
	CRM_STATUS_OVERRIDE = ''

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/dicarlo/'

	# Values to change
	BASE_URL = "https://dicarlo.cutanddry.com/market/dicarlo/131360908/131360897/quantities?verifiedVendorId=1861927&categoryId=1&categoryName=All+Items&page=1"
	SUB_DOMAIN = "https://dicarlo.cutanddry.com"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dairy",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Dairy.png",
          "id": "120859952",
          "name": "Dairy",
          "sortIndex": "0",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 163,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 163,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859953",
              "name": "Dairy",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "grocery canned dry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Grocery+Canned.png",
          "id": "120859964",
          "name": "Grocery Canned Dry",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 1045,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 1045,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859965",
              "name": "Grocery Canned Dry",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "refrigerated",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Refridgerated.png",
          "id": "120859970",
          "name": "Refrigerated",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 154,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 154,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859971",
              "name": "Refrigerated",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "frozen",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Frozen.png",
          "id": "120859960",
          "name": "Frozen",
          "sortIndex": "3",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 817,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 817,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859961",
              "name": "Frozen",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "shortenings/oils",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Shortening+Oils.png",
          "id": "120859972",
          "name": "Shortenings/Oils",
          "sortIndex": "4",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 41,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 41,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859973",
              "name": "Shortenings/Oils",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "spices/packets",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Spices+Packets.png",
          "id": "120859976",
          "name": "Spices/Packets",
          "sortIndex": "5",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 159,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 159,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859977",
              "name": "Spices/Packets",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "paper & disposables",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Paper+and+Disposable.png",
          "id": "120859966",
          "name": "Paper & Disposables",
          "sortIndex": "6",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 417,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 417,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859967",
              "name": "Paper & Disposables",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "beverage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Beverages.png",
          "id": "120859948",
          "name": "Beverage",
          "sortIndex": "7",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 262,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 262,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859949",
              "name": "Beverage",
              "sortIndex": 0
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
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Produce.png",
          "id": "120859968",
          "name": "Produce",
          "sortIndex": "8",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 382,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 382,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859969",
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
          "baseName": "specialty foods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Specialty+Foods.png",
          "id": "120859974",
          "name": "Specialty Foods",
          "sortIndex": "9",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 205,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 205,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859975",
              "name": "Specialty Foods",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "frozen meats & poultry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Frozen+Meats+%26+Poultry.png",
          "id": "120859962",
          "name": "Frozen Meats & Poultry",
          "sortIndex": "10",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 267,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 267,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859963",
              "name": "Frozen Meats & Poultry",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "fresh meat & poultry",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Fresh+Meat+and+Poultry.png",
          "id": "120859956",
          "name": "Fresh Meat & Poultry",
          "sortIndex": "11",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 115,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 115,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859957",
              "name": "Fresh Meat & Poultry",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "seafood fresh",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/890e29e9d806bebb1ff7e3d315ab8bd9.jpg",
          "id": "218853530",
          "name": "Seafood Fresh",
          "sortIndex": "12",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 19,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 19,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "218853531",
              "name": "Seafood Fresh",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "seafood frozen",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://ordering-supplies-images-1.s3.us-east-2.amazonaws.com/890e29e9d806bebb1ff7e3d315ab8bd9.jpg",
          "id": "218853526",
          "name": "Seafood Frozen",
          "sortIndex": "13",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 142,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 142,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "218853527",
              "name": "Seafood Frozen",
              "sortIndex": 0
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
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Chemicals.png",
          "id": "120859950",
          "name": "Chemicals",
          "sortIndex": "14",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 104,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 104,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859951",
              "name": "Chemicals",
              "sortIndex": 0
            }
          }
        ]
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "equipment & supply",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/category-images/1861927/Equp+and+Supplies.png",
          "id": "120859954",
          "name": "Equipment & Supply",
          "sortIndex": "15",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 46,
        "subcategories": [
          {
            "__typename": "subcategoryOption",
            "productCount": 46,
            "subcategory": {
              "__typename": "ProductSubcategory",
              "id": "120859955",
              "name": "Equipment & Supply",
              "sortIndex": 0
            }
          }
        ]
      }
    ]
  }
}    
		''')

	VENDOR_NAME = 'DiCarlo'
	VENDOR_URL_NAME = 'dicarlo/131360908/131360897'
	VERIFIED_VENDOR_ID = 1861927

	def __init__(self, options=None):
		super().__init__(options)

