import json
from .dry import CutScraper


class TheFishGuysScraper(CutScraper):
    """Scraper for The Fish Guys on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/thefishguys/'

    # Values to change
    BASE_URL = "https://thefishguys.cutanddry.com/catalog/thefishguys?verifiedVendorId=103097510&categoryId=1&page=1"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://thefishguys.cutanddry.com"
    VENDOR_URL_NAME = 'thefishguys'
    VERIFIED_VENDOR_ID = 103097510

    # This the name of the vendor
    VENDOR_NAME = "The Fish Guys"

    CATEGORIES = json.loads('''
    {
      "data": {
        "catalogCategoryOptions": [
          {
            "category": {
              "id": "1",
              "baseName": "all-items",
              "name": "All Items",
              "visibleOnHeader": true,
              "visibleOnSidebar": true,
              "__typename": "ProductCategory"
            },
            "productCount": 0,
            "subcategories": [],
            "__typename": "categoryOption"
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