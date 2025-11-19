from scrapers.pepper.pepper import PepperScraper

class PerroneScraper(PepperScraper):
    # 1961/edit_note/1509/
    CRM_ID = 1961
    CRM_NOTE_ID = 1509
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = 'Ready'

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/perrone_and_sons'
    INPUT_FILE = 'perrone_and_sons.json'
    OUTPUT_FILE = 'perrone_and_sons_data.csv'

    BASE_URL = 'https://www.perroneandsons.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Perrone and Sons'

    def __init__(self, options=None):
        super().__init__(options)


