import os
from os import times_result

import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from seleniumwire.utils import decode

from scrapers.scraper import Scraper, SkuNotFound, ProductNotFound

"""
	Sysco
	Type: Standard shop website
	Method: 
		Get Categories: Scape Navigation
		Get Products: Scape Product List from GraphQL API
		Get Product from GraphQL API
	Issues:
		Website resets after about 1500 products pulled
		Must sometime manually click to get started
		Can not direct link, have to bypass the dialogs and then click on a menu item to get started
"""


class SyscoScraper(Scraper):
	# /2974/edit_note/1709/
	CRM_ID = 2974
	CRM_NOTE_ID = 1709
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = 'Ready'

	DISTRIBUTOR_PRODUCT_DATA_SPEC = {
		'extra_data_3': '',
		'product_id': '',
		'productGroupId': '',
		'manufacturerUPC': '',
		'sellerId': '',
	}
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/sysco/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = 'https://shop.sysco.com/app/discover'
	VENDOR_NAME = 'Sysco'
	CATEGORIES = json.loads('''{
  "data": {
    "categories": 
      [
        {
          "id": 1,
          "name": "Produce",
          "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce",
          "subcategories": [
            {
              "name": "Vegetables",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables",
              "subcategories": [
                {
                  "name": "Mushrooms",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_mushrooms"
                },
                {
                  "name": "Lettuce and Leafy Greens",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_lettuceandleafygreens"
                },
                {
                  "name": "Asparagus and Artichoke and Celery",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_asparagusandartichokeandcel"
                },
                {
                  "name": "Potatoes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_potatoes"
                },
                {
                  "name": "Squash and Eggplant and Pumpkin",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_squashandeggplantandpumpkin"
                },
                {
                  "name": "Cabbages and Sauerkraut",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_cabbagesandsauerkraut"
                },
                {
                  "name": "Root Vegetables",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_rootvegetables"
                },
                {
                  "name": "Onions, Leeks and Garlic",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_onionsleeksandgarlic"
                },
                {
                  "name": "Herbs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_herbs"
                },
                {
                  "name": "Value Added Fresh Blends",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_valueaddedfreshblends"
                },
                {
                  "name": "Peppers and Pimentos",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_peppersandpimentos"
                },
                {
                  "name": "Corn",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_corn"
                },
                {
                  "name": "Cucumbers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_cucumbers"
                },
                {
                  "name": "Beans and Peas",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_beansandpeas_L3_3"
                },
                {
                  "name": "Baby and Specialty Vegetables",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_babyandspecialtyvegetables"
                },
                {
                  "name": "Asian Vegetables",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_asianvegetables_L3"
                },
                {
                  "name": "Broccoli and Cauliflower",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_broccoliandcauliflower"
                },
                {
                  "name": "Tomatoes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_tomatoes_L3"
                }
              ]
            },
            {
              "name": "Fruit",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_fruit",
              "subcategories": [
                {
                  "name": "Citrus Fruit",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_fruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_citrusfruit"
                },
                {
                  "name": "Grapes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_fruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_grapes"
                },
                {
                  "name": "Melons",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_fruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_melons"
                },
                {
                  "name": "Bananas and Tropical Fruit",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_fruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_bananasandtropicalfruit"
                },
                {
                  "name": "Apples",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_fruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_apples"
                },
                {
                  "name": "Avocados",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_fruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_avocados"
                },
                {
                  "name": "Pears",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_fruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_pears"
                },
                {
                  "name": "Guacamole and Processed Avocados",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_fruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_guacamoleandprocessedavocad"
                },
                {
                  "name": "Peaches and Plums",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_fruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_peachesandplums_L3"
                },
                {
                  "name": "Berries",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_fruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_berries_L3"
                },
                {
                  "name": "Mixed Fruit",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_fruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_mixedfruit"
                }
              ]
            },
            {
              "name": "Prepared Salads",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_preparedsalads",
              "subcategories": [
                {
                  "name": "Bean Salads",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_preparedsalads&ATTRIBUTE_GROUP_ID=syy_cust_tax_beansalads"
                },
                {
                  "name": "Prepared Salads",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_preparedsalads&ATTRIBUTE_GROUP_ID=syy_cust_tax_preparedsalads_L3"
                },
                {
                  "name": "Salad Kits",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_preparedsalads&ATTRIBUTE_GROUP_ID=syy_cust_tax_saladkits"
                },
                {
                  "name": "Relish",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_preparedsalads&ATTRIBUTE_GROUP_ID=syy_cust_tax_relish_L3"
                }
              ]
            },
            {
              "name": "Produce Wash",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_producewash",
              "subcategories": []
            }
          ]
        },
        {
          "id": 2,
          "name": "Meat & Seafood",
          "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood",
          "subcategories": [
            {
              "name": "Poultry",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry",
              "subcategories": [
                {
                  "name": "Duck",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_duck"
                },
                {
                  "name": "Turkey",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_turkey"
                },
                {
                  "name": "Chicken Breasts",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_chickenbreasts"
                },
                {
                  "name": "Fajita Strips",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_fajitastrips"
                },
                {
                  "name": "Other Poultry",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_otherpoultry"
                },
                {
                  "name": "Hot Dogs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_hotdogs"
                },
                {
                  "name": "Chicken Thighs and Legs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_chickenthighsandlegs"
                },
                {
                  "name": "Chicken Wings",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_chickenwings"
                },
                {
                  "name": "Deli Meat",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_delimeat"
                },
                {
                  "name": "Chicken Tenders",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_chickentenders"
                },
                {
                  "name": "Ground Meats",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_groundmeats"
                },
                {
                  "name": "Chicken Nuggets and Patties",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_chickennuggetsandpatties"
                },
                {
                  "name": "Sausage",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_sausage"
                },
                {
                  "name": "Whole Chicken Cuts",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_wholechickencuts"
                },
                {
                  "name": "Whole Chicken",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_wholechicken"
                },
                {
                  "name": "Turkey Bacon",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_turkeybacon"
                },
                {
                  "name": "Chicken Diced, Pulled and Shredded",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_chickendicedpulledandshred"
                },
                {
                  "name": "Other Chicken",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_otherchicken"
                },
                {
                  "name": "Quail",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_poultry&ATTRIBUTE_GROUP_ID=syy_cust_tax_quail"
                }
              ]
            },
            {
              "name": "Beef",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef",
              "subcategories": [
                {
                  "name": "Ribs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_ribs"
                },
                {
                  "name": "Other Beef",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_otherbeef"
                },
                {
                  "name": "Steaks",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_steaks"
                },
                {
                  "name": "Thins",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_thins"
                },
                {
                  "name": "Value Added Beef",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_valueaddedbeef"
                },
                {
                  "name": "Deli Meat",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_delimeat_L3"
                },
                {
                  "name": "Patties",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_patties"
                },
                {
                  "name": "Brisket",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_brisket"
                },
                {
                  "name": "Loins",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_loins"
                },
                {
                  "name": "Ground & Diced",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_grounddiced"
                },
                {
                  "name": "Chuck",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_chuck"
                },
                {
                  "name": "Round",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_round"
                },
                {
                  "name": "Meatballs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_meatballs"
                },
                {
                  "name": "Hot Dogs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_hotdogs_L3_3"
                },
                {
                  "name": "Pizza Toppings",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_pizzatoppings_L3"
                },
                {
                  "name": "Sausage",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_sausage_L3_3"
                },
                {
                  "name": "Bacon",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_beef&ATTRIBUTE_GROUP_ID=syy_cust_tax_bacon_L3"
                }
              ]
            },
            {
              "name": "Pork",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork",
              "subcategories": [
                {
                  "name": "Bacon",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_bacon"
                },
                {
                  "name": "Pork Loins",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_porkloins"
                },
                {
                  "name": "Pork Chops and Steaks",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_porkchopsandsteaks"
                },
                {
                  "name": "Pizza Toppings",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_pizzatoppings"
                },
                {
                  "name": "Deli Meat",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_delimeat_L3_3"
                },
                {
                  "name": "Sausage",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_sausage_L3"
                },
                {
                  "name": "Ham",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_ham"
                },
                {
                  "name": "Other Pork",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_otherpork"
                },
                {
                  "name": "Ground and Diced Pork",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_groundanddicedpork"
                },
                {
                  "name": "Value Added Pork",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_valueaddedpork"
                },
                {
                  "name": "Shoulders and Butts",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_shouldersandbutts"
                },
                {
                  "name": "Ribs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_ribs_L3"
                },
                {
                  "name": "Hot Dogs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_hotdogs_L3"
                },
                {
                  "name": "Pork Bellies",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_pork&ATTRIBUTE_GROUP_ID=syy_cust_tax_porkbellies"
                }
              ]
            },
            {
              "name": "Seafood",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood",
              "subcategories": [
                {
                  "name": "Shrimp",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood&ATTRIBUTE_GROUP_ID=syy_cust_tax_shrimp"
                },
                {
                  "name": "Salmon",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood&ATTRIBUTE_GROUP_ID=syy_cust_tax_salmon"
                },
                {
                  "name": "Sushi",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood&ATTRIBUTE_GROUP_ID=syy_cust_tax_sushi"
                },
                {
                  "name": "Tuna",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood&ATTRIBUTE_GROUP_ID=syy_cust_tax_tuna"
                },
                {
                  "name": "Other Finfish",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood&ATTRIBUTE_GROUP_ID=syy_cust_tax_otherfinfish"
                },
                {
                  "name": "Value Added Seafood",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood&ATTRIBUTE_GROUP_ID=syy_cust_tax_valueaddedseafood"
                },
                {
                  "name": "Other Shellfish",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood&ATTRIBUTE_GROUP_ID=syy_cust_tax_othershellfish"
                },
                {
                  "name": "Crab",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood&ATTRIBUTE_GROUP_ID=syy_cust_tax_crab"
                },
                {
                  "name": "Lobster and Crawfish",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood&ATTRIBUTE_GROUP_ID=syy_cust_tax_lobsterandcrawfish"
                },
                {
                  "name": "Canned Seafood",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood&ATTRIBUTE_GROUP_ID=syy_cust_tax_cannedseafood"
                },
                {
                  "name": "Catfish",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood&ATTRIBUTE_GROUP_ID=syy_cust_tax_catfish"
                },
                {
                  "name": "Exotic Seafood",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_seafood&ATTRIBUTE_GROUP_ID=syy_cust_tax_exoticseafood"
                }
              ]
            },
            {
              "name": "Other Meats",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_othermeats",
              "subcategories": [
                {
                  "name": "Veal",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_othermeats&ATTRIBUTE_GROUP_ID=syy_cust_tax_veal"
                },
                {
                  "name": "Lamb",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_othermeats&ATTRIBUTE_GROUP_ID=syy_cust_tax_lamb"
                },
                {
                  "name": "Game and Exotic Meats",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_othermeats&ATTRIBUTE_GROUP_ID=syy_cust_tax_gameandexoticmeats"
                },
                {
                  "name": "Goat",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_othermeats&ATTRIBUTE_GROUP_ID=syy_cust_tax_goat"
                }
              ]
            },
            {
              "name": "Alternative Protein",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_alternativeprotein",
              "subcategories": [
                {
                  "name": "Tofu",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_alternativeprotein&ATTRIBUTE_GROUP_ID=syy_cust_tax_tofu"
                },
                {
                  "name": "Plant-based Protein",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_meatseafood&ITEM_GROUP_ID=syy_cust_tax_alternativeprotein&ATTRIBUTE_GROUP_ID=syy_cust_tax_plant-basedprotein"
                }
              ]
            }
          ]
        },
        {
          "id": 3,
          "name": "Bakery & Bread",
          "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread",
          "subcategories": [
            {
              "name": "Bread",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bread",
              "subcategories": [
                {
                  "name": "Sandwich Carriers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bread&ATTRIBUTE_GROUP_ID=syy_cust_tax_sandwichcarriers"
                },
                {
                  "name": "Baguettes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bread&ATTRIBUTE_GROUP_ID=syy_cust_tax_baguettes"
                },
                {
                  "name": "Flat Breads",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bread&ATTRIBUTE_GROUP_ID=syy_cust_tax_flatbreads"
                },
                {
                  "name": "Sheet Breads",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bread&ATTRIBUTE_GROUP_ID=syy_cust_tax_sheetbreads"
                },
                {
                  "name": "Sandwich Loaves",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bread&ATTRIBUTE_GROUP_ID=syy_cust_tax_sandwichloaves"
                },
                {
                  "name": "Dinner Rolls",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bread&ATTRIBUTE_GROUP_ID=syy_cust_tax_dinnerrolls"
                },
                {
                  "name": "Bread Dough",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bread&ATTRIBUTE_GROUP_ID=syy_cust_tax_breaddough"
                },
                {
                  "name": "Breadsticks",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bread&ATTRIBUTE_GROUP_ID=syy_cust_tax_breadsticks"
                },
                {
                  "name": "Soft Pretzels",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bread&ATTRIBUTE_GROUP_ID=syy_cust_tax_softpretzels"
                }
              ]
            },
            {
              "name": "Breakfast Breads and Pastries",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_breakfastbreadsandpastries",
              "subcategories": [
                {
                  "name": "Biscuits",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_breakfastbreadsandpastries&ATTRIBUTE_GROUP_ID=syy_cust_tax_biscuits"
                },
                {
                  "name": "Danish",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_breakfastbreadsandpastries&ATTRIBUTE_GROUP_ID=syy_cust_tax_danish"
                },
                {
                  "name": "Muffins and Muffin Batter",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_breakfastbreadsandpastries&ATTRIBUTE_GROUP_ID=syy_cust_tax_muffinsandmuffinbatter"
                },
                {
                  "name": "Donuts and Churros",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_breakfastbreadsandpastries&ATTRIBUTE_GROUP_ID=syy_cust_tax_donutsandchurros"
                },
                {
                  "name": "Bagels",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_breakfastbreadsandpastries&ATTRIBUTE_GROUP_ID=syy_cust_tax_bagels"
                },
                {
                  "name": "Cinnamon Rolls and Sweet Rolls",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_breakfastbreadsandpastries&ATTRIBUTE_GROUP_ID=syy_cust_tax_cinnamonrollsandsweetrolls"
                },
                {
                  "name": "English Muffins",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_breakfastbreadsandpastries&ATTRIBUTE_GROUP_ID=syy_cust_tax_englishmuffins"
                },
                {
                  "name": "Scones",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_breakfastbreadsandpastries&ATTRIBUTE_GROUP_ID=syy_cust_tax_scones"
                }
              ]
            },
            {
              "name": "Desserts",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_desserts",
              "subcategories": [
                {
                  "name": "Cake",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_desserts&ATTRIBUTE_GROUP_ID=syy_cust_tax_cake"
                },
                {
                  "name": "Pastries and Mini Desserts",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_desserts&ATTRIBUTE_GROUP_ID=syy_cust_tax_pastriesandminidesserts"
                },
                {
                  "name": "Brownies",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_desserts&ATTRIBUTE_GROUP_ID=syy_cust_tax_brownies"
                },
                {
                  "name": "Snack Bars",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_desserts&ATTRIBUTE_GROUP_ID=syy_cust_tax_snackbars"
                },
                {
                  "name": "Cheesecake",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_desserts&ATTRIBUTE_GROUP_ID=syy_cust_tax_cheesecake"
                },
                {
                  "name": "Pies",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_desserts&ATTRIBUTE_GROUP_ID=syy_cust_tax_pies"
                },
                {
                  "name": "Cookies",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_desserts&ATTRIBUTE_GROUP_ID=syy_cust_tax_cookies_L3"
                },
                {
                  "name": "Cookie Dough",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_desserts&ATTRIBUTE_GROUP_ID=syy_cust_tax_cookiedough"
                }
              ]
            },
            {
              "name": "Baking Elements",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bakingelements",
              "subcategories": [
                {
                  "name": "Breading and Batters",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bakingelements&ATTRIBUTE_GROUP_ID=syy_cust_tax_breadingandbatters"
                },
                {
                  "name": "Melting Chocolates",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bakingelements&ATTRIBUTE_GROUP_ID=syy_cust_tax_meltingchocolates"
                },
                {
                  "name": "Crusts, Sheet Dough & Shells",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bakingelements&ATTRIBUTE_GROUP_ID=syy_cust_tax_crustssheetdoughshells"
                },
                {
                  "name": "Chocolate Chips",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bakingelements&ATTRIBUTE_GROUP_ID=syy_cust_tax_chocolatechips"
                },
                {
                  "name": "Dessert and Ice Cream Toppings",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bakingelements&ATTRIBUTE_GROUP_ID=syy_cust_tax_dessertandicecreamtoppings"
                },
                {
                  "name": "Baking Chips and Cocoa Powder",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bakingelements&ATTRIBUTE_GROUP_ID=syy_cust_tax_bakingchipsandcocoapowder"
                },
                {
                  "name": "Frosting and Icing",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bakingelements&ATTRIBUTE_GROUP_ID=syy_cust_tax_frostingandicing"
                },
                {
                  "name": "Pie and Pastry Fillings",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bakingelements&ATTRIBUTE_GROUP_ID=syy_cust_tax_pieandpastryfillings"
                },
                {
                  "name": "Extracts & Food Colorings",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bakingelements&ATTRIBUTE_GROUP_ID=syy_cust_tax_extractsfoodcolorings"
                },
                {
                  "name": "Cornstarch and Baking Soda",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bakingelements&ATTRIBUTE_GROUP_ID=syy_cust_tax_cornstarchandbakingsoda"
                },
                {
                  "name": "Coconut Flakes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_bakingelements&ATTRIBUTE_GROUP_ID=syy_cust_tax_coconutflakes"
                }
              ]
            },
            {
              "name": "Tortillas and Wraps",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_tortillasandwraps",
              "subcategories": [
                {
                  "name": "Cut Tortillas",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_tortillasandwraps&ATTRIBUTE_GROUP_ID=syy_cust_tax_cuttortillas"
                },
                {
                  "name": "Tortillas and Wraps",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_tortillasandwraps&ATTRIBUTE_GROUP_ID=syy_cust_tax_tortillasandwraps_L3"
                }
              ]
            },
            {
              "name": "Taco and Tostada Shells",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_tacoandtostadashells",
              "subcategories": []
            },
            {
              "name": "Croissants",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_bakerybread&ITEM_GROUP_ID=syy_cust_tax_croissants",
              "subcategories": []
            }
          ]
        },
        {
          "id": 4,
          "name": "Dairy & Eggs",
          "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs",
          "subcategories": [
            {
              "name": "Eggs",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_eggs",
              "subcategories": [
                {
                  "name": "Pre-Cooked Eggs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_eggs&ATTRIBUTE_GROUP_ID=syy_cust_tax_pre-cookedeggs"
                },
                {
                  "name": "Liquid Eggs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_eggs&ATTRIBUTE_GROUP_ID=syy_cust_tax_liquideggs"
                },
                {
                  "name": "Shell Eggs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_eggs&ATTRIBUTE_GROUP_ID=syy_cust_tax_shelleggs"
                },
                {
                  "name": "Dry and Powdered Eggs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_eggs&ATTRIBUTE_GROUP_ID=syy_cust_tax_dryandpowderedeggs"
                }
              ]
            },
            {
              "name": "Cheese",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese",
              "subcategories": [
                {
                  "name": "Blue Cheeses",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_bluecheeses"
                },
                {
                  "name": "Soft Italian Cheese",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_softitaliancheese"
                },
                {
                  "name": "Hispanic Cheese",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_hispaniccheese"
                },
                {
                  "name": "Mozzarella and Provolone",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_mozzarellaandprovolone"
                },
                {
                  "name": "Hard Italian Cheese",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_harditaliancheese"
                },
                {
                  "name": "Fresh Cheeses",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_freshcheeses"
                },
                {
                  "name": "Cheddars",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_cheddars"
                },
                {
                  "name": "Semi Hard Cheeses",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_semihardcheeses"
                },
                {
                  "name": "Soft Cheeses",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_softcheeses"
                },
                {
                  "name": "Pepper Jack",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_pepperjack"
                },
                {
                  "name": "Colby & Colby Jack",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_colbycolbyjack"
                },
                {
                  "name": "Semi Soft Cheeses",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_semisoftcheeses"
                },
                {
                  "name": "Hard Cheeses",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_hardcheeses"
                },
                {
                  "name": "Monterey Jack",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_montereyjack"
                },
                {
                  "name": "Blend Cheeses",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_blendcheeses"
                },
                {
                  "name": "Hispanic Cheeses",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_hispaniccheeses"
                }
              ]
            },
            {
              "name": "Butter & Margarine",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_buttermargarine",
              "subcategories": []
            },
            {
              "name": "Milk",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_milk",
              "subcategories": []
            },
            {
              "name": "Yogurt and Pudding",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_yogurtandpudding",
              "subcategories": []
            },
            {
              "name": "Cream",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cream",
              "subcategories": []
            },
            {
              "name": "Processed Cheese",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_processedcheese",
              "subcategories": [
                {
                  "name": "Cheese Spreads",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_processedcheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_cheesespreads"
                },
                {
                  "name": "Processed Cheese",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_processedcheese&ATTRIBUTE_GROUP_ID=syy_cust_tax_processedcheese_L3"
                }
              ]
            },
            {
              "name": "Sour Cream",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_sourcream",
              "subcategories": []
            },
            {
              "name": "Non-Dairy Alternatives",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_non-dairyalternatives",
              "subcategories": [
                {
                  "name": "Non-Dairy Milk",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_non-dairyalternatives&ATTRIBUTE_GROUP_ID=syy_cust_tax_non-dairymilk"
                },
                {
                  "name": "Non-Dairy Creamer",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_non-dairyalternatives&ATTRIBUTE_GROUP_ID=syy_cust_tax_non-dairycreamer"
                },
                {
                  "name": "Non-Dairy Yogurt",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_non-dairyalternatives&ATTRIBUTE_GROUP_ID=syy_cust_tax_non-dairyyogurt"
                },
                {
                  "name": "Non-Dairy Cheese",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_non-dairyalternatives&ATTRIBUTE_GROUP_ID=syy_cust_tax_non-dairycheese"
                },
                {
                  "name": "Non-Dairy Cream",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_non-dairyalternatives&ATTRIBUTE_GROUP_ID=syy_cust_tax_non-dairycream"
                },
                {
                  "name": "Non-Dairy Puddings",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_non-dairyalternatives&ATTRIBUTE_GROUP_ID=syy_cust_tax_non-dairypuddings"
                },
                {
                  "name": "Non-Dairy Toppings",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_non-dairyalternatives&ATTRIBUTE_GROUP_ID=syy_cust_tax_non-dairytoppings"
                },
                {
                  "name": "Non-Dairy Cream Cheese",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_non-dairyalternatives&ATTRIBUTE_GROUP_ID=syy_cust_tax_non-dairycreamcheese"
                },
                {
                  "name": "Non-Dairy Eggs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_non-dairyalternatives&ATTRIBUTE_GROUP_ID=syy_cust_tax_non-dairyeggs"
                },
                {
                  "name": "Non-Dairy Sour Cream",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_non-dairyalternatives&ATTRIBUTE_GROUP_ID=syy_cust_tax_non-dairysourcream"
                }
              ]
            },
            {
              "name": "Toppings",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_toppings",
              "subcategories": [
                {
                  "name": "Dairy Toppings",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_toppings&ATTRIBUTE_GROUP_ID=syy_cust_tax_dairytoppings"
                }
              ]
            },
            {
              "name": "Cream Cheese",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_creamcheese",
              "subcategories": []
            },
            {
              "name": "Cultures",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_cultures",
              "subcategories": []
            },
            {
              "name": "Creamer",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_creamer",
              "subcategories": [
                {
                  "name": "Creamer",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_dairyeggs&ITEM_GROUP_ID=syy_cust_tax_creamer&ATTRIBUTE_GROUP_ID=syy_cust_tax_creamer_L3"
                }
              ]
            }
          ]
        },
        {
          "id": 5,
          "name": "Canned & Dry",
          "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry",
          "subcategories": [
            {
              "name": "Sauces and Marinades",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_saucesandmarinades",
              "subcategories": [
                {
                  "name": "Sauces",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_saucesandmarinades&ATTRIBUTE_GROUP_ID=syy_cust_tax_sauces"
                },
                {
                  "name": "Gravies",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_saucesandmarinades&ATTRIBUTE_GROUP_ID=syy_cust_tax_gravies"
                },
                {
                  "name": "Salsa",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_saucesandmarinades&ATTRIBUTE_GROUP_ID=syy_cust_tax_salsa"
                },
                {
                  "name": "Wing Sauce",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_saucesandmarinades&ATTRIBUTE_GROUP_ID=syy_cust_tax_wingsauce"
                },
                {
                  "name": "Tomato Sauces",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_saucesandmarinades&ATTRIBUTE_GROUP_ID=syy_cust_tax_tomatosauces"
                }
              ]
            },
            {
              "name": "Spices and Seasonings",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_spicesandseasonings",
              "subcategories": [
                {
                  "name": "Spices and Herbs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_spicesandseasonings&ATTRIBUTE_GROUP_ID=syy_cust_tax_spicesandherbs"
                },
                {
                  "name": "Salt and Pepper",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_spicesandseasonings&ATTRIBUTE_GROUP_ID=syy_cust_tax_saltandpepper"
                },
                {
                  "name": "Seasonings",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_spicesandseasonings&ATTRIBUTE_GROUP_ID=syy_cust_tax_seasonings"
                }
              ]
            },
            {
              "name": "Condiments",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_condiments",
              "subcategories": [
                {
                  "name": "Sauces",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_condiments&ATTRIBUTE_GROUP_ID=syy_cust_tax_sauces_L3"
                },
                {
                  "name": "Pickles",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_condiments&ATTRIBUTE_GROUP_ID=syy_cust_tax_pickles"
                },
                {
                  "name": "Pickled Vegetables",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_condiments&ATTRIBUTE_GROUP_ID=syy_cust_tax_pickledvegetables"
                },
                {
                  "name": "Spreads",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_condiments&ATTRIBUTE_GROUP_ID=syy_cust_tax_spreads"
                },
                {
                  "name": "Relish",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_condiments&ATTRIBUTE_GROUP_ID=syy_cust_tax_relish"
                },
                {
                  "name": "Ketchup",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_condiments&ATTRIBUTE_GROUP_ID=syy_cust_tax_ketchup"
                },
                {
                  "name": "Mustard",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_condiments&ATTRIBUTE_GROUP_ID=syy_cust_tax_mustard"
                },
                {
                  "name": "Mayonnaise",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_condiments&ATTRIBUTE_GROUP_ID=syy_cust_tax_mayonnaise"
                }
              ]
            },
            {
              "name": "Snacks and Candy",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_snacksandcandy",
              "subcategories": [
                {
                  "name": "Chocolate",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_snacksandcandy&ATTRIBUTE_GROUP_ID=syy_cust_tax_chocolate"
                },
                {
                  "name": "Candy",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_snacksandcandy&ATTRIBUTE_GROUP_ID=syy_cust_tax_candy"
                },
                {
                  "name": "Crackers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_snacksandcandy&ATTRIBUTE_GROUP_ID=syy_cust_tax_crackers"
                },
                {
                  "name": "Cookies",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_snacksandcandy&ATTRIBUTE_GROUP_ID=syy_cust_tax_cookies"
                },
                {
                  "name": "Cones",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_snacksandcandy&ATTRIBUTE_GROUP_ID=syy_cust_tax_cones"
                },
                {
                  "name": "Nuts and Seeds",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_snacksandcandy&ATTRIBUTE_GROUP_ID=syy_cust_tax_nutsandseeds"
                },
                {
                  "name": "Snacks",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_snacksandcandy&ATTRIBUTE_GROUP_ID=syy_cust_tax_snacks"
                },
                {
                  "name": "Popcorn",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_snacksandcandy&ATTRIBUTE_GROUP_ID=syy_cust_tax_popcorn"
                },
                {
                  "name": "Chips",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_snacksandcandy&ATTRIBUTE_GROUP_ID=syy_cust_tax_chips"
                },
                {
                  "name": "Fruit and Sweets",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_snacksandcandy&ATTRIBUTE_GROUP_ID=syy_cust_tax_fruitandsweets"
                }
              ]
            },
            {
              "name": "Canned Fruit",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit",
              "subcategories": [
                {
                  "name": "Olives",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_olives"
                },
                {
                  "name": "Peaches and Plums",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_peachesandplums"
                },
                {
                  "name": "Dried Fruits",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_driedfruits"
                },
                {
                  "name": "Apples",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_apples_L3"
                },
                {
                  "name": "Bananas",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_bananas"
                },
                {
                  "name": "Dried Fruit and Nuts",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_driedfruitandnuts"
                },
                {
                  "name": "Berries",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_berries_L3_3"
                },
                {
                  "name": "Mixed Fruit",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_mixedfruit_L3"
                },
                {
                  "name": "Pears",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_pears_L3"
                },
                {
                  "name": "Fruit Purees",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_fruitpurees_L3"
                },
                {
                  "name": "Citrus Fruit",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_citrusfruit_L3"
                },
                {
                  "name": "Melons",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_melons_L3"
                }
              ]
            },
            {
              "name": "Canned Vegetables",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables",
              "subcategories": [
                {
                  "name": "Onions and Garlic",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_onionsandgarlic"
                },
                {
                  "name": "Peppers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_peppers"
                },
                {
                  "name": "Asparagus",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_asparagus_L3"
                },
                {
                  "name": "Beans and Peas",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_beansandpeas"
                },
                {
                  "name": "Mushrooms",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_mushrooms_L3"
                },
                {
                  "name": "Asian Vegetables",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_asianvegetables"
                },
                {
                  "name": "Potatoes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_potatoes_L3"
                },
                {
                  "name": "Squash",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_squash_L3"
                },
                {
                  "name": "Root Vegetables",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_rootvegetables_L3_3"
                },
                {
                  "name": "Corn",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_corn_L3"
                },
                {
                  "name": "Baby Vegatables",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_babyvegatables"
                },
                {
                  "name": "Sauerkraut and Cabbage",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_sauerkrautandcabbage"
                },
                {
                  "name": "Vegetable Mixes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_vegetablemixes_L3"
                },
                {
                  "name": "Lettuce",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_lettuce"
                },
                {
                  "name": "Tomatoes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cannedvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_tomatoes"
                }
              ]
            },
            {
              "name": "Baking Ingredients",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingingredients",
              "subcategories": [
                {
                  "name": "Flour",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingingredients&ATTRIBUTE_GROUP_ID=syy_cust_tax_flour"
                },
                {
                  "name": "Oils and Shorteners",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingingredients&ATTRIBUTE_GROUP_ID=syy_cust_tax_oilsandshorteners"
                },
                {
                  "name": "Cooking Sprays",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingingredients&ATTRIBUTE_GROUP_ID=syy_cust_tax_cookingsprays"
                }
              ]
            },
            {
              "name": "Baking Mixes",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingmixes",
              "subcategories": [
                {
                  "name": "Muffin Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingmixes&ATTRIBUTE_GROUP_ID=syy_cust_tax_muffinmix"
                },
                {
                  "name": "Bread Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingmixes&ATTRIBUTE_GROUP_ID=syy_cust_tax_breadmix"
                },
                {
                  "name": "Cake Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingmixes&ATTRIBUTE_GROUP_ID=syy_cust_tax_cakemix"
                },
                {
                  "name": "Cookie Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingmixes&ATTRIBUTE_GROUP_ID=syy_cust_tax_cookiemix"
                },
                {
                  "name": "Pudding Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingmixes&ATTRIBUTE_GROUP_ID=syy_cust_tax_puddingmix"
                },
                {
                  "name": "Biscuit Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingmixes&ATTRIBUTE_GROUP_ID=syy_cust_tax_biscuitmix"
                },
                {
                  "name": "Specialty Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingmixes&ATTRIBUTE_GROUP_ID=syy_cust_tax_specialtymix"
                },
                {
                  "name": "Cornbread Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingmixes&ATTRIBUTE_GROUP_ID=syy_cust_tax_cornbreadmix"
                },
                {
                  "name": "Brownie Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_bakingmixes&ATTRIBUTE_GROUP_ID=syy_cust_tax_browniemix"
                }
              ]
            },
            {
              "name": "Pasta and Rice",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_pastaandrice",
              "subcategories": [
                {
                  "name": "Rice",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_pastaandrice&ATTRIBUTE_GROUP_ID=syy_cust_tax_rice"
                },
                {
                  "name": "Pasta",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_pastaandrice&ATTRIBUTE_GROUP_ID=syy_cust_tax_pasta_L3"
                }
              ]
            },
            {
              "name": "Cereal and Breakfast",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cerealandbreakfast",
              "subcategories": [
                {
                  "name": "Cold Cereal",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cerealandbreakfast&ATTRIBUTE_GROUP_ID=syy_cust_tax_coldcereal"
                },
                {
                  "name": "Hot Cereal",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cerealandbreakfast&ATTRIBUTE_GROUP_ID=syy_cust_tax_hotcereal"
                },
                {
                  "name": "Pancake and Waffle Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cerealandbreakfast&ATTRIBUTE_GROUP_ID=syy_cust_tax_pancakeandwafflemix"
                },
                {
                  "name": "Syrup",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_cerealandbreakfast&ATTRIBUTE_GROUP_ID=syy_cust_tax_syrup_L3"
                }
              ]
            },
            {
              "name": "Dressings, Oil and Vinegar",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_dressingsoilandvinegar",
              "subcategories": [
                {
                  "name": "Salad Dressing",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_dressingsoilandvinegar&ATTRIBUTE_GROUP_ID=syy_cust_tax_saladdressing"
                },
                {
                  "name": "Vinegar",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_dressingsoilandvinegar&ATTRIBUTE_GROUP_ID=syy_cust_tax_vinegar"
                },
                {
                  "name": "Toppings and Croutons",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_dressingsoilandvinegar&ATTRIBUTE_GROUP_ID=syy_cust_tax_toppingsandcroutons"
                }
              ]
            },
            {
              "name": "Soups and Chili",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_soupsandchili",
              "subcategories": [
                {
                  "name": "Bases",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_soupsandchili&ATTRIBUTE_GROUP_ID=syy_cust_tax_bases"
                },
                {
                  "name": "Chili",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_soupsandchili&ATTRIBUTE_GROUP_ID=syy_cust_tax_chili"
                },
                {
                  "name": "Soups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_soupsandchili&ATTRIBUTE_GROUP_ID=syy_cust_tax_soups"
                },
                {
                  "name": "Chowder",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_soupsandchili&ATTRIBUTE_GROUP_ID=syy_cust_tax_chowder"
                }
              ]
            },
            {
              "name": "Sugar and Sweeteners",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_sugarandsweeteners",
              "subcategories": [
                {
                  "name": "Sugar",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_sugarandsweeteners&ATTRIBUTE_GROUP_ID=syy_cust_tax_sugar"
                },
                {
                  "name": "Syrup",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_sugarandsweeteners&ATTRIBUTE_GROUP_ID=syy_cust_tax_syrup"
                },
                {
                  "name": "Sugar Substitutes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_sugarandsweeteners&ATTRIBUTE_GROUP_ID=syy_cust_tax_sugarsubstitutes"
                }
              ]
            },
            {
              "name": "Baby Food and Formula",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_canneddry&ITEM_GROUP_ID=syy_cust_tax_babyfoodandformula",
              "subcategories": []
            }
          ]
        },
        {
          "id": 6,
          "name": "Frozen Foods",
          "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods",
          "subcategories": [
            {
              "name": "French Fries",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frenchfries",
              "subcategories": []
            },
            {
              "name": "Ice Cream",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_icecream",
              "subcategories": [
                {
                  "name": "Sorbet",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_icecream&ATTRIBUTE_GROUP_ID=syy_cust_tax_sorbet"
                },
                {
                  "name": "Ice Cream Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_icecream&ATTRIBUTE_GROUP_ID=syy_cust_tax_icecreammix"
                },
                {
                  "name": "Frozen Novelties",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_icecream&ATTRIBUTE_GROUP_ID=syy_cust_tax_frozennovelties"
                },
                {
                  "name": "Ice Cream",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_icecream&ATTRIBUTE_GROUP_ID=syy_cust_tax_icecream_L3"
                },
                {
                  "name": "Sherbet",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_icecream&ATTRIBUTE_GROUP_ID=syy_cust_tax_sherbet"
                },
                {
                  "name": "Frozen Yogurt Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_icecream&ATTRIBUTE_GROUP_ID=syy_cust_tax_frozenyogurtmix"
                },
                {
                  "name": "Gelato",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_icecream&ATTRIBUTE_GROUP_ID=syy_cust_tax_gelato"
                }
              ]
            },
            {
              "name": "Appetizers",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_appetizers",
              "subcategories": [
                {
                  "name": "Hispanic Appetizers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_appetizers&ATTRIBUTE_GROUP_ID=syy_cust_tax_hispanicappetizers"
                },
                {
                  "name": "Breaded and Battered Appetizers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_appetizers&ATTRIBUTE_GROUP_ID=syy_cust_tax_breadedandbatteredappetizer"
                },
                {
                  "name": "Hors D'oeuvres",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_appetizers&ATTRIBUTE_GROUP_ID=syy_cust_tax_horsd'oeuvres"
                },
                {
                  "name": "Asian Appetizers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_appetizers&ATTRIBUTE_GROUP_ID=syy_cust_tax_asianappetizers"
                }
              ]
            },
            {
              "name": "Frozen Entr\u00e9es and Sides",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenentreesandsides",
              "subcategories": [
                {
                  "name": "Prepared Entr\u00e9es and Sides",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenentreesandsides&ATTRIBUTE_GROUP_ID=syy_cust_tax_preparedentreesandsides"
                },
                {
                  "name": "Handheld Entr\u00e9es",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenentreesandsides&ATTRIBUTE_GROUP_ID=syy_cust_tax_handheldentrees"
                },
                {
                  "name": "Meal Kits",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenentreesandsides&ATTRIBUTE_GROUP_ID=syy_cust_tax_mealkits"
                }
              ]
            },
            {
              "name": "Frozen Fruit",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenfruit",
              "subcategories": [
                {
                  "name": "Fruit Purees",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_fruitpurees"
                },
                {
                  "name": "Berries",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_berries"
                },
                {
                  "name": "Apples",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_apples_L3_3"
                },
                {
                  "name": "Guacamole",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_guacamole"
                },
                {
                  "name": "Bananas and Tropical Fruit",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_bananasandtropicalfruit_L3"
                },
                {
                  "name": "Peaches and Plums",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_peachesandplums_L3_3"
                },
                {
                  "name": "Mixed Fruit",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_mixedfruit_L3_3"
                },
                {
                  "name": "Pears",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenfruit&ATTRIBUTE_GROUP_ID=syy_cust_tax_pears_L3_3"
                }
              ]
            },
            {
              "name": "Frozen Vegetables",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables",
              "subcategories": [
                {
                  "name": "Squash",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_squash"
                },
                {
                  "name": "Vegetable Mixes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_vegetablemixes"
                },
                {
                  "name": "Asparagus",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_asparagus"
                },
                {
                  "name": "Vegetable Purees",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_vegetablepurees"
                },
                {
                  "name": "Beans and Peas",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_beansandpeas_L3"
                },
                {
                  "name": "Root Vegetables",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_rootvegetables_L3"
                },
                {
                  "name": "Leafy Greens",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_leafygreens"
                },
                {
                  "name": "Broccoli",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_broccoli"
                },
                {
                  "name": "Baby Vegetables",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_babyvegetables"
                },
                {
                  "name": "Corn",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_corn_L3_3"
                },
                {
                  "name": "Peppers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_peppers_L3"
                },
                {
                  "name": "Onions and Garlic",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_onionsandgarlic_L3"
                },
                {
                  "name": "Mushrooms",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_mushrooms_L3_3"
                },
                {
                  "name": "Tomatoes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenvegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_tomatoes_L3_3"
                }
              ]
            },
            {
              "name": "Frozen Breakfast",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenbreakfast",
              "subcategories": [
                {
                  "name": "Pancakes, Waffles and French Toast",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenbreakfast&ATTRIBUTE_GROUP_ID=syy_cust_tax_pancakeswafflesandfrenchto"
                },
                {
                  "name": "Handheld Breakfast",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenbreakfast&ATTRIBUTE_GROUP_ID=syy_cust_tax_handheldbreakfast"
                },
                {
                  "name": "Blintzes and Crepes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenbreakfast&ATTRIBUTE_GROUP_ID=syy_cust_tax_blintzesandcrepes"
                },
                {
                  "name": "Breakfast Entr\u00e9es",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_frozenbreakfast&ATTRIBUTE_GROUP_ID=syy_cust_tax_breakfastentrees"
                }
              ]
            },
            {
              "name": "Pizza",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_pizza",
              "subcategories": [
                {
                  "name": "Pizza Crust and Dough",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_pizza&ATTRIBUTE_GROUP_ID=syy_cust_tax_pizzacrustanddough"
                },
                {
                  "name": "Pre-Topped Pizza",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_pizza&ATTRIBUTE_GROUP_ID=syy_cust_tax_pre-toppedpizza"
                }
              ]
            },
            {
              "name": "Pasta",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_pasta",
              "subcategories": []
            },
            {
              "name": "Specialty Potatoes",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_frozenfoods&ITEM_GROUP_ID=syy_cust_tax_specialtypotatoes",
              "subcategories": []
            }
          ]
        },
        {
          "id": 7,
          "name": "Beverages",
          "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages",
          "subcategories": [
            {
              "name": "Juice",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_juice",
              "subcategories": [
                {
                  "name": "Juice 100%",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_juice&ATTRIBUTE_GROUP_ID=syy_cust_tax_juice100%25"
                },
                {
                  "name": "Less than 100%",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_juice&ATTRIBUTE_GROUP_ID=syy_cust_tax_lessthan100%25"
                }
              ]
            },
            {
              "name": "Dispensed Beverages",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_dispensedbeverages",
              "subcategories": [
                {
                  "name": "Drink Base",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_dispensedbeverages&ATTRIBUTE_GROUP_ID=syy_cust_tax_drinkbase"
                },
                {
                  "name": "Syrup",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_dispensedbeverages&ATTRIBUTE_GROUP_ID=syy_cust_tax_syrup_L3_3"
                },
                {
                  "name": "Drink Mix",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_dispensedbeverages&ATTRIBUTE_GROUP_ID=syy_cust_tax_drinkmix"
                }
              ]
            },
            {
              "name": "Coffee",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_coffee",
              "subcategories": [
                {
                  "name": "Whole Bean",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_coffee&ATTRIBUTE_GROUP_ID=syy_cust_tax_wholebean"
                },
                {
                  "name": "Cappuccino",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_coffee&ATTRIBUTE_GROUP_ID=syy_cust_tax_cappuccino"
                },
                {
                  "name": "Ground Coffee",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_coffee&ATTRIBUTE_GROUP_ID=syy_cust_tax_groundcoffee"
                },
                {
                  "name": "Instant Coffee",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_coffee&ATTRIBUTE_GROUP_ID=syy_cust_tax_instantcoffee"
                },
                {
                  "name": "Concentrate Coffee",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_coffee&ATTRIBUTE_GROUP_ID=syy_cust_tax_concentratecoffee"
                },
                {
                  "name": "Ready to Drink",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_coffee&ATTRIBUTE_GROUP_ID=syy_cust_tax_readytodrink_L3"
                }
              ]
            },
            {
              "name": "Soft Drinks",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_softdrinks",
              "subcategories": []
            },
            {
              "name": "Water",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_water",
              "subcategories": [
                {
                  "name": "Purified",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_water&ATTRIBUTE_GROUP_ID=syy_cust_tax_purified"
                },
                {
                  "name": "Spring and Artesian",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_water&ATTRIBUTE_GROUP_ID=syy_cust_tax_springandartesian"
                },
                {
                  "name": "Distilled",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_water&ATTRIBUTE_GROUP_ID=syy_cust_tax_distilled"
                }
              ]
            },
            {
              "name": "Healthcare Beverages",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_healthcarebeverages",
              "subcategories": [
                {
                  "name": "Supplements",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_healthcarebeverages&ATTRIBUTE_GROUP_ID=syy_cust_tax_supplements"
                },
                {
                  "name": "Purees",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_healthcarebeverages&ATTRIBUTE_GROUP_ID=syy_cust_tax_purees"
                },
                {
                  "name": "Thickened Beverages",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_healthcarebeverages&ATTRIBUTE_GROUP_ID=syy_cust_tax_thickenedbeverages"
                }
              ]
            },
            {
              "name": "Tea",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_tea",
              "subcategories": [
                {
                  "name": "Hot Tea",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_tea&ATTRIBUTE_GROUP_ID=syy_cust_tax_hottea"
                },
                {
                  "name": "Iced Tea",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_tea&ATTRIBUTE_GROUP_ID=syy_cust_tax_icedtea"
                }
              ]
            },
            {
              "name": "Sports Drinks",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_sportsdrinks",
              "subcategories": []
            },
            {
              "name": "Cocktail Mixers and Syrup",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_cocktailmixersandsyrup",
              "subcategories": [
                {
                  "name": "Cocktail Mixes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_cocktailmixersandsyrup&ATTRIBUTE_GROUP_ID=syy_cust_tax_cocktailmixes"
                },
                {
                  "name": "Smoothies and Shakes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_cocktailmixersandsyrup&ATTRIBUTE_GROUP_ID=syy_cust_tax_smoothiesandshakes"
                },
                {
                  "name": "Powdered Drink Mixes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_cocktailmixersandsyrup&ATTRIBUTE_GROUP_ID=syy_cust_tax_powdereddrinkmixes"
                },
                {
                  "name": "Syrups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_cocktailmixersandsyrup&ATTRIBUTE_GROUP_ID=syy_cust_tax_syrups"
                }
              ]
            },
            {
              "name": "Beer and Wine",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_beerandwine",
              "subcategories": [
                {
                  "name": "Beer",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_beerandwine&ATTRIBUTE_GROUP_ID=syy_cust_tax_beer"
                },
                {
                  "name": "Wine",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_beerandwine&ATTRIBUTE_GROUP_ID=syy_cust_tax_wine"
                }
              ]
            },
            {
              "name": "Cocoa",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_cocoa",
              "subcategories": []
            },
            {
              "name": "Ready To Drink",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_readytodrink",
              "subcategories": [
                {
                  "name": "Iced Tea",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_beverages&ITEM_GROUP_ID=syy_cust_tax_readytodrink&ATTRIBUTE_GROUP_ID=syy_cust_tax_icedtea_L3"
                }
              ]
            }
          ]
        },
        {
          "id": 8,
          "name": "Equipment & Supplies",
          "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies",
          "subcategories": [
            {
              "name": "Register and POS",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_registerandpos",
              "subcategories": [
                {
                  "name": "Guest Checks",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_registerandpos&ATTRIBUTE_GROUP_ID=syy_cust_tax_guestchecks"
                },
                {
                  "name": "Register Rolls and Ribbons",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_registerandpos&ATTRIBUTE_GROUP_ID=syy_cust_tax_registerrollsandribbons"
                }
              ]
            },
            {
              "name": "Other Supplies",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_othersupplies",
              "subcategories": []
            },
            {
              "name": "Kitchen and Cutlery",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_kitchenandcutlery",
              "subcategories": [
                {
                  "name": "Kitchen Supplies",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_kitchenandcutlery&ATTRIBUTE_GROUP_ID=syy_cust_tax_kitchensupplies"
                },
                {
                  "name": "Cutlery",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_kitchenandcutlery&ATTRIBUTE_GROUP_ID=syy_cust_tax_cutlery"
                },
                {
                  "name": "Cooking Fuels",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_kitchenandcutlery&ATTRIBUTE_GROUP_ID=syy_cust_tax_cookingfuels"
                },
                {
                  "name": "Charcoal and Wood",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_kitchenandcutlery&ATTRIBUTE_GROUP_ID=syy_cust_tax_charcoalandwood"
                }
              ]
            },
            {
              "name": "Health and Personal Care",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_healthandpersonalcare",
              "subcategories": [
                {
                  "name": "Healthcare Supplies",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_healthandpersonalcare&ATTRIBUTE_GROUP_ID=syy_cust_tax_healthcaresupplies"
                },
                {
                  "name": "Hand and Body Care",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_healthandpersonalcare&ATTRIBUTE_GROUP_ID=syy_cust_tax_handandbodycare"
                },
                {
                  "name": "Healthcare Equipment",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_healthandpersonalcare&ATTRIBUTE_GROUP_ID=syy_cust_tax_healthcareequipment"
                }
              ]
            },
            {
              "name": "Tabletop Dining and Bar",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_tabletopdiningandbar",
              "subcategories": [
                {
                  "name": "Tableware",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_tabletopdiningandbar&ATTRIBUTE_GROUP_ID=syy_cust_tax_tableware"
                },
                {
                  "name": "Beverageware",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_tabletopdiningandbar&ATTRIBUTE_GROUP_ID=syy_cust_tax_beverageware"
                },
                {
                  "name": "Dining Room Supplies",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_tabletopdiningandbar&ATTRIBUTE_GROUP_ID=syy_cust_tax_diningroomsupplies"
                },
                {
                  "name": "Bar Supplies",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_tabletopdiningandbar&ATTRIBUTE_GROUP_ID=syy_cust_tax_barsupplies"
                },
                {
                  "name": "Ice Melt",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_tabletopdiningandbar&ATTRIBUTE_GROUP_ID=syy_cust_tax_icemelt"
                },
                {
                  "name": "Water Softener",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_tabletopdiningandbar&ATTRIBUTE_GROUP_ID=syy_cust_tax_watersoftener"
                }
              ]
            },
            {
              "name": "Restaurant Equipment",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_restaurantequipment",
              "subcategories": []
            },
            {
              "name": "Food Storage and Wraps",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_foodstorageandwraps",
              "subcategories": [
                {
                  "name": "Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_foodstorageandwraps&ATTRIBUTE_GROUP_ID=syy_cust_tax_containers"
                },
                {
                  "name": "Food Rotation and Safety Labels",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_foodstorageandwraps&ATTRIBUTE_GROUP_ID=syy_cust_tax_foodrotationandsafetylabels"
                },
                {
                  "name": "Pan Liners",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_foodstorageandwraps&ATTRIBUTE_GROUP_ID=syy_cust_tax_panliners_L3"
                }
              ]
            },
            {
              "name": "Furniture",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_furniture",
              "subcategories": [
                {
                  "name": "Fixtures",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_furniture&ATTRIBUTE_GROUP_ID=syy_cust_tax_fixtures"
                },
                {
                  "name": "Furniture",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_furniture&ATTRIBUTE_GROUP_ID=syy_cust_tax_furniture_L3"
                },
                {
                  "name": "Equipment",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_furniture&ATTRIBUTE_GROUP_ID=syy_cust_tax_equipment"
                }
              ]
            },
            {
              "name": "Janitorial and Cleaning",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_janitorialandcleaning",
              "subcategories": [
                {
                  "name": "Janitorial Sanitation",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_janitorialandcleaning&ATTRIBUTE_GROUP_ID=syy_cust_tax_janitorialsanitation"
                }
              ]
            },
            {
              "name": "Dispensers",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_dispensers",
              "subcategories": []
            },
            {
              "name": "Apparel and Uniforms",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_apparelanduniforms",
              "subcategories": []
            },
            {
              "name": "Catering",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_equipmentsupplies&ITEM_GROUP_ID=syy_cust_tax_catering_L2",
              "subcategories": []
            }
          ]
        },
        {
          "id": 9,
          "name": "Disposables",
          "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables",
          "subcategories": [
            {
              "name": "Beverage Cups",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups",
              "subcategories": [
                {
                  "name": "Paper Cups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups&ATTRIBUTE_GROUP_ID=syy_cust_tax_papercups"
                },
                {
                  "name": "Poly-lined Paper Cups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups&ATTRIBUTE_GROUP_ID=syy_cust_tax_poly-linedpapercups"
                },
                {
                  "name": "Coasters",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups&ATTRIBUTE_GROUP_ID=syy_cust_tax_coasters"
                },
                {
                  "name": "Foam Cups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups&ATTRIBUTE_GROUP_ID=syy_cust_tax_foamcups"
                },
                {
                  "name": "Beverage Carriers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups&ATTRIBUTE_GROUP_ID=syy_cust_tax_beveragecarriers"
                },
                {
                  "name": "Polypropylene Cups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups&ATTRIBUTE_GROUP_ID=syy_cust_tax_polypropylenecups"
                },
                {
                  "name": "PET Cups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups&ATTRIBUTE_GROUP_ID=syy_cust_tax_petcups"
                },
                {
                  "name": "RPET Cups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups&ATTRIBUTE_GROUP_ID=syy_cust_tax_rpetcups"
                },
                {
                  "name": "Molded Fiber Cups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups&ATTRIBUTE_GROUP_ID=syy_cust_tax_moldedfibercups"
                },
                {
                  "name": "HIPS Cups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups&ATTRIBUTE_GROUP_ID=syy_cust_tax_hipscups"
                },
                {
                  "name": "OPS Cups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups&ATTRIBUTE_GROUP_ID=syy_cust_tax_opscups"
                },
                {
                  "name": "PLA Cups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragecups&ATTRIBUTE_GROUP_ID=syy_cust_tax_placups"
                }
              ]
            },
            {
              "name": "Catering",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_catering",
              "subcategories": [
                {
                  "name": "Lids",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_catering&ATTRIBUTE_GROUP_ID=syy_cust_tax_lids"
                },
                {
                  "name": "Trays",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_catering&ATTRIBUTE_GROUP_ID=syy_cust_tax_trays"
                },
                {
                  "name": "Bowls",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_catering&ATTRIBUTE_GROUP_ID=syy_cust_tax_bowls"
                },
                {
                  "name": "Platters",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_catering&ATTRIBUTE_GROUP_ID=syy_cust_tax_platters"
                }
              ]
            },
            {
              "name": "Plates, Bowls and Lids",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_platesbowlsandlids",
              "subcategories": []
            },
            {
              "name": "To-go Containers",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers",
              "subcategories": [
                {
                  "name": "Polystyrene Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers&ATTRIBUTE_GROUP_ID=syy_cust_tax_polystyrenecontainers"
                },
                {
                  "name": "Laminated Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers&ATTRIBUTE_GROUP_ID=syy_cust_tax_laminatedcontainers"
                },
                {
                  "name": "Unlaminated Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers&ATTRIBUTE_GROUP_ID=syy_cust_tax_unlaminatedcontainers"
                },
                {
                  "name": "Paper Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers&ATTRIBUTE_GROUP_ID=syy_cust_tax_papercontainers"
                },
                {
                  "name": "Polypropylene Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers&ATTRIBUTE_GROUP_ID=syy_cust_tax_polypropylenecontainers"
                },
                {
                  "name": "Aluminum Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers&ATTRIBUTE_GROUP_ID=syy_cust_tax_aluminumcontainers"
                },
                {
                  "name": "Polyethylene Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers&ATTRIBUTE_GROUP_ID=syy_cust_tax_polyethylenecontainers"
                },
                {
                  "name": "Molded Fiber Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers&ATTRIBUTE_GROUP_ID=syy_cust_tax_moldedfibercontainers"
                },
                {
                  "name": "Bagasse Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers&ATTRIBUTE_GROUP_ID=syy_cust_tax_bagassecontainers"
                },
                {
                  "name": "High Impact Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers&ATTRIBUTE_GROUP_ID=syy_cust_tax_highimpactcontainers"
                },
                {
                  "name": "Palm Leaf Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers&ATTRIBUTE_GROUP_ID=syy_cust_tax_palmleafcontainers"
                },
                {
                  "name": "PLA Containers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_to-gocontainers&ATTRIBUTE_GROUP_ID=syy_cust_tax_placontainers"
                }
              ]
            },
            {
              "name": "Apparel",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_apparel",
              "subcategories": [
                {
                  "name": "Aprons",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_apparel&ATTRIBUTE_GROUP_ID=syy_cust_tax_aprons"
                },
                {
                  "name": "Hats and Caps",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_apparel&ATTRIBUTE_GROUP_ID=syy_cust_tax_hatsandcaps"
                },
                {
                  "name": "Gloves",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_apparel&ATTRIBUTE_GROUP_ID=syy_cust_tax_gloves"
                },
                {
                  "name": "Undergarments",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_apparel&ATTRIBUTE_GROUP_ID=syy_cust_tax_undergarments"
                },
                {
                  "name": "Feminine Hygiene",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_apparel&ATTRIBUTE_GROUP_ID=syy_cust_tax_femininehygiene"
                },
                {
                  "name": "Shoe Covers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_apparel&ATTRIBUTE_GROUP_ID=syy_cust_tax_shoecovers"
                },
                {
                  "name": "Masks",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_apparel&ATTRIBUTE_GROUP_ID=syy_cust_tax_masks"
                },
                {
                  "name": "Arm Guards",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_apparel&ATTRIBUTE_GROUP_ID=syy_cust_tax_armguards"
                },
                {
                  "name": "Coats",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_apparel&ATTRIBUTE_GROUP_ID=syy_cust_tax_coats"
                }
              ]
            },
            {
              "name": "Liners and Storage Bags",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_linersandstoragebags",
              "subcategories": [
                {
                  "name": "Storage Bags",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_linersandstoragebags&ATTRIBUTE_GROUP_ID=syy_cust_tax_storagebags"
                },
                {
                  "name": "Molds and Cups",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_linersandstoragebags&ATTRIBUTE_GROUP_ID=syy_cust_tax_moldsandcups"
                },
                {
                  "name": "Liners and Tissue",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_linersandstoragebags&ATTRIBUTE_GROUP_ID=syy_cust_tax_linersandtissue"
                },
                {
                  "name": "Pan Liners",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_linersandstoragebags&ATTRIBUTE_GROUP_ID=syy_cust_tax_panliners"
                }
              ]
            },
            {
              "name": "Containers and Lids",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_containersandlids",
              "subcategories": [
                {
                  "name": "Boxes and Cartons",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_containersandlids&ATTRIBUTE_GROUP_ID=syy_cust_tax_boxesandcartons"
                },
                {
                  "name": "Food Pans and Lids",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_containersandlids&ATTRIBUTE_GROUP_ID=syy_cust_tax_foodpansandlids"
                },
                {
                  "name": "Soufflee Cups and Lids",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_containersandlids&ATTRIBUTE_GROUP_ID=syy_cust_tax_souffleecupsandlids"
                },
                {
                  "name": "Beverage Dispensers and Jugs",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_containersandlids&ATTRIBUTE_GROUP_ID=syy_cust_tax_beveragedispensersandjugs"
                }
              ]
            },
            {
              "name": "Food Wraps",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_foodwraps",
              "subcategories": [
                {
                  "name": "Paper",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_foodwraps&ATTRIBUTE_GROUP_ID=syy_cust_tax_paper"
                },
                {
                  "name": "Cloth and Wraps",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_foodwraps&ATTRIBUTE_GROUP_ID=syy_cust_tax_clothandwraps"
                },
                {
                  "name": "Plastic and Film",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_foodwraps&ATTRIBUTE_GROUP_ID=syy_cust_tax_plasticandfilm"
                },
                {
                  "name": "Foil",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_foodwraps&ATTRIBUTE_GROUP_ID=syy_cust_tax_foil"
                }
              ]
            },
            {
              "name": "Pads and Filters",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_padsandfilters",
              "subcategories": [
                {
                  "name": "Dispensers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_padsandfilters&ATTRIBUTE_GROUP_ID=syy_cust_tax_dispensers_L3"
                }
              ]
            },
            {
              "name": "Placemats",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_placemats",
              "subcategories": [
                {
                  "name": "Skewers and Picks",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_placemats&ATTRIBUTE_GROUP_ID=syy_cust_tax_skewersandpicks"
                }
              ]
            },
            {
              "name": "Towels, Tissue, Napkins, Wipers and Wipes",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_towelstissuenapkinswiper",
              "subcategories": [
                {
                  "name": "Napkins",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_towelstissuenapkinswiper&ATTRIBUTE_GROUP_ID=syy_cust_tax_napkins"
                },
                {
                  "name": "Disposable Wipes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_towelstissuenapkinswiper&ATTRIBUTE_GROUP_ID=syy_cust_tax_disposablewipes"
                },
                {
                  "name": "Paper Towels",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_towelstissuenapkinswiper&ATTRIBUTE_GROUP_ID=syy_cust_tax_papertowels"
                },
                {
                  "name": "Toilet Paper",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_towelstissuenapkinswiper&ATTRIBUTE_GROUP_ID=syy_cust_tax_toiletpaper"
                },
                {
                  "name": "Sanitary Covers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_towelstissuenapkinswiper&ATTRIBUTE_GROUP_ID=syy_cust_tax_sanitarycovers"
                },
                {
                  "name": "Tissues",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_towelstissuenapkinswiper&ATTRIBUTE_GROUP_ID=syy_cust_tax_tissues"
                }
              ]
            },
            {
              "name": "Beverage Lids",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragelids",
              "subcategories": [
                {
                  "name": "Straws",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragelids&ATTRIBUTE_GROUP_ID=syy_cust_tax_straws"
                },
                {
                  "name": "Foam Lids",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragelids&ATTRIBUTE_GROUP_ID=syy_cust_tax_foamlids"
                },
                {
                  "name": "Paper Lids",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragelids&ATTRIBUTE_GROUP_ID=syy_cust_tax_paperlids"
                },
                {
                  "name": "Polypropylene Lids",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragelids&ATTRIBUTE_GROUP_ID=syy_cust_tax_polypropylenelids"
                },
                {
                  "name": "RPET Lids",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragelids&ATTRIBUTE_GROUP_ID=syy_cust_tax_rpetlids"
                },
                {
                  "name": "PET Lids",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragelids&ATTRIBUTE_GROUP_ID=syy_cust_tax_petlids"
                },
                {
                  "name": "PLA Lids",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_beveragelids&ATTRIBUTE_GROUP_ID=syy_cust_tax_plalids"
                }
              ]
            },
            {
              "name": "Carryout Bags",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_carryoutbags",
              "subcategories": [
                {
                  "name": "Merchandise Bags",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_carryoutbags&ATTRIBUTE_GROUP_ID=syy_cust_tax_merchandisebags"
                },
                {
                  "name": "Grocery Bags",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_carryoutbags&ATTRIBUTE_GROUP_ID=syy_cust_tax_grocerybags"
                },
                {
                  "name": "Shopping Bags",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_carryoutbags&ATTRIBUTE_GROUP_ID=syy_cust_tax_shoppingbags"
                },
                {
                  "name": "T-shirt Bags",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_carryoutbags&ATTRIBUTE_GROUP_ID=syy_cust_tax_t-shirtbags"
                },
                {
                  "name": "Liquor Bags",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_carryoutbags&ATTRIBUTE_GROUP_ID=syy_cust_tax_liquorbags"
                }
              ]
            },
            {
              "name": "Platters and Lids",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_plattersandlids",
              "subcategories": []
            },
            {
              "name": "Trash Can Bags and Liners",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_trashcanbagsandliners",
              "subcategories": []
            },
            {
              "name": "Cutlery",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_cutlery_L2",
              "subcategories": [
                {
                  "name": "Cutlery",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_cutlery_L2&ATTRIBUTE_GROUP_ID=syy_cust_tax_cutlery_L3"
                },
                {
                  "name": "Serving Utensils",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_cutlery_L2&ATTRIBUTE_GROUP_ID=syy_cust_tax_servingutensils"
                },
                {
                  "name": "Skewers and Picks",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_cutlery_L2&ATTRIBUTE_GROUP_ID=syy_cust_tax_skewersandpicks_L3"
                },
                {
                  "name": "Non-pouch Kits",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_cutlery_L2&ATTRIBUTE_GROUP_ID=syy_cust_tax_non-pouchkits"
                },
                {
                  "name": "Junior Kits",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_cutlery_L2&ATTRIBUTE_GROUP_ID=syy_cust_tax_juniorkits"
                },
                {
                  "name": "Pouch kits",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_cutlery_L2&ATTRIBUTE_GROUP_ID=syy_cust_tax_pouchkits"
                }
              ]
            },
            {
              "name": "Pizza Boxes",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_pizzaboxes",
              "subcategories": []
            },
            {
              "name": "Placemats, Table Covers and Trays",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_placematstablecoversandtra",
              "subcategories": []
            },
            {
              "name": "Coffee and Tea Filters",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_disposables&ITEM_GROUP_ID=syy_cust_tax_coffeeandteafilters",
              "subcategories": []
            }
          ]
        },
        {
          "id": 10,
          "name": "Chemicals",
          "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals",
          "subcategories": [
            {
              "name": "Specialty Chemicals",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_specialtychemicals",
              "subcategories": [
                {
                  "name": "Polishes",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_specialtychemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_polishes"
                },
                {
                  "name": "Odor Control",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_specialtychemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_odorcontrol"
                },
                {
                  "name": "Absorbants",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_specialtychemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_absorbants"
                },
                {
                  "name": "Lubricants",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_specialtychemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_lubricants"
                },
                {
                  "name": "Dumpster and Waste Cleaners",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_specialtychemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_dumpsterandwastecleaners"
                },
                {
                  "name": "Pest Control",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_specialtychemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_pestcontrol"
                },
                {
                  "name": "Test Strips and Systems",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_specialtychemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_teststripsandsystems"
                },
                {
                  "name": "Automotive",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_specialtychemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_automotive"
                },
                {
                  "name": "Concrete",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_specialtychemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_concrete"
                }
              ]
            },
            {
              "name": "Cleaning Chemicals",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_cleaningchemicals",
              "subcategories": [
                {
                  "name": "Drain and Restroom Cleaners",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_cleaningchemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_drainandrestroomcleaners"
                },
                {
                  "name": "Glass and Multisurface Cleaners",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_cleaningchemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_glassandmultisurfacecleaner"
                },
                {
                  "name": "Floor Care",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_cleaningchemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_floorcare"
                },
                {
                  "name": "Degreasers",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_cleaningchemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_degreasers"
                },
                {
                  "name": "Freezer and Beverage Equipment Cleaners",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_cleaningchemicals&ATTRIBUTE_GROUP_ID=syy_cust_tax_freezerandbeverageequipment"
                }
              ]
            },
            {
              "name": "Warewash",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_warewash",
              "subcategories": [
                {
                  "name": "Detergent",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_warewash&ATTRIBUTE_GROUP_ID=syy_cust_tax_detergent"
                },
                {
                  "name": "Rinse Aid and Other Warewash",
                  "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_warewash&ATTRIBUTE_GROUP_ID=syy_cust_tax_rinseaidandotherwarewash"
                }
              ]
            },
            {
              "name": "Laundry Detergent",
              "url": "https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_chemicals&ITEM_GROUP_ID=syy_cust_tax_laundrydetergent",
              "subcategories": []
            }
          ]
        }
      
    ]
  }
}
                    
		''')

	SEARCH_API_OPERATION = 'ConsumerCanonicalProductsByCategoriesQuery'
	PRODUCT_NUTRITION_API_OPERATION = 'getProducts_nutrition_SHOP_WEB'
	PRODUCT_API_OPERATION = 'getProducts_details_unifiedBFF_SHOP_WEB'
	# PRODUCT_API_OPERATION_2 = 'GetPersonalizedPageModules'
	GRAPHQL_API_FILTER = 'gateway-api.shop.sysco.com/graphql'
	JSON_GET_PRODUCTS = 'GetProducts'
	JSON_CANONICAL_PRODUCTS = 'getProducts'
	JSON_SEARCH_PRODUCTS = 'SearchProducts'
	PAGE_SIZE = 24

	def __init__(self, options=None):
		super().__init__(headless=False)
		# There are only 2 navigation categories we want to process and we only want to process 1 sub category
		self.options['test_categories'] = 100
		self.options['attempts'] = 40
		self.PRODUCT_DATA_SPEC = self.BASE_PRODUCT_DATA_SPEC.copy()
		for spec in self.DISTRIBUTOR_PRODUCT_DATA_SPEC:
			self.PRODUCT_DATA_SPEC[spec] = ''
		print(self.PRODUCT_DATA_SPEC)

	def set_zip(self, url):
		print("set_zip()")
		try:
			self.driver.get(url)
			time.sleep(20)
			# dropdown = self.wait.until(
			# 	EC.presence_of_element_located((By.CSS_SELECTOR, '.zipcode-container'))
			# )
			# dropdown.click()
			modal = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '.initial-zipcode-modal'))
			)
			print("found modal")
			field = modal.find_element(By.CSS_SELECTOR, '[data-id="initial_zipcode_modal_input"]')
			button = modal.find_element(By.CSS_SELECTOR, '[data-id="initial_zipcode_modal_start_shopping_button"]')
			field.send_keys("60016")
			button.click()
			print("Bypassed set_zip")
		except Exception as e:
			print(f"Error: {e}")

	def scraping_setup(self):
		"""Scrape products from the website"""
		print("scraping_setup()")
		url = self.BASE_URL
		self.set_zip(url)
		time.sleep(10)
		return

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

	# ************************************************************************
	# Utility Functions
	# ************************************************************************

	def build_product_url(self, product_id=None, seller_id=None):
		"""
		Builds the catalog URL with the specified parameters.

		Args:
			product_id (str, optional): The ID of the category to filter by
			seller_id (str, optional): The vendor ID. Defaults to 247696227.

		Returns:
			str: The complete catalog URL with all parameters
		"""
		# https://shop.sysco.com/app/product-details/opco/024/product/5926282?seller_id=USBL

		# URL encode the vendor name and other string parameters
		print(f"Product ID : {product_id}")

		base_url = f"https://shop.sysco.com/app/product-details/opco/024/product/{product_id}?seller_id={seller_id}"
		return f"{base_url}"

	@staticmethod
	def extract_unique_id_from_url(url):
		"""
		Get a unique identifier from the url.
		Standard version example https://website.com/4345353
		"""
		try:
			# Split the URL by 'product/' and get the part after it, then split by any query parameters or slashes
			return url.split('product/')[-1].split('?')[0].split('/')[0]
		except Exception as e:
			print(f"⛔️⛔️⛔️Error extracting product ID from URL: {e}")
			return ''
		return sku

	# ************************************************************************
	# 	Product Scraping Functions
	# ************************************************************************

	def get_product_data(self, data, row_spec):
		print("processing product data from response...")
		print(data)
		if data:
			try:
				# row_spec['sku'] = ''

				row_spec = self.get_product_detail_from_json(row_spec)
			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing get_product_data Complete...")
		return row_spec
	
	def get_product_detail_from_json(self, row_spec=None):
		print("processing product extra data from response...")
		# Navigate to the desired fields in the JSON structure
		try:
			json_data = json.loads(row_spec.get('extra_data_1', {}))
			get_products = json_data.get('data', {}).get('getProducts', [])[0]
			row_spec["product_id"] = get_products.get("productId", "")
			row_spec["sellerId"] = get_products.get("sellerId", "")

			pack_size_data = get_products.get('productInfo', {}).get('packSize', {})
			pack = pack_size_data.get('pack', None)
			size = pack_size_data.get('size', None)

			# Update the column with a formatted string or any logic based on 'pack' and 'size'
			row_spec['pack'] = pack
			row_spec['size'] = size

			name = get_products.get('productInfo', {}).get('name', {})
			# Update the column
			row_spec['name'] = name

			description = get_products.get('productInfo', {}).get('lineDescription', {})
			# Update the column
			row_spec['description'] = description

			is_catch_weight = get_products.get('productInfo', {}).get('isCatchWeight', {})
			# Update the column
			row_spec['is_catch_weight'] = is_catch_weight

			gtin = get_products.get('productInfo', {}).get('gtin', {})
			# Update the column
			row_spec['gtin'] = gtin

			man_upc = get_products.get('productInfo', {}).get('manufacturerUPC', {})
			# Update the column
			row_spec['manufacturerUPC'] = man_upc

			is_broken_case_data = get_products.get('productInfo', {}).get('isSoldAs', {})
			is_broken_case = is_broken_case_data.get('split', None)
			row_spec['is_broken_case'] = is_broken_case

			image = get_products.get('productInfo', {}).get('images', [])[0]
			row_spec['image'] = image
		except Exception as e:
			print(f"⛔️⛔️⛔️Error parsing json: {e}")

		print("processing get_more_extra_data Complete...")
		return row_spec

	def get_price(self, data, row_spec):
		print("get_price")
		try:
			if not isinstance(data, dict):
				data = json.loads(data)

			# Extract price from the nested structure
			price = data.get('offers', {}).get('priceSpecification', [{}])[0].get('price')

			if price is not None:
				row_spec["retail_price"] = str(price)
				print(f"Found price: ${price}")
			else:
				print("No price found in the data")

		except json.JSONDecodeError:
			print("Error: Invalid JSON data")
		except Exception as e:
			print(f"Error getting price: {str(e)}")

		return row_spec

	# ************************************************************************
	# 	Core
	# ************************************************************************

	# Step One:
	def build_categories_list(self):
		"""Build a list of categories from the main navigation menu."""
		try:
			self.scraping_setup()
			# Navigate to the base URL
			self.driver.get(self.BASE_URL)

			# Wait for the navigation menu to load
			request = self.driver.wait_for_request(self.GRAPHQL_API_FILTER)
			id = 0
			all_categories = {
				'data': {
					'categories': []
				}
			}
			for request in self.driver.requests:

				if request.response and self.GRAPHQL_API_FILTER in request.url:  # Filter for API requests
					current_data = request.body.decode('utf-8')
					payload = json.loads(current_data)
					print(f"Payload Method: {payload.get('operationName', '')}")
					if payload.get('operationName', '') == 'GetTaxonomyHierarchy':

						try:
							body = decode(request.response.body,
							              request.response.headers.get('Content-Encoding', 'identity'))

							# If the body is JSON, parse it
							if 'application/json' in request.response.headers.get('Content-Type', ''):
								data = json.loads(body)
							else:
								print(f"Response Body (Text): {body}")

						except Exception as e:
							print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

			# Find all top-level categories (each is in a separate ul)
			# https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce
			# https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables
			# https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_mushrooms
			categories = []
			if data:
				for business_center in data["data"]["getTaxonomyHierarchy"]:
					id += 1
					category_id = business_center["businessCenterId"]
					category_name = business_center["businessCenterLabel"]
					category_url = f"https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID={category_id}"

					subcategories = []

					for item_group in business_center.get("itemGroups", []):
						subcategory_id = item_group["itemGroupId"]
						subcategory_name = item_group["itemGroupLabel"]
						subcategory_url = f"{category_url}&ITEM_GROUP_ID={subcategory_id}"

						attributes = []

						for attr_group in item_group.get("attributeGroups", []):
							attr_id = attr_group["attributeGroupId"]
							attr_name = attr_group["attributeGroupLabel"]
							attr_url = f"{subcategory_url}&ATTRIBUTE_GROUP_ID={attr_id}"

							attributes.append({
								'name': attr_name,
								'url': attr_url
							})

						subcategories.append({
							'name': subcategory_name,
							'url': subcategory_url,
							'subcategories': attributes
						})

					categories.append({
						'id': id,
						'name': category_name,
						'url': category_url,
						'subcategories': subcategories
					})

				all_categories['data']['categories'].append(categories)

				return json.dumps(all_categories, indent=2)

		except Exception as e:
			print(f"Error building categories list: {str(e)}")
			return []
		
	def process(self, url):
		print( f"process()")
		product_urls = set()
		try:
			print(f"Visiting: {url}")
			self.driver.get(url)

			# Find script tags that might contain the JSON data
			script_elements = self.driver.find_elements(By.TAG_NAME, 'script')

			for script in script_elements:
				script_type = script.get_attribute('type')
				if script_type in ['application/json', 'application/ld+json'] or not script_type:
					try:
						script_content = script.get_attribute('innerHTML').replace("<!--", "").replace("-->", "")
						if script_content and script_content.strip().startswith(
								'{') and script_content.strip().endswith('}'):

							try:
								json_data = json.loads(script_content)
								# Process the children array if it exists
								if 'children' in json_data and isinstance(json_data['children'], list):
									for child in json_data['children']:
										if 'link' in child:
											full_url = self.BASE_URL + child['link'] if child['link'].startswith(
												'/') else child['link']
											product_urls.add(full_url)
											# print(f"Found product URL: {full_url}")

							except json.JSONDecodeError:
								continue
					except Exception as e:
						print(f"Error processing script: {str(e)}")
						continue

		except Exception as e:
			print(f"Error processing URL {url}: {str(e)}")
		print(product_urls)
		return product_urls

	# Step Two: Get links to products
	def build_products_list(self):
		"""Scrape products from the website"""
		# https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_mushrooms
		# https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_mushrooms
		# https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_mushrooms
		# https://shop.sysco.com/app/catalog?BUSINESS_CENTER_ID=syy_cust_tax_produce&ITEM_GROUP_ID=syy_cust_tax_vegetables&ATTRIBUTE_GROUP_ID=syy_cust_tax_mushrooms
		self.scraping_setup()

		category = self.wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, '.category-grid-image'))
			)
		category.click()
		html = ""
		all_urls = []
		# Use the options with fallback to module-level variables
		max_products = self.options.get('max_products', self.MAX_API_PRODUCTS)
		category_to_process = self.options.get('category_to_process', 0)
		chosen_category = int(self.options.get('chosen_category', 0))
		test_categories = self.options.get('test_categories', 100)
		category_count = 0
		if int(self.options['chosen_category']) == 0:
			categories = self.CATEGORIES.get('data', {}).get('categories', {})
			print(f"All Categories ")
		else:
			for category in self.CATEGORIES.get('data', {}).get('categories', {}):
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
			print(category)
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
							detail_urls, html = self.get_category_page(url, category_name, sub_category_name,
							                                           sub_sub_category_name)
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

	def get_product_details(self, url, row_spec=None):
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print("processing product detail page")
		print(f"Loading page...{url}")

		data = ''
		# We used an id to identify the product
		row_spec['id'] = row_spec['sku']
		del self.driver.requests
		print(row_spec)
		self.driver.get(url)
		print(f"Sent Request")
		try:
			request = self.driver.wait_for_request(self.GRAPHQL_API_FILTER)
			first_found = False
			second_found = False
			attempts = 0

			while (not first_found and not second_found) and attempts < self.options['attempts']:
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
								body = decode(request.response.body,
								              request.response.headers.get('Content-Encoding', 'identity'))

								# If the body is JSON, parse it
								if 'application/json' in request.response.headers.get('Content-Type', ''):
									data = json.loads(body)
									row_spec["extra_data_1"] = json.dumps(data)
								else:
									print(f"Response Body (Text): {body}")
							except Exception as e:
								print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

						if payload.get('operationName', '') == self.PRODUCT_NUTRITION_API_OPERATION and not second_found:
							second_found = True
							try:
								body = decode(request.response.body,
								              request.response.headers.get('Content-Encoding', 'identity'))

								# If the body is JSON, parse it
								if 'application/json' in request.response.headers.get('Content-Type', ''):
									nutrition_data = json.loads(body)
									row_spec["extra_data_2"] = json.dumps(nutrition_data)
								else:
									print(f"Response Body (Text): {body}")

							except Exception as e:
								print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

			if not first_found:
				raise ProductNotFound

			# These use the data if available, then try to scrape from the page
			row_spec = self.get_product_data(data, row_spec)

		except Exception as e:
			print(f"⛔️⛔️⛔️Error waiting for request: {e}")

		return row_spec

	def get_product_data_2(self, row_spec):
		print("processing product data 2 from response...")
		data = {}
		try:
			extra_data_2 = row_spec.get('extra_data_2', {})
			if extra_data_2:
				data = json.loads(extra_data_2)
		except json.JSONDecodeError as e:
			print(f"Error parsing JSON in extra_data_2 for SKU: {e}")
			print(extra_data_2)
			# Write the original row if there's an error
		except Exception as e:
			print(f"Error processing row with SKU : {e}")
		# print(data)
		if data:
			try:
				# row_spec["extra_data_1"] = json.dumps(data)
				data = data.get('data',{}).get('canonicalProduct',{})

				row_spec["sku"] = data.get("itemCode", "")
				# row_spec["name"] = data.get("nameWithoutBrand", "")
				try:
					row_spec["brand"] = data.get("productbrand", {}).get("displayName", "")
				except:
					print(f" ⚠️No Brand info found")

				row_spec["distributor_name"] = self.VENDOR_NAME

				row_spec["size"] = data.get('size', '')
				row_spec["pack"] = data.get('pack', '')
				row_spec["gtin"] = data.get('gtin', '')

				row_spec = self.get_first_image_url_2(data, row_spec)
				# row_spec = self.get_classification(data, row_spec)
				row_spec["description"] = data.get("description", "")
				row_spec = self.get_manufacturer_2(data, row_spec)
				# row_spec = self.get_additional_info(data, row_spec)
				# row_spec["extra_data_1"] = json.dumps(data)

			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing get_product_data Complete...")
		return row_spec

	def get_product_detail_from_json_in_html(self, url, row_spec=None, target="script[type='application/json']"):
		#  Wait for the product name element on the product page detail page
		print("Webstaurant.get_product_detail_from_json_in_html()")
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print(f"processing product detail page for target {target}")
		print(f"Loading page...{url}")

		data = ''
		sku = row_spec['sku']
		request_filter = url

		self.driver.get(url)
		print(f"Sent Request")
		script_data = ''
		product_data = ''
		product_data_2 = ''
		try:
			# Wait for the page to load
			WebDriverWait(self.driver, 20).until(
				EC.presence_of_element_located(
				(By.CSS_SELECTOR, target))
			)
			print(f"Script Loaded")
			# Get the page source and parse it with BeautifulSoup
			soup = BeautifulSoup(self.driver.page_source, 'html.parser')

			scripts = soup.find_all('script', {'type': 'application/ld+json'})
			for script in scripts:
				print(script.string)
				if script and script.string:
					print("Loading product data")
					try:
						# Parse the JSON data from the script tag
						script_data = json.loads(script.string.replace("<!--", "").replace("-->", ""))
						try:
							if script_data.get('@type') == "Product":
								print("Found Product")
								product_data = script_data
							if script_data.get('@type') == "ProductGroup":
								print("Found Group")
								product_data_2 = script_data
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

		return product_data, product_data_2

	def get_product_detail_2_from_json_in_html(self, url, row_spec=None, target="script[data-hypernova-key='ProductDetails']"):
		"""
		Extract JSON data from a script tag with the specified ID.

		Args:
			url (str): The URL to load
			row_spec (dict, optional): Product data specification. Defaults to None.
			target (str, optional): CSS selector for the script tag. Defaults to "script[type='application/json']".

		Returns:
			dict: Parsed JSON data from the script tag
		"""
		print(f"Webstaruant.get_product_detail_2_from_json_in_html() - Target: {target}")

		product_data = {}
		try:
			# Wait for the target script tag to be present
			script_element = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, target))
			)
			# Get the inner HTML of the script tag
			script_content = script_element.get_attribute('innerHTML').replace("<!--", "").replace("-->", "")

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

		except Exception as e:
			print(f"Error extracting data from script tag: {e}")
		finally:
			# Clean up any pending requests
			if hasattr(self, 'driver') and hasattr(self.driver, 'requests'):
				del self.driver.requests
		# Force a wait before the next one is called
		time.sleep(1)
		return product_data
	# ************************************************************************
	# Product List Extraction Functions
	# ************************************************************************
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
			subcat_name = subcat['name']
			url = subcat['url']
			print(f"Loading page...{url}")
			del self.driver.request_interceptor
			# self.driver.request_interceptor = self.create_interceptor(self.options['max_products'], page=page)
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

									if self.JSON_CANONICAL_PRODUCTS in data.get('data', {}).get(self.JSON_CANONICAL_PRODUCTS, {}):
										print(f"Response products: TRUE")
										detail_urls = [
											self.build_product_url(product.get('id', ''))
											for product in data.get('data', {}).get(self.JSON_CANONICAL_PRODUCTS, [])]
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

	def get_category_page(self, base_url, category_name, sub_category_name, sub_sub_category_name):
		still_looking = True
		html = ''
		page = 0
		all_urls = []
		url = base_url
		test_products = self.options.get('test_products', 0)
		print(f"wait_and_process_products()")
		while still_looking and page < self.options['max_products']:
			page = page + 1
			if page * self.options['max_products'] > test_products:
				# We have reached the maximum number of products we
				break

			self.options['url_output_file'] = self.make_filename_safe(category_name.lower()) + "_product_urls.csv"
			# subcat_name = subcat['name']
			print(f"Loading page...{url}")
			del self.driver.request_interceptor
			# self.driver.request_interceptor = self.create_interceptor(self.options['max_products'], page=page)
			del self.driver.requests
			if page > 1:
				url = base_url + f"&page={page}"
			self.driver.get(url)
			print(f"URL Loaded")
			print(f"Page : {page}")

			attempts = 0

			print("Processing Requests")
			while attempts < self.options['attempts']:
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
						if payload.get('operationName', '') == self.JSON_SEARCH_PRODUCTS:
							print(f"{self.JSON_SEARCH_PRODUCTS} found")
							print(f"URL: {request.url}")
							print(f"Status Code: {request.response.status_code}")
							print(f"Content Type: {request.response.headers.get('Content-Type')}")
							try:
								body = decode(request.response.body,
								              request.response.headers.get('Content-Encoding', 'identity'))

								# If the body is JSON, parse it
								if 'application/json' in request.response.headers.get('Content-Type', ''):
									data = json.loads(body)

									if 'searchProducts' in data.get('data', {}):
										print(f"Response products: TRUE")
										detail_urls = [
											self.build_product_url(product.get('productId', ''), product.get('sellerId', ''))
											for product in data.get('data', {}).get('searchProducts', []).get('results', [])]
										print(f"== Number of products: {len(detail_urls)}")
										all_urls.extend(detail_urls)
										html += f"<h2>{category_name} -> {sub_category_name} -> page {page}</h2>"
										html += "<div>Products found: " + str(len(detail_urls)) + "</div>"
										if len(detail_urls) != 0:
											self.save_urls_to_csv(detail_urls, category_name, sub_category_name, sub_sub_category_name)
										print(f"=== Number of products: {len(detail_urls)}")
										attempts = self.options['attempts']
										if len(detail_urls) == 0 or len(detail_urls) % self.PAGE_SIZE != 0:
											still_looking = False
										break
									else:
										print(
											f"Response canonical products ({self.JSON_CANONICAL_PRODUCTS}) missing: {self.JSON_CANONICAL_PRODUCTS in data} ")
								# print(f"data: {data} ")

								else:
									print(f"Response Body (Text): ")
									print(f"Response not JSON  ")

							except Exception as e:
								print(f"⛔️⛔️⛔️Error decoding detail response body: {e}")

			# del self.driver.request_interceptor
			del self.driver.requests
		print(f"get_category_page() complete for {category_name}")
		return all_urls, html

	def get_products_from_json_in_html(self):
		print("get_products_from_json_in_html")
		target = "script[data-hypernova-key='LeafCategoryPage']"
		detail_urls = []

		try:
			# Wait for the target script tag to be present
			script_element = WebDriverWait(self.driver, 20).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, target))
			)
			print(f"Found script element")
			# Get the inner HTML of the script tag
			script_content = script_element.get_attribute('innerHTML').replace("<!--", "").replace("-->", "")

			if script_content:
				try:
					# Parse the JSON data
					json_data = json.loads(script_content)
					print("Successfully extracted and parsed JSON data")

					# Extract product links from the products array
					if 'products' in json_data and isinstance(json_data['products'], list):
						for product in json_data['products']:
							if 'link' in product:
								full_url = f"{self.BASE_URL}{product['link']}" if not product['link'].startswith(
									'http') else product['link']
								detail_urls.append(full_url)
								# print(f"Found product URL: {full_url}")

				except json.JSONDecodeError as e:
					print(f"Error parsing JSON data: {e}")
			else:
				print(f"No content found in script tag matching: {target}")

		except Exception as e:
			print(f"Error extracting data from script tag: {e}")
		finally:
			# Clean up any pending requests
			if hasattr(self, 'driver') and hasattr(self.driver, 'requests'):
				del self.driver.requests

		# print(f"Found {len(detail_urls)} product URLs")
		time.sleep(1)
		return '', detail_urls
