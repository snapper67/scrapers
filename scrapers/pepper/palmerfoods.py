from scrapers.pepper.pepper import PepperScraper

class PalmerFoodsScraper(PepperScraper):
    # 1978/edit_note/1530/
    CRM_ID = 1978
    CRM_NOTE_ID = 1530
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = ''

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/palmer_foods'
    INPUT_FILE = 'palmer_foods.json'
    OUTPUT_FILE = 'palmer_foods_data.csv'

    BASE_URL = 'https://www.palmerfoods.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Palmer Foods'

    def __init__(self, options=None):
        super().__init__(options)


