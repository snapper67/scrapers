from scrapers.pepper.pepper import PepperScraper

class ExpressFoodsScraper(PepperScraper):
    # 3201/edit_note/1541/
    CRM_ID = 3201
    CRM_NOTE_ID = 1541
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = ''

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/express_foods'
    INPUT_FILE = 'express_foods.json'
    OUTPUT_FILE = 'express_foods_data.csv'

    BASE_URL = 'https://www.495expressfoods.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = '495 Express Foods'

    def __init__(self, options=None):
        super().__init__(options)

