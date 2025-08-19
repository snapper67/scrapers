import json
from .dry import CutScraper


class WoolcoFoodsScraper(CutScraper):
    """Scraper for Woolco Foods on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/woolcofoods/'

    # Values to change
    BASE_URL = "https://woolcofoods.cutanddry.com/catalog/woolcofoods?verifiedVendorId=1862249&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://woolcofoods.cutanddry.com"
    VENDOR_URL_NAME = 'woolcofoods'
    VERIFIED_VENDOR_ID = 1862249

    # This the name of the vendor
    VENDOR_NAME = "Woolco Foods"

    # Categories will be fetched dynamically
    CATEGORIES = json.loads('''
        {
  "data": {
    "catalogCategoryOptions": [
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "beverage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Beverage.png",
          "id": "97261021",
          "name": "Beverage",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 559,
        "subcategories": []
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dairy + eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Dairy.png",
          "id": "97266943",
          "name": "Dairy + Eggs",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 456,
        "subcategories": []
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "dry goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/dry_goods.png",
          "id": "97263354",
          "name": "Dry Goods",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 481,
        "subcategories": []
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "furniture + equipment",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Furniture+%26+Equipment.png",
          "id": "97268157",
          "name": "Furniture + Equipment",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 427,
        "subcategories": []
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "grocery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Grocery.png",
          "id": "97266353",
          "name": "Grocery",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 920,
        "subcategories": []
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "meat + game",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Meat.png",
          "id": "97267416",
          "name": "Meat + Game",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 417,
        "subcategories": []
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "operational supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Operational+Supplies.png",
          "id": "97270043",
          "name": "Operational Supplies",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 3367,
        "subcategories": []
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "poultry + fowl",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/paultry.png",
          "id": "97263642",
          "name": "Poultry + Fowl",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 166,
        "subcategories": []
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "prepared items",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Prepared+Item.png",
          "id": "97265044",
          "name": "Prepared Items",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 1288,
        "subcategories": []
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Produce.png",
          "id": "97266522",
          "name": "Produce",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 995,
        "subcategories": []
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Sea+food.png",
          "id": "97263998",
          "name": "Seafood",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 173,
        "subcategories": []
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "spices",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Spices.png",
          "id": "97264398",
          "name": "Spices",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 345,
        "subcategories": []
      },
      {
        "__typename": "categoryOption",
        "category": {
          "__typename": "ProductCategory",
          "baseName": "uncategorised",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "id": "4",
          "name": "Uncategorised",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true
        },
        "productCount": 46,
        "subcategories": []
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
