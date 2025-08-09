
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

from scrapers.cut import CutScraper
from scrapers.scraper import Scraper, ProductNotFound


class PrimizieScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/primizie'

	# Values to change
	BASE_URL = "https://app.cutanddry.com/catalog/primizieny?verifiedVendorId=50714839&categoryId=1&page=1"
	CATEGORIES = json.loads('''{
	    "data": {
	        "catalogCategoryOptions": [
	            {
	                "category": {
	                    "id": "52280800",
	                    "baseName": "appetizers & entrees",
	                    "examplePictureUrl": null,
	                    "iconAltUrl": null,
	                    "iconUrl": null,
	                    "name": "Appetizers & Entrees",
	                    "sortIndex": "0",
	                    "visibleOnHeader": true,
	                    "visibleOnSidebar": true,
	                    "__typename": "ProductCategory"
	                },
	                "productCount": 182,
	                "subcategories": [
	                    {
	                        "subcategory": {
	                            "id": "321949156",
	                            "name": "Pizzas & Crusts",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 12,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "311212170",
	                            "name": "Vegetables & Sides",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 60,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "231305258",
	                            "name": "Meat & Charcuterie",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 56,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "76655796",
	                            "name": "Ready Meals",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 33,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "212025720",
	                            "name": "Savory Bites",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 8,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "321949062",
	                            "name": "Beans_ Rice & Mushrooms",
	                            "sortIndex": null,
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
	                    "id": "279104564",
	                    "baseName": "bakery",
	                    "examplePictureUrl": null,
	                    "iconAltUrl": null,
	                    "iconUrl": null,
	                    "name": "Bakery",
	                    "sortIndex": "1",
	                    "visibleOnHeader": true,
	                    "visibleOnSidebar": true,
	                    "__typename": "ProductCategory"
	                },
	                "productCount": 71,
	                "subcategories": [
	                    {
	                        "subcategory": {
	                            "id": "76655800",
	                            "name": "Ready to Serve",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 34,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "52280805",
	                            "name": "Bread & Dough",
	                            "sortIndex": 0,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 8,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "211948250",
	                            "name": "Pastries & Croissants",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 29,
	                        "__typename": "subcategoryOption"
	                    }
	                ],
	                "__typename": "categoryOption"
	            },
	            {
	                "category": {
	                    "id": "278666567",
	                    "baseName": "butter cheese & dairy",
	                    "examplePictureUrl": null,
	                    "iconAltUrl": null,
	                    "iconUrl": null,
	                    "name": "Butter Cheese & Dairy",
	                    "sortIndex": "6",
	                    "visibleOnHeader": true,
	                    "visibleOnSidebar": true,
	                    "__typename": "ProductCategory"
	                },
	                "productCount": 17,
	                "subcategories": [
	                    {
	                        "subcategory": {
	                            "id": "278746261",
	                            "name": "Butter & Dairy",
	                            "sortIndex": null,
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
	                    "id": "52280789",
	                    "baseName": "desserts",
	                    "examplePictureUrl": null,
	                    "iconAltUrl": null,
	                    "iconUrl": null,
	                    "name": "Desserts",
	                    "sortIndex": "7",
	                    "visibleOnHeader": true,
	                    "visibleOnSidebar": true,
	                    "__typename": "ProductCategory"
	                },
	                "productCount": 94,
	                "subcategories": [
	                    {
	                        "subcategory": {
	                            "id": "278850605",
	                            "name": "Individual Desserts",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 22,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "76655841",
	                            "name": "Cookies",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 6,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "212025718",
	                            "name": "Sweet Bites & Petits Fours",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 17,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "211948263",
	                            "name": "Pre-cut Cakes",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 19,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "76655797",
	                            "name": "Glass Desserts",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 13,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "76655794",
	                            "name": "Gelato & Sorbetto",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 11,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "76655789",
	                            "name": "Whole Cakes & Strip Cakes",
	                            "sortIndex": null,
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
	                    "id": "52280816",
	                    "baseName": "pasta & ravioli",
	                    "examplePictureUrl": null,
	                    "iconAltUrl": null,
	                    "iconUrl": null,
	                    "name": "Pasta & Ravioli",
	                    "sortIndex": "12",
	                    "visibleOnHeader": true,
	                    "visibleOnSidebar": true,
	                    "__typename": "ProductCategory"
	                },
	                "productCount": 4,
	                "subcategories": [
	                    {
	                        "subcategory": {
	                            "id": "211770752",
	                            "name": "Frozen Pasta",
	                            "sortIndex": null,
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
	                    "id": "212025709",
	                    "baseName": "savory ingredients",
	                    "examplePictureUrl": null,
	                    "iconAltUrl": null,
	                    "iconUrl": null,
	                    "name": "Savory Ingredients",
	                    "sortIndex": "13",
	                    "visibleOnHeader": true,
	                    "visibleOnSidebar": true,
	                    "__typename": "ProductCategory"
	                },
	                "productCount": 33,
	                "subcategories": [
	                    {
	                        "subcategory": {
	                            "id": "309694234",
	                            "name": "Neutral Tart Shells",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 12,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "321949781",
	                            "name": "Oils & Vinegars",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 7,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "321949802",
	                            "name": "Bases & Sauces",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 5,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "76655799",
	                            "name": "Condiments",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 9,
	                        "__typename": "subcategoryOption"
	                    }
	                ],
	                "__typename": "categoryOption"
	            },
	            {
	                "category": {
	                    "id": "212025711",
	                    "baseName": "sweet ingredients",
	                    "examplePictureUrl": null,
	                    "iconAltUrl": null,
	                    "iconUrl": null,
	                    "name": "Sweet Ingredients",
	                    "sortIndex": "15",
	                    "visibleOnHeader": true,
	                    "visibleOnSidebar": true,
	                    "__typename": "ProductCategory"
	                },
	                "productCount": 129,
	                "subcategories": [
	                    {
	                        "subcategory": {
	                            "id": "311178927",
	                            "name": "Fruit Purees",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 55,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "321948523",
	                            "name": "Jams & Jellies",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 16,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "212025726",
	                            "name": "Toppings Fillings & Sugars",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 17,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "76655781",
	                            "name": "Individual Jams & Jellies",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 14,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "321948701",
	                            "name": "Frozen Fruit Jug",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 10,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "321948630",
	                            "name": "Frozen Fruit",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 13,
	                        "__typename": "subcategoryOption"
	                    },
	                    {
	                        "subcategory": {
	                            "id": "76655793",
	                            "name": "Sweet Tart Shells",
	                            "sortIndex": null,
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
	                    "id": "357480535",
	                    "baseName": "meat",
	                    "examplePictureUrl": null,
	                    "iconAltUrl": null,
	                    "iconUrl": null,
	                    "name": "Meat",
	                    "sortIndex": "17",
	                    "visibleOnHeader": true,
	                    "visibleOnSidebar": true,
	                    "__typename": "ProductCategory"
	                },
	                "productCount": 1,
	                "subcategories": [
	                    {
	                        "subcategory": {
	                            "id": "446028798",
	                            "name": "Processed Meat",
	                            "sortIndex": null,
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
	                    "id": "493512795",
	                    "baseName": "iqf vegetables",
	                    "examplePictureUrl": null,
	                    "iconAltUrl": null,
	                    "iconUrl": null,
	                    "name": "IQF Vegetables",
	                    "sortIndex": "22",
	                    "visibleOnHeader": true,
	                    "visibleOnSidebar": true,
	                    "__typename": "ProductCategory"
	                },
	                "productCount": 1,
	                "subcategories": [
	                    {
	                        "subcategory": {
	                            "id": "568284112",
	                            "name": "Caribean Vegetables",
	                            "sortIndex": null,
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
	                    "id": "518514570",
	                    "baseName": "bread_ croissants & danishes",
	                    "examplePictureUrl": null,
	                    "iconAltUrl": null,
	                    "iconUrl": null,
	                    "name": "Bread_ Croissants & Danishes",
	                    "sortIndex": "23",
	                    "visibleOnHeader": true,
	                    "visibleOnSidebar": true,
	                    "__typename": "ProductCategory"
	                },
	                "productCount": 1,
	                "subcategories": [
	                    {
	                        "subcategory": {
	                            "id": "518514571",
	                            "name": "Croissants and Danishes",
	                            "sortIndex": null,
	                            "__typename": "ProductSubcategory"
	                        },
	                        "productCount": 1,
	                        "__typename": "subcategoryOption"
	                    }
	                ],
	                "__typename": "categoryOption"
	            }
	        ]
	    }
	}
		''')

	VENDOR_NAME = 'Primizie NY'
	VENDOR_URL_NAME = 'primizieny'
	VENDOR_ID = 247696227
	VERIFIED_VENDOR_ID = 120984264

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

