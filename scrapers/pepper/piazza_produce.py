from scrapers.pepper.pepper import PepperScraper

class PiazzaProduceScraper(PepperScraper):
    # 886/edit_note/1700/
    CRM_ID = 886
    CRM_NOTE_ID = 1700
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = 'Ready'

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/piazza'
    INPUT_FILE = 'piazza.json'
    OUTPUT_FILE = 'piazza_data.csv'

    BASE_URL = 'https://piazzaproduce.pepr.app/'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Piazza Produce'

    def __init__(self, options=None):
        super().__init__(options)
