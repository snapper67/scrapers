from scrapers.pepper.pepper import PepperScraper

class NortheastSpecialtyScraper(PepperScraper):
    # 1977/edit_note/1529/
    CRM_ID = 1977
    CRM_NOTE_ID = 1529
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = ''

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/northeast_specialty_foods'
    INPUT_FILE = 'northeast_specialty_foods.json'
    OUTPUT_FILE = 'northeast_specialty_foods_data.csv'

    BASE_URL = 'https://www.nespecialtyfoods.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Northeast Specialty Foods'

    def __init__(self, options=None):
        super().__init__(options)

    def process_products_from_csv(self):
        print("earthlygourmet->process_products_from_csv()")
        return self.get_product_details_json_2()