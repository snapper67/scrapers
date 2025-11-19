import json
import time


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

class BittersBottlesScraper(ShopifyScraper):
	# 36/edit_note/1646/
	CRM_ID = 36
	CRM_NOTE_ID = 1646
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = ''

	TEST_CATEGORIES = 100
	TEST_PRODUCTS = 20000
	CSV_START_ROW = 0
	TEST_TABS = 2
	MAX_API_PRODUCTS = 999  # Maximum number to change the search request page size
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/bitters_bottles'

	BASE_URL = 'https://www.bittersandbottles.com/collections/spirits'
	VENDOR_NAME = 'Bitters and Bottles'

	DEDUP_INPUT_FILE = 'dedupe_product_data.csv'

	CATEGORIES = json.loads('''{
  "data":
    {
      "categories": [
        {
          "id": 1,
          "name": "Spirits",
          "subcategories": [
            {
              "name": "Store Picks",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/private-selection"
            },
            {
              "name": "Curated",
              "subcategories": [
                {
                  "name": "New Arrivals",
                  "url": "https://www.bittersandbottles.com/collections/new-arrivals"
                },
                {
                  "name": "Rare & Limited",
                  "url": "https://www.bittersandbottles.com/collections/curated-rare-limited"
                },
                {
                  "name": "NOT Collection",
                  "url": "https://www.bittersandbottles.com/collections/the-not-collection"
                },
                {
                  "name": "Just 50 ml",
                  "url": "https://www.bittersandbottles.com/collections/just-a-nip"
                }
              ],
              "url": "https://www.bittersandbottles.com/collections/curated"
            },
            {
              "name": "New Arrivals",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/new-arrivals"
            },
            {
              "name": "Rare & Limited",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/curated-rare-limited"
            },
            {
              "name": "NOT Collection",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/the-not-collection"
            },
            {
              "name": "Just 50 ml",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/just-a-nip"
            },
            {
              "name": "Whiskey",
              "subcategories": [
                {
                  "name": "Whiskey Club",
                  "url": "https://www.bittersandbottles.com/products/whiskey-club"
                },
                {
                  "name": "Bourbon & Corn",
                  "url": "https://www.babliquor.com/collections/bourbon-corn"
                },
                {
                  "name": "Rye, Wheat, Other",
                  "url": "https://www.babliquor.com/collections/rye-wheat-other"
                },
                {
                  "name": "Scotch & Malt",
                  "url": "https://www.babliquor.com/collections/scotch-malt"
                },
                {
                  "name": "Flavored",
                  "url": "https://www.babliquor.com/collections/flavored-whiskey"
                },
                {
                  "name": "Flights",
                  "url": "https://www.bittersandbottles.com/collections/whiskey-flights"
                }
              ],
              "url": "https://www.babliquor.com/collections/whiskey"
            },
            {
              "name": "Whiskey Club",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/products/whiskey-club"
            },
            {
              "name": "Bourbon & Corn",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/bourbon-corn"
            },
            {
              "name": "Rye, Wheat, Other",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/rye-wheat-other"
            },
            {
              "name": "Scotch & Malt",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/scotch-malt"
            },
            {
              "name": "Flavored",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/flavored-whiskey"
            },
            {
              "name": "Flights",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/whiskey-flights"
            },
            {
              "name": "Rum",
              "subcategories": [
                {
                  "name": "Rum Club",
                  "url": "https://www.bittersandbottles.com/products/rum-club"
                },
                {
                  "name": "White",
                  "url": "https://www.babliquor.com/collections/white-rum"
                },
                {
                  "name": "Dark",
                  "url": "https://www.babliquor.com/collections/dark-rum"
                },
                {
                  "name": "Agricole & Sugarcane",
                  "url": "https://www.babliquor.com/collections/agricole-sugarcane"
                },
                {
                  "name": "Pot Still",
                  "url": "https://www.bittersandbottles.com/collections/pot-still-rums"
                },
                {
                  "name": "Unadulterated",
                  "url": "https://www.bittersandbottles.com/collections/unadulterated-rum"
                },
                {
                  "name": "Flavored",
                  "url": "https://www.babliquor.com/collections/flavored-rum"
                },
                {
                  "name": "Flights",
                  "url": "https://www.bittersandbottles.com/collections/rum-flights"
                }
              ],
              "url": "https://www.babliquor.com/collections/rum"
            },
            {
              "name": "Rum Club",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/products/rum-club"
            },
            {
              "name": "White",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/white-rum"
            },
            {
              "name": "Dark",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/dark-rum"
            },
            {
              "name": "Agricole & Sugarcane",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/agricole-sugarcane"
            },
            {
              "name": "Pot Still",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/pot-still-rums"
            },
            {
              "name": "Unadulterated",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/unadulterated-rum"
            },
            {
              "name": "Flavored",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/flavored-rum"
            },
            {
              "name": "Flights",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/rum-flights"
            },
            {
              "name": "Gin",
              "subcategories": [
                {
                  "name": "Gin Club",
                  "url": "https://www.bittersandbottles.com/products/gin-club"
                },
                {
                  "name": "Dry & Citrusy",
                  "url": "https://www.babliquor.com/collections/dry-citrusy"
                },
                {
                  "name": "Floral, Fruity, Savory",
                  "url": "https://www.babliquor.com/collections/floral-fruity-savory"
                },
                {
                  "name": "Barrel Aged",
                  "url": "https://www.babliquor.com/collections/barrel-aged-gin"
                },
                {
                  "name": "Flights",
                  "url": "https://www.bittersandbottles.com/collections/gin-flights"
                }
              ],
              "url": "https://www.babliquor.com/collections/gin"
            },
            {
              "name": "Gin Club",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/products/gin-club"
            },
            {
              "name": "Dry & Citrusy",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/dry-citrusy"
            },
            {
              "name": "Floral, Fruity, Savory",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/floral-fruity-savory"
            },
            {
              "name": "Barrel Aged",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/barrel-aged-gin"
            },
            {
              "name": "Flights",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/gin-flights"
            },
            {
              "name": "Tequila",
              "subcategories": [
                {
                  "name": "Agave Club",
                  "url": "https://www.bittersandbottles.com/products/agave-club"
                },
                {
                  "name": "Blanco",
                  "url": "https://www.babliquor.com/collections/blanco"
                },
                {
                  "name": "Reposado",
                  "url": "https://www.babliquor.com/collections/reposado"
                },
                {
                  "name": "Anejo & Extra",
                  "url": "https://www.babliquor.com/collections/anejo-extra"
                },
                {
                  "name": "Additive Free",
                  "url": "https://www.bittersandbottles.com/collections/additive-free-tequila"
                },
                {
                  "name": "Flavored",
                  "url": "https://www.babliquor.com/collections/flavored-tequila"
                },
                {
                  "name": "Flights",
                  "url": "https://www.bittersandbottles.com/collections/agave-flights"
                }
              ],
              "url": "https://www.babliquor.com/collections/tequila"
            },
            {
              "name": "Agave Club",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/products/agave-club"
            },
            {
              "name": "Blanco",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/blanco"
            },
            {
              "name": "Reposado",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/reposado"
            },
            {
              "name": "Anejo & Extra",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/anejo-extra"
            },
            {
              "name": "Additive Free",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/additive-free-tequila"
            },
            {
              "name": "Flavored",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/flavored-tequila"
            },
            {
              "name": "Flights",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/agave-flights"
            },
            {
              "name": "Mezcal",
              "subcategories": [
                {
                  "name": "Agave Club",
                  "url": "https://www.bittersandbottles.com/products/agave-club"
                },
                {
                  "name": "Espadin",
                  "url": "https://www.babliquor.com/collections/espadin"
                },
                {
                  "name": "Wild Agave",
                  "url": "https://www.babliquor.com/collections/wild-agave"
                },
                {
                  "name": "Pechuga",
                  "url": "https://www.babliquor.com/collections/pechuga"
                },
                {
                  "name": "Flights",
                  "url": "https://www.bittersandbottles.com/collections/agave-flights"
                }
              ],
              "url": "https://www.babliquor.com/collections/mezcal"
            },
            {
              "name": "Agave Club",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/products/agave-club"
            },
            {
              "name": "Espadin",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/espadin"
            },
            {
              "name": "Wild Agave",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/wild-agave"
            },
            {
              "name": "Pechuga",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/pechuga"
            },
            {
              "name": "Flights",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/agave-flights"
            },
            {
              "name": "Brandy",
              "subcategories": [
                {
                  "name": "Grape",
                  "url": "https://www.babliquor.com/collections/grape"
                },
                {
                  "name": "Apple, Pear, Other",
                  "url": "https://www.babliquor.com/collections/apple-pear-other"
                }
              ],
              "url": "https://www.babliquor.com/collections/brandy"
            },
            {
              "name": "Grape",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/grape"
            },
            {
              "name": "Apple, Pear, Other",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/apple-pear-other"
            },
            {
              "name": "Vodka",
              "subcategories": [
                {
                  "name": "Neutral",
                  "url": "https://www.babliquor.com/collections/neutral-vodka"
                },
                {
                  "name": "Flavored",
                  "url": "https://www.babliquor.com/collections/flavored-vodka"
                },
                {
                  "name": "Flights",
                  "url": "https://www.bittersandbottles.com/collections/vodka-flights"
                }
              ],
              "url": "https://www.babliquor.com/collections/vodka"
            },
            {
              "name": "Neutral",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/neutral-vodka"
            },
            {
              "name": "Flavored",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/flavored-vodka"
            },
            {
              "name": "Flights",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/vodka-flights"
            },
            {
              "name": "Liqueur",
              "subcategories": [
                {
                  "name": "Fruit & Veggie",
                  "url": "https://www.babliquor.com/collections/fruit-veggie-liqueur"
                },
                {
                  "name": "Floral, Herbal, Honey",
                  "url": "https://www.babliquor.com/collections/floral-herbal-honey"
                },
                {
                  "name": "Bean, Cream, Nut",
                  "url": "https://www.babliquor.com/collections/bean-cream-nut"
                },
                {
                  "name": "Spiced",
                  "url": "https://www.babliquor.com/collections/spiced-liqueur"
                },
                {
                  "name": "Bitter",
                  "url": "https://www.babliquor.com/collections/bitter-liqueur"
                },
                {
                  "name": "Flights",
                  "url": "https://www.bittersandbottles.com/collections/amaro-flights"
                }
              ],
              "url": "https://www.babliquor.com/collections/liqueur"
            },
            {
              "name": "Fruit & Veggie",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/fruit-veggie-liqueur"
            },
            {
              "name": "Floral, Herbal, Honey",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/floral-herbal-honey"
            },
            {
              "name": "Bean, Cream, Nut",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/bean-cream-nut"
            },
            {
              "name": "Spiced",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/spiced-liqueur"
            },
            {
              "name": "Bitter",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/bitter-liqueur"
            },
            {
              "name": "Flights",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/amaro-flights"
            },
            {
              "name": "Fortified/Specialty",
              "subcategories": [
                {
                  "name": "Red & White Vermouth",
                  "url": "https://www.babliquor.com/collections/red-white-vermouth"
                },
                {
                  "name": "Dry Vermouth",
                  "url": "https://www.babliquor.com/collections/dry-vermouth"
                },
                {
                  "name": "Aperitif & Digestif",
                  "url": "https://www.babliquor.com/collections/aperitif-digestif"
                },
                {
                  "name": "Sherry & Port",
                  "url": "https://www.babliquor.com/collections/sherry-port"
                },
                {
                  "name": "Specialty",
                  "url": "https://www.bittersandbottles.com/collections/specialty-spirits"
                }
              ],
              "url": "https://www.babliquor.com/collections/fortified"
            },
            {
              "name": "Red & White Vermouth",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/red-white-vermouth"
            },
            {
              "name": "Dry Vermouth",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/dry-vermouth"
            },
            {
              "name": "Aperitif & Digestif",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/aperitif-digestif"
            },
            {
              "name": "Sherry & Port",
              "subcategories": null,
              "url": "https://www.babliquor.com/collections/sherry-port"
            },
            {
              "name": "Specialty",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/specialty-spirits"
            },
            {
              "name": "Alcohol Free",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/alcohol-free"
            }
          ],
          "url": "https://www.babliquor.com/collections/liquor-shop"
        },
        {
          "id": 2,
          "name": "Cocktails",
          "subcategories": [
            {
              "name": "Canned & Bottled",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/ready-made-cocktail"
            },
            {
              "name": "Negroni Shop",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/the-negroni-shop"
            },
            {
              "name": "Daiquiri Shop",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/daiquiri-shop"
            },
            {
              "name": "Margarita Shop",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/margarita-shop"
            },
            {
              "name": "Chinola Shop",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/fun-with-chinola"
            },
            {
              "name": "Kits By Type",
              "subcategories": [
                {
                  "name": "Whiskey",
                  "url": "https://www.bittersandbottles.com/collections/cocktails-whiskey"
                },
                {
                  "name": "Rum",
                  "url": "https://www.bittersandbottles.com/collections/cocktails-rum"
                },
                {
                  "name": "Gin",
                  "url": "https://www.bittersandbottles.com/collections/cocktails-gin"
                },
                {
                  "name": "Tequila & Mezcal",
                  "url": "https://www.bittersandbottles.com/collections/cocktails-agave"
                },
                {
                  "name": "Brandy",
                  "url": "https://www.bittersandbottles.com/collections/cocktails-brandy"
                },
                {
                  "name": "Vodka",
                  "url": "https://www.bittersandbottles.com/collections/cocktails-vodka"
                },
                {
                  "name": "Alcohol Free",
                  "url": "https://www.bittersandbottles.com/collections/cocktails-no-abv"
                }
              ],
              "url": "https://www.bittersandbottles.com/collections/kits-by-type"
            },
            {
              "name": "Whiskey",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/cocktails-whiskey"
            },
            {
              "name": "Rum",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/cocktails-rum"
            },
            {
              "name": "Gin",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/cocktails-gin"
            },
            {
              "name": "Tequila & Mezcal",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/cocktails-agave"
            },
            {
              "name": "Brandy",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/cocktails-brandy"
            },
            {
              "name": "Vodka",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/cocktails-vodka"
            },
            {
              "name": "Alcohol Free",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/cocktails-no-abv"
            },
            {
              "name": "More Shops",
              "subcategories": [
                {
                  "name": "Brucato Shop",
                  "url": "https://www.bittersandbottles.com/collections/brucato-cocktail-shop"
                },
                {
                  "name": "Olehna Shop",
                  "url": "https://www.bittersandbottles.com/collections/olehna-cocktail-shop"
                },
                {
                  "name": "Stiggins Shop",
                  "url": "https://www.bittersandbottles.com/collections/stiggins-cocktail-shop"
                }
              ],
              "url": "https://www.bittersandbottles.com/collections/cocktail-shop"
            },
            {
              "name": "Brucato Shop",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/brucato-cocktail-shop"
            },
            {
              "name": "Olehna Shop",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/olehna-cocktail-shop"
            },
            {
              "name": "Stiggins Shop",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/stiggins-cocktail-shop"
            }
          ],
          "url": "https://www.bittersandbottles.com/collections/cocktails"
        },
        {
          "id": 3,
          "name": "Supplies",
          "subcategories": [
            {
              "name": "Bitters",
              "subcategories": [
                {
                  "name": "Aromatic & Spice",
                  "url": "https://www.bittersandbottles.com/collections/bitters-aromatic-spice"
                },
                {
                  "name": "Fruit & Veggie",
                  "url": "https://www.bittersandbottles.com/collections/bitters-fruit-veggie"
                },
                {
                  "name": "Floral & Herbal",
                  "url": "https://www.bittersandbottles.com/collections/bitters-floral-herbal"
                },
                {
                  "name": "Bean & Nut",
                  "url": "https://www.bittersandbottles.com/collections/bitters-bean-nut"
                },
                {
                  "name": "Regional",
                  "url": "https://www.bittersandbottles.com/collections/bitters-regional-flavors"
                }
              ],
              "url": "https://www.bittersandbottles.com/collections/bitters"
            },
            {
              "name": "Aromatic & Spice",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/bitters-aromatic-spice"
            },
            {
              "name": "Fruit & Veggie",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/bitters-fruit-veggie"
            },
            {
              "name": "Floral & Herbal",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/bitters-floral-herbal"
            },
            {
              "name": "Bean & Nut",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/bitters-bean-nut"
            },
            {
              "name": "Regional",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/bitters-regional-flavors"
            },
            {
              "name": "Syrups & Mixers",
              "subcategories": [
                {
                  "name": "Syrups",
                  "url": "https://www.bittersandbottles.com/collections/mixers-syrups"
                },
                {
                  "name": "Mixers",
                  "url": "https://www.bittersandbottles.com/collections/mixers-ready-made-mixer"
                },
                {
                  "name": "Specialty",
                  "url": "https://www.bittersandbottles.com/collections/cocktail-specialty"
                },
                {
                  "name": "Garnish",
                  "url": "https://www.bittersandbottles.com/collections/mixers-garnish"
                },
                {
                  "name": "Sodas & Tonics",
                  "url": "https://www.bittersandbottles.com/collections/sodas-tonics"
                }
              ],
              "url": "https://www.bittersandbottles.com/collections/mixers"
            },
            {
              "name": "Syrups",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/mixers-syrups"
            },
            {
              "name": "Mixers",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/mixers-ready-made-mixer"
            },
            {
              "name": "Specialty",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/cocktail-specialty"
            },
            {
              "name": "Garnish",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/mixers-garnish"
            },
            {
              "name": "Sodas & Tonics",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/sodas-tonics"
            },
            {
              "name": "Bar Tools",
              "subcategories": [
                {
                  "name": "Juice & Muddle",
                  "url": "https://www.bittersandbottles.com/collections/bar-tools-juice-muddle"
                },
                {
                  "name": "Measure, Stir, Strain",
                  "url": "https://www.bittersandbottles.com/collections/bar-tools-measure-stir-strain"
                },
                {
                  "name": "Mix & Shake",
                  "url": "https://www.bittersandbottles.com/collections/bar-tools-mix-shake"
                },
                {
                  "name": "Dispense & Garnish",
                  "url": "https://www.bittersandbottles.com/collections/bar-tools-dispense-garnish"
                },
                {
                  "name": "Home & Travel",
                  "url": "https://www.bittersandbottles.com/collections/bar-tools-home-travel"
                }
              ],
              "url": "https://www.bittersandbottles.com/collections/bar-tools"
            },
            {
              "name": "Juice & Muddle",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/bar-tools-juice-muddle"
            },
            {
              "name": "Measure, Stir, Strain",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/bar-tools-measure-stir-strain"
            },
            {
              "name": "Mix & Shake",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/bar-tools-mix-shake"
            },
            {
              "name": "Dispense & Garnish",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/bar-tools-dispense-garnish"
            },
            {
              "name": "Home & Travel",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/bar-tools-home-travel"
            },
            {
              "name": "Curated",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/curated-supplies"
            },
            {
              "name": "Alcohol Free Spirits",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/alcohol-free"
            }
          ],
          "url": "https://www.bittersandbottles.com/collections/bar-supplies"
        },
        {
          "id": 4,
          "name": "Clubs",
          "subcategories": [
            {
              "name": "Club Shop",
              "subcategories": [
                {
                  "name": "Learn More",
                  "url": "https://www.bittersandbottles.com/pages/club-shop-entry"
                }
              ],
              "url": "https://www.bittersandbottles.com/collections/club-shop"
            },
            {
              "name": "Learn More",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/pages/club-shop-entry"
            },
            {
              "name": "Whiskey",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/products/whiskey-club"
            },
            {
              "name": "Rum",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/products/rum-club"
            },
            {
              "name": "Agave",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/products/agave-club"
            },
            {
              "name": "Gin",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/products/gin-club"
            },
            {
              "name": "Negroni",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/products/negroni-club"
            },
            {
              "name": "Old Fashioned",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/products/old-fashioned-club"
            }
          ],
          "url": "https://www.bittersandbottles.com/pages/clubs"
        },
        {
          "id": 5,
          "name": "Rewards",
          "subcategories": [
            {
              "name": "Points Auction",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/vbp-points-auction"
            },
            {
              "name": "4x Points Bonus",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/4x-points-bonus"
            },
            {
              "name": "6x Points Bonus",
              "subcategories": null,
              "url": "https://www.bittersandbottles.com/collections/6x-points-bonus"
            }
          ],
          "url": "https://www.bittersandbottles.com/pages/rewards"
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
		return category['url']

	# ************************************************************************

	# 	Product Scraping Functions
	# ************************************************************************

	def get_pack_size(self, data, row_spec):
		print("get_pack_size()")
		data = data.get('variants', None)
		if data:
			data = data[0]
			try:
				options = data.get('options', None)
				# Find the specification with displayName "Manufacturer Name"
				print(options)
				if options:

					if len(options) == 1:
						row_spec['pack_size'] = options[0].replace('Default Title','')
						print(f"Found pack size: {options[0]}")
					else:
						row_spec['pack_size'] = options[0].replace('Default Title','')
						print(f"Found pack size: {options[0]}")
						print("⚠️ need to handle multiple pack sizes")

			except Exception as e:
				print(f"⛔️ Error processing pack size information: {type(e).__name__} - {str(e)}")

			print("Processing pack size information complete...")
		return row_spec

	def get_product_details(self, url, row_spec=None):
		"""Get Product Details"""
		print("BittersBottlesScraper.get_product_details()")
		data = self.get_product_details_scrape(url, row_spec, target="script[type='application/json'][data-section-type='static-product']")
		row_spec = self.get_product_data(data.get('product', {}), row_spec)
		return row_spec

	# ************************************************************************
	def build_categories_list(self):
		url = "https://www.bittersandbottles.com/"
		navigation = self.get_navigation_structure(url)
		# self.print_navigation_structure(navigation)
		return f"<div>{navigation}</div>"

	# def build_products_list(self):
	# 	"""Scrape products from the website"""
	# 	html = ""
	# 	all_urls = []
	# 	# Use the options with fallback to module-level variables
	# 	max_products = self.options.get('max_products', self.MAX_API_PRODUCTS)
	# 	category_to_process = self.options.get('category_to_process', 0)
	# 	chosen_category = int(self.options.get('chosen_category', 0))
	# 	test_categories = self.options.get('test_categories', 100)
	# 	category_count = 0
	# 	if int(self.options['chosen_category']) == 0:
	# 		categories = self.get_taxonomy()
	# 		print(f"All Categories ")
	# 	else:
	# 		for category in self.get_taxonomy():
	# 			print(f"category : {category.get('name', '')}")
	# 			if int(category.get('id', '')) == chosen_category:
	# 				categories = [category]  # Only process the chosen category
	# 				print(f"Category found : {categories}")
	# 				break
	# 	url_output_file = self.options.get('url_output_file', '')
	#
	# 	# Wait for the page to be fully loaded
	# 	print(f"Output File Name: {url_output_file}")
	# 	total_products = 0
	# 	loop_counter = 0
	# 	category_found_count = 1
	#
	# 	if category_to_process > 0:
	# 		print(f"Category to process: {category_to_process}")
	# 		loop_counter = category_to_process - 1
	# 		test_categories = category_to_process
	# 		category_found_count = category_to_process
	# 	for category in categories:
	# 		category_name = category['name']
	# 		print(f"category: {category_name}")
	# 		sub_categories = category['subcategories']
	# 		category_found_count = len(sub_categories)
	# 		print(f"Found {category_found_count} categories to process...")
	# 		for sub_category in sub_categories:
	# 			sub_category_name = sub_category['name']
	# 			print(f"sub category: {sub_category_name}")
	# 			if sub_category.get('subcategories', False):
	# 				for sub_sub_category in sub_category['subcategories']:
	# 					sub_sub_category_name = sub_sub_category['name']
	# 					print(f"sub sub category: {sub_sub_category_name}")
	# 					if loop_counter < category_found_count and loop_counter < test_categories:
	# 						loop_counter += 1
	# 						url = sub_sub_category['url']
	# 						print(f"Url: {url}")
	# 						detail_urls, html = self.get_category_page(url, category_name, sub_category_name, sub_sub_category_name)
	# 						all_urls.extend(detail_urls)
	# 					time.sleep(3)
	# 			else:
	# 				url = sub_category['url']
	# 				print(f"Url: {url}")
	# 				detail_urls, html = self.get_category_page(url, category_name, sub_category_name, '')
	# 				all_urls.extend(detail_urls)
	#
	# 	# html_table_to_csv(html_table)
	# 	html += f"<h2>Total products found: {total_products}</h2>"
	#
	# 	print(f"Total products found: {len(all_urls)}")
	# 	return html

	def get_category_page(self, url, category_name, sub_category_name, sub_sub_category_name):
		print("get_category_page()")
		main_window = self.driver.current_window_handle
		html = ''
		total_products = 0
		self.driver.get(url)
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
					self.save_urls_to_csv(detail_urls, category_name, sub_category_name, sub_sub_category_name)

				except Exception as e:
					print(f"****************** ⛔️⛔️⛔️ Error getting details: {e}")
					html += f"<div>Name: {sub_category_name} (Error getting details)</div>"

				try:
					paging = self.wait.until(
						EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination--inner'))
					)
					paging.find_element(By.CLASS_NAME, 'pagination--next').click()
					next_page = True
				except Exception as e:
					next_page = False


		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing category: {e}")

		return detail_urls, html

