from scrapers.pepper.pepper import PepperScraper

class AccDistributorsScraper(PepperScraper):
	# 1632/edit_note/1502/
	CRM_ID = 1632
	CRM_NOTE_ID = 1502
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/acc_distributors'
	INPUT_FILE = 'acc_distributors.txt'
	OUTPUT_FILE = 'acc_distributors_data.csv'

	BASE_URL = ''
	BASE_PRODUCT_URL = ''
	VENDOR_NAME = 'ACC Distributors'

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	def __init__(self, options=None):
		super().__init__(options)
