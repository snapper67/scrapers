from scrapers.pepper.pepper import PepperScraper

class AceEndicoScraper(PepperScraper):
	# 1392/edit_note/1510/
	CRM_ID = 1392
	CRM_NOTE_ID = 1510
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/ace_endico'
	INPUT_FILE = 'ace_endico.txt'
	OUTPUT_FILE = 'ace_endico_data.csv'

	BASE_URL = ''
	BASE_PRODUCT_URL = ''
	VENDOR_NAME = 'Ace Endico'

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	def __init__(self, options=None):
		super().__init__(options)

