from scrapers.pepper.pepper import PepperScraper

class GetFreshProduceScraper(PepperScraper):
    CRM_ID = 119
    CRM_NOTE_ID = 1699
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = 'Ready'

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/get_fresh_produce'
    INPUT_FILE = 'get_fresh_produce.json'
    OUTPUT_FILE = 'get_fresh_produce_data.csv'

    BASE_URL = 'https://www.getfreshproduce.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Get Fresh Produce'

    def __init__(self, options=None):
        super().__init__(options)

