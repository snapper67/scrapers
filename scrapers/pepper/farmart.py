from scrapers.pepper.pepper import PepperScraper

class FarmArtScraper(PepperScraper):
    # 1975/edit_note/1526/
    CRM_ID = 1975
    CRM_NOTE_ID = 1526
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = ''

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/farm_art'
    INPUT_FILE = 'farm_art.json'
    OUTPUT_FILE = 'farmart_data.csv'

    BASE_URL = 'https://www.farmart.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'FarmArt'

    def __init__(self, options=None):
        super().__init__(options)

