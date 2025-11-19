from scrapers.pepper.pepper import PepperScraper

class FlanaganFoodserviceScraper(PepperScraper):
    # 1316/edit_note/1507/
    CRM_ID = 1316
    CRM_NOTE_ID = 1507
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = ''

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/flanagan_foodservice'
    INPUT_FILE = 'flanagan_foodservice.json'
    OUTPUT_FILE = 'flanagan_foodservice_data.csv'

    BASE_URL = 'https://www.flanaganfoodservice.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Flanagan Foodservice'

    def __init__(self, options=None):
        super().__init__(options)

