import csv
import json
import os
import sys
import time
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

from scrapers.scraper import Scraper, SkuNotFound

"""
	City Hive
	Type: Standard shop website
	Method: 
		Get Categories: Scape Navigation
		Get Products: Scape Product List
		Get Product Manual Scrape and json data from html
	Issues:
		The embedded json data does not have all the information needed to create a product. Data like 
		sku and description are not included in the json data.
"""

class HiveScraper(Scraper):
	HIVE_PRODUCT_DATA_SPEC = {
		'vintage': '',
		'varietal': '',
		'appellation': '',
		'bpc': '',
		'supplier': '',
		'producer': '',
		'region': '',
		'country_of_origin': '',
		'alcohol_proof': '',
		'alcohol_by_volume': '',
		'sub-type': '',
		'producer_description': '',
		'container_type': '',
		'closure_type': '',
		'units_per_case': '',
		'packs_per_case': '',
		'units_per_pack': '',
		'outer_pkg': '',
		'product_id': '',
		'option_id': '',
		'page_description': '',
		'page_image': '',
		'page_sku': '',
		'page_pack_size': '',
		'state': '',
	}

	SCRAPER_TYPE = 'City Hive'

	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/empire_metro/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = ''
	VENDOR_NAME = ''
	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "name": "Wine",
        "id": 2,
        "url": "https://empire360.com/shop/?type=Wine",
        "subcategories": [
          {
            "name": "By Style",
            "url": "",
            "subcategories": [
              {
                "name": "Red",
                "url": "https://empire360.com/shop/?subtype=red"
              },
              {
                "name": "White",
                "url": "https://empire360.com/shop/?subtype=white"
              },
              {
                "name": "Ros\u00e9 & Blush",
                "url": "https://empire360.com/shop/?subtype=rose"
              },
              {
                "name": "Champagne & Sparkling",
                "url": "https://empire360.com/shop/?subtype=sparkling"
              },
              {
                "name": "Dessert & Port",
                "url": "https://empire360.com/shop/?subtype=dessert&subtype=port"
              },
              {
                "name": "Other Wines",
                "url": "https://empire360.com/shop/?category=other_wine&title=Other+Wine"
              }
            ]
          },
          {
            "name": "By Varietal",
            "url": "",
            "subcategories": [
              {
                "name": "Cabernet Sauvignon",
                "url": "https://empire360.com/shop/?category=cabernet_sauvignon_name&title=Cabernet%20Sauvignon"
              },
              {
                "name": "Chardonnay",
                "url": "https://empire360.com/shop/?category=chardonnay_name&title=Chardonnay"
              },
              {
                "name": "Sauvignon Blanc",
                "url": "https://empire360.com/shop/?category=sauvignon_blanc_name&title=Sauvignon%20Blanc"
              },
              {
                "name": "Red Blends",
                "url": "https://empire360.com/shop/?varietal=red+blend"
              },
              {
                "name": "Pinot Noir",
                "url": "https://empire360.com/shop/?category=pinot_noir_name&title=Pinot%20Noir"
              },
              {
                "name": "Pinot Grigio",
                "url": "https://empire360.com/shop/?category=pinot_grigio_name&title=Pinot%20Grigio"
              },
              {
                "name": "Rose",
                "url": "https://empire360.com/shop/?varietal=rose"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "France",
                "url": "https://empire360.com/shop/?type=wine&country=france"
              },
              {
                "name": "Italy",
                "url": "https://empire360.com/shop/?type=wine&country=italy"
              },
              {
                "name": "Spain",
                "url": "https://empire360.com/shop/?type=wine&country=spain"
              },
              {
                "name": "Germany",
                "url": "https://empire360.com/shop/?type=wine&country=germany"
              },
              {
                "name": "Argentina",
                "url": "https://empire360.com/shop/?type=wine&country=argentina"
              },
              {
                "name": "United States",
                "url": "https://empire360.com/shop/?type=wine&country=united%20states"
              },
              {
                "name": "New Zealand",
                "url": "https://empire360.com/shop/?type=wine&country=new%20zealand"
              }
            ]
          },
          {
            "name": "By Region",
            "url": "",
            "subcategories": [
              {
                "name": "Bordeaux",
                "url": "https://empire360.com/shop/?type=wine®ion=bordeaux"
              },
              {
                "name": "Tuscany",
                "url": "https://empire360.com/shop/?type=wine®ion=tuscany"
              },
              {
                "name": "Rioja",
                "url": "https://empire360.com/shop/?type=wine®ion=rioja"
              },
              {
                "name": "Burgundy",
                "url": "https://empire360.com/shop/?type=wine®ion=burgundy"
              },
              {
                "name": "Napa Valley",
                "url": "https://empire360.com/shop/?type=wine®ion=napa%20valley"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://empire360.com/shop?group-id=62c43e4c8301df4064ffb563&title=New+Arrivals&type=Wine"
              },
              {
                "name": "Wine Combo Packs",
                "url": "https://empire360.com/shop/product-groups/wine-combo-packs"
              },
              {
                "name": "Cans",
                "url": "https://empire360.com/shop/product-groups/cans?type=Wine"
              },
              {
                "name": "Kegs",
                "url": "https://empire360.com/shop/product-groups/kegs"
              },
              {
                "name": "Wine-Only License Products",
                "url": "https://empire360.com/shop/product-groups/wine-only-license-products"
              },
              {
                "name": "My Past Purchased Wine",
                "url": "https://empire360.com/shop/?type=Wine&customer_purchased_products=true"
              },
              {
                "name": "All Wine",
                "url": "https://empire360.com/shop/?type=wine"
              }
            ]
          }
        ]
      },
      {
        "name": "Spirits",
        "id": 3,
        "url": "https://empire360.com/shop/?type=Spirits",
        "subcategories": [
          {
            "name": "By Type",
            "url": "",
            "subcategories": [
              {
                "name": "Vodka",
                "url": "https://empire360.com/shop/?subtype=vodka"
              },
              {
                "name": "Whiskey",
                "url": "https://empire360.com/shop/?subtype=whiskey"
              },
              {
                "name": "Sake",
                "url": "https://empire360.com/shop/?subtype=sake"
              },
              {
                "name": "Tequila",
                "url": "https://empire360.com/shop/?subtype=tequila"
              },
              {
                "name": "Rum",
                "url": "https://empire360.com/shop/?subtype=rum"
              },
              {
                "name": "Gin",
                "url": "https://empire360.com/shop/?subtype=gin"
              },
              {
                "name": "Brandy",
                "url": "https://empire360.com/shop/?subtype=brandy"
              },
              {
                "name": "Liqueur",
                "url": "https://empire360.com/shop/?subtype=liqueur"
              }
            ]
          },
          {
            "name": "By Country",
            "url": "",
            "subcategories": [
              {
                "name": "United States",
                "url": "https://empire360.com/shop/?type=spirits&country=united%20states"
              },
              {
                "name": "France",
                "url": "https://empire360.com/shop/?type=spirits&country=france"
              },
              {
                "name": "Ireland",
                "url": "https://empire360.com/shop/?type=spirits&country=ireland"
              },
              {
                "name": "Japan",
                "url": "https://empire360.com/shop/?type=spirits&country=japan"
              },
              {
                "name": "Italy",
                "url": "https://empire360.com/shop/?type=spirits&country=italy"
              },
              {
                "name": "Mexico",
                "url": "https://empire360.com/shop/?type=spirits&country=mexico"
              }
            ]
          },
          {
            "name": "Explore",
            "url": "",
            "subcategories": [
              {
                "name": "New Arrivals",
                "url": "https://empire360.com/shop?group-id=62c43e4c8301df4064ffb563&title=New+Arrivals&type=Spirits"
              },
              {
                "name": "Spirits Combo Packs",
                "url": "https://empire360.com/shop/product-groups/spirits-combo-packs"
              },
              {
                "name": "Cans",
                "url": "https://empire360.com/shop/product-groups/cans?type=Spirits"
              },
              {
                "name": "My Past Purchased Spirits",
                "url": "https://empire360.com/shop/?type=Spirits&customer_purchased_products=true"
              },
              {
                "name": "All Spirits",
                "url": "https://empire360.com/shop/?type=spirits"
              }
            ]
          }
        ]
      },
      {
        "name": "Shop By Brand",
        "id": 4,
        "url": "https://empire360.com/shop/?container-id=6194f35920459128ccff17cd&title=Shop+By+Brand",
        "subcategories": [
          {
            "name": "Shop Divisions",
            "url": "",
            "subcategories": [
              {
                "name": "Shop Freedom",
                "url": "https://empire360.com/pages/mhusa-metro"
              }
            ]
          }
        ]
      },
      {
        "name": "Payments, Invoices & Orders",
        "id": 5,
        "url": "https://empire360.com/profile?section=payments&sub_section=invoices&Status=Open",
        "subcategories": [
          {
            "name": "Order History",
            "url": "",
            "subcategories": [
              {
                "name": "Past Orders",
                "url": "https://empire360.com/profile?section=order_history"
              },
              {
                "name": "My Past Purchased Items",
                "url": "https://empire360.com/shop/?customer_purchased_products=true"
              }
            ]
          },
          {
            "name": "Bill and Store",
            "url": "",
            "subcategories": [
              {
                "name": "Release Stored Items",
                "url": "https://empire360.com/shop?list_name=stored_items"
              },
              {
                "name": "How Do I? - Bill and Store",
                "url": "https://empire360.com/pages/billandstorehowdoi/"
              }
            ]
          },
          {
            "name": "Empire360 Bill Pay",
            "url": "",
            "subcategories": [
              {
                "name": "View & Pay Invoices",
                "url": "https://empire360.com/profile?section=payments&sub_section=invoices&Status=Open"
              },
              {
                "name": "View Payments",
                "url": "https://empire360.com/profile?section=payments&sub_section=payments+"
              },
              {
                "name": "Manage Bank Accounts",
                "url": "https://empire360.com/profile?section=payments&sub_section=banking"
              },
              {
                "name": "Pay On Account",
                "url": "https://empire360.com/checkout?payment-id=on-account-payment"
              }
            ]
          },
          {
            "name": "Empire360 Bill Pay Help",
            "url": "",
            "subcategories": [
              {
                "name": "How Do I? - Bill Pay",
                "url": "https://cityhive-prod-cdn.cityhive.net/media_gallery/distributor/6064695850a0357d42357a6a/pdf/681ca06a9724d91dc0e3466e.pdf?1746706538"
              },
              {
                "name": "Start Bill Pay - FAQ",
                "url": "https://empire360.com/pages/startbillpay/"
              }
            ]
          }
        ]
      },
      {
        "name": "Customer Service",
        "id": 6,
        "url": "https://empire360.com/profile",
        "subcategories": [
          {
            "name": "GENERAL - Empire North",
            "url": "",
            "subcategories": [
              {
                "name": "Customer Service North",
                "url": "https://empirenorth.com/customers/customers-service/#service-form"
              },
              {
                "name": "Policies & Updates North",
                "url": "https://empirenorth.com/customers/policies-announcements/#policy-docs"
              },
              {
                "name": "Announcements North",
                "url": "https://empirenorth.com/customers/policies-announcements/#announce"
              },
              {
                "name": "Become a Customer North",
                "url": "https://empirenorth.com/customers/new-customer/"
              }
            ]
          },
          {
            "name": "GENERAL - Empire Metro",
            "url": "",
            "subcategories": [
              {
                "name": "Customer Service Metro",
                "url": "https://csform.empiremerchants.com/"
              },
              {
                "name": "Policies & Updates Metro",
                "url": "https://www.empiremerchants.com/customers/policies-announcements/#policy-docs"
              },
              {
                "name": "Announcements Metro",
                "url": "https://www.empiremerchants.com/customers/policies-announcements/#announce"
              },
              {
                "name": "Become a Customer Metro",
                "url": "https://www.empiremerchants.com/customers/new-customer/"
              },
              {
                "name": "Customer Service Request Form - Metro",
                "url": "https://csform.empiremerchants.com/"
              }
            ]
          },
          {
            "name": "HOW-TO VIDEOS",
            "url": "",
            "subcategories": [
              {
                "name": "Overview",
                "url": "https://empire360.com/pages/how-to-videos#overview"
              },
              {
                "name": "Registration & Login",
                "url": "https://empire360.com/pages/how-to-videos#register"
              },
              {
                "name": "Pricing",
                "url": "https://empire360.com/pages/how-to-videos#pricing"
              },
              {
                "name": "Assortments",
                "url": "https://empire360.com/pages/how-to-videos#assortments"
              }
            ]
          },
          {
            "name": "QUICK GUIDES",
            "url": "",
            "subcategories": [
              {
                "name": "Register & Add Users",
                "url": "https://empire360.com/pages/register"
              },
              {
                "name": "Start Bill Pay - FAQ",
                "url": "https://empire360.com/pages/startbillpay/"
              },
              {
                "name": "How Do I? - Bill Pay",
                "url": "https://cityhive-prod-cdn.cityhive.net/media_gallery/distributor/6064695850a0357d42357a6a/pdf/681ca06a9724d91dc0e3466e.pdf?1746706538"
              },
              {
                "name": "Empire360 Bill & Store Metro",
                "url": "https://d3omj40jjfp5tk.cloudfront.net/media_gallery/distributor/6064695850a0357d42357a6a/pdf/648a1b0853dac92aded955dc.pdf?1686772488"
              },
              {
                "name": "Empire360 Bill & Store North",
                "url": "https://d3omj40jjfp5tk.cloudfront.net/media_gallery/distributor/6064695850a0357d42357a6a/pdf/648a1afe56bea24b8ea3df3b.pdf?1686772478"
              }
            ]
          }
        ]
      },
      {
        "name": "Monthly Pricing",
        "id": 7,
        "url": "https://empire360.com/#",
        "subcategories": []
      }
    ]
  }
}
                                         
		''')

	def __init__(self, options=None):
		super().__init__(options, headless=False)
		# self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		# self.options['home_directory'] = self.DEFAULT_DIRECTORY
		# self.options['base_url'] = self.BASE_URL
		# There are only 2 navigation categories we want to process and we only want to process 1 sub category
		self.options['test_categories'] = 8
		self.PRODUCT_DATA_SPEC = self.BASE_PRODUCT_DATA_SPEC.copy()
		for spec in self.HIVE_PRODUCT_DATA_SPEC:
			self.PRODUCT_DATA_SPEC[spec] = ''
		print(self.PRODUCT_DATA_SPEC)

	def bypass_cookie_consent(self, url):
		print("bypass_cookie_consent()")
		try:
			self.driver.get(url)
			# time.sleep(2)
			modal = self.wait.until(
				EC.presence_of_element_located((By.ID, 'consent-banner'))
			)
			select = self.driver.find_element(By.ID, 'truste-consent-button')
			select.click()
			print("Bypassed cookie consent")
		except Exception as e:
			print(f"Error: {e}")

	def scraping_setup(self):
		"""Scrape products from the website"""
		print("scraping_setup()")
		self.bypass_cookie_consent(self.BASE_URL)
		return

	def get_unique_keys(self, data_file):
		""" Some websites do not use SKU as the unique identifier"""
		keys = set()
		if os.path.exists(data_file):
			with open(data_file, 'r', newline='', encoding='utf-8') as f:
				reader = csv.DictReader(f)
				csv.field_size_limit(sys.maxsize)
				if 'option_id' in reader.fieldnames:
					keys = {row['option_id'] for row in reader}
		return keys

	# ************************************************************************
	# Utility Functions
	# ************************************************************************

	@staticmethod
	def extract_unique_id_from_url(url):
		"""
		Get a unique identifier from the url.
		https://empire360.com/shop?product-id=57aa2a3f69702d628dbdc600&option-id=4d3feb910fa16b9fd8409ff3103e9ef639d68c2c606d5967ce66b6ecff6cb157
		"""

		parsed_url = urlparse(url)
		params = parse_qs(parsed_url.query)
		
		sku = params.get('option-id', [''])[0]
		
		return sku

	# ************************************************************************
	# 	Product Scraping Functions
	# ************************************************************************

	def get_first_image_url(self, data):
		"""
		Extract the first available image URL from the product detail page.

		Args:
			row_spec (dict): the row that will be written to the output file

		Returns:
			str: URL of the first available image, or None if no image found
		"""
		print("get_first_image_url()")
		image_url = ''
		try:

			image_url = data.get("image", "")

		except Exception as e:
			print(f"Error extracting image from page: {str(e)}")

		return image_url

	def get_first_image_url_scrape(self):
		"""
		Extract the first available image URL from the product detail page.

		Args:

		Returns:
			str: URL of the first available image, or None if no image found
		"""
		print("get_first_image_url_scrape()")
		image_url = ''
		try:
			image_element = self.driver.find_element(By.CSS_SELECTOR, ".ch-product-page .product-image-container [data-hook='loaded-product-image']")
			self.print_element(image_element)
			image_url = image_element.get_attribute("src")

		except NoSuchElementException as e:
			print(f"No Image found")
		except Exception as e:
			print(f"⛔️️ Error processing get_first_image_url_scrape: {type(e)}")
		print(image_url)
		return image_url

	def get_product_data(self, data, row_spec):
		print("processing product data from response...")
		if data:
			try:
				row_spec["image"] = self.get_first_image_url(data)
				row_spec["product_id"] = data.get("product_id", "")

				row_spec = self.parse_product_schema(data, row_spec)

				print(row_spec['brand'])
				row_spec['brand'] = row_spec['brand'][0].get('name', '')
				print("Getting price")
				retail_price = data.get('offers', {}).get('price', '')
				if retail_price:
					retail_price = int(retail_price * 100)
				print(retail_price)
				row_spec['retail_price'] = retail_price
				row_spec["extra_data_1"] = json.dumps(data)

			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing get_product_data Complete...")

		return row_spec

	def get_product_data_2(self, data, row_spec):
		print("processing product data 2 from response...")
		print(data)
		if data:
			try:
				row_spec = self.parse_product_schema(data, row_spec)
				print("Getting pack size")
				row_spec['pack_size'] = row_spec['size']
				print(row_spec['pack_size'])
				row_spec['size'] = row_spec['pack_size'].get('measure', '')
				row_spec['pack'] = row_spec['pack_size'].get('quantity', '')
				row_spec["extra_data_2"] = json.dumps(data)

			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing get_product_data Complete...")
		return row_spec

	def get_more_extra_data(self, row):
		print("get_more_extra_data()")
		try:
			extra_data_2 = row['extra_data_2']
			if isinstance(extra_data_2, str):
				try:
					extra_data = json.loads(extra_data_2)
					if extra_data:
						row = self.get_product_data_2(extra_data, row)
				except json.JSONDecodeError as e:
					# If it's not valid JSON, keep it as is
					print(
						f"⛔️⛔️⛔️Error getting JSON in extra_data_market for SKU {row.get('sku', 'unknown')}: {e}")
			print("get_more_extra_data() Complete")
			return row

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing more extra data: {e}")

	def get_table_section(self, row_spec):
		# Scrape the section that contains the manufacturer information. It is in an unordered list
		print("get_table_section()")
		#product-info-table-container
		details = self.driver.find_element(By.CSS_SELECTOR, 'div.product-info-table-container')
		print(details)
		try:
			hidden_element = self.driver.find_element(By.CSS_SELECTOR, '.product-info-table-container div.product-info-hide')
			self.driver.execute_script("arguments[0].style.display = 'block';", hidden_element)
		except Exception as e:
			print(f"No hidden element: {type(e)}")
		try:
			rows = details.find_elements(By.CSS_SELECTOR, 'div.g-row')
			print(rows)
			for row in rows:
				key = row.find_element(By.CSS_SELECTOR, '.product-info-table-left').text.strip()
				key = key.lower().replace(' ', '_').replace('_(%)', '')
				print(key)
				value = row.find_element(By.CSS_SELECTOR, '.product-info-table-right').text.strip()
				if key in self.PRODUCT_DATA_SPEC.keys():
					row_spec[key] = value

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing table data: {type(e)}")
		return row_spec

	def get_merchant_section(self, data, row_spec):
		# Scrape the section that contains the manufacturer information. It is in an unordered list
		print("get_merchant_section()")
		try:
			if not data or 'merchants' not in data or not data['merchants']:
				return row_spec

			merchant_info = data['merchants'][0]
			if 'product_options' in merchant_info and merchant_info['product_options']:
				print("getting merchant data")
				product_options = merchant_info['product_options'][0]
				row_spec['product_id'] = product_options.get('product_id', '')
				option_params = product_options.get('option_params', {})
				row_spec['vintage'] = option_params.get('vintage', '')
				print("getting additional_properties data")
				additional_properties = option_params.get('additional_properties', {})
				row_spec['sku'] = additional_properties.get('sku', '')
				row_spec['country_of_origin'] = additional_properties.get('country', '')
				row_spec['closure_type'] = additional_properties.get('closure', '')

				option_display = product_options.get('option_display_data', {})
				if option_display:
					props = option_display.get('properties', {})
					row_spec['varietal'] = props.get('varietal', [''])[0] if isinstance(props.get('varietal'), list) else props.get('varietal', '')
					row_spec['region'] = props.get('region', '')
					row_spec['state'] = props.get('state', '')
					row_spec['country_of_origin'] = props.get('country', '')

				# Extract units of measure
				units = product_options.get('units_of_measure', [])
				if units:
					# Get the first unit of measure (usually the smallest)
					unit = units[0]
					row_spec['ordering_unit'] = unit.get('unit_name', '')
					row_spec['units_per_pack'] = unit.get('num_of_base_units', '')

					# If there's a case size (usually the second unit)
					if len(units) > 1:
						row_spec['units_per_case'] = units[1].get('num_of_base_units', '')

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing variant data: {type(e)}")
		return row_spec

	def get_description(self, row_spec):
		print("get_description()")
		self.driver.execute_script("document.body.style.zoom = '20%'")
		try:
			description = self.driver.find_element(By.CSS_SELECTOR, "[data-hook='product-description']").text.strip()
			print(description)
			if description:
				print("here")
				row_spec["page_description"] = description
		except NoSuchElementException as e:
			print(f"No Description found")
		except Exception as e:
			print(f"⛔️️ Error processing product description: {type(e)}")
			print(f"⛔️️ Error processing product description: {e}")

		print("processing product description Complete...")
		return row_spec

	def get_pack_size_from_html(self, row_spec):
		print("get_pack_size()")
		self.driver.execute_script("document.body.style.zoom = '20%'")
		try:
			pack_size_text = self.driver.find_element(By.CSS_SELECTOR,
			                                          "[data-hook='product-price-discount-size-label']").text.strip()
			print(pack_size_text)
			if pack_size_text:
				print("here")
				row_spec["page_pack_size"] = pack_size_text
		except NoSuchElementException as e:
			print(f"No Description found")
		except Exception as e:
			print(f"⛔️️ Error processing product description: {type(e)}")
			print(f"⛔️️ Error processing product description: {e}")

		print("processing product pack_size Complete...")
		return row_spec

	def get_pack_size(self, row_spec):
		print("get_pack_size()")
		row_spec['size'] = row_spec['pack_size'].get('measure', '')
		row_spec['pack'] = row_spec['pack_size'].get('quantity', '')

		print("processing product pack_size Complete...")
		return row_spec

	def get_distributor_specific(self, row_spec):
		return row_spec
	# ************************************************************************
	# 	Core
	# ************************************************************************

	# Step One:
	def build_categories_list(self):
		"""Parse the navigation menu to extract categories and their subcategories."""
		""" ******* This only works in with headless mode disabled ******* """
		print(f"{self.__class__}->build_categories_list()")
		url = self.BASE_URL
		self.scraping_setup()
		self.driver.get(url)

		# Wait for the navigation menu to load
		self.wait.until(
			EC.presence_of_element_located((By.CSS_SELECTOR, "nav.ch-top-menu-nav"))
		)

		# Initialize the categories structure
		all_categories = {
			'data': {
				'categories': []
			}
		}

		# Get all top-level menu items
		menu_items = self.driver.find_elements(
			By.CSS_SELECTOR,
			"ul.ch-wp-menu-desktop > li"
		)

		print(f"menu_items: {len(menu_items)}")
		i = 0
		for item in menu_items:
			i += 1
			try:
				print(f"item: {item}")
				# Get the main category link
				link = item.find_element(By.CSS_SELECTOR, "a.ch-wp-menu-item-link")
				category_name = link.text.strip()
				category_url = link.get_attribute("href")

				# Skip if no meaningful name
				if not category_name or category_name.lower() in ['home', '']:
					continue

				category_data = {
					'name': category_name,
					'id': i,
					'url': category_url,
					'subcategories': []
				}

				# Check for dropdown menu
				dropdown = item.find_elements(
					By.CSS_SELECTOR,
					".ch-wp-menu-item-dropdown"
				)

				if dropdown:
					print("dropdown found")
					# Get all subcategory groups
					sub_menus = item.find_elements(
						By.CSS_SELECTOR,
						".ch-wp-menu-item-subitem"
					)
					print(f"sum menus = {len(sub_menus)}")
					for sub_menu in sub_menus:
						print(f"sub_menu: {sub_menu}")
						# self.print_element(sub_menu)
						try:
							# Get subcategory title
							sub_title = sub_menu.find_element(
								By.CSS_SELECTOR,
								"li.ch-wp-menu-item-subitem-title"
							)
							self.print_element(sub_title)
							# print(f"subtitle: {sub_title}")
							# Skip if no subcategories under this group
							sub_title = sub_title.get_attribute('textContent').strip()
							if not sub_title or "LOG IN" in sub_title.upper():
								continue

							subcategory_group = {
								'name': sub_title,
								'url': '',
								'subcategories': []
							}

							# Get all subcategory items
							sub_items = sub_menu.find_elements(
								By.CSS_SELECTOR,
								"a .ch-wp-menu-item-subitem-record"
							)

							for sub_item in sub_items:
								try:
									sub_name = sub_item.get_attribute('textContent').strip()
									print(f"sub_name: {sub_name}")
									sub_url = sub_item.find_element(
										By.XPATH,
										"./parent::a"
									).get_attribute("href")
									print(f"sub_url: {sub_url}")
									if sub_name and sub_url:
										subcategory_group['subcategories'].append({
											'name': sub_name,
											'url': sub_url
										})
								except Exception as e:
									print(f"Error processing subcategory item: {e}")
									continue

							if subcategory_group['subcategories']:
								category_data['subcategories'].append(subcategory_group)

						except Exception as e:
							print(f"Error processing submenu: {e}")
							continue

				all_categories['data']['categories'].append(category_data)

			except Exception as e:
				print(f"Error processing menu item: {e}")
				continue

		# Print the result for debugging
		import json
		print(json.dumps(all_categories, indent=2))

		return json.dumps(all_categories, indent=2)

	# Step Two: Get links to products
	def build_products_list(self):
		"""Scrape products from the website"""
		html = ""
		all_urls = []
		# Use the options with fallback to module-level variables
		max_products = self.options.get('max_products', self.MAX_API_PRODUCTS)
		category_to_process = self.options.get('category_to_process', 0)
		chosen_category = int(self.options.get('chosen_category', 0))
		test_categories = self.options.get('test_categories', 100)
		category_count = 0
		if int(self.options['chosen_category']) == 0:
			categories = self.get_categories()
			print(f"All Categories ")
		else:
			for category in self.get_categories():
				print(f"category : {category.get('name', '')}")
				if int(category.get('id', '')) == chosen_category:
					categories = [category]  # Only process the chosen category
					print(f"Category found : {categories}")
					break
		url_output_file = self.options.get('url_output_file', '')

		# Wait for the page to be fully loaded
		print(f"Output File Name: {url_output_file}")
		total_products = 0
		loop_counter = 0
		category_found_count = 1

		# Check to see if we asked for a specific category
		if category_to_process > 0:
			print(f"Category to process: {category_to_process}")
			loop_counter = category_to_process - 1
			test_categories = category_to_process
			category_found_count = category_to_process

		for category in categories:
			category_name = category['name']
			print(f"category: {category_name}")
			sub_categories = category['subcategories']
			sub_category_found_count = len(sub_categories)
			print(f"Found {sub_category_found_count} sub categories to process...")
			for sub_category in sub_categories:
				sub_category_name = sub_category['name']
				print(f"sub category: {sub_category_name}")

				sub_sub_categories = sub_category.get('subcategories', False)
				if sub_sub_categories:
					sub_sub_category_found_count = len(sub_sub_categories)
					print(f"Found {sub_sub_category_found_count} sub categories to process...")
					for sub_sub_category in sub_category['subcategories']:
						sub_sub_category_name = sub_sub_category['name']
						print(f"sub sub category: {sub_sub_category_name}")
						if loop_counter < test_categories:
							loop_counter += 1

							url = self.get_category_url(sub_sub_category)
							print(f"Url: {url}")
							detail_urls, html = self.get_category_page(url, category_name, sub_category_name, sub_sub_category_name)
							all_urls.extend(detail_urls)
						time.sleep(2)
				else:
					url = self.get_category_url(sub_category)
					print(f"Url: {url}")
					detail_urls, html = self.get_category_page(url, category_name, sub_category_name, '')
					all_urls.extend(detail_urls)

		# html_table_to_csv(html_table)
		html += f"<h2>Total products found: {total_products}</h2>"

		print(f"Total products found: {len(all_urls)}")
		return html

	# ************************************************************************
	# Functions for extracting product data
	# ************************************************************************

	def get_product_details(self, url, row_spec=None):
		"""
		Product detail pages are rendered server-side. Page must be manually scraped.
		Additional packages also need to be pulled or visited from the dropdown
		To get the product detail page, visit the product detail page and then pull the additional packages
		"""
		# The initial row_spec contains the information from the product list page
		initial_row_spec = row_spec
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print(f"{self.__class__}->get_product_details()")

		print(f"Loading page: {url}")
		self.driver.get(url)

		data = ''
		# sku = row_spec['sku']
		row_spec['content_url'] = url

		print(f"Loading page...{url}")
		try:
			data, data_2 = self.get_product_detail_from_json_in_html(url, row_spec=row_spec, target="#product-metadata")

			row_spec['option_id'] = row_spec['sku']
			row_spec['sku'] = ''
			row_spec['distributor_name'] = self.VENDOR_NAME
			row_spec = self.get_product_data(data, row_spec)
			row_spec = self.get_product_data_2(data_2, row_spec)
			row_spec = self.get_merchant_section(data_2, row_spec)
			row_spec = self.get_distributor_specific(row_spec)

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing get_product_details: {type(e)}")
			raise
		# row_spec = self.get_product_detail_from_html(row_spec=row_spec)
		time.sleep(2)
		print("get_product_details complete")
		return row_spec

	def get_product_detail_from_json_in_html(self, url, row_spec=None, target="script[type='application/json']"):
		"""
		Extract JSON data from a script tag with the specified ID.

		Args:
			url (str): The URL to load
			row_spec (dict, optional): Product data specification. Defaults to None.
			target (str, optional): CSS selector for the script tag. Defaults to "script[type='application/json']".

		Returns:
			dict: Parsed JSON data from the script tag
		"""
		print(f"Hive.get_product_detail_from_json_in_html() - Target: {target}")
		if not row_spec:
			row_spec = self.PRODUCT_DATA_SPEC.copy()

		product_data = {}
		product_data2 = {}
		try:
			# Wait for the target script tag to be present
			script_element = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, target))
			)
			# Get the inner HTML of the script tag
			script_content = script_element.get_attribute('innerHTML')

			script_element2 = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((By.TAG_NAME, 'ch-elements.product.page'))
			)
			# Get the inner HTML of the script tag
			script_content2 = script_element2.get_attribute('product')
			if script_content:
				try:
					# Parse the JSON data
					product_data = json.loads(script_content)
					print("Successfully extracted and parsed JSON data")
					print(product_data)
				except json.JSONDecodeError as e:
					print(f"Error parsing JSON data: {e}")
			else:
				print(f"No content found in script tag matching: {target}")

			if script_content2:
				try:
					# Parse the JSON data
					product_data2 = json.loads(script_content2)
					print("Successfully extracted and parsed JSON data")
					print(product_data2)
				except json.JSONDecodeError as e:
					print(f"Error parsing JSON data: {e}")
			else:
				print(f"No content found in script tag matching: ch-elements.product.page")

		except Exception as e:
			print(f"Error extracting data from script tag: {e}")
		finally:
			# Clean up any pending requests
			if hasattr(self, 'driver') and hasattr(self.driver, 'requests'):
				del self.driver.requests
		return product_data, product_data2

	def get_product_detail_from_html(self, url='', row_spec=None):
		print(f"get_product_detail_from_html()")
		try:
			print("here")
			container = self.wait.until(
				EC.presence_of_element_located((By.TAG_NAME, 'ch-elements.product.page'))
			)
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing get_product_detail_from_html: {type(e)}")
			raise
		try:
			# row_spec['content_url'] = self.driver.current_url
			print("here2")
			row_spec = self.get_description(row_spec)
			row_spec = self.get_pack_size_from_html(row_spec)
			row_spec['image'] = self.get_first_image_url_scrape()

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing get_product_detail_from_html: {type(e)}")
		print("get_product_detail_from_html complete")
		return row_spec

	# ************************************************************************
	# Product List Extraction Functions
	# ************************************************************************
	def get_category_page(self, url, category_name, sub_category_name, sub_sub_category_name):
		print("get_category_page()")
		main_window = self.driver.current_window_handle
		html = ''
		total_products = 0
		all_urls = []
		detail_urls = []
		page_count = 0

		self.driver.get(url)
		try:
			# Update URL from the redirect
			url = self.driver.current_url
			print(f"Current URl: {self.driver.current_url}")

			target = "#search-results-item-list"

			# Find all window handles and switch to the new window if it opens in a new tab
			if len(self.driver.window_handles) > self.TEST_TABS:
				print("must be a tab...")
				for handle in self.driver.window_handles:
					if handle != main_window:
						self.driver.switch_to.window(handle)
						break
			next_page = True

			while next_page:
				page_count += 1
				try:
					# Wait for page to load
					detail_urls = []
					if url in self.driver.current_url:
						print("Found products page")
						time.sleep(2)
						html_line, detail_urls = self.get_products_from_html()
					products_found_count = len(detail_urls)
					all_urls.extend(detail_urls)
					html += f"<div>Found {products_found_count} products for category {category_name} page {page_count}</div>"
					print(f"Found {products_found_count} products for category {category_name} page {page_count}")
					total_products += products_found_count
					# self.save_urls_to_csv(detail_urls, category_name, sub_category_name, sub_sub_category_name)

				except Exception as e:
					print(f"****************** ⛔️⛔️⛔️ Error getting details: {e}")
					html += f"<div>Name: {sub_category_name} (Error getting details)</div>"

				try:
					paging = self.wait.until(
						EC.presence_of_element_located((By.CSS_SELECTOR, ".pages-wrapper"))
					)
					print("found paging area")
					button = paging.find_element(By.CSS_SELECTOR, "[data-hook='pagination-next-page']")
					self.driver.execute_script("arguments[0].scrollIntoView();", button)
					button.click()
					next_page = True
					print("go to next page")
				except Exception as e:
					next_page = False
					print(f"no next page")

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing category: {e}")

		html += f"<h2>Total products found: {total_products}</h2>"
		print(f"Total Products {len(all_urls)}")

		# write all the urls to file
		self.save_urls_to_csv(all_urls, category_name, sub_category_name, sub_sub_category_name)
		# return results to results page
		return all_urls, html

	def get_products_from_html(self):
		print("get_products_from_html")
		products = self.wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ch-product-item"))
		)

		print(f"products found: {len(products)}")
		detail_urls = [product.find_element(By.CSS_SELECTOR,'a').get_attribute("href") for product in products]
		return '', detail_urls
