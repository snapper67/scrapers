from scrapers.pepper.pepper import PepperScraper

class DennisFoodserviceScraper(PepperScraper):
	# 1982/edit_note/1535/
	CRM_ID = 1982
	CRM_NOTE_ID = 1535
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/dennis_foodservice'
	INPUT_FILE = 'dennis.json'
	OUTPUT_FILE = 'dennis_foodservice_data.csv'

	BASE_URL = 'https://dennisfoodservice.com/'
	BASE_PRODUCT_URL = 'https://dennisfoodservice.pepr.app/'
	VENDOR_NAME = 'Dennis Foodservice'

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	def __init__(self, options=None):
		super().__init__(options)

