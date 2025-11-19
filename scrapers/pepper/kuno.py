from scrapers.pepper.pepper import PepperScraper

class KunoScraper(PepperScraper):
    # 2652/edit_note/1736/
    CRM_ID = 2652
    CRM_NOTE_ID = 1736
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = 'Ready'

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/kuno'
    INPUT_FILE = 'kuno.json'
    OUTPUT_FILE = 'kuno_data.csv'

    BASE_URL = 'https://kunafoodservice.pepr.app/'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Kuno'

    def __init__(self, options=None):
        super().__init__(options)

