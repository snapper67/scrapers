from scrapers.pepper.pepper import PepperScraper

class GravesFoodsScraper(PepperScraper):
    # 3537/edit_note/1734/
    CRM_ID = 1866
    CRM_NOTE_ID = 1734
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = 'Ready'

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/graves'
    INPUT_FILE = 'graves.json'
    OUTPUT_FILE = 'graves_data.csv'

    BASE_URL = 'https://primesourcefoods.pepr.app/'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Graves Foods'

    def __init__(self, options=None):
        super().__init__(options)

