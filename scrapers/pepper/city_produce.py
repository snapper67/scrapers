from scrapers.pepper.pepper import PepperScraper

class CityProduceScraper(PepperScraper):
	# 1980/edit_note/1533/
	CRM_ID = 1980
	CRM_NOTE_ID = 1533
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/city_produce'
	INPUT_FILE = 'city_produce.txt'
	OUTPUT_FILE = 'city_produce_data.csv'

	BASE_URL = 'https://cityproducefl.com/'
	BASE_PRODUCT_URL = 'https://cityproduceconnect.pepr.app/'
	VENDOR_NAME = 'City Produce'

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	def __init__(self, options=None):
		super().__init__(options)

