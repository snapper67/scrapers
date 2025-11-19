from scrapers.pepper.pepper import PepperScraper

class SchenckFoodsScraper(PepperScraper):
    # 3200/edit_note/1540/
    CRM_ID = 3200
    CRM_NOTE_ID = 1540
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = ''

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/schenck_foods'
    INPUT_FILE = 'schenck_foods.json'
    OUTPUT_FILE = 'schenck_foods_data.csv'

    BASE_URL = 'https://www.schenkfoods.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Schenck Foods'

    def __init__(self, options=None):
        super().__init__(options)


