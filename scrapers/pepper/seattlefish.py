from scrapers.pepper.pepper import PepperScraper

class SeattleFishScraper(PepperScraper):
    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/seattle_fish'
    INPUT_FILE = 'seattle_fish.json'
    OUTPUT_FILE = 'seattle_fish_data.csv'

    BASE_URL = 'https://www.seattlefish.com'
    BASE_PRODUCT_URL = f'{BASE_URL}/products/'
    VENDOR_NAME = 'Seattle Fish Company'

    def __init__(self, options=None):
        super().__init__(options)
        self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
        self.options['home_directory'] = self.DEFAULT_DIRECTORY
        self.options['base_url'] = self.BASE_URL

