
import json
from scrapers.cut.dry import CutScraper


class SandWScraper(CutScraper):

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/sandw/'

	# Values to change
	BASE_URL = "https://app.cutanddry.com/catalog/swfoods?verifiedVendorId=1862163&page=2&categoryId=1"
	CATEGORIES = json.loads('''{
  "data": {
    "catalogCategoryOptions": [
      {
        "category": {
          "id": "97261021",
          "baseName": "beverage",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Beverage.png",
          "name": "Beverage",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 307,
        "subcategories": [],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "97266943",
          "baseName": "dairy + eggs",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Dairy.png",
          "name": "Dairy + Eggs",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 486,
        "subcategories": [],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "97263354",
          "baseName": "dry goods",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/dry_goods.png",
          "name": "Dry Goods",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 185,
        "subcategories": [],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "97268157",
          "baseName": "furniture + equipment",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Furniture+%26+Equipment.png",
          "name": "Furniture + Equipment",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 135,
        "subcategories": [],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "97264166",
          "baseName": "grocery",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Grocery.png",
          "name": "Grocery",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 398,
        "subcategories": [],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "97267416",
          "baseName": "meat + game",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Meat.png",
          "name": "Meat + Game",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 600,
        "subcategories": [],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "97270043",
          "baseName": "operational supplies",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Operational+Supplies.png",
          "name": "Operational Supplies",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1506,
        "subcategories": [],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "97263642",
          "baseName": "poultry + fowl",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/paultry.png",
          "name": "Poultry + Fowl",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 243,
        "subcategories": [],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "97267693",
          "baseName": "prepared items",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Prepared+Item.png",
          "name": "Prepared Items",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1574,
        "subcategories": [],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "97266522",
          "baseName": "produce",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Produce.png",
          "name": "Produce",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 422,
        "subcategories": [],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "97263998",
          "baseName": "seafood",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Sea+food.png",
          "name": "Seafood",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 153,
        "subcategories": [],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "97264398",
          "baseName": "spices",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": "https://cut-dry-assets.s3.us-east-2.amazonaws.com/images/rosetta-category-images/Spices.png",
          "name": "Spices",
          "sortIndex": "1",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 196,
        "subcategories": [],
        "__typename": "categoryOption"
      },
      {
        "category": {
          "id": "4",
          "baseName": "uncategorised",
          "examplePictureUrl": null,
          "iconAltUrl": null,
          "iconUrl": null,
          "name": "Uncategorised",
          "sortIndex": "2",
          "visibleOnHeader": true,
          "visibleOnSidebar": true,
          "__typename": "ProductCategory"
        },
        "productCount": 1083,
        "subcategories": [],
        "__typename": "categoryOption"
      }
    ]
  }
}
		''')

	VENDOR_NAME = 'S & W Foods'
	VENDOR_URL_NAME = 'swfoods'
	VERIFIED_VENDOR_ID = 1862163

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY

