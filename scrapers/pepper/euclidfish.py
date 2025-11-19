from scrapers.pepper.pepper import PepperScraper

class EuclidFishScraper(PepperScraper):
    # 1976/edit_note/1528/
    CRM_ID = 1976
    CRM_NOTE_ID = 1528
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = ''

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/euclid_fish'
    INPUT_FILE = 'euclid_fish.json'
    OUTPUT_FILE = 'euclid_fish_data.csv'

    BASE_URL = 'https://www.euclidfish.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Euclid Fish'

    def __init__(self, options=None):
        super().__init__(options)

