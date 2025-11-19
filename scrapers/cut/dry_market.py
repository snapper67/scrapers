import csv
import json
import os
import sys
import time
from operator import truediv
from urllib.parse import quote
from seleniumwire.utils import decode
from scrapers.cut.dry import CutScraper
from scrapers.scraper import ProductNotFound


class DryMarketScraper(CutScraper):
	SCRAPER_TYPE = 'Cut+Dry Market'
	CUT_PRODUCT_DATA_SPEC = {
		'features': '',
		'extra_data_market': '',
	}
	DEFAULT_DIRECTORY = ''

	# Values to change
	BASE_URL = "https://allstarspecialties.cutanddry.com/market/AllStar/448081160/448081149/quantities?verifiedVendorId=320450261&categoryId=1&page=1"
	SUB_DOMAIN = ""
	CATEGORIES = json.loads('''
	    {
	      "data": {
	        "catalogCategoryOptions": [
	          {
	            "category": {
	              "id": "1",
	              "baseName": "all-items",
	              "name": "All Items",
	              "visibleOnHeader": true,
	              "visibleOnSidebar": true,
	              "__typename": "ProductCategory"
	            },
	            "productCount": 0,
	            "subcategories": [],
	            "__typename": "categoryOption"
	          }
	        ]
	      }
	    }
	    ''')

	VENDOR_NAME = 'Base Market'
	VENDOR_URL_NAME = ''
	VERIFIED_VENDOR_ID = 320450261

	def __init__(self, options=None):
		super().__init__(options)
		self.PRODUCT_DATA_SPEC = self.BASE_PRODUCT_DATA_SPEC.copy()
		for spec in self.CUT_PRODUCT_DATA_SPEC:
			self.PRODUCT_DATA_SPEC[spec] = ''
		print(self.PRODUCT_DATA_SPEC)

	def get_url_name(self):
		return self.VENDOR_URL_NAME

	def build_catalog_url(self, category_id=None, category_name=None, subcategory_id=None, subcategory_name=None,
	                      page=1):
		"""
		Builds the catalog URL with the specified parameters.

		Args:
			category_id (str, optional): The ID of the category to filter by
			category_name (str, optional): The name of the category (will be URL encoded)
			subcategory_id (str, optional): The ID of the subcategory to filter by
			subcategory_name (str, optional): The name of the subcategory (will be URL encoded)
			page (int, optional): The page number to display. Defaults to 1.
			vendor_name (str, optional): The name of the vendor. Will be URL encoded.
			                           Defaults to "BiRite Foodservice Distributors".
			vendor_id (int, optional): The vendor ID. Defaults to 247696227.
			verified_vendor_id (int, optional): The verified vendor ID. Defaults to 120984264.

		Returns:
			str: The complete catalog URL with all parameters
		"""

		from urllib.parse import quote_plus

		print(f"Category Name : {category_name}")
		print(f"Sub Category Name : {subcategory_name}")
		# https://dicarlo.cutanddry.com/market/dicarlo/131360908/131360897/quantities?verifiedVendorId=1861927&categoryId=120859976&categoryName=Spices/Packets&subcategoryId=120859977&subcategoryName=Spices/Packets&page=11
		# https://dicarlo.cutanddry.com/market/DiCarlo/131360908/131360897/quantities?verifiedVendorId=1861927&categoryId=120859976&categoryName=Spices%2FPackets&page=1
		part = self.get_url_name()
		base_url = f"{self.SUB_DOMAIN}/market/{part}/quantities"
		params = {
			'verifiedVendorId': str(self.VERIFIED_VENDOR_ID),
		}

		# Add category parameters if provided
		if category_id:
			params['categoryId'] = str(category_id)
		if category_name:
			params['categoryName'] = str(category_name).replace('/', '%2F').replace(' ', '+')
		if subcategory_id:
			params['subcategoryId'] = str(subcategory_id)
		if subcategory_name:
			# Replace spaces with + as shown in the example URL
			params['subcategoryName'] = str(subcategory_name).replace('/', '%2F').replace(' ', '+')
		if page > 1:
			params['page'] = str(page)

		# Convert params to URL query string
		query_string = '&'.join(f"{k}={v}" for k, v in params.items())
		return f"{base_url}?{query_string}"

	def build_product_url(self, product_id=None):
		"""
		Builds the catalog URL with the specified parameters.

		Args:
			product_id (str, optional): The ID of the category to filter by
			vendor_id (int, optional): The vendor ID. Defaults to 247696227.
			verified_vendor_id (int, optional): The verified vendor ID. Defaults to 120984264.

		Returns:
			str: The complete catalog URL with all parameters
		"""
		# URL encode the vendor name and other string parameters
		print(f"Product ID : {product_id}")
		part = self.get_url_name()
		base_url = f"{self.SUB_DOMAIN}/market/{part}/quantities?origin=catalog&verifiedVendorId={self.VERIFIED_VENDOR_ID}&canonicalProduct={product_id}&srcPge=Catalog&srcLoc=Catalog+Category+Filtered"

		return f"{base_url}"

	def save_urls_to_csv(self ,urls, category_name="", subcategory_name="", sub_subcategory_name=""):
		"""
		Save a list of URLs to a CSV file. If the file exists, it will append to it.

		Args:
			urls (list): List of URLs to save
			category_name (str): Name of the category
			subcategory_name (str): Name of the sub category
			sub_subcategory_name (str): Name of the sub category of the sub category
		"""
		import csv
		import os
		from datetime import datetime

		print(f"save_urls_to_csv()")
		# print(f"save_urls_to_csv(){urls}")

		# Resolve the file path
		home_dir = self.options.get('home_directory')
		filename = self.get_url_file_path(home_dir)

		# Ensure the directory exists
		os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)

		file_exists = os.path.isfile(filename)

		print(f"Home Directory: {home_dir}, Filename: {filename}")

		try:
			with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
				writer = csv.writer(csvfile)

				# Write header only if file is new
				if not file_exists:
					writer.writerow(['SKU', 'URL', 'Timestamp', 'Category', 'Subcategory', "Sub Subcategory"])

				# Write each URL with timestamp
				for url in urls:
					clean_url = url.rstrip('/')
					# First try to get SKU from canonicalProduct query parameter
					try:
						from urllib.parse import urlparse, parse_qs
						parsed_url = urlparse(clean_url)
						query_params = parse_qs(parsed_url.query)
						sku = query_params.get('canonicalProduct', [None])[0]
						if not sku:
							# Fall back to the original behavior if canonicalProduct not found
							sku = clean_url.split('/')[-1].split('?')[0]
					except Exception:
						# If any error occurs, use the original behavior
						sku = clean_url.split('/')[-1].split('?')[0]

					writer.writerow(
							[sku, url, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), category_name, subcategory_name, sub_subcategory_name])

			mode = "Appended to" if file_exists else "Created new"
			print(f"Successfully {mode} {len(urls)} URLs to {filename}")

		except Exception as e:
			print(f"⛔️⛔️⛔️Error saving URLs to CSV: {e}")

	def wait_and_process_products_urls(self, html, all_urls, category, subcat='', subcat_name='', include_subcategories=True):
		still_looking = True
		page = 0
		test_products = self.options.get('test_products', 0)
		print(f"wait_and_process_products()")
		while still_looking and page < self.options['max_products']:
			page = page + 1
			if page * self.options['max_products'] > test_products:
				# We have reached the maximum number of products we
				break
			category_name = category.get('category', {})['name']
			self.options['url_output_file'] = self.make_filename_safe(category_name.lower()) + "_product_urls.csv"
			if include_subcategories:
				subcat_name = subcat['name']
				url = self.build_catalog_url(category_id=category.get('category', {})['id'],
				                             category_name=category_name,
				                             subcategory_id=subcat['id'], subcategory_name=subcat['name'], page=page)
			else:
				url = self.build_catalog_url(category_id=category.get('category', {})['id'],
				                             category_name=category_name,
				                             page=page)
			print(f"Loading page...{url}")
			del self.driver.request_interceptor
			self.driver.request_interceptor = self.create_interceptor(self.options['max_products'], page=page)
			del self.driver.requests
			self.driver.get(url)
			print(f"URL Loaded")
			print(f"Page : {page}")

			first_found = False
			attempts = 0

			print("Processing Requests")
			while not first_found and attempts < self.options['attempts']:
				time.sleep(1)
				attempts += 1
				print(f"attempt: {attempts}")
				filter_criteria = self.GRAPHQL_API_FILTER
				for request in self.driver.requests:
					if request.response and filter_criteria in request.url:  # Filter for API requests
						current_data = request.body.decode('utf-8')
						# print(f"current_data: {current_data}")
						payload = json.loads(current_data)
						print(f"Payload Method: {payload.get('operationName', '')}")
						if payload.get('operationName', '') == self.SEARCH_API_OPERATION:
							print(f"{self.SEARCH_API_OPERATION} found")
							print(f"URL: {request.url}")
							print(f"Status Code: {request.response.status_code}")
							print(f"Content Type: {request.response.headers.get('Content-Type')}")
							try:
								body = decode(request.response.body,
								              request.response.headers.get('Content-Encoding', 'identity'))

								# If the body is JSON, parse it
								if 'application/json' in request.response.headers.get('Content-Type', ''):
									data = json.loads(body)

									# 08/18/25 new api was released a contextual product wrapper was added
									if self.JSON_CONTEXTUAL_PRODUCTS in data.get('data', {}).get('catalogProductsRootQuery', {}):
										print(f"Response contextual products: TRUE ")
										print(f"Response: {json.dumps(data)}")
										first_found = True
										detail_urls = [
											self.build_product_url(product.get('canonicalProduct', {}).get('id', ''))
											for product in data.get('data', {}).get('catalogProductsRootQuery', {}).get(
												self.JSON_CONTEXTUAL_PRODUCTS, [])]
										print(f"== Number of products: {len(detail_urls)}")
										all_urls.extend(detail_urls)
										html += f"<h2>{category_name} -> {subcat_name} -> page {page}</h2>"
										html += "<div>Products found: " + str(len(detail_urls)) + "</div>"
										self.save_urls_to_csv(detail_urls, category_name, subcat_name)
										print(f"=== Number of products: {len(detail_urls)}")

										if len(detail_urls) < self.options['max_products']:
											still_looking = False
										break
									else:
										print(
											f"Response contextual products ({self.JSON_CONTEXTUAL_PRODUCTS}) missing: {self.JSON_CONTEXTUAL_PRODUCTS in data} ")

									if self.JSON_CANONICAL_PRODUCTS in data.get('data', {}).get('catalogProductsRootQuery', {}):
										print(f"Response products: TRUE")
										first_found = True
										detail_urls = [
											self.build_product_url(product.get('id', ''))
											for product in data.get('data', {}).get('catalogProductsRootQuery', {}).get(
												self.JSON_CANONICAL_PRODUCTS, [])]
										print(f"== Number of products: {len(detail_urls)}")
										all_urls.extend(detail_urls)
										html += f"<h2>{category_name} -> {subcat_name} -> page {page}</h2>"
										html += "<div>Products found: " + str(len(detail_urls)) + "</div>"
										self.save_urls_to_csv(detail_urls, category_name, subcat_name)
										print(f"=== Number of products: {len(detail_urls)}")

										if len(detail_urls) < self.options['max_products']:
											still_looking = False
										break
									else:
										print(f"Response canonical products ({self.JSON_CANONICAL_PRODUCTS}) missing: {self.JSON_CANONICAL_PRODUCTS in data} ")
								# print(f"data: {data} ")

								else:
									print(f"Response Body (Text): ")
									print(f"Response not JSON  ")

							except Exception as e:
								print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

					# del self.driver.request_interceptor
			del self.driver.requests
		print(f"wait_and_process_products() complete")
		return html, all_urls

	def get_price(self, data, row_spec):
		print("get_price()")
		try:
			data = data.get('data', {}).get('canonicalProduct', {})
			row_spec['pack'] = data.get('pack', '')
			row_spec['size'] = data.get('size', '')
			row_spec['item_size'] = data.get('itemSize', '')
			product_shop_data_for_store = data.get('productShopDataForStore', None)
			# Find the specification with displayName "Manufacturer Name"
			if product_shop_data_for_store:
				consumer_price = product_shop_data_for_store.get('consumerPrice', None)
				if consumer_price:
					row_spec['retail_price'] = int(consumer_price['float'] * 100)
			else:
				print("⚠️ Price not found in specifications")

		except Exception as e:
			print(f"⛔️ Error processing price information: {type(e).__name__} - {str(e)}")

		print("Processing price information complete...")
		return row_spec

	def get_product_details(self, url, row_spec=None):
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print("processing product detail page")
		print(f"Loading page...{url}")

		data = ''
		# We used an id to identify the product
		row_spec['id'] = row_spec['sku']
		del self.driver.requests
		self.driver.get(url)
		print(f"Sent Request")
		try:
			request = self.driver.wait_for_request(self.GRAPHQL_API_FILTER)
			first_found = False
			second_found = False
			third_found = False
			found_all = False
			attempts = 0

			# Stop if we found first or second and third

			while not found_all and attempts < self.options['attempts']:
				time.sleep(1)
				attempts += 1
				print(f"attempt: {attempts}")
				for request in self.driver.requests:
					if request.response and self.GRAPHQL_API_FILTER in request.url:  # Filter for API requests
						current_data = request.body.decode('utf-8')
						payload = json.loads(current_data)
						print(f"Payload Method: {payload.get('operationName', '')}")
						if payload.get('operationName', '') == self.PRODUCT_API_OPERATION and not first_found:
							first_found = True
							try:
								body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

								# If the body is JSON, parse it
								if 'application/json' in request.response.headers.get('Content-Type', ''):
									data = json.loads(body)
								else:
									print(f"Response Body (Text): {body}")

							except Exception as e:
								print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

							# These use the data if available, then try to scrape from the page
							row_spec["extra_data_1"] = json.dumps(data)
							row_spec = self.get_product_data(data, row_spec)
						elif payload.get('operationName', '') == 'canonicalProductQuery' and not second_found:
							second_found = True
							try:
								# body = request.response.body.decode(request.response.headers.get('Content-Encoding', 'identity'))
								body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))

								# If the body is JSON, parse it
								if 'application/json' in request.response.headers.get('Content-Type', ''):
									data = json.loads(body)
								else:
									print(f"Response Body (Text): {body}")

							except Exception as e:
								print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")
							row_spec['extra_data_2'] = json.dumps(data)
						elif payload.get('operationName', '') == 'canonicalProductQueryForUPDPage'  and not third_found:
							third_found = True
							try:
								body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
								# If the body is JSON, parse it
								if 'application/json' in request.response.headers.get('Content-Type', ''):
									data = json.loads(body)
								else:
									print(f"Response Body (Text): {body}")

							except Exception as e:
								print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")
							row_spec['extra_data_market'] = json.dumps(data)
							print("getting price")
							row_spec = self.get_price(data, row_spec)
						elif payload.get('operationName', '') == 'TrackPDPViewedMutation':
							# we got to the end but did not find our target response. This sometimes happens
							attempts = 40
				found_all = (first_found or second_found) and third_found
			if not first_found and not second_found:
				raise ProductNotFound
			if second_found and not first_found:
				row_spec = self.get_product_data_2(row_spec)
		except Exception as e:
			print(f"⛔️⛔️⛔️Error waiting for request: {e}")

		return row_spec

	def get_more_extra_data(self, row):
		print("get_more_extra_data()")
		try:
			row = self.get_product_data_2(row)
			extra_data_market = row['extra_data_market']
			if isinstance(extra_data_market, str):
				try:
					extra_data = json.loads(extra_data_market)
					if extra_data:
						row = self.get_price(extra_data, row)
				except json.JSONDecodeError as e:
					# If it's not valid JSON, keep it as is
					print(
						f"⛔️⛔️⛔️Error getting JSON in extra_data_market for SKU {row.get('sku', 'unknown')}: {e}")
			print("get_more_extra_data() Complete")
			return row

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing more extra data: {e}")

	def display_product_details_sample(self, csv_path='product_data_url.csv', num_rows=3):
		"""
		Display details for the first few rows from a product data CSV file.
		
		Args:
			csv_path (str): Path to the CSV file containing product data
			num_rows (int): Number of rows to display (default: 3)
		"""
		try:
			# Check if file exists
			if not os.path.exists(csv_path):
				print(f"Error: File '{csv_path}' not found.")
				return
			
			# Read the CSV file
			with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
				reader = csv.DictReader(csvfile)
				
				# Get the first 'num_rows' rows
				display_count = 0
				for idx, row in enumerate(reader):
					if display_count >= num_rows:
						break
					
					print(f"\n=== Product {idx + 1} ===")
					print("-" * 50)
					
					# Display all fields that have values
					for field in self.PRODUCT_DATA_SPEC.keys():
						if field in row and row[field]:
							# Truncate long values for better display
							value = str(row[field])
							if len(value) > 100:  # Truncate very long values
								value = value[:97] + '...'
							print(f"{field:25}: {value}")
					
					display_count += 1
					print("-" * 50)
			
			if display_count == 0:
				print(f"No data found in {csv_path}")
			else:
				print(f"\nDisplayed {display_count} products from {csv_path}")
				
		except Exception as e:
			print(f"Error reading {csv_path}: {str(e)}")
