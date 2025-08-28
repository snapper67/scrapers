import json
import os
import time

from bs4 import BeautifulSoup
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumwire import webdriver as seleniumwire_webdriver
from seleniumwire.utils import decode

from urllib.parse import urlparse, parse_qs, urlunparse
from io import StringIO
import csv
import os
from collections import OrderedDict
import sys
import glob
import pandas as pd


from ..scraper import Scraper


class ApplicationScraper(Scraper):
    """Scraper for What Chefs Want - South on the Cut & Dry platform"""

    DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/application'

    # Values to change
    BASE_URL = "http://restau-appli-g3wto8bmm2jw-1917384324.us-east-1.elb.amazonaws.com/"

    # These values are pulled from the base URL
    SUB_DOMAIN = "https://whatchefswant.cutanddry.com"
    VENDOR_URL_NAME = 'What%20Chefs%20Want%20-%20Central'
    VERIFIED_VENDOR_ID = 341183528

    # This the name of the vendor
    VENDOR_NAME = "What Chefs Want - Central"

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

    # def setup_driver(self):
    #     """Initialize the WebDriver"""
    #     if not self.driver:
    #         # Get the directory where the current script is located
    #         script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #         # Build the path to chromedriver in the chrome-mac-arm64 directory
    #         driver_path = os.path.join(script_dir, './firefox_driver', 'geckodriver')
    #         # service = Service(driver_path)
    #         from selenium.webdriver.firefox.service import Service
    #         service = Service(driver_path)
    #         self.driver = seleniumwire_webdriver.Firefox(
    #             service=service,
    #             options=self.firefox_options,
    #             seleniumwire_options=self.seleniumwire_options
    #         )
    #     # self.driver.command_executor.set_timeout(1000)
    #     self.wait = WebDriverWait(self.driver, 180)


    @staticmethod
    def create_interceptor():
        def interceptor(request):
            print(request.url)
            if 'ask' in request.url:
                # Update the request URL
                request.url = "http://restau-appli-g3wto8bmm2jw-1917384324.us-east-1.elb.amazonaws.com/ask"
                print(f"👽👽👽 Updated URL: {request.url}")

        return interceptor

    def launch(self):
        print(self.firefox_options)
        self.setup_driver()
        self.driver.request_interceptor = self.create_interceptor()
        print("loading URL")
        self.driver.get("http://restau-appli-g3wto8bmm2jw-1917384324.us-east-1.elb.amazonaws.com")
        print("loaded URL")
        time.sleep(5000000)
        return