from scrapers.pepper.pepper import PepperScraper

class CiboScraper(PepperScraper):
    # 3425/edit_note/1650/
    CRM_ID = 3425
    CRM_NOTE_ID = 1650
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = ''

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/cibo'
    INPUT_FILE = 'cibo.json'
    OUTPUT_FILE = 'cibo_data.csv'

    BASE_URL = 'https://www.cibo.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Cibo'

    def __init__(self, options=None):
        super().__init__(options)
