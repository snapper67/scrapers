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
from typing import List, Dict, Any, Optional

# Only grabbed the first menu item = "Shop All"

class AllenBrothersScraper(ShopifyScraper):
	# 784/edit_note/849/
	CRM_ID = 784
	CRM_NOTE_ID = 849
	CRM_PRICE_TYPE = 'Retail'
	CRM_STATUS_OVERRIDE = ''

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/allen_brothers'

	BASE_URL = 'https://www.allenbrothers.com/'
	BASE_PRODUCT_URL = 'https://www.allenbrothers.com/products'
	VENDOR_NAME = 'Allen Brothers'

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "id": 4,
        "name": "Beef",
        "subcategories": [
          {
            "id": 5,
            "name": "Shop By Cut",
            "subcategories": [
              {
                "id": 6,
                "name": "Filet Mignon",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/filet-mignon?N=filet-mignon"
              },
              {
                "id": 7,
                "name": "Ribeye",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/ribeye?N=ribeye"
              },
              {
                "id": 8,
                "name": "Strip Steak",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/strip-steak?N=strip-steak"
              },
              {
                "id": 9,
                "name": "Porterhouse",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/porterhouse?N=porterhouse"
              },
              {
                "id": 10,
                "name": "Burgers & Grinds",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/burgers-grinds?N=burgers-grinds"
              },
              {
                "id": 11,
                "name": "Hot Dogs & Sausage",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/hot-dogs-sausage?N=hot-dogs-sausage"
              },
              {
                "id": 12,
                "name": "Butcher\u2019s Cuts",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/butchers-cuts?N=butchers-cuts"
              },
              {
                "id": 13,
                "name": "Holiday Roasts",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/holiday-roasts?N=holiday-roasts"
              }
            ],
            "url": "https://www.allenbrothers.com/category/shop-by-cut?N=beef-cut"
          }
        ],
        "url": "https://www.allenbrothers.com/category/shop-beef?N=beef"
      },
      {
        "id": 7,
        "name": "Lamb",
        "subcategories": [],
        "url": "https://www.allenbrothers.com/category/shop-lamb?N=lamb"
      },
      {
        "id": 8,
        "name": "Pork",
        "subcategories": [],
        "url": "https://www.allenbrothers.com/category/shop-pork?N=pork"
      },
      {
        "id": 9,
        "name": "Seafood",
        "subcategories": [
          {
            "id": 10,
            "name": "Fish",
            "subcategories": [
              {
                "id": 11,
                "name": "Salmon",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/salmon?N=salmon"
              },
              {
                "id": 12,
                "name": "Halibut",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/halibut?N=halibut"
              },
              {
                "id": 13,
                "name": "Sea Bass",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/sea-bass?N=sea-bass"
              },
              {
                "id": 14,
                "name": "Grouper",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/grouper?N=grouper"
              },
              {
                "id": 15,
                "name": "Swordfish",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/swordfish?N=swordfish"
              }
            ],
            "url": "https://www.allenbrothers.com/category/fish?N=seafood-and-fish-fish"
          },
          {
            "id": 16,
            "name": "Shellfish",
            "subcategories": [
              {
                "id": 17,
                "name": "Lobster",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/lobster?N=lobster"
              },
              {
                "id": 18,
                "name": "Crab",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/crab?N=crab"
              },
              {
                "id": 19,
                "name": "Shrimp",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/shrimp?N=shrimp"
              },
              {
                "id": 20,
                "name": "Scallops",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/scallops?N=scallops"
              },
              {
                "id": 21,
                "name": "Shop AllSeafood",
                "subcategories": [],
                "url": "https://www.allenbrothers.com/category/shop-seafood-and-fish?N=seafood-and-fish"
              }
            ],
            "url": "https://www.allenbrothers.com/category/shellfish?N=seafood-and-fish-shellfish"
          }
        ],
        "url": "https://www.allenbrothers.com/category/shop-seafood-and-fish?N=seafood-and-fish"
      },
      {
        "id": 12,
        "name": "Poultry",
        "subcategories": [],
        "url": "https://www.allenbrothers.com/category/shop-poultry?N=poultry"
      },
      {
        "id": 13,
        "name": "Veal",
        "subcategories": [],
        "url": "https://www.allenbrothers.com/category/shop-veal?N=veal"
      },
      {
        "id": 14,
        "name": "Game",
        "subcategories": [],
        "url": "https://www.allenbrothers.com/category/shop-game?N=game"
      },
      {
        "id": 15,
        "name": "Specialty",
        "subcategories": [],
        "url": "https://www.allenbrothers.com/category/specialty?N=specialty"
      }
    ]
  }
}                    
	''')

	def __init__(self, options=None):
		super().__init__(options)

	def get_categories(self):
		"""
		Returns a list of category dictionaries from the CATEGORIES data.

		Returns:
			list: A list of dictionaries, each containing 'id' and 'name' of a category
		"""
		category_options = self.CATEGORIES.get('data', {}).get('categories', {})
		return [
			{'id': option['id'], 'name': option['name']}
			for option in category_options
			if option.get('id') and option.get('name')
		]

	def get_taxonomy(self):
		categories = self.CATEGORIES.get('data', {}).get('categories', [])
		print(f"Categories: {categories}")
		return categories

	def get_category_url(self, category):
		print(f"get_category_url: {category}")
		if ("http" in category['url']):
			return category['url']
		else:
			return f"https://www.almagourmet.com{category['url']}"

	# ************************************************************************

	# 	Product Scraping Functions
	# ************************************************************************
	def get_first_image_url(self, response_data):
		"""
		Extract the first available image URL from the product API response.

		Args:
			response_data (dict): The parsed JSON response from the API

		Returns:
			str: URL of the first available image, or None if no image found
		"""
		try:
			image = response_data.get('image', {})

			# If there are assets, get the first one's URL
			if image:
				# Get the first asset and extract the URL
				return image.get('url', '')

		except Exception as e:
			print(f"Error extracting image from viewModel.assets: {str(e)}")

		return ''

	def get_product_data(self, data, row_spec):
		print("processing product data from response...")
		print(data)
		if data:
			try:
				row_spec["name"] = data.get("displayName", "")
				print(f"name: {row_spec['name']}")
				row_spec["description"] = data.get("description", "")
				row_spec["productId"] = data.get("productId", "")

				sku_details = data.get('skuDetails', {})
				row_spec["retail_price"] = sku_details.get("price", {}).get("ListPrice", {}).get("price", "").replace('.','')
				row_spec["pack_size"] = sku_details.get("skuOptions", [])[0].get("optionValue", "")
				print(f"pack_size: {row_spec['pack_size']}")
				# self.get_pack_size(data, row_spec)
				# row_spec["image"] = self.get_first_image_url(data)

				# move sku - which was just a unique identifier to id
				row_spec['id'] = row_spec['sku']
				row_spec['sku'] = data.get('skuId', '')

				row_spec["extra_data_1"] = json.dumps(data)

			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing get_product_data Complete...")
		# row_spec = self.get_product_data_additional(data, row_spec)
		return row_spec

	def get_product_details_scrape(self, url, row_spec=None, target="script[type='application/json']"):
		#  Wait for the product name element on the product page detail page
		print("AlmaScraper.get_product_details_scrape()")
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print(f"processing product detail page for target {target}")
		print(f"Loading page...{url}")

		data = ''
		sku = row_spec['sku']
		request_filter = url

		self.driver.get(url)
		print(f"Sent Request")
		product_data = ''
		try:
			# Wait for the page to load
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(
				(By.CSS_SELECTOR, target))
			)
			print(f"Script Loaded")
			# Get the page source and parse it with BeautifulSoup
			soup = BeautifulSoup(self.driver.page_source, 'html.parser')

			scripts = soup.find_all('script', {'id': '__NEXT_DATA__'})
			for script in scripts:
				# print(script.string)
				if script and script.string:
					print("Loading product data")
					try:
						# Parse the JSON data from the script tag
						product_data = json.loads(script.string)
						try:
							if product_data.get('@type') == "Product":
								del self.driver.requests
								return product_data
						except Exception as e:
							print(f"Error getting product data: {type(e)}")
					except json.JSONDecodeError as e:
						print(f"Error parsing JSON data: {e}")
				else:
					print("Could not find the product data script tag")

		except Exception as e:
			print(f"Error getting product details: {e}")
		finally:
			del self.driver.requests

		return product_data

	def get_product_details(self, url, row_spec=None):
		"""Get Product Details"""
		print("AlmaScraper.get_product_details()")
		data = self.get_product_details_scrape(url, row_spec,
		                                       target="script[type='application/json']")
		print("getting data")
		if not data or 'props' not in data:
			print("❌ No product data found")
			return row_spec or {}

		# Extract product data from the nested structure
		product_data = data.get('props', {}).get('pageProps', {}).get('data', {}).get('payLoad', {})
		products = product_data.get('products', [])

		if not products:
			print("❌ No products found in the response")
			return row_spec or {}

		# Get the first product (should only be one)
		product = products[0]
		# data = data.get('props', {}).get('pageProps', {}).get('data', {}).get('payLoad', {}).get('products', [])[0]
		print(data)
		skus = product.get('skus', {})
		specs = []
		row_spec_base = row_spec
		for sku_id, sku_data in skus.items():
			# sku_data = json.loads(sku_data)
			row_spec = self.get_product_data(sku_data, row_spec_base)
			specs.append(row_spec)
		return specs

	def get_product_data_additional(self, data, row_spec):
		row_spec["name"] = data.get("name", "")
		row_spec['sku'] = data.get('sku', '')
		price = round(data.get("offers", [])[0].get("price", 0) * 100)
		row_spec["retail_price"] = "" if price == 0 else price
		return row_spec

	# ************************************************************************
	# def get_products_from_html(self, start=None):
	# 	print("get_products_from_html()")
	# 	product_count = 0
	# 	if start:
	# 		products = self.wait.until(
	# 			EC.presence_of_all_elements_located((By.CSS_SELECTOR, f'#{start} a.card__image.product-item__image'))
	# 		)
	# 	else:
	# 		products = self.wait.until(
	# 			EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.card__image.product-item__image'))
	# 		)
	# 	while len(products) > product_count:
	# 		product_count = len(products)
	# 		self.driver.execute_script("arguments[0].scrollIntoView();", products[product_count - 1])
	# 		products = self.wait.until(
	# 			EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.card__image.product-item__image'))
	# 		)
	#
	# 	print(f"products found: {len(products)}")
	# 	detail_urls = [product.get_attribute("href") for product in products]
	# 	return '', detail_urls

	def build_categories_list(self):
		url = self.BASE_URL
		navigation = self.get_navigation_structure(url)
		# self.print_navigation_structure(navigation)
		return f"<div>{navigation}</div>"

	def get_navigation_dict(self, url: str, headers: Optional[Dict] = None) -> Dict:
		"""
		Parse the navigation menu and return a structured dictionary of categories.

		Args:
			url: The URL to fetch the navigation from
			headers: Optional request headers

		Returns:
			Dict containing the navigation structure
		"""
		print("Allen->get_navigation_dict()")
		if not headers:
			headers = {
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
			}

		try:
			# Use the provided HTML directly
			html = """
	        <nav class="container navbar redesign-navbar"><div><ul class="navbar-nav nav nav-list"><li class="nav-item js-dropdown navListItems"><a class="first-dropdown" href="#" style="text-decoration:none;text-transform:capitalize">Shop All</a><button class="header-menu" type="button" data-target="" aria-label="Open Shop All menu"><i class="fa fa-chevron-down"></i></button><div class="header-dropdown-menu dropdown-menu firstDropDownMegaMenu level0Menu"><ul class="category-list list-unstyled c-list"><li class="nav-item js-dropdown sub-nav menu-column"><div class="categoryL1ListContainer"><a class="js-dropdown__btn" href="/category/shop-beef?N=beef">Beef</a><button class="header-menu" type="button" aria-label="Open Beef menu"><i class="fa fa-chevron-right"></i></button></div><div class="flyout-menu"><div><a href="/category/shop-by-cut?N=beef-cut" class="category-heading sub-nav1 list-heading">Shop By Cut</a><ul class="category-list list-unstyled sub-nav1 bg-color"><li class="category-list-item-navbar"><a href="/category/filet-mignon?N=filet-mignon">Filet Mignon</a></li><li class="category-list-item-navbar"><a href="/category/ribeye?N=ribeye">Ribeye</a></li><li class="category-list-item-navbar"><a href="/category/strip-steak?N=strip-steak">Strip Steak</a></li><li class="category-list-item-navbar"><a href="/category/porterhouse?N=porterhouse">Porterhouse</a></li><li class="category-list-item-navbar"><a href="/category/burgers-grinds?N=burgers-grinds">Burgers &amp; Grinds</a></li><li class="category-list-item-navbar"><a href="/category/hot-dogs-sausage?N=hot-dogs-sausage">Hot Dogs &amp; Sausage</a></li><li class="category-list-item-navbar"><a href="/category/butchers-cuts?N=butchers-cuts">Butcher’s Cuts</a></li><li class="category-list-item-navbar"><a href="/category/holiday-roasts?N=holiday-roasts">Holiday Roasts</a></li></ul></div><div><a href="/category/shop-by-type?N=beef-type" class="category-heading sub-nav1 list-heading">Shop By Type</a><ul class="category-list list-unstyled sub-nav1 bg-color"><li class="category-list-item-navbar"><a href="/category/usda-prime?N=usda-prime">USDA Prime</a></li><li class="category-list-item-navbar"><a href="/category/usda-choice?N=usda-choice">USDA Choice</a></li><li class="category-list-item-navbar"><a href="/category/wagyu?N=wagyu">Wagyu</a></li><li class="category-list-item-navbar"><a href="/category/dry-aged-beef?N=dry-aged-beef">Dry Age</a></li><li class="category-list-item-navbar"><a href="/category/shop-beef?N=beef" class="shopAllInL2Category">Shop All <!-- -->Beef</a></li></ul></div></div></li><li class="nav-item js-dropdown sub-nav menu-column"><div class="categoryL1ListContainer"><a class="js-dropdown__btn" href="/category/shop-lamb?N=lamb">Lamb</a><button class="header-menu" type="button" aria-label="Open Lamb menu"><i class="fa fa-chevron-right"></i></button></div><div class="flyout-menu"><div><ul class="category-list list-unstyled sub-nav1 bg-color"><li class="category-list-item-navbar"><a href="/category/lamb-chops?N=lamb-chops">Lamb Chops</a></li><li class="category-list-item-navbar"><a href="/category/lamb-rack-roast?N=lamb-rack-roast">Lamb Racks &amp; Roasts</a></li><li class="category-list-item-navbar"><a href="/category/lamb-shanks?N=lamb-shanks">Lamb Shanks</a></li><li class="category-list-item-navbar"><a href="/category/shop-lamb?N=lamb" class="shopAllInL2Category">Shop All <!-- -->Lamb</a></li></ul></div></div></li><li class="nav-item js-dropdown sub-nav menu-column"><div class="categoryL1ListContainer"><a class="js-dropdown__btn" href="/category/shop-pork?N=pork">Pork</a><button class="header-menu" type="button" aria-label="Open Pork menu"><i class="fa fa-chevron-right"></i></button></div><div class="flyout-menu"><div><ul class="category-list list-unstyled sub-nav1 bg-color"><li class="category-list-item-navbar"><a href="/category/pork-chops?N=pork-chops">Pork Chops</a></li><li class="category-list-item-navbar"><a href="/category/pork-ribs?N=pork-ribs">Pork Ribs</a></li><li class="category-list-item-navbar"><a href="/category/pork-roasts?N=pork-roasts">Pork Roasts</a></li><li class="category-list-item-navbar"><a href="/category/pork-belly-bacon?N=pork-belly-bacon">Bacon &amp; Belly</a></li><li class="category-list-item-navbar"><a href="/category/pork-ham?N=pork-ham">Ham</a></li><li class="category-list-item-navbar"><a href="/category/shop-pork?N=pork" class="shopAllInL2Category">Shop All <!-- -->Pork</a></li></ul></div></div></li><li class="nav-item js-dropdown sub-nav menu-column"><div class="categoryL1ListContainer"><a class="js-dropdown__btn" href="/category/shop-seafood-and-fish?N=seafood-and-fish">Seafood</a><button class="header-menu" type="button" aria-label="Open Seafood menu"><i class="fa fa-chevron-right"></i></button></div><div class="flyout-menu"><div><a href="/category/fish?N=seafood-and-fish-fish" class="category-heading sub-nav1 list-heading">Fish</a><ul class="category-list list-unstyled sub-nav1 bg-color"><li class="category-list-item-navbar"><a href="/category/salmon?N=salmon">Salmon</a></li><li class="category-list-item-navbar"><a href="/category/halibut?N=halibut">Halibut</a></li><li class="category-list-item-navbar"><a href="/category/sea-bass?N=sea-bass">Sea Bass</a></li><li class="category-list-item-navbar"><a href="/category/grouper?N=grouper">Grouper</a></li><li class="category-list-item-navbar"><a href="/category/swordfish?N=swordfish">Swordfish</a></li></ul></div><div><a href="/category/shellfish?N=seafood-and-fish-shellfish" class="category-heading sub-nav1 list-heading">Shellfish</a><ul class="category-list list-unstyled sub-nav1 bg-color"><li class="category-list-item-navbar"><a href="/category/lobster?N=lobster">Lobster</a></li><li class="category-list-item-navbar"><a href="/category/crab?N=crab">Crab</a></li><li class="category-list-item-navbar"><a href="/category/shrimp?N=shrimp">Shrimp</a></li><li class="category-list-item-navbar"><a href="/category/scallops?N=scallops">Scallops</a></li><li class="category-list-item-navbar"><a href="/category/shop-seafood-and-fish?N=seafood-and-fish" class="shopAllInL2Category">Shop All <!-- -->Seafood</a></li></ul></div></div></li><li class="nav-item js-dropdown sub-nav menu-column"><div class="categoryL1ListContainer"><a class="js-dropdown__btn" href="/category/shop-poultry?N=poultry">Poultry</a><button class="header-menu" type="button" aria-label="Open Poultry menu"><i class="fa fa-chevron-right"></i></button></div><div class="flyout-menu"><div><ul class="category-list list-unstyled sub-nav1 bg-color"><li class="category-list-item-navbar"><a href="/category/turkey?N=poultry-turkey">Turkey</a></li><li class="category-list-item-navbar"><a href="/category/duck?N=poultry-duck">Duck</a></li><li class="category-list-item-navbar"><a href="/category/chicken?N=poultry-chicken">Chicken</a></li><li class="category-list-item-navbar"><a href="/category/shop-poultry?N=poultry" class="shopAllInL2Category">Shop All <!-- -->Poultry</a></li></ul></div></div></li><li class="nav-item js-dropdown sub-nav menu-column"><div class="categoryL1ListContainer"><a class="js-dropdown__btn" href="/category/shop-veal?N=veal">Veal</a><button class="header-menu" type="button" aria-label="Open Veal menu"><i class="fa fa-chevron-right"></i></button></div><div class="flyout-menu"><div><ul class="category-list list-unstyled sub-nav1 bg-color"><li class="category-list-item-navbar"><a href="/category/veal-chops?N=veal-chops">Veal Chops</a></li><li class="category-list-item-navbar"><a href="/category/veal-shanks?N=veal-shanks">Veal Shanks</a></li><li class="category-list-item-navbar"><a href="/category/veal-slices?N=veal-slices">Veal Slices</a></li><li class="category-list-item-navbar"><a href="/category/shop-veal?N=veal" class="shopAllInL2Category">Shop All <!-- -->Veal</a></li></ul></div></div></li><li class="nav-item js-dropdown sub-nav menu-column"><div class="categoryL1ListContainer"><a class="js-dropdown__btn" href="/category/shop-game?N=game">Game</a><button class="header-menu" type="button" aria-label="Open Game menu"><i class="fa fa-chevron-right"></i></button></div><div class="flyout-menu"><div><ul class="category-list list-unstyled sub-nav1 bg-color"><li class="category-list-item-navbar"><a href="/category/bison?N=game-bison">Bison</a></li><li class="category-list-item-navbar"><a href="/category/shop-game?N=game" class="shopAllInL2Category">Shop All <!-- -->Game</a></li></ul></div></div></li><li class="nav-item js-dropdown sub-nav menu-column"><div class="categoryL1ListContainer"><a class="js-dropdown__btn" href="/category/specialty?N=specialty">Specialty</a><button class="header-menu" type="button" aria-label="Open Specialty menu"><i class="fa fa-chevron-right"></i></button></div><div class="flyout-menu"><div><ul class="category-list list-unstyled sub-nav1 bg-color"><li class="category-list-item-navbar"><a href="/category/fats?N=fats">Fats</a></li><li class="category-list-item-navbar"><a href="/category/specialty-cookware?N=specialty-cookware">Cookware</a></li><li class="category-list-item-navbar"><a href="/category/prepared-foods?N=and-more-prepared-foods">Prepared Foods</a></li><li class="category-list-item-navbar"><a href="/category/specialty?N=specialty" class="shopAllInL2Category">Shop All <!-- -->Specialty</a></li></ul></div></div></li><li class="nav-item js-dropdown sub-nav menu-column"><div class="categoryL1ListContainer"><a class="js-dropdown__btn" href="/category/shop-bundles?N=bundles">Gifts &amp; Bundles</a><button class="header-menu" type="button" aria-label="Open Gifts &amp; Bundles menu"><i class="fa fa-chevron-right"></i></button></div><div class="flyout-menu"><div><ul class="category-list list-unstyled sub-nav1 bg-color"><li class="category-list-item-navbar"><a href="/category/grilling-assortments?N=assortments-grilling">Grilling</a></li><li class="category-list-item-navbar"><a href="/category/surf-and-turf-assortments?N=assortments-surf-and-turf">Surf &amp; Turf</a></li><li class="category-list-item-navbar"><a href="/category/favorite-assortments?N=assortments-favorite">Favorites</a></li><li class="category-list-item-navbar"><a href="/category/shop-bundles?N=bundles" class="shopAllInL2Category">Shop All <!-- -->Gifts &amp; Bundles</a></li></ul></div></div></li><li class="nav-item js-dropdown sub-nav menu-column"><div class="categoryL1ListContainer"><a class="js-dropdown__btn" href="/category/shop-brand?N=brand">Brand</a><button class="header-menu" type="button" aria-label="Open Brand menu"><i class="fa fa-chevron-right"></i></button></div><div class="flyout-menu"><div><ul class="category-list list-unstyled sub-nav1 bg-color"><li class="category-list-item-navbar"><a href="/category/westholme-wagyu?N=westholme-wagyu">Westholme Australian Wagyu</a></li><li class="category-list-item-navbar"><a href="/category/labelle-patrimoine?N=labelle-patrimoine">LaBelle Patrimoine®</a></li><li class="category-list-item-navbar"><a href="/category/rosewood-ranches-wagyu?N=rosewood-wagyu">Rosewood Ranches Texas Wagyu</a></li><li class="category-list-item-navbar"><a href="/category/bakers-bacon?N=bakers-bacon">Baker's Bacon</a></li><li class="category-list-item-navbar"><a href="/category/vande-rose-farms?N=vande-rose-farms">Vande Rose Farms Heritage Duroc Pork</a></li><li class="category-list-item-navbar"><a href="/category/shop-brand?N=brand" class="shopAllInL2Category">Shop All <!-- -->Brand</a></li></ul></div></div></li></ul></div></li><li class="nav-item js-dropdown navListItems"><a class="first-dropdown" href="/category/shop-beef?N=beef" style="text-decoration:none;text-transform:capitalize">Beef</a></li><li class="nav-item js-dropdown navListItems"><a class="first-dropdown" href="/category/shop-lamb?N=lamb" style="text-decoration:none;text-transform:capitalize">Lamb</a></li><li class="nav-item js-dropdown navListItems"><a class="first-dropdown" href="/category/shop-pork?N=pork" style="text-decoration:none;text-transform:capitalize">Pork</a></li><li class="nav-item js-dropdown navListItems"><a class="first-dropdown" href="/category/shop-seafood-and-fish?N=seafood-and-fish" style="text-decoration:none;text-transform:capitalize">Seafood</a></li><li class="nav-item js-dropdown navListItems"><a class="first-dropdown" href="/category/best-sellers?N=best-sellers" style="text-decoration:none;text-transform:capitalize">Best Sellers</a></li><li class="nav-item js-dropdown navListItems"><a class="first-dropdown" href="/category/on-sale?N=on-sale" style="text-decoration:none;text-transform:capitalize">On Sale</a></li><li class="nav-item js-dropdown navListItems"><a class="first-dropdown" href="#" style="text-decoration:none;text-transform:capitalize">Gift Center</a><button class="header-menu" type="button" aria-label="Open Gift Center menu"><i class="fa fa-chevron-down"></i></button><div class="header-dropdown-menu dropdown-menu nav-redesign level0Menu"><ul class="category-list list-unstyled"><li class="category-list-item"><a href="/category/shop-bundles?N=bundles">Gifts &amp; Bundles</a></li><li class="category-list-item"><a href="/category/shop-gift-cards?N=giftCards">Gifts Cards</a></li><li class="category-list-item"><a href="/corporate-gifting">Corporate Gifting</a></li></ul></div></li><li class="nav-item js-dropdown navListItems"><a class="first-dropdown" href="#" style="text-decoration:none;text-transform:capitalize">Cooking</a><button class="header-menu" type="button" aria-label="Open Cooking menu"><i class="fa fa-chevron-down"></i></button><div class="header-dropdown-menu dropdown-menu nav-redesign level0Menu"><ul class="category-list list-unstyled"><li class="category-list-item"><a href="/content/cooking-guides">Cooking Guides</a></li><li class="category-list-item"><a href="/article/delivery-storage-thawing/cg10001">Storage &amp; Thawing</a></li><li class="category-list-item"><a href="/article/recipes-steaks-halibut-lamb-shrimp-pork-/bg0015">Recipes</a></li><li class="category-list-item"><a href="/content/blog">Steaks Insider Blog</a></li></ul></div></li><li class="nav-item js-dropdown navListItems"><a class="first-dropdown" href=" https://protein.chefswarehouse.com/" style="text-decoration:none;text-transform:capitalize">Restaurant Sales</a></li></ul></div></nav>
	        """

			soup = BeautifulSoup(html, 'html.parser')
			nav = soup.find('nav', class_='container')

			if not nav:
				return {"error": "Navigation menu not found"}

			categories = []
			category_id = 1

			# Find all top-level nav items
			nav_items = nav.find_all('li', class_='nav-item', recursive=True)

			for item in nav_items:
				# Get the main category link
				main_link = item.find('a', class_='first-dropdown') or item.find('a', class_='js-dropdown__btn')

				category_name = main_link.get_text(strip=True)
				category_url = main_link.get('href', '')

				# Create category entry
				category = {
					'id': category_id,
					'name': category_name,
					'url': self.BASE_URL.rstrip('/') + category_url if category_url and not category_url.startswith(
						'http') else category_url,
					'subcategories': []
				}
				category_id += 1

				# Check for dropdown menu
				dropdown = item.find('div', class_='flyout-menu')
				if dropdown:
					# Process subcategories
					self._process_subcategories(dropdown, category, category_id)
					category_id += len(category['subcategories'])

				categories.append(category)

			return {
				"data": {
					"categories": categories
				}
			}

		except Exception as e:
			return {"error": f"Error parsing navigation: {str(e)}"}

	def _process_subcategories(self, dropdown, parent_category, start_id):
		"""
		Process subcategories from a dropdown menu.

		Args:
			dropdown: BeautifulSoup dropdown element
			parent_category: Parent category dictionary
			start_id: Starting ID for subcategories
		"""
		print("Allen->_process_subcategories()")
		current_id = start_id

		# Find all direct subcategory items
		# sub_menu = dropdown.find('div', class_='flyout-menu')
		sub_items = dropdown.find_all(['div'], recursive=False)
		print("sub_items: ", sub_items)
		for item in sub_items:
			print("item: ", item)
			# Skip if it's not a valid subcategory container
			if not (item.name == 'li' or (item.name == 'div' and item.find('a', class_='category-heading'))):
				continue

			# Handle section headings (like "Shop By Cut")
			section_heading = item.find('a', class_='category-heading')
			print("section_heading: ", section_heading)
			if section_heading:
				section_name = section_heading.get_text(strip=True)
				section_url = section_heading.get('href', '')

				section = {
					'id': current_id,
					'name': section_name,
					'url': self.BASE_URL.rstrip('/') + section_url if section_url and not section_url.startswith(
						'http') else section_url,
					'subcategories': []
				}
				current_id += 1

				# Process items in this section
				subcategory_items = item.find_all('li', class_='category-list-item-navbar')
				print("subcategory_items: ", subcategory_items)
				for sub_item in subcategory_items:
					print("sub_item: ", sub_item)
					anchor = sub_item.find('a')
					sub_name = anchor.get_text(strip=True)
					sub_url = anchor.get('href', '')

					if sub_name and sub_url:
						section['subcategories'].append({
							'id': current_id,
							'name': sub_name,
							'url': self.BASE_URL.rstrip('/') + sub_url if not sub_url.startswith('http') else sub_url,
							'subcategories': []
						})
						current_id += 1

				if section['subcategories']:
					parent_category['subcategories'].append(section)
			else:
				# Handle regular subcategories
				sub_link = item.find('a', class_='js-dropdown__btn') or item.find('a', class_='category-list-item')
				if sub_link:
					sub_name = sub_link.get_text(strip=True)
					sub_url = sub_link.get('href', '')

					if sub_name and sub_url and not sub_name.startswith('Shop All'):
						subcategory = {
							'id': current_id,
							'name': sub_name,
							'url': self.BASE_URL.rstrip('/') + sub_url if not sub_url.startswith('http') else sub_url,
							'subcategories': []
						}
						current_id += 1

						# Check for nested subcategories
						nested_dropdown = item.find('div', class_='flyout-menu')
						if nested_dropdown:
							self._process_subcategories(nested_dropdown, subcategory, current_id)
							current_id += len(subcategory['subcategories'])

						parent_category['subcategories'].append(subcategory)

	def get_category_page(self, url, category_name, sub_category_name, sub_sub_category_name):
		print("get_category_page()")
		detail_urls = []
		main_window = self.driver.current_window_handle
		html = ''
		total_products = 0
		self.driver.get(url)
		self.wait = WebDriverWait(self.driver, 10)
		try:
			# Update URL from the redirect
			url = self.driver.current_url
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
					if url in self.driver.current_url:
						print("Found products page")
						time.sleep(2)
						html_line, detail_urls = self.get_products_from_html()
					products_found_count = len(detail_urls)
					html += f"<div>Found {products_found_count} products for category {sub_category_name}</div>"
					print(f"Found {products_found_count} products for category {sub_category_name}")
					total_products += products_found_count
					print(detail_urls)
					self.save_urls_to_csv(detail_urls, category_name, sub_category_name, sub_sub_category_name)

				except Exception as e:
					print(f"****************** ⛔️⛔️⛔️ Error getting details: {e}")
					html += f"<div>Name: {sub_category_name} (Error getting details)</div>"

				try:
					paging = self.wait.until(
						EC.presence_of_element_located((By.CSS_SELECTOR, '.page_c'))
					)
					print("Checking 1")
					next_disabled = paging.find_element(By.CSS_SELECTOR, 'a.next')
					class_attribute = next_disabled.get_attribute("class")
					classes = class_attribute.split()
					print(next_disabled)
					print("Checking 2")
					if not 'disabled' in classes:
						paging.find_element(By.CLASS_NAME, 'next').click()
						print("Going to next page")
						next_page = True
					else:
						print("Next is disabled")
						next_page = False
				except Exception as e:
					print("There is no next page")
					next_page = False


		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing category: {e}")

		return detail_urls, html

	def get_products_from_html(self):

		products = self.wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.product-image'))
		)

		print(f"products found: {len(products)}")
		detail_urls = [product.get_attribute("href") for product in products]
		return '', detail_urls
