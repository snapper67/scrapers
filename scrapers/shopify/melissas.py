import csv
import json
import re
import requests
import time
import os
from collections import OrderedDict
import sys
import glob
import pandas as pd

from bs4 import BeautifulSoup
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumwire import webdriver as seleniumwire_webdriver
from seleniumwire.utils import decode

from scrapers.scraper import Scraper
from scrapers.shopify.shopify import ShopifyScraper


class MelissasScraper(ShopifyScraper):

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/melissas_produce'

	BASE_URL = 'https://www.melissas.com/pages/asian'
	BASE_PRODUCT_URL = 'https://www.melissas.com/products/'
	VENDOR_NAME = 'Melissa\'s Produce'

	CATEGORY_IDS = {
		"FRUIT": 1,
		"VEGETABLES": 2,
		"CONVENIENCE": 3,
		"ASIAN": 4,
		"LATIN": 5,
	}
	# Category Names (can use category ID as key)
	CATEGORY_NAMES = {
		1: "fruits",
		2: "vegetables",
		3: "convenience",
		4: "asian",
		5: "latin",
	}
	CATEGORY_URLS = {
		1: "fruits",
		2: "vegetables",
		3: "convenience",
		4: "asian",
		5: "latin",
	}

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	DEFAULT_OPTIONS = {
		'scrape_products': False,
		'process_csv': False,
		'reprocess_csv': False,
		'dedupe_csv': False,
		'count_csv': False,
		'test_products': TEST_PRODUCTS,
		'max_products': 999,
		'csv_start_row': CSV_START_ROW,
		'category_to_process': 0,
		'test_categories': 100,
		'chosen_category': '10001',
		'url_output_file': '',
		'data_output_file': '',
		'home_directory': DEFAULT_DIRECTORY
	}

	def __init__(self, options=None):
		super().__init__(options)
		self.options = {**self.DEFAULT_OPTIONS, **(options or {})}
		self.options['home_directory'] = self.DEFAULT_DIRECTORY
		self.options['base_url'] = self.BASE_URL


	# ************************************************************************

	# 	Product Scraping Functions
	# ************************************************************************


	def get_product_details(self, url, row_spec=None):
		"""Get Product Details"""
		data = self.get_product_details_json( url, row_spec)
		row_spec = self.get_product_data(data, row_spec)
		return row_spec

	# ************************************************************************

	def build_products_list(self):
		"""Scrape products from the website"""
		html = ""
		all_urls = []
		# Use the options with fallback to module-level variables
		test_categories = self.options.get('test_categories', self.TEST_CATEGORIES)
		max_products = self.options.get('max_products', self.MAX_API_PRODUCTS)
		category_to_process = self.options.get('category_to_process', 0)
		chosen_category = self.options.get('chosen_category', '')
		chosen_category_id = self.CATEGORY_IDS[chosen_category]
		category_url_part = self.CATEGORY_URLS[chosen_category_id]
		category_name = self.options.get('chosen_category', self.CATEGORY_NAMES[chosen_category_id])
		url_output_file = self.options.get('url_output_file', '')

		category_URL = f"https://www.melissas.com/pages/{category_url_part}"
		category_URL = self.get_category_url()
		# Wait for the page to be fully loaded
		wait = WebDriverWait(self.driver, 10)
		print(f"Scraping products from category {category_name}")
		print(f"Output File Name: {url_output_file}")
		self.driver.get(category_URL)
		self.driver.request_interceptor = self.create_interceptor(max_products)
		total_products = 0
		loop_counter = 0
		category_found_count = 1

		# Starting on the page for a specific category
		print(f"Loading category page {category_URL}")
		self.driver.get(category_URL)
		self.driver.execute_script("document.body.style.zoom = '50%'")

		print(f"Page title: {self.driver.title}")

		if category_to_process > 0:
			print(f"Category to process: {category_to_process}")
			loop_counter = category_to_process - 1
			test_categories = category_to_process
			category_found_count = category_to_process

		while loop_counter < category_found_count and loop_counter < test_categories:
			loop_counter += 1

			# Wait for category cards to be present and visible
			sub_categories = wait.until(
				EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.shogun-image-link'))
			)
			print(f"Page title: {self.driver.title}")

			category_found_count = len(sub_categories)
			print(f"Found {category_found_count} categories to process...")

			# Store the main window handle
			main_window = self.driver.current_window_handle

			try:
				# for category_index, sub_category in enumerate(sub_categories[loop_counter:loop_counter]):
				sub_category = sub_categories[loop_counter - 1]
				link = sub_category.get_attribute("href")
				print(f"\nProcessing category {loop_counter} of {category_found_count}...")
				self.driver.execute_script("arguments[0].scrollIntoView();", sub_category)

				sub_category_name = os.path.basename(link)
				print(f"Category name: {sub_category_name}")
				html += f"<h2>Category Name: {sub_category_name}</h2>"

				# Click on the category to open detail page
				sub_category.click()
				print("Clicked on category, waiting for detail page to load...")

				# Wait for the detail page to load
				time.sleep(6)  # Wait for the page to load
				print(f"Looking for Page: {sub_category_name} - Melissas Produce")
				print(f"Found:           {self.driver.title}")
				print(f"Current URl: {self.driver.current_url}")

				# Find all window handles and switch to the new window if it opens in a new tab
				if len(self.driver.window_handles) > self.TEST_TABS:
					print("must be a tab...")
					for handle in self.driver.window_handles:
						if handle != main_window:
							self.driver.switch_to.window(handle)
							break
				page_count = 1
				next_page = True

				while next_page:
					try:
						# Wait for page to load
						detail_urls = []
						if link in self.driver.current_url:
							print("Found products page")
							time.sleep(2)
							html_line, detail_urls = self.grab_products()
						products_found_count = len(detail_urls)
						html += f"<div>Found {products_found_count} products for category {sub_category_name}</div>"
						print(f"Found {products_found_count} products for category {sub_category_name}")
						total_products += products_found_count
						self.save_urls_to_csv(detail_urls, category_name, sub_category_name)
						all_urls.extend(detail_urls)

					except Exception as e:
						print(f"****************** ⛔️⛔️⛔️ Error getting details: {e}")
						html += f"<div>Name: {sub_category_name} (Error getting details) {loop_counter}</div>"

					try:
						paging = wait.until(
							EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination--inner'))
						)
						paging.find_element(By.CLASS_NAME, 'pagination--next').click()
						next_page = True
					except Exception as e:
						next_page = False

				self.driver.get(category_URL)
				self.driver.execute_script("document.body.style.zoom = '50%'")
				print(f"Going back to get next category: {self.driver.title}")
				# Wait before processing next category
				time.sleep(3)

			except Exception as e:
				print(f"⛔️⛔️⛔️Error processing category: {e}")
				continue

		time.sleep(3)


		# html_table_to_csv(html_table)
		html += f"<h2>Total products found: {total_products}</h2>"

		print(f"Total products found: {len(all_urls)}")
		return html

