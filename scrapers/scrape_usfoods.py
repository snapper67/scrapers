# import csv
# import json
# import time
# import os
# from collections import OrderedDict
# import sys
# import glob
# import pandas as pd
# 
# from bs4 import BeautifulSoup
# from pathlib import Path
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# 
# from seleniumwire import webdriver as seleniumwire_webdriver
# from seleniumwire.utils import decode
# 
# from urllib.parse import urlparse, parse_qs, urlunparse
# from io import StringIO
# 
# 
# class USFoodsScraper:
#     # Class variables for default values
#     TEST_CATEGORIES = 100
#     TEST_PRODUCTS = 20000
#     CSV_START_ROW = 0
#     TEST_TABS = 2
#     MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
#     DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/'
#     
#     # Default file names
#     URL_OUTPUT_FILE = 'product_urls.csv'
#     DATA_OUTPUT_FILE = 'product_data.csv'
#     DEDUP_INPUT_FILE = 'product_data.csv'
#     
#     # Import specification
#     IMPORT_SPEC = [
#         'name', 'sku', 'gtin', 'image', 'pack', 'size', 'retail_price', 'ordering_unit', 
#         'is_catch_weight', 'is_broken_case', 'average_case_weight', 'brand', 'taxonomy', 
#         'level_1', 'level_2', 'level_3', 'manufacturer_name', 'manufacturer_sku', 
#         'distributor_name', 'content_url', 'description', 'unit_price', 'extra_data_1', 'extra_data_2'
#     ]
#     
#     # Categories and options
#     CATEGORY_IDS = {
#         'Meat': '10001',
#         'Seafood': '10002',
#         'Produce': '10003',
#         'Dairy': '10004',
#         'Bakery': '10005',
#         'Frozen': '10006',
#         'Grocery': '10007',
#         'Beverages': '10008',
#         'Equipment': '10009',
#         'Supplies': '10010',
#     }
#     
#     # Default options
#     DEFAULT_OPTIONS = {
#         'scrape_products': True,
#         'process_csv': False,
#         'reprocess_csv': False,
#         'dedupe_csv': False,
#         'count_csv': False,
#         'test_products': TEST_PRODUCTS,
#         'max_products': 999,
#         'csv_start_row': CSV_START_ROW,
#         'category_to_process': 0,
#         'chosen_category': '10001',  # Default to Meat
#         'url_output_file': URL_OUTPUT_FILE,
#         'data_output_file': DATA_OUTPUT_FILE,
#         'home_directory': DEFAULT_DIRECTORY
#     }
#     
#     def __init__(self, options=None):
#         """Initialize the scraper with options"""
#         # Update default options with any provided options
#         self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
#         
#         # Initialize Chrome options
#         self.chrome_options = Options()
#         # Uncomment for headless mode
#         # self.chrome_options.add_argument('--headless')
#         self.chrome_options.add_argument('--disable-gpu')
#         self.chrome_options.add_argument('--no-sandbox')
#         
#         # Selenium Wire options
#         self.seleniumwire_options = {
#             'disable_encoding': True,
#         }
#         
#         # Initialize WebDriver
#         self.driver = None
#         
#     def __enter__(self):
#         """Context manager entry"""
#         self.setup_driver()
#         return self
#         
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """Context manager exit - ensure driver is closed"""
#         self.cleanup()
#         
#     def setup_driver(self):
#         """Initialize the WebDriver"""
#         if not self.driver:
#             chromedriver_path = self.get_file_path('/Users/mark/Downloads/chrome-mac-arm64/chromedriver')
#             service = Service(chromedriver_path)
#             self.driver = seleniumwire_webdriver.Chrome(
#                 service=service, 
#                 options=self.chrome_options, 
#                 seleniumwire_options=self.seleniumwire_options
#             )
#     
#     def cleanup(self):
#         """Clean up resources"""
#         if self.driver:
#             self.driver.quit()
#             self.driver = None
#     
#     def get_file_path(self, filename, home_dir=None):
#         """
#         Get the full file path by joining with the home directory if the path is not absolute.
#         
#         Args:
#             filename (str): The filename or path to resolve
#             home_dir (str, optional): The home directory to use as base for relative paths
#             
#         Returns:
#             str: The resolved absolute file path
#         """
#         if not filename:
#             return filename
#             
#         # Convert to Path object
#         path = Path(filename)
#         
#         # If it's already an absolute path, return as is
#         if path.is_absolute():
#             return str(path)
#             
#         # Otherwise, join with home directory
#         home_dir = home_dir or self.options.get('home_directory', self.DEFAULT_DIRECTORY)
#         home_path = Path(home_dir).expanduser().resolve()
#         return str(home_path / path)
#     
#     def run(self):
#         """
#         Main entry point that determines which action to take based on the options
#         """
#         if self.options.get('scrape_products'):
#             return self.scrape_products()
#         elif self.options.get('process_csv'):
#             return self.process_products_from_csv()
#         elif self.options.get('reprocess_csv'):
#             return self.reprocess_products()
#         elif self.options.get('dedupe_csv'):
#             return self.remove_duplicate_skus()
#         elif self.options.get('count_csv'):
#             return self.count_csv_rows()
#         else:
#             return "No action specified. Please select an option."
#     
#     # Placeholder methods that will be implemented by moving existing functions
#     def scrape_products(self):
#         """Scrape products from the website"""
#         raise NotImplementedError("scrape_products method not implemented")
#     
#     def process_products_from_csv(self):
#         """Process products from a CSV file"""
#         raise NotImplementedError("process_products_from_csv method not implemented")
#     
#     def reprocess_products(self):
#         """Reprocess products that failed previously"""
#         raise NotImplementedError("reprocess_products method not implemented")
#     
#     def remove_duplicate_skus(self, input_file=None, output_file=None):
#         """Remove duplicate SKUs from a CSV file"""
#         raise NotImplementedError("remove_duplicate_skus method not implemented")
#     
#     def count_csv_rows(self, directory=None):
#         """Count rows in CSV files in a directory"""
#         raise NotImplementedError("count_csv_rows method not implemented")
# 
# # For backward compatibility
# def main(options=None):
#     """
#     Main function for backward compatibility
#     """
#     with USFoodsScraper(options) as scraper:
#         return scraper.run()
# 
# # Keep the original function signatures for backward compatibility
# # These will be removed in a future version
# def remove_duplicate_skus(input_file=None, output_file=None, home_dir=None):
#     with USFoodsScraper({
#         'dedupe_csv': True,
#         'home_directory': home_dir or USFoodsScraper.DEFAULT_DIRECTORY
#     }) as scraper:
#         return scraper.remove_duplicate_skus(input_file, output_file)
# 
# # ... (other compatibility functions)
# 
# 
# 
# # Path to your chromedriver executable
# chromedriver_path = '/Users/mark/Downloads/chrome-mac-arm64/chromedriver'
# 
# service = Service(chromedriver_path)
# # driver = seleniumwire_webdriver.Chrome(service=service, options=chrome_options, seleniumwire_options=seleniumwire_options)
# # https://usfoodsproduction10upnbvk4.org.coveo.com/rest/organizations/usfoodsproduction10upnbvk4/commerce/v2/search
# 
# TEST_CATEGORIES = 100
# TEST_PRODUCTS = 20000
# CSV_START_ROW = 0
# TEST_TABS = 2
# MAX_API_PRODUCTS = 999 # Maximum number to change the search request page size
# DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/'
# 
# SCRAPE_PRODUCTS = True
# PROCESS_CSV = False
# DEDUPE_CSV = False
# 
# # Category IDs (Constant mapping for code lookup)
# CATEGORY_IDS = {
#     "BEEF": 15,
#     "BEVERAGE": 16,
#     "FRUIT": 17,
#     "CHEESE": 18,
#     "CHEMICALS": 19,
#     "APPETIZER": 20,
#     "DAIRY": 21,
#     "GROCERY_DRY": 22,
#     "EQUIPMENT": 23,
#     "DISPOSABLES": 24,
#     "PRODUCE": 25,
#     "GROCERY_FRZ": 26,
#     "OIL": 29,
#     "PORK": 30,
#     "POULTRY": 31,
#     "PROCESSED": 32,
#     "SEAFOOD": 33,
#     "SPECIALTY_MEAT": 34,
#     "SALADS": 35,
#     "MEAT_SUB": 37,
# }
# # Category Names (can use category ID as key)
# CATEGORY_NAMES = {
#     15: "Beef",
#     16: "Beverage",
#     17: "Fruits & Vegetables, Canned & Dried",
#     18: "Cheese",
#     19: "Chemicals & Cleaning Agents",
#     20: "Appetizers, Entrees, & Potatoes Ref & Fzn",
#     21: "Dairy",
#     22: "Grocery, Dry",
#     23: "Equipment & Supplies",
#     24: "Disposables",
#     25: "Produce, Fresh",
#     26: "Grocery, Ref & Fzn",
#     29: "Oils & Shortening",
#     30: "Pork",
#     31: "Poultry",
#     32: "Processed Meat",
#     33: "Seafood",
#     34: "Specialty Meats",
#     35: "Salads, Wet, Ref & Fzn",
#     37: "Meat Substitute",
# }
# URL_FILE_NAMES = {
#     15: "beef_product_urls.csv",
#     16: "bev_product_urls.csv",
#     17: "fruit_product_urls.csv",
#     18: "cheese_product_urls.csv",
#     19: "chem_product_urls.csv",
#     20: "app_product_urls.csv",
#     21: "dairy_product_urls.csv",
#     22: "dry_product_urls.csv",
#     23: "equip_product_urls.csv",
#     24: "disp_product_urls.csv",
#     25: "produce_product_urls.csv",
#     26: "frozen_product_urls.csv",
#     29: "oil_product_urls.csv",
#     30: "pork_product_urls.csv",
#     31: "poultry_product_urls.csv",
#     32: "processed_product_urls.csv",
#     33: "seafood_product_urls.csv",
#     34: "specialty_product_urls.csv",
#     35: "salad_product_urls.csv",
#     37: "ms_product_urls.csv",
# }
# DATA_FILE_NAMES = {
#     15: "beef_product_data.csv",
#     16: "bev_product_data.csv",
#     17: "fruit_product_data.csv",
#     18: "cheese_product_datas.csv",
#     19: "chem_product_data.csv",
#     20: "app_product_data.csv",
#     21: "dairy_product_data.csv",
#     22: "dry_product_data.csv",
#     23: "equip_product_data.csv",
#     24: "disp_product_data.csv",
#     25: "produce_product_data.csv",
#     26: "frozen_product_data.csv",
#     29: "oil_product_data.csv",
#     30: "pork_product_data.csv",
#     31: "poultry_product_data.csv",
#     32: "processed_product_data.csv",
#     33: "seafood_product_data.csv",
#     34: "specialty_product_data.csv",
#     35: "salad_product_data.csv",
#     37: "ms_product_data.csv",
# }
# 
# CHOSEN_CATEGORY = CATEGORY_IDS["GROCERY_DRY"]
# CATEGORY_NAME = CATEGORY_NAMES[CHOSEN_CATEGORY]
# URL_OUTPUT_FILE = URL_FILE_NAMES[CHOSEN_CATEGORY]
# DATA_OUTPUT_FILE = DATA_FILE_NAMES[CHOSEN_CATEGORY]
# DEDUP_INPUT_FILE = "dry_product_data.csv"
# 
# starting_URL = "https://order.usfoods.com/desktop/search/browse"
# 
# usfoods_options = {
# 	'max_products': MAX_API_PRODUCTS,
# 	'test_categories': TEST_CATEGORIES,
# 	'test_products': TEST_PRODUCTS,
# 	'csv_start_row': CSV_START_ROW,
# 	'scrape_products': False,
# 	'process_csv': True,
# 	'reprocess_csv': False,
# 	'dedupe_csv': False,
# 	'count_csv': False,
# 	'chosen_category': CHOSEN_CATEGORY,
# 	'url_output_file': URL_OUTPUT_FILE,
# 	'data_output_file': DATA_OUTPUT_FILE,
# 	'category_name': CATEGORY_NAME,
# 	'category_to_process': 0,
# 	'home_directory': ''
# }
# 
# IMPORT_SPEC = [
# 			'name', 'sku', 'gtin', 'image', 'pack', 'size', 'retail_price', 'ordering_unit', 'is_catch_weight', 'is_broken_case',
# 			'average_case_weight', 'brand', 'taxonomy', 'level_1', 'level_2', 'level_3', 'manufacturer_name',
# 			'manufacturer_sku', 'distributor_name', 'content_url', 'description', 'unit_price', 'extra_data_1', 'extra_data_2'
# 		]
# # SKU	URL	Timestamp	Category	Subcategory	Name	PS	Brand	Image	Classification 1	Classification 2	Classification 3	Description	Desc 1	Desc 2	Desc 3	Man 1	Man 2	Man 3
# US_FOODS_SPEC = [
# 			'timestamp', 'category', 'subcategory', 'name', 'ps', 'brand', 'image', 'pack_size', 'classCode', 'classDescription', 'groupCode', 'groupDescription', 'categoryCode', 'categoryDescription',
# 			'standardComparisonUOM', 'standardComparisonValue', 'volume', 'volumeUnits', 'yield', 'yieldUOM', 'countryOfOriginGrownHarvested', 'countryOfOriginProcessed'
# 		]
# 
# PRODUCT_DATA_SPEC = {
# 	# Fields from IMPORT_SPEC
# 	'name': '',
# 	'sku': '',
# 	'gtin': '',
# 	'image': '',
# 	'pack': '',
# 	'size': '',
# 	'retail_price': '',
# 	'ordering_unit': '',
# 	'is_catch_weight': '',
# 	'is_broken_case': '',
# 	'average_case_weight': '',
# 	'brand': '',
# 	'taxonomy': '',
# 	'level_1': '',
# 	'level_2': '',
# 	'level_3': '',
# 	'manufacturer_name': '',
# 	'manufacturer_sku': '',
# 	'distributor_name': '',
# 	'content_url': '',
# 	'description': '',
# 	'unit_price': '',
# 	'extra_data_1': '',
# 	'extra_data_2': '',
# 
# 	# Fields from US_FOODS_SPEC
# 	'timestamp': '',
# 	'pack_size': '',
# 	'category': '',
# 	'subcategory': '',
# 	'classCode': '',
# 	'classDescription': '',
# 	'groupCode': '',
# 	'groupDescription': '',
# 	'categoryCode': '',
# 	'categoryDescription': '',
# 	'standardComparisonUOM': '',
# 	'standardComparisonValue': '',
# 	'volume': '',
# 	'volumeUnits': '',
# 	'yield': '',
# 	'yieldUOM': '',
# 	'countryOfOriginGrownHarvested': '',
# 	'countryOfOriginProcessed': ''
# }
# 
# 
# def get_file_path(filename, home_dir='.'):
# 	"""
# 	Get the full file path by joining with the home directory if the path is not absolute.
# 
# 	Args:
# 		filename (str): The filename or path to resolve
# 		home_dir (str): The home directory to use as base for relative paths
# 
# 	Returns:
# 		str: The resolved absolute file path
# 	"""
# 	if not filename:
# 		return filename
# 
# 	# Convert to Path object
# 	path = Path(filename)
# 
# 	# If it's already an absolute path, return as is
# 	if path.is_absolute():
# 		return str(path)
# 
# 	# Otherwise, join with home directory
# 	home_path = Path(home_dir).expanduser().resolve()
# 	return str(home_path / path)
# 
# def extract_and_update(self, *args, **options):
# 	print("Processing Row")
# 	directory = options['directory']
# 	distributor_name = options['distributor_name']
# 
# 	if not os.path.isdir(directory):
# 		self.stderr.write(self.style.ERROR(f"Error: '{directory}' is not a valid directory."))
# 		return
# 
# 	# csv_files = [f for f in os.listdir(directory) if f.lower().endswith('.csv')]
# 	csv_files = glob.glob(os.path.join(directory, "**/*.csv"), recursive=True)
# 
# 	if not csv_files:
# 		self.stdout.write(self.style.WARNING("No CSV files found in the directory."))
# 		return
# 
# 	for file_name in csv_files:
# 		file_path = os.path.join(directory, file_name)
# 		try:
# 			df = pd.read_csv(file_path)
# 
# 			if 'distributor_name' not in df.columns:
# 				self.stdout.write(self.style.WARNING(f"Skipped '{file_name}': No 'distributor_name' column."))
# 				continue
# 
# 			df = df.apply(self.extract_and_update, axis=1)
# 
# 			df.to_csv(file_path, index=False)
# 			self.stdout.write(self.style.SUCCESS(f"Updated '{file_name}' successfully."))
# 
# 		except Exception as e:
# 			self.stderr.write(self.style.ERROR(f"Failed to update '{file_name}': {str(e)}"))
# 
# def remove_duplicate_skus(input_file=DEDUP_INPUT_FILE, output_file=None, home_dir=DEFAULT_DIRECTORY):
# 	"""
# 	Remove duplicate rows from a CSV file based on the SKU column.
# 
# 	Args:
# 		input_file (str): Path to the input CSV file
# 		output_file (str, optional): Path to save the deduplicated CSV. If None, will append '_deduped' to input filename.
# 	    home_dir (str): Home directory for relative paths
# 
# 	Returns:
# 		str: Path to the output file with duplicates removed
# 	"""
# 	print("Starting remove_duplicate_skus")
# 	input_file = get_file_path(input_file, home_dir)
# 
# 	if output_file is None:
# 		file_parts = os.path.splitext(input_file)
# 		output_file = f"{file_parts[0]}_deduped{file_parts[1]}"
# 	else:
# 		output_file = get_file_path(output_file, home_dir)
# 
# 	# Dictionary to store unique rows by SKU
# 	unique_rows = OrderedDict()
# 	total_rows = 0
# 	duplicates_removed = 0
# 	sample_sku = ''
# 	print("Lets Try")
# 	try:
# 		# Read the input file
# 		with open(input_file, 'r', newline='', encoding='utf-8') as infile:
# 			reader = csv.DictReader(infile)
# 			print("Lets Try 2")
# 			fieldnames = reader.fieldnames
# 			print("Lets Try 3")
# 			sku_field = 'SKU'
# 			# Check if 'SKU' or 'sku' column exists
# 			if 'SKU' not in fieldnames:
# 				sku_field = 'sku'
# 				csv.field_size_limit(sys.maxsize)
# 				if 'sku' not in fieldnames:
# 					raise ValueError("Input file must contain an 'SKU' column")
# 			found = False
# 			print("Lets Try 4")
# 			# Process each row
# 			for row in reader:
# 				total_rows += 1
# 				print(sku_field)
# 				sku = row[sku_field]
# 				print(sku)
# 				# Keep the first occurrence of each SKU
# 				if sku not in unique_rows:
# 					unique_rows[sku] = row
# 				else:
# 					if not found:
# 						print(f"Duplicate SKU found at line : {total_rows}")
# 						print(f"SKU was : {sku}")
# 						sample_sku = sku
# 						found = True
# 
# 		# Count duplicates
# 		duplicates_removed = total_rows - len(unique_rows)
# 
# 		# Write the deduplicated rows to the output file
# 		with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
# 			writer = csv.DictWriter(outfile, fieldnames=fieldnames)
# 			writer.writeheader()
# 			writer.writerows(unique_rows.values())
# 
# 		print(f"Processed {total_rows} rows")
# 		print(f"Removed {duplicates_removed} duplicate SKUs")
# 		print(f"Saved {len(unique_rows)} unique rows to {output_file}")
# 		html = f"<p>Processed {total_rows} rows</p>"
# 		html += f"<p>Removed {duplicates_removed} duplicate SKUs</p>"
# 		html += f"<p>Example Duplicate SKU: {sample_sku}</p><p>Removed</p>"
# 		html += f"<p>Saved {len(unique_rows)} unique rows to {output_file}</p>"
# 		return html
# 
# 	except FileNotFoundError:
# 		print(f"⛔️⛔️⛔️Error: Input file '{input_file}' not found")
# 		return None
# 	except Exception as e:
# 		print(f"⛔️⛔️⛔️Error processing file: {e}")
# 		return None
# 
# def html_table_to_csv(html_content, output_file='products_export.csv', home_dir=DEFAULT_DIRECTORY):
# 	"""
# 	Convert an HTML table to a CSV file.
# 
# 	Args:
# 		html_content (str): HTML content containing a table
# 		output_file (str): Path to save the CSV file
# 		home_dir (str): Home directory for relative paths
# 	"""
# 	try:
# 		# Parse the HTML
# 		# Resolve output file path
# 		output_file = get_file_path(output_file, home_dir)
# 
# 		# Ensure the output directory exists
# 		os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
# 
# 		soup = BeautifulSoup(html_content, 'html.parser')
# 		table = soup.find('table')
# 
# 		if not table:
# 			print("No table found in the HTML content")
# 			return False
# 
# 		# Open the CSV file for writing
# 		with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
# 			writer = csv.writer(csvfile)
# 
# 			# Process each row in the table
# 			rows = table.find_all('tr')
# 			for row in rows:
# 				# Get all cells in the row
# 				cells = row.find_all(['th', 'td'])
# 				# Extract text from each cell and clean it
# 				row_data = [cell.get_text(strip=True) for cell in cells]
# 				# Write the row to CSV
# 				writer.writerow(row_data)
# 
# 		print(f"Successfully exported data to {output_file}")
# 		return True
# 
# 	except Exception as e:
# 		print(f"⛔️⛔️⛔️Error exporting to CSV: {e}")
# 		return False
# 
# 
# def process_missing_skus(driver, skus_to_check, url_file=URL_OUTPUT_FILE, data_file=DATA_OUTPUT_FILE, home_dir=DEFAULT_DIRECTORY):
# 	"""
# 	Process SKUs that exist in the URL file but are missing from the data file.
# 
# 	Args:
# 		driver: Selenium WebDriver instance
# 		skus_to_check: List of SKUs to check and process
# 		url_file: Path to the CSV file containing product URLs
# 		data_file: Path to the CSV file containing product data
# 		home_dir (str): Home directory for relative paths
# 
# 	Returns:
# 		tuple: (list of processed SKUs, list of not found SKUs)
# 	"""
# 	print("Starting Processing missing SKUs")
# 	specified_skus = len(skus_to_check) > 0
# 
# 	url_file = get_file_path(url_file, home_dir)
# 	data_file = get_file_path(data_file, home_dir)
# 
# 	# Read existing data to check which SKUs we already have
# 	existing_skus = set()
# 	if os.path.exists(data_file):
# 		with open(data_file, 'r', newline='', encoding='utf-8') as f:
# 			reader = csv.DictReader(f)
# 			csv.field_size_limit(sys.maxsize)
# 			if 'sku' in reader.fieldnames:
# 				existing_skus = {row['sku'] for row in reader}
# 
# 	# Read URL file to get URL for each SKU
# 	print("Here")
# 	# Process missing SKUs
# 	processed_skus = []
# 	not_found_skus = []
# 
# 	if os.path.exists(url_file):
# 		with open(url_file, 'r', newline='', encoding='utf-8') as f:
# 			reader = csv.DictReader(f)
# 			print("Here 2")
# 
# 			if 'SKU' in reader.fieldnames and 'URL' in reader.fieldnames:
# 				print("Here 3")
# 				for row in reader:
# 					sku = row['SKU']
# 					if (sku in skus_to_check or not specified_skus) and sku not in existing_skus:
# 						row_spec = PRODUCT_DATA_SPEC.copy()
# 						try:
# 							print(f"Processing missing SKU: {sku}")
# 							# Copy values from import file
# 							row_spec['subcategory'] = row['Subcategory']
# 							row_spec['timestamp'] = row['Timestamp']
# 							row_spec['content_url'] = row['URL']
# 							row_spec['sku'] = row['SKU']
# 							row_spec['category'] = row['Category']
# 							row_spec = process_product(driver,  row['URL'], row_spec)
# 							processed_skus.append(row['SKU'])
# 
# 							# Write to CSV
# 							print(f"Saving product {row_spec['name']} to {data_file}")
# 							write_product_to_csv(row_spec, data_file)
# 						except Exception as e:
# 							print(f"⛔️⛔️⛔️Error processing SKU {sku}: {str(e)}")
# 							not_found_skus.append(sku)
# 
# 	return processed_skus, not_found_skus
# 
# 
# def count_csv_rows(directory='./Product_URLS_999_Max', home_dir=DEFAULT_DIRECTORY):
# 	"""
# 	Counts the number of rows in all CSV files in the specified directory.
# 
# 	Args:
# 		directory (str): Path to the directory containing CSV files. Defaults to current directory.
# 		home_dir (str): Home directory for relative paths
# 
# 	Returns:
# 		str: HTML formatted string with the results
# 	"""
# 	# Resolve directory path
# 	directory = get_file_path(directory, home_dir)
# 	# Dictionary to store file counts
# 	file_counts = {}
# 	total_rows = 0
# 
# 	# Get all CSV files in the directory
# 	csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
# 
# 	if not csv_files:
# 		return "<p>No CSV files found in the directory.</p>"
# 	csv.field_size_limit(sys.maxsize)
# 
# 	# Count rows in each CSV file
# 	for filename in csv_files:
# 		filepath = os.path.join(directory, filename)
# 		try:
# 			with open(filepath, 'r', encoding='utf-8') as file:
# 				# Count rows (excluding header)
# 				row_count = sum(1 for row in csv.reader(file)) - 1
# 				file_counts[filename] = row_count
# 				total_rows += row_count
# 		except Exception as e:
# 			print(f"⛔️⛔️⛔️Error processing {filename}: {e}")
# 			file_counts[filename] = f"Error: {str(e)}"
# 
# 	# Generate HTML output
# 	html = "<h3>CSV File Row Counts:</h3>"
# 	html += "<table class='table table-striped'><thead><tr><th>File</th><th>Rows</th></tr></thead><tbody>"
# 
# 	# Sort files by name for consistent output
# 	for filename in sorted(file_counts.keys()):
# 		row_count = file_counts[filename]
# 		html += f"<tr><td>{filename}</td><td>{row_count}</td></tr>"
# 
# 	html += f"<tr><td><strong>Total Rows</strong></td><td><strong>{total_rows}</strong></td></tr>"
# 	html += "</tbody></table>"
# 
# 	return html
# 
# 
# def save_urls_to_csv(urls, category_name="", subcategory_name="", filename=URL_OUTPUT_FILE, home_dir=DEFAULT_DIRECTORY ):
# 	"""
# 	Save a list of URLs to a CSV file. If the file exists, it will append to it.
# 	
# 	Args:
# 		urls (list): List of URLs to save
# 		filename (str): Name of the output CSV file
# 		category_name (str): Name of the category
# 		subcategory_name (str): Name of the sub category
# 		home_dir (str): Home directory for relative paths
# 	"""
# 	import csv
# 	import os
# 	from datetime import datetime
# 
# 	# Resolve the file path
# 	filename = get_file_path(filename, home_dir)
# 
# 	# Ensure the directory exists
# 	os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)
# 
# 	file_exists = os.path.isfile(filename)
# 
# 	try:
# 		with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
# 			writer = csv.writer(csvfile)
# 
# 			# Write header only if file is new
# 			if not file_exists:
# 				writer.writerow(['SKU', 'URL', 'Timestamp', 'Category', 'Subcategory'])
# 
# 			# Write each URL with timestamp
# 			for url in urls:
# 				sku = url.split('/')[-1].split('?')[0]  # Remove any query parameters
# 				writer.writerow([sku, url, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), category_name, subcategory_name])
# 
# 		mode = "Appended to" if file_exists else "Created new"
# 		print(f"Successfully {mode} {len(urls)} URLs to {filename}")
# 
# 	except Exception as e:
# 		print(f"⛔️⛔️⛔️Error saving URLs to CSV: {e}")
# 
# 
# def split_code_and_text(input_string):
# 	"""
# 	Splits a string in the format '9999 - text text-text' into code and text.
# 
# 	Args:
# 		input_string (str): The input string to split
# 
# 	Returns:
# 		tuple: (code, text) where code is the numeric part and text is the rest
# 	"""
# 	# Split on the first occurrence of ' - ' (space-hyphen-space)
# 	try:
# 		parts = input_string.split(' - ', 1)
# 
# 		if len(parts) == 2:
# 			code = parts[0].strip()
# 			text = parts[1].strip()
# 		else:
# 			# Handle case where the delimiter isn't found
# 			code = input_string.strip()
# 			text = ''
# 
# 		return code, text
# 	except Exception as e:
# 		return '', ''
# 
# 
# def write_product_to_csv(product_data, filename=DATA_OUTPUT_FILE, home_dir=DEFAULT_DIRECTORY):
# 	"""
# 	Write a product data dictionary to a CSV file. If the file doesn't exist,
# 	it will be created with headers. If it exists, the data will be appended.
# 
# 	Args:
# 		product_data (dict): Dictionary containing product data following PRODUCT_DATA_SPEC
# 		filename (str): Path to the CSV file (defaults to DATA_OUTPUT_FILE)
# 		home_dir (str): Home directory for relative paths
# 
# 	Returns:
# 		bool: True if successful, False otherwise
# 	"""
# 	try:
# 		# Convert all values to strings and handle None values
# 		row_data = {k: str(v) if v is not None else '' for k, v in product_data.items()}
# 
# 		filename = get_file_path(filename, home_dir)
# 
# 		# Ensure the directory exists
# 		os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)
# 
# 		# Check if file exists to determine if we need to write headers
# 		file_exists = os.path.isfile(filename)
# 
# 		with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
# 			writer = csv.DictWriter(csvfile, fieldnames=PRODUCT_DATA_SPEC.keys())
# 
# 			# Write header if file is being created
# 			if not file_exists or os.path.getsize(filename) == 0:
# 				writer.writeheader()
# 
# 			# Write the product data
# 			writer.writerow(row_data)
# 			csvfile.flush()
# 
# 		print(f"Successfully wrote product {product_data.get('sku', '')} to {filename}")
# 
# 		return True
# 
# 	except Exception as e:
# 		print(f"⛔️⛔️⛔️Error writing product to CSV: {e}")
# 		return False
# 
# 
# def get_first_image_url(response_data):
# 	"""
# 	Extract the first available image URL from the product API response.
# 
# 	Args:
# 		response_data (dict): The parsed JSON response from the API
# 
# 	Returns:
# 		str: URL of the first available image, or None if no image found
# 	"""
# 	try:
# 		# Get the first item's product assets
# 		product_assets = response_data['summary'].get('productAssets', {})
# 		product_images = product_assets.get('productImages', {})
# 
# 		# Get the first image group (C1CD, C1CB, etc.)
# 		if product_images:
# 			first_image_group = next(iter(product_images.values()))
# 			renditions = first_image_group.get('renditions', {})
# 
# 			# Try to get the Original image first, then fall back to other sizes
# 			for size in ['Original', 'Large', 'Medium', 'Small', 'XLarge', 'Thumbnail']:
# 				if size in renditions:
# 					return renditions[size]
# 
# 	except (KeyError, IndexError, AttributeError) as e:
# 		print(f"⛔️⛔️⛔️Error extracting image URL: {e}")
# 
# 	return None
# 
# def get_product_data(product_data, row_spec):
# 
# 	print("processing product data from response...")
# 	# print(product_data)
# 	if product_data:
# 		try:
# 			product_name = product_data.get('summary', {}).get('productDescTxtl', '')
# 			print(f"product_name: {product_name}")
# 			product_sku = product_data.get('summary', {}).get('productNumber', '')
# 			print(f"product_sku: {product_sku}")
# 			product_ps = product_data.get('summary', {}).get('salesPackSize', '')
# 			print(f"product_ps: {product_ps}")
# 			product_brand = product_data.get('summary', {}).get('brand', {})
# 			print(f"product_brand: {product_brand}")
# 			product_image = get_first_image_url(product_data)
# 			print(f"product_image: {product_image}")
# 			row_spec["name"] = product_name
# 			row_spec["pack_size"] = product_ps
# 			row_spec["brand"] = product_brand
# 			row_spec["image"] = product_image
# 			# print(row_spec)
# 			row_spec['extra_data_1'] = product_data
# 		except Exception as e:
# 			print(f" ⛔️⛔️⛔️Error processing product data: {e}")
# 
# 	print("processing product additional data Complete...")
# 	return row_spec
# 
# def get_classification(driver, wait, product_data, row_spec):
# 	print("processing product classification...")
# 	if product_data:
# 		row_spec['classCode'] = product_data.get('summary').get('classCode')
# 		row_spec['classDescription'] = product_data.get('summary').get('classDescription')
# 		row_spec['categoryCode'] = product_data.get('summary').get('categoryCode')
# 		row_spec['categoryDescription'] = product_data.get('summary').get('categoryDescription')
# 		row_spec['groupCode'] = product_data.get('summary').get('groupCode')
# 		row_spec['groupDescription'] = product_data.get('summary').get('groupDescription')
# 		print(f"classification completed using product data...{row_spec['classCode']}")
# 	else:
# 		try:
# 			classification = wait.until(
# 				EC.presence_of_element_located((By.CSS_SELECTOR, 'section.desktop-tablet-classification-details'))
# 			)
# 			driver.execute_script("arguments[0].scrollIntoView();", classification)
# 			classification_list = classification.find_elements(By.TAG_NAME, 'li')
# 			level_1 = classification_list[0].text.strip()
# 			print(f" Level 1: {level_1}")
# 			level_2 = classification_list[1].text.strip()
# 			print(f" Level 2: {level_2}")
# 			level_3 = classification_list[2].text.strip()
# 			print(f" Level 3: {level_3}")
# 			row_spec['classCode'], row_spec['classDescription']  = split_code_and_text(level_1)
# 			row_spec['categoryCode'], row_spec['categoryDescription'] = split_code_and_text(level_2)
# 			row_spec['groupCode'], row_spec['groupDescription'] = split_code_and_text(level_3)
# 		except Exception as e:
# 			print(f"⛔️⛔️⛔️Error processing product classification: {e}")
# 		print("processing product classification Complete...")
# 
# 	return row_spec
# 
# def get_manufacturer(driver, wait, data, row_spec):
# 	level_1 = ''
# 	level_2 = ''
# 	level_3 = ''
# 	print("processing product manufacturer...")
# 	if data:
# 		level_1 = data.get('manufacturerName')
# 		level_2 = data.get('manufacturerProductNumber')
# 		html = f"<td>{level_1}</td><td>{level_2}</td><td>{level_3}</td>"
# 	else:
# 		try:
# 			container = wait.until(
# 				EC.presence_of_element_located((By.CSS_SELECTOR, 'section.desktop-tablet-manufacturer'))
# 			)
# 			driver.execute_script("arguments[0].scrollIntoView();", container)
# 			ul_list = container.find_elements(By.TAG_NAME, 'li')
# 			level_1 = ul_list[0].text.replace("Manufacturer: ", "").strip()
# 			print(f"  Level 1: {level_1}")
# 			level_2 = ul_list[1].text.replace("Manufacturer Product #:", "").strip()
# 			print(f"  Level 2: {level_2}")
# 			row_spec['manufacturer_name'] = level_1
# 			row_spec['manufacturer_sku'] = level_2
# 		except Exception as e:
# 			print(f"⛔️⛔️⛔️Error processing product manufacturer: {e}")
# 	print("processing product manufacturer Complete...")
# 	return row_spec
# 
# def get_additional_info(data, row_spec):
# 
# 	print("processing product additional data...")
# 	if data:
# 		try:
# 			row_spec['standardComparisonUOM'] = data.get('standardComparisonUOM')
# 			row_spec['standardComparisonValue'] = data.get('standardComparisonValue')
# 			row_spec['volume'] = data.get('volume')
# 			row_spec['volumeUnits'] = data.get('volumeUnits')
# 			row_spec['yield'] = data.get('yield')
# 			row_spec['yieldUOM'] = data.get('yieldUOM')
# 			row_spec['extra_data_2'] = data
# 		except Exception as e:
# 			print(f"⛔️⛔️⛔️Error processing additional data: {e}")
# 
# 	print("processing product additional data Complete...")
# 	return row_spec
# 
# def get_description(driver, wait, data, row_spec):
# 	print("processing product overview...")
# 	description = ''
# 	level_1 = ''
# 	level_2 = ''
# 	level_3 = ''
# 	if data:
# 		description = data.get('additionalDescription')
# 		level_1 = data.get('countryOfOriginGrownHarvested')
# 		level_2 = data.get('countryOfOriginProcessed')
# 		row_spec['description'] = description
# 		row_spec['countryOfOriginGrownHarvested'] = level_1
# 		row_spec['countryOfOriginProcessed'] = level_2
# 	else:
# 		try:
# 			container = wait.until(
# 				EC.presence_of_element_located((By.CSS_SELECTOR, 'div.overview-benefits section'))
# 			)
# 			driver.execute_script("arguments[0].scrollIntoView();", container)
# 			try:
# 				description = container.find_element(By.CSS_SELECTOR, 'p').text.strip()
# 			except Exception as e:
# 				print(f"  Description not found:")
# 
# 			processing_list = container.find_elements(By.TAG_NAME, 'li')
# 			level_1 = processing_list[0].text.strip()
# 			print(f"  Level 1: {level_1}")
# 			level_2 = processing_list[1].text.strip()
# 			print(f"  Level 2: {level_2}")
# 			level_3 = processing_list[2].text.strip()
# 			print(f"  Level 3: {level_3}")
# 			row_spec['description'] = level_1
# 			row_spec['countryOfOriginGrownHarvested'] = level_2
# 			row_spec['countryOfOriginProcessed'] = level_3
# 		except Exception as e:
# 			print(f"⛔️️ Error processing product overview: {e}")
# 
# 	print("processing product overview Complete...")
# 	return row_spec
# 
# def process_product(driver, url, row_spec=None):
# 	#  Wait for the product name element on the product page detail page
# 	if not row_spec: row_spec = PRODUCT_DATA_SPEC.copy()
# 	print("processing product detail page")
# 	wait = WebDriverWait(driver, 15)
# 	driver.get(url)
# 	driver.execute_script("document.body.style.zoom = '50%'")
# 	print(f"Loading page...{url}")
# 	data = ''
# 	request = driver.wait_for_request('domain-api/v1/productdetail')
# 	if request.response and "domain-api/v1/productdetail" in request.url:  # Filter for API requests
# 		print(f"URL: {request.url}")
# 		print(f"Status Code: {request.response.status_code}")
# 		print(f"Content Type: {request.response.headers.get('Content-Type')}")
# 
# 		# Decode the response body (it's bytes by default)
# 		try:
# 			# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
# 			body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
# 
# 			# If the body is JSON, parse it
# 			if 'application/json' in request.response.headers.get('Content-Type', ''):
# 				data = json.loads(body)
# 			else:
# 				print(f"Response Body (Text): {body}")
# 
# 		except Exception as e:
# 			print(f"⛔️⛔️⛔️Error decoding response body: {e}")
# 	# Wait for the container to be present
# 
# 	# Check to see we got a product details response. This only populates part of the product detail page
# 
# 	product_data = ''
# 	for request in driver.requests:
# 		if data and product_data:
# 			break
# 		# https://panamax-api.ama.usfoods.com/product-domain-api/v1/search?worksWellWith=true
# 		if request.response and "domain-api/v1/productdetail" in request.url:  # Filter for API requests
# 			print(f"URL: {request.url}")
# 			print(f"Status Code: {request.response.status_code}")
# 			print(f"Content Type: {request.response.headers.get('Content-Type')}")
# 
# 			# Decode the response body (it's bytes by default)
# 			try:
# 				# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
# 				body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
# 
# 				# If the body is JSON, parse it
# 				if 'application/json' in request.response.headers.get('Content-Type', ''):
# 					data = json.loads(body)
# 				else:
# 					print(f"Response Body (Text): {body}")
# 
# 			except Exception as e:
# 				print(f"⛔️⛔️⛔️Error decoding response body: {e}")
# 		if request.response and "product-domain-api/v2/products" in request.url and not product_data:  # Filter for API requests
# 			print(f"URL: {request.url}")
# 			print(f"Status Code: {request.response.status_code}")
# 			print(f"Content Type: {request.response.headers.get('Content-Type')}")
# 
# 			# Decode the response body (it's bytes by default)
# 			try:
# 				# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
# 				body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
# 
# 				# If the body is JSON, parse it
# 				if 'application/json' in request.response.headers.get('Content-Type', ''):
# 					response_data = json.loads(body)
# 
# 					# Check if the response contains items and it's a list
# 					if 'items' in response_data and isinstance(response_data['items'], list):
# 						# Find the product with matching SKU
# 						target_sku = str(row_spec.get('sku', '')).strip()
# 						for item in response_data['items']:
# 							# Check both string and integer SKU matches
# 							if (str(item.get('summary', {}).get('productNumber', '')) == target_sku or
# 									str(item.get('summary', {}).get('productNumber')) == str(
# 										int(target_sku) if target_sku.isdigit() else '')):
# 								product_data = item
# 								print(f"✅✅✅ Found matching product: {target_sku}")
# 								# print(item)
# 								break
# 						else:
# 							print(f"No matching product found for SKU: {target_sku}")
# 					else:
# 						print("❌ No items found in the API response")
# 
# 			except Exception as e:
# 				print(f"⛔️⛔️⛔️Error decoding response body: {e}")
# 	print(f"Product Details Captured")
# 
# 	if product_data:
# 		print(f"Product Data: {product_data}")
# 		row_spec["content_url"] = url
# 		row_spec = get_product_data(product_data, row_spec)
# 	else:
# 		container = wait.until(
# 			EC.presence_of_element_located((By.CSS_SELECTOR, 'ion-row.pdp-summary-info'))
# 		)
# 
# 		product_brand = wait.until(
# 			EC.presence_of_element_located((By.CSS_SELECTOR, 'div.pdp-summary-brand-text'))
# 		).text.strip()
# 
# 		product_name = wait.until(
# 			EC.presence_of_element_located((By.CSS_SELECTOR, 'div.pdp-summary-desc-text'))
# 		)
# 		# Scrape other information from the product page
# 		product_name = product_name.text.strip()
# 		print(product_name)
# 
# 		other_info = wait.until(
# 			EC.presence_of_element_located((By.CSS_SELECTOR, 'div.pdp-summary-other-info-container'))
# 		)
# 
# 		product_sku = other_info.find_element(By.TAG_NAME, 'p').text
# 
# 		product_ps = wait.until(
# 			EC.presence_of_element_located((By.CSS_SELECTOR, 'p.ng-star-inserted'))
# 		).text.strip()
# 		product_sku = product_sku.replace("#", "").strip()
# 		print(product_sku)
# 		print(product_ps)
# 
# 		print("Getting image")
# 		product_image = ""
# 		try:
# 			product_image = container.find_element(By.CSS_SELECTOR, "div.main-image-container img").get_attribute("src")
# 		except Exception as e:
# 			print(f"⛔️⛔️⛔️Error getting product image:")
# 		row_spec["content_url"] = url
# 		row_spec["name"] = product_name
# 		row_spec["pack_size"] = product_ps
# 		row_spec["brand"] = product_brand
# 		row_spec["image"] = product_image
# 
# 	# These use the data if available, then try to scrape from the page
# 	row_spec = get_classification(driver, wait, product_data, row_spec)
# 	row_spec = get_description(driver, wait, data, row_spec)
# 	row_spec = get_manufacturer(driver, wait, data, row_spec)
# 	row_spec = get_additional_info(data, row_spec)
# 
# 	del driver.requests
# 	return row_spec
# 
# 
# def process_products_from_csv(driver, start_row=CSV_START_ROW, filename=URL_OUTPUT_FILE, output_file=DATA_OUTPUT_FILE, test_products=TEST_PRODUCTS, home_dir=DEFAULT_DIRECTORY):
# 	"""
# 	Read product URLs from a CSV file, process each product, and save results to a CSV file.
# 
# 	Args:
# 		driver (WebDriver): WebDriver instance
# 		start_row (int): Row number to start processing from (0-based index)
# 		filename (str): Path to the CSV file containing product URLs
# 		output_file (styr): Path to the output CSV file
# 		test_products (int): Maximum number of products to process
# 		home_dir (str): Home directory for relative paths
# 
# 	"""
# 
# 	filename = get_file_path(filename, home_dir)
# 	output_file = get_file_path(output_file, home_dir)
# 
# 	if not os.path.exists(filename):
# 		print(f"Error: File {filename} not found")
# 		return f"Error: File {filename} not found"
# 
# 	# Define output CSV file
# 	output_filename = output_file
# 	file_exists = os.path.exists(output_filename)
# 	print(f"Output file exists: {file_exists}")  # Print the value of file_exists)
# 
# 	# First count total rows for progress tracking
# 	with open(filename, 'r', encoding='utf-8') as csvfile:
# 		reader = csv.DictReader(csvfile)
# 		total_rows = sum(1 for _ in reader)
# 		print(f"Total rows: {total_rows}")
# 
# 	# Now process the file
# 	with open(filename, 'r', encoding='utf-8') as csvfile:
# 		reader = csv.DictReader(csvfile)
# 
# 		# Skip to start_row
# 		for _ in range(start_row):
# 			next(reader, None)
# 
# 		for row_num, row in enumerate(reader, start=start_row):
# 			row_spec = PRODUCT_DATA_SPEC.copy()
# 			try:
# 				url = row.get('URL', '')
# 				if not url:
# 					continue
# 				if row_num < (start_row + test_products):
# 					print(f"\nProcessing row {row_num + 1}/{total_rows} - {url}")
# 
# 					# Process the product
# 					# Copy values from import file
# 					row_spec['subcategory'] = row.get('Subcategory', '')
# 					row_spec['timestamp'] = row.get('Timestamp', '')
# 					row_spec['content_url'] = row.get('URL', '')
# 					row_spec['sku'] = row.get('SKU', '')
# 					row_spec['category'] = row.get('Category', '')
# 					# Call the product processing function
# 					row_spec = process_product(driver, url, row_spec)
# 
# 					# Write to CSV
# 					print(f"Saving product {row_spec['name']} to {output_filename}")
# 					write_product_to_csv(row_spec, output_filename)
# 
# 					print(f"Saved product {row_spec['name']} to {output_filename}")
# 
# 					time.sleep(1)
# 
# 			except Exception as e:
# 				print(f"⛔️⛔️⛔️Error processing row {row_num + 1}: {e}")
# 				continue
# 
# 	print(f"\nProcessing complete. Results saved to {output_filename}")
# 	return f"<p>Processing complete. Processed {total_rows - start_row} products. Results saved to {output_filename}</p>"
# 
# def process_product_list_search_API(driver, wait, main_window, html, category, sub_category, url_output_file):
# 	# Build a list of product URLs
# 	detail_urls = []
# 
# 	product_wrappers = wait.until(
# 		EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-wrapper'))
# 	)
# 	print(f"Found Product Wrapper: {len(product_wrappers)}")
# 
# 	for request in driver.requests:
# 		# https://panamax-api.ama.usfoods.com/product-domain-api/v2/products
# 		if request.response and "commerce/v2/search" in request.url:  # Filter for API requests
# 			print(f"URL: {request.url}")
# 			print(f"Status Code: {request.response.status_code}")
# 			print(f"Content Type: {request.response.headers.get('Content-Type')}")
# 
# 			# Decode the response body (it's bytes by default)
# 			try:
# 				# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
# 				body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
# 
# 				# If the body is JSON, parse it
# 				if 'application/json' in request.response.headers.get('Content-Type', ''):
# 					data = json.loads(body)
# 					detail_urls = [product['clickUri'] for product in data['products']]
# 					save_urls_to_csv(detail_urls, category, sub_category, url_output_file)
# 				else:
# 					print(f"Response Body (Text): {body}")
# 
# 			except Exception as e:
# 				print(f"⛔️⛔️⛔️Error decoding response body: {e}")
# 	print(f"========= Number of products: {len(detail_urls)}")
# 	del driver.requests
# 	return html, detail_urls
# 
# def process_product_list_search_P_API(driver, wait, main_window, html, category, sub_category, url_output_file):
# 	# Build a list of product URLs
# 	detail_urls = []
# 
# 	product_wrappers = wait.until(
# 		EC.presence_of_all_elements_located((By.TAG_NAME, 'app-selectable-search-result'))
# 	)
# 	print(f"Found Product Wrapper: {len(product_wrappers)}")
# 
# 	for request in driver.requests:
# 		# https://panamax-api.ama.usfoods.com/product-domain-api/v1/search?worksWellWith=true
# 		if request.response and "domain-api/v1/search" in request.url:  # Filter for API requests
# 			print(f"URL: {request.url}")
# 			print(f"Status Code: {request.response.status_code}")
# 			print(f"Content Type: {request.response.headers.get('Content-Type')}")
# 
# 			# Decode the response body (it's bytes by default)
# 			try:
# 				# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
# 				body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
# 
# 				# If the body is JSON, parse it
# 				if 'application/json' in request.response.headers.get('Content-Type', ''):
# 					data = json.loads(body)
# 					# url = f"https://order.usfoods.com/desktop/products/{product_sku}?isSearch=true"
# 					detail_urls = [f"https://order.usfoods.com/products/{product}" for product in data['productNumbers']]
# 					save_urls_to_csv(detail_urls, category, sub_category, url_output_file)
# 				else:
# 					print(f"Response Body (Text): {body}")
# 
# 			except Exception as e:
# 				print(f"⛔️⛔️⛔️Error decoding response body: {e}")
# 	print(f"========= Number of products: {len(detail_urls)}")
# 	del driver.requests
# 	return html, detail_urls
# 
# def create_interceptor(max_api_products=MAX_API_PRODUCTS):
# 	def interceptor(request):
# 		# https://usfoodsproduction10upnbvk4.org.coveo.com/rest/organizations/usfoodsproduction10upnbvk4/commerce/v2/search
# 		# https://panamax-api.ama.usfoods.com/product-domain-api/v1/search?worksWellWith=true
# 		if request.method == 'POST' and 'commerce/v2/search' in request.url:  # Replace 'your_target_url'
# 			print(f"👽👽👽Intercepting request: {request.url}")
# 			# Get the current POST data
# 			current_data = request.body.decode('utf-8')
# 			print(f"Original POST data: {current_data}")
# 
# 			# Modify the POST data
# 			# Example: change a value in a JSON payload
# 			try:
# 				payload = json.loads(current_data)
# 				page = payload.get('page', {})
# 				if int(page) == 0:
# 					payload['page'] = 0  # Replace 'key_to_change' and 'new_value'
# 					payload['perPage'] = max_api_products   # Replace 'key_to_change' and 'new_value'
# 				request.body = json.dumps(payload).encode('utf-8')
# 				# Update the Content-Length header to reflect the new body size
# 				del request.headers['Content-Length']
# 				request.headers['Content-Length'] = str(len(request.body))
# 				print(f"Modified POST data: {request.body.decode('utf-8')}")
# 			except json.JSONDecodeError:
# 				# Handle cases where the body is not JSON
# 				print("Request body is not JSON. Cannot modify in this example.")
# 		if request.method == 'POST' and 'product-domain-api/v1/search' in request.url:  # Replace 'your_target_url'
# 			print(f"👽👽👽Intercepting request: {request.url}")
# 			# Get the current POST data
# 			current_data = request.body.decode('utf-8')
# 			print(f"Original POST data: {current_data}")
# 
# 			# Modify the POST data
# 			# Example: change a value in a JSON payload
# 			try:
# 				payload = json.loads(current_data)
# 				payload['recordsPerPage'] = max_api_products   # Replace 'key_to_change' and 'new_value'
# 				request.body = json.dumps(payload).encode('utf-8')
# 				# Update the Content-Length header to reflect the new body size
# 				del request.headers['Content-Length']
# 				request.headers['Content-Length'] = str(len(request.body))
# 				print(f"Modified POST data: {request.body.decode('utf-8')}")
# 			except json.JSONDecodeError:
# 				# Handle cases where the body is not JSON
# 				print("Request body is not JSON. Cannot modify in this example.")
# 		# https://panamax-api.ama.usfoods.com/product-domain-api/v2/products
# 		if request.method == 'POST' and 'product-domain-api/v2/products' in request.url:
# 			print(f"👽👽👽Intercepting request: {request.url}")
# 			current_data = request.body.decode('utf-8')
# 			print(f"Original POST data: {current_data}")
# 
# 	return interceptor
# 
# def main(options=None):
# 	# driver.scopes = [
# 	# 	'*api/v2/products*',
# 	# 	'*commerce/v2/search*'
# 
# 	if options is None:
# 		options = usfoods_options
# 	print(f"Options: {options}")
# 	# Use the options with fallback to module-level variables
# 	scrape_products = options.get('scrape_products', SCRAPE_PRODUCTS)
# 	reprocess_csv = options.get('reprocess_csv', False)
# 	process_csv = options.get('process_csv', PROCESS_CSV)
# 	dedupe_csv = options.get('dedupe_csv', DEDUPE_CSV)
# 	count_csv = options.get('count_csv', DEDUPE_CSV)
# 	skus_to_check = options.get('skus_to_check', [])
# 	test_products = options.get('test_products', TEST_PRODUCTS)
# 	test_categories = options.get('test_categories', TEST_CATEGORIES)
# 	max_products = options.get('max_products', MAX_API_PRODUCTS)
# 	category_to_process = options.get('category_to_process', 0)
# 	chosen_category = options.get('chosen_category', CHOSEN_CATEGORY)
# 	chosen_category_id = CATEGORY_IDS[chosen_category]
# 	category_name = options.get('chosen_category', CATEGORY_NAMES[chosen_category_id])
# 	url_output_file = options.get('url_output_file', URL_FILE_NAMES[chosen_category_id])
# 	data_output_file = options.get('data_output_file', DATA_FILE_NAMES[chosen_category_id])
# 	csv_start_row = options.get('csv_start_row', CSV_START_ROW)
# 
# 	category_URL = f"https://order.usfoods.com/desktop/search/browse/categories/{chosen_category_id}"
# 
# 	html = ""
# 	all_urls = []
# 	# get the session started
# 
# 	if scrape_products:
# 		driver = seleniumwire_webdriver.Chrome(service=service, options=chrome_options,
# 		                                       seleniumwire_options=seleniumwire_options)
# 
# 		# Wait for the page to be fully loaded
# 		wait = WebDriverWait(driver, 10)
# 		print(f"Scraping products from category {category_name}")
# 		print(f"Output File Name: {url_output_file}")
# 		driver.get(category_URL)
# 		driver.request_interceptor = create_interceptor(max_products)
# 		total_products = 0
# 		loop_counter = 0
# 		category_found_count = 1
# 
# 		html_table = "<table><tr><th>URL</th><th>Name</th><th>SKU</th><th>PS</th><th>Brand</th><th>Image</th><th>Category</th><th>Sub Category</th><th>Classification 1</th><th>Classification 2</th><th>Classification 3</th><th>Description</th><th>Desc 1</th><th>Desc 2</th><th>Desc 3</th><th>Man 1</th><th>Man 2</th><th>Man 3</th></tr></<tbody>"
# 		# Starting on the page for a specific category
# 		print(f"Loading category page {category_URL}")
# 		driver.get(category_URL)
# 		driver.execute_script("document.body.style.zoom = '50%'")
# 
# 		print(f"Page title: {driver.title}")
# 
# 		if category_to_process > 0:
# 			print(f"Category to process: {category_to_process}")
# 			loop_counter = category_to_process - 1
# 			test_categories = category_to_process
# 			category_found_count = category_to_process
# 
# 		while loop_counter < category_found_count and loop_counter < test_categories:
# 			loop_counter += 1
# 			# Target URL for the product category
# 
# 			# Wait for product cards to be present and visible
# 			sub_categories = wait.until(
# 				EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ion-card.md.hydrated'))
# 			)
# 			print(f"Page title: {driver.title}")
# 
# 			category_found_count = len(sub_categories)
# 			print(f"Found {category_found_count} categories to process...")
# 
# 			# Store the main window handle
# 			main_window = driver.current_window_handle
# 
# 			try:
# 				# for category_index, sub_category in enumerate(sub_categories[loop_counter:loop_counter]):
# 				sub_category = sub_categories[loop_counter - 1]
# 				print(f"\nProcessing category {loop_counter } of {category_found_count}...")
# 				driver.execute_script("arguments[0].scrollIntoView();", sub_category)
# 				name_element = WebDriverWait(sub_category, 10).until(
# 					EC.presence_of_element_located((By.CLASS_NAME, 'browse-sub-category-card-description'))
# 				)
# 				sub_category_name = name_element.text.strip()
# 				print(f"Category name: {sub_category_name}")
# 				html += f"<h2>Category Name: {sub_category_name}</h2>"
# 
# 				# Click on the category to open detail page
# 				name_element.click()
# 				print("Clicked on category, waiting for detail page to load...")
# 
# 				# Wait for the detail page to load
# 				time.sleep(12)  # Wait for the page to load
# 				print("Looking for Page: Search New | US Foods")
# 				print(f"Found:           {driver.title}")
# 				print(f"Current URl: {driver.current_url}")
# 
# 				# Find all window handles and switch to the new window if it opens in a new tab
# 				if len(driver.window_handles) > TEST_TABS:
# 					print("must be a tab...")
# 					for handle in driver.window_handles:
# 						if handle != main_window:
# 							driver.switch_to.window(handle)
# 							break
# 				try:
# 					# There are 2 URLS to look for
# 					# https://order.usfoods.com/desktop/search2?correlationId=43939&facetFilters=ec_category:Cheese%252BCHEESE%252C%2520CHEDDAR
# 					# https://order.usfoods.com/desktop/search?searchFilterProperties=336&categoryId=336&pageType=browse&originSearchPage=catalog
# 					if "search2" in driver.current_url:
# 						print("Found search2 page")
# 						time.sleep(6)
# 						html, detail_urls = process_product_list_search_API(driver, wait, main_window, html, category_name, sub_category_name, url_output_file)
# 					else:
# 						print("Found search page")
# 						time.sleep(6)
# 						html, detail_urls = process_product_list_search_P_API(driver, wait, main_window, html, category_name, sub_category_name, url_output_file)
# 					products_found_count = len(detail_urls)
# 					html += f"<div>Found {products_found_count} products for category {sub_category_name}</div>"
# 					print(f"Found {products_found_count} products for category {sub_category_name}")
# 					total_products += products_found_count
# 
# 					all_urls.extend(detail_urls)
# 
# 				except Exception as e:
# 					print(f"****************** ⛔️⛔️⛔️ Error getting details: {e}")
# 					html += f"<div>Name: {sub_category_name} (Error getting details) {loop_counter}</div>"
# 					# driver.quit()
# 					# return html
# 
# 				# Close the detail tab and switch back to the main window
# 				# if len(driver.window_handles) > 2:
# 				# 	driver.close()
# 				# 	driver.switch_to.window(main_window)
# 
# 				driver.back()
# 				print(f"Going back to get next category: {driver.title}")
# 				# Wait before processing next category
# 				time.sleep(3)
# 
# 			except Exception as e:
# 				print(f"⛔️⛔️⛔️Error processing category: {e}")
# 				continue
# 
# 		time.sleep(3)
# 
# 		html_table += "</tbody></table>"
# 		# html_table_to_csv(html_table)
# 		html += f"<h2>Total products found: {total_products}</h2>"
# 		html += html_table
# 		print(f"Total products found: {len(all_urls)}")
# 		driver.quit()
# 	if process_csv:
# 		driver = seleniumwire_webdriver.Chrome(service=service, options=chrome_options,
# 		                                       seleniumwire_options=seleniumwire_options)
# 		print("==Processing CSV==")
# 		print(f"Input File Name: {url_output_file}")
# 		html = process_products_from_csv(driver,
# 			start_row=csv_start_row,
# 			filename=url_output_file,
# 			output_file=data_output_file,
# 			test_products=test_products
# 		)
# 		driver.quit()
# 	if reprocess_csv:
# 		# Check both files to see if data is missing.
# 		driver = seleniumwire_webdriver.Chrome(service=service, options=chrome_options,
# 		                                       seleniumwire_options=seleniumwire_options)
# 		try:
# 			processed, not_found = process_missing_skus(
# 				driver=driver,
# 				skus_to_check=skus_to_check,
# 				url_file=url_output_file,
# 				data_file=data_output_file
# 			)
# 			html += f"<div>Processed {len(processed)} SKUs and {not_found}</div>"
# 		except Exception as e:
# 			print(f"⛔️⛔️⛔️Error processing missing SKUs: {e}")
# 		driver.quit()
# 	if dedupe_csv:
# 		print("==Deduping CSV==")
# 		print(f"Input File Name: {url_output_file}")
# 		html = remove_duplicate_skus(
#             input_file=url_output_file,
#             output_file=f"deduped_{url_output_file}"
#         )
# 	if count_csv:
# 		html = count_csv_rows(url_output_file)  # Defaults to current directory
# 		# Or specify a directory: count_csv_rows('/path/to/csv/files')
# 		return html
# 	# save_urls_to_csv(all_urls)
# 	print("==Finished==")
# 
# 	return html if html else "No products found or unable to process products."