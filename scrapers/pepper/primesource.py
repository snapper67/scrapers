from scrapers.pepper.pepper import PepperScraper

class PrimeSourceScraper(PepperScraper):
    # 1345/edit_note/1732/
    CRM_ID = 1345
    CRM_NOTE_ID = 1732
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = 'Ready'

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/prime_source'
    INPUT_FILE = 'prime_source.json'
    OUTPUT_FILE = 'prime_source_data.csv'

    BASE_URL = 'https://primesourcefoods.pepr.app/'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Prime Source Foods'

    def __init__(self, options=None):
        super().__init__(options)

