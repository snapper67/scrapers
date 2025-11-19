from scrapers.pepper.pepper import PepperScraper

class TestaProduceScraper(PepperScraper):
    #  1606/edit_note/1702/
    CRM_ID = 1606
    CRM_NOTE_ID = 1702
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = 'Ready'

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/testa_produce'
    INPUT_FILE = 'testa_produce.json'
    OUTPUT_FILE = 'testa_produce_data.csv'

    BASE_URL = 'https://www.testaproduce.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Testa Produce'

    def __init__(self, options=None):
        super().__init__(options)
        self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
        self.options['home_directory'] = self.DEFAULT_DIRECTORY
        self.options['base_url'] = self.BASE_URL

    def process_products_from_csv(self):
        print("earthlygourmet->process_products_from_csv()")
        return self.get_product_details_json_2()