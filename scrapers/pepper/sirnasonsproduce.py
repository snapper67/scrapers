from scrapers.pepper.pepper import PepperScraper

class SirnaSonsProduceScraper(PepperScraper):
    #  1074/edit_note/1701/
    CRM_ID = 1074
    CRM_NOTE_ID = 1701
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = 'Ready'

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/sirnasonsproduce'
    INPUT_FILE = 'sirnasonsproduce.json'
    OUTPUT_FILE = 'sirnasonsproduce_data.csv'

    BASE_URL = 'https://www.cibo.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Sirna Sons Produce'

    def __init__(self, options=None):
        super().__init__(options)
