
import json
import time
from urllib.parse import quote

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.options import PageLoadStrategy
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire.utils import decode
from typing import List, Dict, Any, Optional

from scrapers.scraper import Scraper, ProductNotFound


class PrimizieScraper(Scraper):
	PRODUCT_DATA_SPEC = {
		# Fields from IMPORT_SPEC
		'name': '',
		'sku': '',
		'gtin': '',
		'image': '',
		'pack': '',
		'size': '',
		'retail_price': '',
		'ordering_unit': '',
		'is_catch_weight': '',
		'is_broken_case': '',
		'average_case_weight': '',
		'brand': '',
		'taxonomy': '',
		'level_1': '',
		'level_2': '',
		'level_3': '',
		'manufacturer_name': '',
		'manufacturer_sku': '',
		'distributor_name': '',
		'content_url': '',
		'description': '',
		'unit_price': '',
		'extra_data_1': '',
		'timestamp': '',
		# Fields from Southern Glazier
		'extra_data_2': '',
		'id': '',
		'features': '',
		'pack_size': '',
		'category': '',
		'subcategory': '',
	}

	ENCODING = "utf-8"

	CATEGORY_IDS = {}
	CATEGORY_NAMES = {}
	CATEGORY_URLS = {}

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 45  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/primiizie'

	SEARCH_API_OPERATION = 'ConsumerCanonicalProductsByCategoriesQuery'
	PRODUCT_API_OPERATION = 'UniversalProductForPDP'
	GRAPHQL_API_FILTER = 'app.cutanddry.com/GraphQLController'

	# Values to change
	BASE_URL = 'https://app.cutanddry.com/catalog/primizieny?verifiedVendorId=50714839&categoryId=1&page=1'
	CATEGORIES = json.loads('''{
    "data": {
        "catalogCategoryOptions": [
            {
                "category": {
                    "id": "154067862",
                    "baseName": "produce",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Produce",
                    "sortIndex": "0",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 953,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067863",
                            "name": "Fresh Produce",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 951,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069146",
                            "name": "Lemon Wraps",
                            "sortIndex": 0,
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
                    "id": "154067892",
                    "baseName": "grocery",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Grocery",
                    "sortIndex": "1",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 1360,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "385186681",
                            "name": "Fruit",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 139,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067907",
                            "name": "Pasta",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 90,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067939",
                            "name": "Syrups",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 36,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067893",
                            "name": "Chocolate & Cocoa",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 104,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067962",
                            "name": "Mayonnaise",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 20,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067940",
                            "name": "Sauces",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 122,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067903",
                            "name": "Snacks",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 116,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067896",
                            "name": "Ethnic",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 119,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385186682",
                            "name": "Vegetables",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 198,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067966",
                            "name": "Tortilla",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 24,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067970",
                            "name": "Portion Packs",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 71,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067961",
                            "name": "Salad Dressings",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 35,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067897",
                            "name": "Condiments",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 107,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067933",
                            "name": "Baking Mixes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 25,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067904",
                            "name": "Jams, Jelly, And Preserv",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 19,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385186684",
                            "name": "Olives",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 32,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067946",
                            "name": "Cereals",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 38,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067968",
                            "name": "Tomatoes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 48,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067972",
                            "name": "Nut Butters",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 11,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067941",
                            "name": "Stuffing",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067956",
                            "name": "Capers",
                            "sortIndex": 0,
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
                    "id": "154067894",
                    "baseName": "dry goods",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Dry Goods",
                    "sortIndex": "2",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 702,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067895",
                            "name": "Baking Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 340,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067905",
                            "name": "Nuts",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 39,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067900",
                            "name": "Batter And Breading",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 23,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067906",
                            "name": "Shortening And Oils",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 86,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067901",
                            "name": "Grains And Legumes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 116,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067908",
                            "name": "Vinegar",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 59,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385186683",
                            "name": "Bases",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 37,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067947",
                            "name": "Polenta",
                            "sortIndex": 0,
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
                    "id": "154067898",
                    "baseName": "spices",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Spices",
                    "sortIndex": "3",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 236,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067899",
                            "name": "Spices",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 236,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067909",
                    "baseName": "prepared foods",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Prepared Foods",
                    "sortIndex": "4",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 275,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067930",
                            "name": "Appetizers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 66,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068073",
                            "name": "Soups",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 37,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067929",
                            "name": "Entrees",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 27,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219285",
                            "name": "Protein - Deli Meats",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 42,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219292",
                            "name": "Vegetarian",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 36,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219328",
                            "name": "Protein - Meatballs",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 8,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067934",
                            "name": "Pizza",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 33,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219324",
                            "name": "Protein - Hot Dogs",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 14,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068032",
                            "name": "Salads And Sides",
                            "sortIndex": 0,
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
                    "id": "154067911",
                    "baseName": "seafood",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Seafood",
                    "sortIndex": "5",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 212,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067912",
                            "name": "Protein - Seafood",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 212,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067913",
                    "baseName": "meat + game",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Meat + Game",
                    "sortIndex": "6",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 488,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067915",
                            "name": "Protein - Beef",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 289,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067916",
                            "name": "Protein - Pork",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 85,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067918",
                            "name": "Protein - Sausage",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 67,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067924",
                            "name": "Protein - Lamb",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 30,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067925",
                            "name": "Protein - Veal",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067914",
                            "name": "Protein - Exotic Meats",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 10,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068028",
                            "name": "Protein - Philly Sandwic",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 5,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068027",
                            "name": "Protein - Gyro",
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
                    "id": "154067919",
                    "baseName": "poultry",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Poultry",
                    "sortIndex": "7",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 223,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067922",
                            "name": "Protein - Turkey",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 29,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067923",
                            "name": "Protein - Duck",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 9,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067920",
                            "name": "Protein - Chicken",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 182,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067921",
                            "name": "Protein - Game Hens",
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
                    "id": "154067926",
                    "baseName": "bakery",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Bakery",
                    "sortIndex": "8",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 258,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067927",
                            "name": "Baked Goods",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 145,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067928",
                            "name": "Bread",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 113,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067937",
                    "baseName": "beverage",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Beverage",
                    "sortIndex": "9",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 396,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067955",
                            "name": "Beverages",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 290,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067953",
                            "name": "Coffee, Tea, And Cocoa",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 75,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067938",
                            "name": "Bar Supplies And Mixes",
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
                    "id": "154067942",
                    "baseName": "dairy + eggs",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Dairy + Eggs",
                    "sortIndex": "10",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 343,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067948",
                            "name": "Cheese",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 240,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067943",
                            "name": "Dairy",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 78,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067958",
                            "name": "Creamer",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 9,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067944",
                            "name": "Eggs",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 16,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154067951",
                    "baseName": "miscellaneous",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Miscellaneous",
                    "sortIndex": "11",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 2,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067952",
                            "name": "Non Commission",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068072",
                            "name": "Trackmax Test Pbh It",
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
                    "id": "154067959",
                    "baseName": "frozen desserts",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Frozen Desserts",
                    "sortIndex": "12",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 85,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154067969",
                            "name": "Toppings",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 15,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154067960",
                            "name": "Desserts",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 70,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            },
            {
                "category": {
                    "id": "154068232",
                    "baseName": "equipment + furniture",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Equipment + Furniture",
                    "sortIndex": "13",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 1290,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "385187583",
                            "name": "Baskets",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 6,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187548",
                            "name": "Glassware",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 111,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187245",
                            "name": "Dining Room Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 79,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069020",
                            "name": "Pizza Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 12,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068261",
                            "name": "Pots And Pans",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 53,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068246",
                            "name": "Kitchen Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 248,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219489",
                            "name": "Brushes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 9,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187472",
                            "name": "Flatware",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 93,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187246",
                            "name": "China",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 30,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068233",
                            "name": "Equipment",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 42,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187763",
                            "name": "Vacuum Bags",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 11,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068254",
                            "name": "Storage",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 44,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069159",
                            "name": "Squeeze Bottles",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 12,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069157",
                            "name": "Carts",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068251",
                            "name": "Bar Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 31,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068245",
                            "name": "Parts",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 16,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187907",
                            "name": "Pastry Cloth",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069158",
                            "name": "Warewashing",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 24,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069164",
                            "name": "Racks",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385188009",
                            "name": "Bell",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069199",
                            "name": "Shakers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 7,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187695",
                            "name": "Textiles",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 5,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068635",
                            "name": "Light Bulbs",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069163",
                            "name": "Servers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069017",
                            "name": "Hoses",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 3,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069160",
                            "name": "Mandolines",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 3,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069165",
                            "name": "Valves",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "411509560",
                            "name": "Baking Supplies",
                            "sortIndex": 2,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 340,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "411516576",
                            "name": "Cutlery",
                            "sortIndex": 3,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 69,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "411516527",
                            "name": "Trays",
                            "sortIndex": 3,
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
                    "id": "154068234",
                    "baseName": "janitorial",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Janitorial",
                    "sortIndex": "14",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 267,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "154068239",
                            "name": "Restroom Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 46,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068235",
                            "name": "Chemical-dispensed",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 53,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068236",
                            "name": "Chemical-green Dispense",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 9,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068237",
                            "name": "Chemical-nondispensed",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 80,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187873",
                            "name": "Waste Receptacles",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 9,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187876",
                            "name": "Signs",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069114",
                            "name": "Chemical-green Non-disp",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 6,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069130",
                            "name": "Brooms",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187742",
                            "name": "Can Liners",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 31,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069137",
                            "name": "Buckets",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069131",
                            "name": "Mops And Handles",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 7,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069139",
                            "name": "Squeegees",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069134",
                            "name": "Dust Mops And Handles",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187905",
                            "name": "Spray Bottle",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 7,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069133",
                            "name": "Dust Pans",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 3,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385188391",
                            "name": "Vacuums",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069138",
                            "name": "Plunger",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219331",
                            "name": "Distilled Water",
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
                    "id": "154068262",
                    "baseName": "operational supplies",
                    "examplePictureUrl": null,
                    "iconAltUrl": null,
                    "iconUrl": null,
                    "name": "Operational Supplies",
                    "sortIndex": "15",
                    "visibleOnHeader": true,
                    "visibleOnSidebar": true,
                    "__typename": "ProductCategory"
                },
                "productCount": 765,
                "subcategories": [
                    {
                        "subcategory": {
                            "id": "385187909",
                            "name": "Wipes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 5,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187293",
                            "name": "Containers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 51,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187260",
                            "name": "Environmentally Friendly",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 167,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187290",
                            "name": "Cups",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 42,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187469",
                            "name": "Food Safety",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 41,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187892",
                            "name": "Dispensers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 23,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187289",
                            "name": "Boxes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 37,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187292",
                            "name": "Food Wraps",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 41,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187388",
                            "name": "Lids",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 34,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187291",
                            "name": "Bags",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 49,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187390",
                            "name": "Cutlery",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 69,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187908",
                            "name": "Filters",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 7,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187686",
                            "name": "Food Pans",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187547",
                            "name": "Napkins",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 35,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385219491",
                            "name": "Scouring Pads",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 12,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187586",
                            "name": "Guest Checks",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 10,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187904",
                            "name": "Doilies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187386",
                            "name": "Trays",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 31,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187389",
                            "name": "Straws",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 12,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187903",
                            "name": "Skewers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187910",
                            "name": "Twine",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187471",
                            "name": "Platters",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187911",
                            "name": "Tablecover",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187893",
                            "name": "Picks",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 11,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187470",
                            "name": "Java Jackets",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187589",
                            "name": "Stir Sticks",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154069016",
                            "name": "Apparel",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187543",
                            "name": "Fuel",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 21,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187598",
                            "name": "Bowls",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187549",
                            "name": "Beverage Carriers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187392",
                            "name": "Pan Liners",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 9,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187585",
                            "name": "Corrugated Circles",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187906",
                            "name": "Placemats",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385188349",
                            "name": "Grill Scrapers",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187387",
                            "name": "Plates",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 7,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187874",
                            "name": "Grill Pads",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 7,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187950",
                            "name": "Masking Tape",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 4,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "154068263",
                            "name": "Back Office Supplies",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 1,
                        "__typename": "subcategoryOption"
                    },
                    {
                        "subcategory": {
                            "id": "385187550",
                            "name": "Towelettes",
                            "sortIndex": 0,
                            "__typename": "ProductSubcategory"
                        },
                        "productCount": 2,
                        "__typename": "subcategoryOption"
                    }
                ],
                "__typename": "categoryOption"
            }
        ]
    }
}
	''')

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
		'url': 'https://app.cutanddry.com/catalog/primizieny?verifiedVendorId=50714839&categoryId=1&page=1',
		'search_term': 'Spices',
		'attempts': '40',
	}

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}

	def get_category_ids(self):
		return self.CATEGORY_IDS

	@staticmethod
	def build_catalog_url(category_id=None, category_name=None, subcategory_id=None, subcategory_name=None,
	                    page=1, vendor_name="BiRite Foodservice Distributors",
	                    vendor_id=247696227, verified_vendor_id=120984264):
		"""
		Builds the catalog URL with the specified parameters.

		Args:
			category_id (str, optional): The ID of the category to filter by
			category_name (str, optional): The name of the category (will be URL encoded)
			subcategory_id (str, optional): The ID of the subcategory to filter by
			subcategory_name (str, optional): The name of the subcategory (will be URL encoded)
			page (int, optional): The page number to display. Defaults to 1.
			vendor_name (str, optional): The name of the vendor. Will be URL encoded.
			                           Defaults to "BiRite Foodservice Distributors".
			vendor_id (int, optional): The vendor ID. Defaults to 247696227.
			verified_vendor_id (int, optional): The verified vendor ID. Defaults to 120984264.

		Returns:
			str: The complete catalog URL with all parameters
		"""
		from urllib.parse import quote_plus

		print(f"Category Name : {category_name}")
		print(f"Sub Category Name : {subcategory_name}")

		# URL encode the vendor name and other string parameters
		encoded_vendor_name = quote_plus(vendor_name)

		base_url = f"https://app.cutanddry.com/catalog/{encoded_vendor_name}/{vendor_id}"
		params = {
			'verifiedVendorId': str(verified_vendor_id),
		}

		# Add category parameters if provided
		if category_id:
			params['categoryId'] = str(category_id)
		if category_name:
			params['categoryName'] = str(category_name)
		if subcategory_id:
			params['subcategoryId'] = str(subcategory_id)
		if subcategory_name:
			# Replace spaces with + as shown in the example URL
			params['subcategoryName'] = str(subcategory_name).replace(' ', '+')
		if page > 1:
			params['page'] = str(page)

		# Convert params to URL query string
		query_string = '&'.join(f"{k}={v}" for k, v in params.items())
		return f"{base_url}?{query_string}"

	@staticmethod
	def build_product_url(product_id=None, vendor_name="BiRite Foodservice Distributors", vendor_id=247696227, verified_vendor_id=120984264):
		"""
		Builds the catalog URL with the specified parameters.

		Args:
			product_id (str, optional): The ID of the category to filter by
			vendor_id (int, optional): The vendor ID. Defaults to 247696227.
			verified_vendor_id (int, optional): The verified vendor ID. Defaults to 120984264.

		Returns:
			str: The complete catalog URL with all parameters
		"""
		# https://app.cutanddry.com/catalog/BiRite%20Foodservice%20Distributors/product/161881595?srcPge=Public%20Catalog&srcLoc=General&verifiedVendorId=120984264
		from urllib.parse import quote_plus

		# URL encode the vendor name and other string parameters
		encoded_vendor_name = quote(vendor_name)

		base_url = f"https://app.cutanddry.com/catalog/{encoded_vendor_name}/product/{product_id}?srcPge=Public%20Catalog&srcLoc=General&verifiedVendorId={verified_vendor_id}"
		params = {
			'verifiedVendorId': str(verified_vendor_id),
		}

		return f"{base_url}"

	def get_categories(self):
		"""
		Returns a list of category dictionaries from the CATEGORIES data.

		Returns:
			list: A list of dictionaries, each containing 'id' and 'name' of a category
		"""
		category_options = self.CATEGORIES.get('data', {}).get('catalogCategoryOptions', [])
		return [
			{'id': option['category']['id'], 'name': option['category']['name']}
			for option in category_options
			if option.get('category', {}).get('id') and option.get('category', {}).get('name')
		]

	def get_taxonomy(self):
		categories = self.CATEGORIES.get('data', {}).get('catalogCategoryOptions', [])
		print(f"Categories: {categories}")
		return categories

	def get_category_names(self):
		return self.CATEGORY_NAMES

	def get_category_urls(self):
		return self.CATEGORY_URLS

	def clean_url_file(self, input_file=None, output_file=None):
		"""
		Clean the URL file by removing rows that don't have a value in the 'name' column.

		Args:
			input_file (str, optional): Path to the input CSV file. If None, uses the URL output file from options.
			output_file (str, optional): Path to save the cleaned CSV. If None, overwrites the input file.

		Returns:
			tuple: (success: bool, message: str) indicating the result of the operation
		"""
		try:
			# Get input file path
			if input_file is None:
				input_file = self.get_data_file_path(self.options.get('home_directory', self.DEFAULT_DIRECTORY))

			# Set default output file to input file if not specified
			if output_file is None:
				output_file = input_file

			# Read the CSV file
			# df = pd.read_csv(csv_file, encoding=ENCODING)
			df = pd.read_csv(input_file, dtype=str, keep_default_na=False, encoding=self.ENCODING, on_bad_lines='skip')

			# Check if 'name' column exists
			if 'name' not in df.columns:
				return False, f"Error: 'name' column not found in {input_file}"

			# Count rows before cleaning
			initial_count = len(df)

			# Remove rows where name is empty or whitespace
			clean_df = df[df['name'].str.strip().astype(bool)]

			# Count rows after cleaning
			final_count = len(clean_df)
			removed_count = initial_count - final_count

			# Save the cleaned data
			clean_df.to_csv(output_file, index=False)

			# If we removed any rows, return success with count
			if removed_count > 0:
				return True, f"Removed {removed_count} rows without names. {final_count} rows remaining in {output_file}"
			else:
				return True, "No rows without names found. File was not modified."

		except Exception as e:
			return False, f"Error cleaning URL file: {str(e)}"

	def process_subcategories(self):
		# Build a list of product URLs
		urls = []
		subcategories = ''
		category_name = ''

		sub_categories = self.wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.card__wrap'))
		)
		print(f"Found Category Wrapper: {len(sub_categories)}")
		category_url_part = str(self.options['category_url_part']) + "?expand"
		print(f"category_url_part: {category_url_part}")
		for request in self.driver.requests:
			#
			# https://www.chefswarehouse.com/products/meat-and-poultry/?expand=*&currentPageUrl=%252Fproducts%252Fmeat-and-poultry%252F&tz=America%252FNew_York&t=1753496336262
			if request.response and category_url_part in request.url:  # Filter for API requests
				print(f"URL: {request.url}")
				print(f"Status Code: {request.response.status_code}")
				print(f"Content Type: {request.response.headers.get('Content-Type')}")

				# Decode the response body (it's bytes by default)
				try:
					# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
					body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

					# If the body is JSON, parse it
					if 'application/json' in request.response.headers.get('Content-Type', ''):
						data = json.loads(body)
						# {
						# 	"name": "Foie Gras",
						# 	"imageUrl": "/siteassets/foie-gras_330.png",
						# 	"url": "/products/meat-and-poultry/foie-gras/"
						# },
						category_name = data.get('name', '')
						view_model = data.get('viewModel', {})
						subcategories = view_model.get('subCategories', [])
						urls = [category['url'] for category in subcategories]
						print(f"==== sub categories: {subcategories}")
					else:
						print(f"Response Body was not JSON:")

				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding response body: {e}")
		print(f"========= Number of sub categories: {len(urls)}")

		del self.driver.requests
		return subcategories, category_name

	def scraping_setup(self):
		"""Scrape products from the website"""
		print("scraping_setup()")
		return

	# ************************************************************************

	# 	Product Scraping Functions
	# ************************************************************************

	def get_first_image_url(self, data):
		"""
		Extract the first available image URL from the product API response.

		Args:
			data (dict): The parsed JSON response from the API

		Returns:
			str: URL of the first available image, or None if no image found
		"""
		print("get_first_image_url()")
		image_url = ''
		try:
			# product-viewer-image
			image_url = data.get('images', {})[0].get('url', '')
		except Exception as e:
			print(f"Error extracting image from page: {type(e)}")

		return image_url

	def get_product_data(self, data, row_spec):
		print("processing product data from response...")
		# print(data)
		if data:
			try:
				row_spec["extra_data_1"] = json.dumps(data)
				data = data.get('data',{}).get('universalProduct',{})
				row_spec["sku"] = data.get("itemCode", "")
				row_spec["name"] = data.get("name", "")
				row_spec["brand"] = data.get("brandDetails", {}).get("name", "")

				row_spec["pack_size"] = data.get('packSize', {})
				row_spec["gtin"] = data.get('gtin', {})

				row_spec["image"] = self.get_first_image_url(data)
				# row_spec = self.get_classification(data, row_spec)
				row_spec = self.get_description(data, row_spec)
				row_spec = self.get_manufacturer(data, row_spec)
				# row_spec = self.get_additional_info(data, row_spec)
				row_spec["extra_data_1"] = json.dumps(data)

			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing get_product_data Complete...")
		return row_spec

	def get_description(self, data, row_spec):
		print("get_description()")
		description = ''
		# product-info-about-container

		try:
			description = data.get('description', {}).get('productDescription', '')
			if description:
				row_spec["description"] = description
		except Exception as e:
			print(f"⛔️️ Error processing product producer description: {type(e)}")

		try:
			features = data.get('description', {}).get('featuresAndBenefits', '')
			if features:
				row_spec["features"] = features
		except Exception as e:
			print(f"⛔️️ Error processing product description: {type(e)}")
		print("processing product description Complete...")
		return row_spec

	def get_manufacturer(self, data, row_spec):
		print("get_manufacturer()")
		try:
			specifications = data.get('specifications', [])
			# Find the specification with displayName "Manufacturer Name"
			manufacturer_spec = next(
				(spec for spec in specifications 
				 if isinstance(spec, dict) and spec.get('displayName') == 'Manufacturer Name'),
				None
			)
			
			if manufacturer_spec and 'value' in manufacturer_spec:
				row_spec['manufacturer_name'] = manufacturer_spec['value']
				print(f"Found manufacturer: {manufacturer_spec['value']}")
			else:
				print("⚠️ Manufacturer name not found in specifications")

			manufacturer_spec = next(
				(spec for spec in specifications
				 if isinstance(spec, dict) and spec.get('displayName') == 'Manufacturer Product Code'),
				None
			)

			if manufacturer_spec and 'value' in manufacturer_spec:
				row_spec['manufacturer_sku'] = manufacturer_spec['value']
				print(f"Found manufacturer id: {manufacturer_spec['value']}")
			else:
				print("⚠️ Manufacturer name not found in specifications")

		except Exception as e:
			print(f"⛔️ Error processing manufacturer information: {type(e).__name__} - {str(e)}")
			
		print("Processing manufacturer information complete...")
		return row_spec

	def create_interceptor(self, max_api_products=200, page=1):
		def interceptor(request):
			# southernglazerswinespiritsproduction78xh7hnm.org.coveo.com/rest/search/v2
			if request.method == 'POST' and self.GRAPHQL_API_FILTER in request.url:
				print(f"👽👽👽Intercepting request: {request.url}")
				# Get the current POST data
				current_data = request.body.decode('utf-8')
				# print(f"Original POST data: {current_data}")

				try:
					payload = json.loads(current_data)

					if payload.get('operationName', '') == self.SEARCH_API_OPERATION:
						print(self.SEARCH_API_OPERATION)
						# search = payload.get('search', {})
						print(f"Incoming number of results: {payload.get('variables', {})['limit']}")
						payload.get('variables', {})['limit'] = max_api_products
						payload.get('variables', {})['offset'] = (page - 1) * max_api_products
						request.body = json.dumps(payload).encode('utf-8')
						# Update the Content-Length header to reflect the new body size
						del request.headers['Content-Length']
						request.headers['Content-Length'] = str(len(request.body))
						print(f"Modified POST data: {payload.get('variables', {})['limit']}")
						print(f"Modified POST data: {payload.get('variables', {})['offset']}")
				except json.JSONDecodeError:
					# Handle cases where the body is not JSON
					print("Request body is not JSON. Cannot modify in this example.")

		return interceptor

	def build_products_list(self):
		"""Scrape products from the website"""
		print(f"build_products_list()")
		html = ''
		html_table = ''
		all_urls = []
		categories = []
		chosen_category = int(self.options.get('chosen_category', 0))
		test_categories = self.options.get('test_categories', 100)
		test_products = self.options.get('test_products', 0)
		category_count = 0
		if int(self.options['chosen_category']) == 0:
			categories = self.get_taxonomy()
			print(f"All Categories ")
		else:
			for category in self.get_taxonomy():
				print(f"category : {category.get('name', '')}")
				if int(category.get('category', {}).get('id', '')) == chosen_category:
					categories = [category]  # Only process the chosen category
					print(f"Category found : {categories}")
					break
		del self.driver.requests
		for category in categories:
			print(f"category : {category}")
			category_count = category_count + 1
			if category_count > test_categories:
				break
			for  subcategory in category.get('subcategories', []):
				print(f"subcategory : {subcategory}")
				subcat = subcategory.get('subcategory', {})
				subcat_name = subcat.get('name', '')

				url = self.build_catalog_url(category_id=category.get('category', {})['id'],category_name=category.get('category', {})['name'], subcategory_id=subcat['id'], subcategory_name=subcat['name'])
				# See if we need to skip this category because it is not the direct category
				if len(self.options['direct_category_to_process']) > 0 and self.options[
					'direct_category_to_process'] != url:
					print(f"Skipping category {category['name']} as it is not the direct category to process")
					continue

				still_looking = True
				page = 0
				while still_looking and page < self.options['max_products']:
					page = page + 1
					if page * self.options['max_products'] > test_products:
						# We have reached the maximum number of products we
						break
					category_name = category.get('category', {})['name']
					self.options['url_output_file'] = category_name.lower() + "_product_urls.csv"

					url = self.build_catalog_url(category_id=category.get('category', {})['id'],
					                             category_name=category_name,
					                             subcategory_id=subcat['id'], subcategory_name=subcat['name'], page=page)
					print(f"Loading page...{url}")
					del self.driver.request_interceptor
					self.driver.request_interceptor = self.create_interceptor(self.options['max_products'], page=page)
					del self.driver.requests
					self.driver.get(url)
					print(f"URL Loaded")
					print(f"Page : {page}")
					filter_criteria = "/api/1431646/store/"
					try:
						# Wait for the request we think is one of the last
						request = self.driver.wait_for_request(filter_criteria, 50)
					except Exception as e:
						print(f"⛔️⛔️⛔️Request failed: {e}")
						html += f"<h2>{category_name} -> {subcat_name} -> Page {page}</h2>"
						html += "<div>TIme Out </div>"
						break

					print("Processing Requests")
					filter_criteria = self.GRAPHQL_API_FILTER
					for request in self.driver.requests:
						if request.response and filter_criteria in request.url:  # Filter for API requests
							current_data = request.body.decode('utf-8')
							# print(f"current_data: {current_data}")
							payload = json.loads(current_data)
							if payload.get('operationName','') == self.SEARCH_API_OPERATION:
								print(f"{self.SEARCH_API_OPERATION} found")
								print(f"URL: {request.url}")
								print(f"Status Code: {request.response.status_code}")
								print(f"Content Type: {request.response.headers.get('Content-Type')}")
								try:
									body = decode(request.response.body,
								              request.response.headers.get('Content-Encoding', 'identity'))

									# If the body is JSON, parse it
									if 'application/json' in request.response.headers.get('Content-Type', ''):
										data = json.loads(body)
										# https://app.salsify.com/catalogs/a256467d-fc0a-4bce-8971-1d14466fd28f/products/9258080
										if 'canonicalProducts' in data.get('data', {}).get('catalogProductsRootQuery', {}):
											print(f"Response products: {'canonicalProducts' in data} ")
											detail_urls = [
												self.build_product_url(product.get('id', ''))
												for product in data.get('data', {}).get('catalogProductsRootQuery', {}).get('canonicalProducts', [])]
											print(f"== Number of products: {len(detail_urls)}")
											all_urls.extend(detail_urls)
											html += f"<h2>{category_name} -> {subcat_name} -> page {page}</h2>"
											html += "<div>Products found: " + str(len(detail_urls)) + "</div>"
											self.save_urls_to_csv(detail_urls, category_name, subcat_name)
											print(f"=== Number of products: {len(detail_urls)}")

											if len(detail_urls) < self.options['max_products']:
												still_looking = False
										else:
											print(f"Response products missing: {'canonicalProducts' in data} ")
											# print(f"data: {data} ")

									else:
										print(f"Response Body (Text): ")
										print(f"Response not JSON  ")

								except Exception as e:
									print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

						# del self.driver.request_interceptor
						del self.driver.requests

				time.sleep(2)

		html_table += "</tbody></table>"

		html += f"<h2>Total products found: {len(all_urls)}</h2>"
		html += html_table
		print(f"Total products found: {len(all_urls)}")
		return html

	def get_product_details(self, url, row_spec=None):
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print("processing product detail page")
		print(f"Loading page...{url}")

		data = ''
		# We used an id to identify the product
		row_spec['id'] = row_spec['sku']
		del self.driver.requests
		self.driver.get(url)
		print(f"Sent Request")
		try:
			request = self.driver.wait_for_request(self.GRAPHQL_API_FILTER)
			first_found = False
			second_found = False
			attempts = 0

			while (not first_found or not second_found) and attempts < self.options['attempts']:
				time.sleep(1)
				attempts += 1
				print(f"attempt: {attempts}")
				for request in self.driver.requests:
					if request.response and self.GRAPHQL_API_FILTER in request.url:  # Filter for API requests
						# print(f"URL: {request.url}")
						# print(f"Status Code: {request.response.status_code}")
						# print(f"Content Type: {request.response.headers.get('Content-Type')}")
						# UniversalProductForPDP
						# Decode the response body (it's bytes by default)
						current_data = request.body.decode('utf-8')
						payload = json.loads(current_data)
						print(f"Payload Method: {payload.get('operationName', '')}")
						if payload.get('operationName', '') == self.PRODUCT_API_OPERATION and not first_found:
							first_found = True
							try:
								body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

								# If the body is JSON, parse it
								if 'application/json' in request.response.headers.get('Content-Type', ''):
									data = json.loads(body)
								else:
									print(f"Response Body (Text): {body}")

							except Exception as e:
								print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

							# These use the data if available, then try to scrape from the page
							row_spec = self.get_product_data(data, row_spec)
						elif payload.get('operationName', '') == 'canonicalProductQuery' and not second_found:
							second_found = True
							try:
								# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
								body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

								# If the body is JSON, parse it
								if 'application/json' in request.response.headers.get('Content-Type', ''):
									data = json.loads(body)
								else:
									print(f"Response Body (Text): {body}")

							except Exception as e:
								print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")
							row_spec['extra_data_2'] = json.dumps(data)
						# else:
						# 	# self.driver.delete_request(request.id)
						# 	print(f"attempts: {attempts}")
			if not first_found:
				raise ProductNotFound
		except Exception as e:
			print(f"⛔️⛔️⛔️Error waiting for request: {e}")

		return row_spec

	def build_categories_list(self):
		# Run on all to get a category list then copy the list to CATEGORIES
		url = "https://app.cutanddry.com/catalog/primizieny?verifiedVendorId=50714839&categoryId=1&page=1"
		categories = []
		print(f"Loading page...{url}")
		del self.driver.requests
		self.driver.get(url)

		found = self.wait.until(
			EC.text_to_be_present_in_element((By.TAG_NAME, "div"), "All Items")
		)
		data = ''
		for request in self.driver.requests:
			if request.response and self.GRAPHQL_API_FILTER in request.url:  # Filter for API requests
				try:
					current_data = request.body.decode('utf-8')
					payload = json.loads(current_data)
					print(f"Found response :")
					# print(f"Response Body (Text): {payload}")
					if payload['operationName'] == 'CatalogCategoryOptionsQuery':
						print("CatalogCategoryOptionsQuery")
						body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

						# If the body is JSON, parse it
						if 'application/json' in request.response.headers.get('Content-Type', ''):
							data = json.loads(body)
						else:
							print(f"Response not JSON :")
				except Exception as e:
					print(f"⛔️⛔️⛔️Error decoding search response body: {e}")

		print(f"")
		print(f"categories : {json.dumps(data)}")
		del self.driver.requests

		return f"<div>{json.dumps(data)}</div>"

	def get_navigation_categories(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
		"""
		Extract product categories from search response data.

		Args:
			data: Dictionary containing the search response data (already parsed JSON)

		Returns:
			List of dictionaries containing category information with 'id' and 'name' keys
		"""
		print(f"data : {data}")
		if not isinstance(data, dict) or 'catalogCategoryOptions' not in data:
			return []

		# Find the category facet
		category_facets = []
		for category in data['catalogCategoryOptions']:
			category_facets = [
				{
					'name': item.get('category', {})['name'],
					'count': str(item['productCount']),
					"number": str(index + 1),
				}
				for index, item in category['values']
			]
			break
		print(f"category_facets : {category_facets}")
		return category_facets
