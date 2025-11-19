from scrapers.pepper.pepper import PepperScraper

class BrothersFoodServiceScraper(PepperScraper):
    # 3536/edit_note/1731/
    CRM_ID = 3536
    CRM_NOTE_ID = 1731
    CRM_PRICE_TYPE = ''
    CRM_STATUS_OVERRIDE = 'Ready'

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/brothers_food_service'
    INPUT_FILE = 'brothers_food_service.json'
    OUTPUT_FILE = 'brothers_food_service_data.csv'

    BASE_URL = 'https://bfs.pepr.app/'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Brothers Food Service'

    def __init__(self, options=None):
        super().__init__(options)

    def process_products_from_csv(self):
        print("brothers->process_products_from_csv()")
        return self.get_product_details_json_2()
