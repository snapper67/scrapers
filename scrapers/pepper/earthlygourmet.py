from scrapers.pepper.pepper import PepperScraper

class EarthlyGourmetScraper(PepperScraper):
    # 1964/edit_note/1513/
    CRM_ID = 1964
    CRM_NOTE_ID = 1513
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = ''

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/earthly_gourmet'
    INPUT_FILE = 'earthly_gourmet.txt'
    OUTPUT_FILE = 'earthly_gourmet_data.csv'

    BASE_URL = 'https://www.earthlygourmet.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Earthly Gourmet'

    def __init__(self, options=None):
        super().__init__(options)

    def process_products_from_csv(self):
        print("earthlygourmet->process_products_from_csv()")
        return self.get_product_details_json_2()


