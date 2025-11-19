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

from scrapers.scraper import Scraper, SkuNotFound

"""
	Webstaurant.com
	Type: Standard shop website
	Method: 
		Get Categories: Scape Navigation
		Get Products: Scape Product List
		Get Product Manual Scrape and json data from html
	Issues:
		The embedded json data does not have all the information needed to create a product. Data like 
		sku and description are not included in the json data.
"""


class WebstaurantScraper(Scraper):
	# /3103/edit_note/1721/
	CRM_ID = 3103
	CRM_NOTE_ID = 1721
	CRM_PRICE_TYPE = ''
	CRM_STATUS_OVERRIDE = 'Ready'

	DISTRIBUTOR_PRODUCT_DATA_SPEC = {
		'extra_data_3': '',
		'product_id': '',
		'productGroupId': ''
	}
	DEFAULT_DIRECTORY = '/Users/mark/Downloads/scrapers/webstaurant_store/'
	URL_OUTPUT_FILE = 'product_urls.csv'
	DATA_OUTPUT_FILE = 'product_data.csv'

	BASE_URL = 'https://www.webstaurantstore.com'
	VENDOR_NAME = 'Webstaurant Store'
	CATEGORIES = json.loads('''{
  "data": {
    "categories": [
      {
        "id": 1539,
        "name": "Restaurant Equipment",
        "url": "https://www.webstaurantstore.com/restaurant-equipment.html",
        "subcategories": [
          {
            "id": "",
            "name": "Equipment Parts",
            "url": "https://www.webstaurantstore.com/parts.html"
          },
          {
            "id": "",
            "name": "Stainless Steel Work Tables with Undershelf",
            "url": "https://www.webstaurantstore.com/13729/stainless-steel-work-tables-with-undershelf.html"
          },
          {
            "id": "",
            "name": "Commercial Fryers",
            "url": "https://www.webstaurantstore.com/48429/commercial-fryers.html"
          },
          {
            "id": "",
            "name": "Gas Ranges",
            "url": "https://www.webstaurantstore.com/15037/commercial-restaurant-ranges.html"
          },
          {
            "id": "",
            "name": "Convection Ovens",
            "url": "https://www.webstaurantstore.com/14181/commercial-convection-ovens.html"
          },
          {
            "id": "",
            "name": "Frozen Drink Machines",
            "url": "https://www.webstaurantstore.com/14061/granita-slushy-machines.html"
          },
          {
            "id": "",
            "name": "Commercial Mixers",
            "url": "https://www.webstaurantstore.com/14255/commercial-mixers.html"
          },
          {
            "id": "",
            "name": "Griddles",
            "url": "https://www.webstaurantstore.com/50439/griddles.html"
          },
          {
            "id": "",
            "name": "Food Processors",
            "url": "https://www.webstaurantstore.com/14245/commercial-food-processors.html"
          },
          {
            "id": "",
            "name": "Meat Slicers",
            "url": "https://www.webstaurantstore.com/14199/meat-slicers.html"
          },
          {
            "id": "",
            "name": "3 Compartment Sinks",
            "url": "https://www.webstaurantstore.com/14927/3-compartment-sinks.html"
          },
          {
            "id": "",
            "name": "Commercial Dishwashers",
            "url": "https://www.webstaurantstore.com/49791/commercial-dishwashers.html"
          },
          {
            "id": "",
            "name": "Commercial Blenders",
            "url": "https://www.webstaurantstore.com/14251/commercial-blenders-food-blenders.html"
          },
          {
            "id": "",
            "name": "Rapid Cook Ovens",
            "url": "https://www.webstaurantstore.com/22267/rapid-cook-high-speed-hybrid-ovens.html"
          },
          {
            "id": "",
            "name": "Vacuum Packaging Machines",
            "url": "https://www.webstaurantstore.com/14279/vacuum-packaging-machines.html"
          },
          {
            "id": "",
            "name": "Commercial Microwaves",
            "url": "https://www.webstaurantstore.com/14351/commercial-microwaves.html"
          },
          {
            "id": "",
            "name": "Charbroilers",
            "url": "https://www.webstaurantstore.com/50437/charbroilers.html"
          },
          {
            "id": "",
            "name": "Espresso Machines",
            "url": "https://www.webstaurantstore.com/13977/cappuccino-espresso-machines.html"
          },
          {
            "id": "",
            "name": "Steam Tables",
            "url": "https://www.webstaurantstore.com/14141/commercial-steam-tables.html"
          },
          {
            "id": "",
            "name": "Immersion Blenders",
            "url": "https://www.webstaurantstore.com/14253/commercial-immersion-blenders.html"
          },
          {
            "id": "",
            "name": "Coffee Machines",
            "url": "https://www.webstaurantstore.com/13953/commercial-coffee-makers-brewers.html"
          },
          {
            "id": "",
            "name": "Toasters",
            "url": "https://www.webstaurantstore.com/14603/commercial-conveyor-toasters.html"
          },
          {
            "id": "",
            "name": "Conveyor and Impinger Ovens",
            "url": "https://www.webstaurantstore.com/14185/conveyor-ovens-and-impinger-ovens.html"
          },
          {
            "id": "",
            "name": "Commercial Faucets",
            "url": "https://www.webstaurantstore.com/plumbing-and-faucets.html"
          }
        ]
      },
      {
        "id": 13403,
        "name": "Refrigeration",
        "url": "https://www.webstaurantstore.com/refrigeration-equipment.html",
        "subcategories": [
          {
            "id": "",
            "name": " Sandwich & Salad Prep Refrigerators",
            "url": "https://www.webstaurantstore.com/13415/commercial-sandwich-salad-preparation-refrigerators.html"
          },
          {
            "id": "",
            "name": "Reach-In Refrigerators",
            "url": "https://www.webstaurantstore.com/52705/reach-in-refrigerators.html"
          },
          {
            "id": "",
            "name": "Reach-In Freezers",
            "url": "https://www.webstaurantstore.com/52711/reach-in-freezers.html"
          },
          {
            "id": "",
            "name": "Glass Door Refrigerators",
            "url": "https://www.webstaurantstore.com/21387/merchandising-glass-door-refrigerators-coolers.html"
          },
          {
            "id": "",
            "name": "Back Bar Coolers",
            "url": "https://www.webstaurantstore.com/42397/back-bar-coolers.html"
          },
          {
            "id": "",
            "name": "Beer Dispensers",
            "url": "https://www.webstaurantstore.com/42399/beer-dispensers.html"
          },
          {
            "id": "",
            "name": "Air Curtain Merchandisers",
            "url": "https://www.webstaurantstore.com/54811/horizontal-vertical-air-curtain-merchandisers.html"
          },
          {
            "id": "",
            "name": "Pizza Prep Refrigerators",
            "url": "https://www.webstaurantstore.com/13623/commercial-pizza-preparation-refrigerators.html"
          },
          {
            "id": "",
            "name": "Commercial Chef Bases",
            "url": "https://www.webstaurantstore.com/13665/commercial-chef-bases.html"
          },
          {
            "id": "",
            "name": "Dry and Refrigerated Bakery Cases",
            "url": "https://www.webstaurantstore.com/13469/refrigerated-bakery-cases-and-dry-bakery-display-cases.html"
          },
          {
            "id": "",
            "name": "Worktop Refrigerators",
            "url": "https://www.webstaurantstore.com/26671/worktop-refrigerators.html"
          },
          {
            "id": "",
            "name": "Walk-In Coolers / Refrigerators",
            "url": "https://www.webstaurantstore.com/13703/walk-in-coolers-refrigerators.html"
          },
          {
            "id": "",
            "name": "Bottle Coolers",
            "url": "https://www.webstaurantstore.com/13501/bottle-coolers.html"
          },
          {
            "id": "",
            "name": "Ice Cream Dipping Cabinets",
            "url": "https://www.webstaurantstore.com/42387/ice-cream-dipping-cabinets.html"
          },
          {
            "id": "",
            "name": "Glass Door Freezers",
            "url": "https://www.webstaurantstore.com/21389/merchandising-glass-door-freezers.html"
          },
          {
            "id": "",
            "name": "Glass Top Display Freezers",
            "url": "https://www.webstaurantstore.com/42389/glass-top-display-freezers.html"
          },
          {
            "id": "",
            "name": "Walk-In Freezers",
            "url": "https://www.webstaurantstore.com/13411/walk-in-freezers.html"
          },
          {
            "id": "",
            "name": "Undercounter Freezers",
            "url": "https://www.webstaurantstore.com/13463/undercounter-freezers.html"
          },
          {
            "id": "",
            "name": "Meat & Deli Cases",
            "url": "https://www.webstaurantstore.com/21423/refrigerated-deli-cases.html"
          },
          {
            "id": "",
            "name": "Countertop Glass Door Refrigeration",
            "url": "https://www.webstaurantstore.com/13393/countertop-glass-door-refrigerators-and-freezers.html"
          },
          {
            "id": "",
            "name": "Commercial Chest Freezers",
            "url": "https://www.webstaurantstore.com/13693/commercial-chest-freezers.html"
          },
          {
            "id": "",
            "name": "Worktop Freezers",
            "url": "https://www.webstaurantstore.com/15067/worktop-freezers.html"
          },
          {
            "id": "",
            "name": "Commercial Ice Cream Makers",
            "url": "https://www.webstaurantstore.com/47343/soft-serve-machines.html"
          },
          {
            "id": "",
            "name": "Wine Refrigeration",
            "url": "https://www.webstaurantstore.com/42401/commercial-wine-coolers.html"
          }
        ]
      },
      {
        "id": 2403,
        "name": "Smallwares",
        "url": "https://www.webstaurantstore.com/restaurant-smallwares.html",
        "subcategories": [
          {
            "id": "",
            "name": "Bartending Supplies",
            "url": "https://www.webstaurantstore.com/2505/bartending-supplies.html"
          },
          {
            "id": "",
            "name": "Restaurant Signs",
            "url": "https://www.webstaurantstore.com/3289/signs-easels.html"
          },
          {
            "id": "",
            "name": "Host and Server Supplies",
            "url": "https://www.webstaurantstore.com/3277/server-supplies-and-accessories.html"
          },
          {
            "id": "",
            "name": "Hotel and Restaurant Linens",
            "url": "https://www.webstaurantstore.com/3321/textiles.html"
          },
          {
            "id": "",
            "name": "Food Storage Containers",
            "url": "https://www.webstaurantstore.com/3087/food-storage-containers.html"
          },
          {
            "id": "",
            "name": "Bun / Sheet Pans",
            "url": "https://www.webstaurantstore.com/2423/bun-sheet-pans.html"
          },
          {
            "id": "",
            "name": "Stainless Steel Steam Table Pans",
            "url": "https://www.webstaurantstore.com/52489/stainless-steel-steam-table-pans-and-hotel-pans.html"
          },
          {
            "id": "",
            "name": "Plastic Food Pans",
            "url": "https://www.webstaurantstore.com/51167/plastic-food-pans.html"
          },
          {
            "id": "",
            "name": "Food Storage Boxes",
            "url": "https://www.webstaurantstore.com/37515/food-storage-boxes-and-covers.html"
          },
          {
            "id": "",
            "name": "Chafing Dishes",
            "url": "https://www.webstaurantstore.com/42675/chafing-dishes.html"
          },
          {
            "id": "",
            "name": "Frying Pans",
            "url": "https://www.webstaurantstore.com/2705/fry-pans.html"
          },
          {
            "id": "",
            "name": "Ingredient Bins",
            "url": "https://www.webstaurantstore.com/2457/ingredient-bins.html"
          },
          {
            "id": "",
            "name": "Restaurant Aprons",
            "url": "https://www.webstaurantstore.com/3323/restaurant-aprons.html"
          },
          {
            "id": "",
            "name": "Cup Dispensers and Lid Organizers",
            "url": "https://www.webstaurantstore.com/2751/cup-dispensers-and-lid-organizers.html"
          },
          {
            "id": "",
            "name": "Stock Pots",
            "url": "https://www.webstaurantstore.com/2733/stock-pots-accessories.html"
          },
          {
            "id": "",
            "name": "Cutting Boards",
            "url": "https://www.webstaurantstore.com/3053/cutting-boards.html"
          },
          {
            "id": "",
            "name": "Bakery Display Cases",
            "url": "https://www.webstaurantstore.com/2411/bakery-display-cases.html"
          },
          {
            "id": "",
            "name": "Cake Pans",
            "url": "https://www.webstaurantstore.com/10375/cake-pans.html"
          },
          {
            "id": "",
            "name": "Measuring Cups and Spoons",
            "url": "https://www.webstaurantstore.com/2925/measuring-cups-spoons.html"
          },
          {
            "id": "",
            "name": "Kitchen Utensils",
            "url": "https://www.webstaurantstore.com/53123/cooking-utensils.html"
          },
          {
            "id": "",
            "name": "Canning Supplies",
            "url": "https://www.webstaurantstore.com/57319/canning-jars-and-accessories.html"
          },
          {
            "id": "",
            "name": "Piping Bags and Icing Tips",
            "url": "https://www.webstaurantstore.com/54643/piping-tips-pastry-bags-and-accessories.html"
          },
          {
            "id": "",
            "name": "Pocket Thermometers",
            "url": "https://www.webstaurantstore.com/56251/probe-thermometers-pocket-thermometers.html"
          },
          {
            "id": "",
            "name": "Beverage Dispensers",
            "url": "https://www.webstaurantstore.com/2585/beverage-dispensers.html"
          },
          {
            "id": "",
            "name": "Work Uniforms & Custom Apparel",
            "url": "https://www.webstaurantstore.com/69357/work-uniforms-custom-apparel.html"
          }
        ]
      },
      {
        "id": 1,
        "name": "Food & Beverage",
        "url": "https://www.webstaurantstore.com/restaurant-consumables.html",
        "subcategories": [
          {
            "id": "",
            "name": "Prepared Foods",
            "url": "https://www.webstaurantstore.com/54671/prepared-foods.html"
          },
          {
            "id": "",
            "name": "Meat and Seafood",
            "url": "https://www.webstaurantstore.com/55063/meat-and-seafood.html"
          },
          {
            "id": "",
            "name": "Cooking Oil and Sprays",
            "url": "https://www.webstaurantstore.com/48639/cooking-oil-and-sprays.html"
          },
          {
            "id": "",
            "name": "Ice Cream and Frozen Treats",
            "url": "https://www.webstaurantstore.com/48635/ice-cream-supplies.html"
          },
          {
            "id": "",
            "name": "Specialty Foods",
            "url": "https://www.webstaurantstore.com/56219/specialty-foods.html"
          },
          {
            "id": "",
            "name": "Dairy",
            "url": "https://www.webstaurantstore.com/54655/dairy.html"
          },
          {
            "id": "",
            "name": "Beverage Flavoring Syrups",
            "url": "https://www.webstaurantstore.com/51/flavoring-syrups.html"
          },
          {
            "id": "",
            "name": "Bar Drink Mixes",
            "url": "https://www.webstaurantstore.com/11/bar-drink-mixes.html"
          },
          {
            "id": "",
            "name": "Flavoring Sauces",
            "url": "https://www.webstaurantstore.com/62797/flavoring-sauces.html"
          },
          {
            "id": "",
            "name": "Non-Dairy Milk and Creamer",
            "url": "https://www.webstaurantstore.com/62897/non-dairy-milk.html"
          },
          {
            "id": "",
            "name": "Baking Toppings",
            "url": "https://www.webstaurantstore.com/64739/baking-toppings.html"
          },
          {
            "id": "",
            "name": "Smoothie Mixes",
            "url": "https://www.webstaurantstore.com/45187/smoothie-mixes.html"
          },
          {
            "id": "",
            "name": "Bulk Chocolate",
            "url": "https://www.webstaurantstore.com/51125/bulk-chocolate.html"
          },
          {
            "id": "",
            "name": "Sweeteners",
            "url": "https://www.webstaurantstore.com/69/sugar-sweetener-and-creamer.html"
          },
          {
            "id": "",
            "name": "Ice Cream Cones",
            "url": "https://www.webstaurantstore.com/109/ice-cream-cones.html"
          },
          {
            "id": "",
            "name": "Bulk Flour",
            "url": "https://www.webstaurantstore.com/8935/bulk-flour.html"
          },
          {
            "id": "",
            "name": "Nuts and Seeds",
            "url": "https://www.webstaurantstore.com/12925/peanuts-and-nuts.html"
          },
          {
            "id": "",
            "name": "Salt and Pepper",
            "url": "https://www.webstaurantstore.com/38509/salt-and-pepper.html"
          },
          {
            "id": "",
            "name": "Extracts, Pastes, & Imitation Flavorings",
            "url": "https://www.webstaurantstore.com/47721/extracts-and-imitation-flavoring.html"
          },
          {
            "id": "",
            "name": "Coffee and Espresso",
            "url": "https://www.webstaurantstore.com/53/coffee-and-espresso.html"
          },
          {
            "id": "",
            "name": "Soda",
            "url": "https://www.webstaurantstore.com/45143/soda.html"
          },
          {
            "id": "",
            "name": "Cheese Spreads",
            "url": "https://www.webstaurantstore.com/56747/cheese-spreads.html"
          },
          {
            "id": "",
            "name": "Bakery Decorating Ingredients",
            "url": "https://www.webstaurantstore.com/57099/cake-decorating-ingredients.html"
          }
        ]
      },
      {
        "id": 3673,
        "name": "Tabletop",
        "url": "https://www.webstaurantstore.com/restaurant-tabletop-supplies.html",
        "subcategories": [
          {
            "id": "",
            "name": "Cocktail Glasses",
            "url": "https://www.webstaurantstore.com/47095/cocktail-glasses.html"
          },
          {
            "id": "",
            "name": "Wine Glasses",
            "url": "https://www.webstaurantstore.com/3749/wine-glasses.html"
          },
          {
            "id": "",
            "name": "Beer Glasses",
            "url": "https://www.webstaurantstore.com/3685/beer-glasses.html"
          },
          {
            "id": "",
            "name": "Knives",
            "url": "https://www.webstaurantstore.com/51003/knives.html"
          },
          {
            "id": "",
            "name": "Forks",
            "url": "https://www.webstaurantstore.com/51005/forks.html"
          },
          {
            "id": "",
            "name": "Spoons",
            "url": "https://www.webstaurantstore.com/51001/spoons.html"
          },
          {
            "id": "",
            "name": "Plastic Tumblers",
            "url": "https://www.webstaurantstore.com/3755/plastic-tumblers.html"
          },
          {
            "id": "",
            "name": "Squeeze Bottles",
            "url": "https://www.webstaurantstore.com/3163/squeeze-bottles.html"
          },
          {
            "id": "",
            "name": "Menu Holders",
            "url": "https://www.webstaurantstore.com/15543/menu-covers-and-boards.html"
          },
          {
            "id": "",
            "name": "Reusable Plastic Beverageware",
            "url": "https://www.webstaurantstore.com/3753/reusable-plastic-beverageware.html"
          },
          {
            "id": "",
            "name": "Pitchers",
            "url": "https://www.webstaurantstore.com/4085/pitchers.html"
          },
          {
            "id": "",
            "name": "Drinking Glasses",
            "url": "https://www.webstaurantstore.com/47097/soda-tea-and-water-glasses.html"
          },
          {
            "id": "",
            "name": "Decanters and Carafes",
            "url": "https://www.webstaurantstore.com/4057/decanters-and-carafes.html"
          },
          {
            "id": "",
            "name": "Porcelain Plates",
            "url": "https://www.webstaurantstore.com/50539/porcelain-plates.html"
          },
          {
            "id": "",
            "name": "Melamine Bowls",
            "url": "https://www.webstaurantstore.com/45291/melamine-bowls.html"
          },
          {
            "id": "",
            "name": "Melamine Plates",
            "url": "https://www.webstaurantstore.com/45289/melamine-plates.html"
          },
          {
            "id": "",
            "name": "China Bowls",
            "url": "https://www.webstaurantstore.com/41999/china-bowls.html"
          },
          {
            "id": "",
            "name": "Serving and Display Platters / Trays",
            "url": "https://www.webstaurantstore.com/41967/serving-and-display-platters-trays.html"
          },
          {
            "id": "",
            "name": "Ramekins and Sauce Cups",
            "url": "https://www.webstaurantstore.com/10397/ramekins-and-sauce-cups.html"
          },
          {
            "id": "",
            "name": "Stoneware Plates",
            "url": "https://www.webstaurantstore.com/50889/stoneware-plates.html"
          },
          {
            "id": "",
            "name": "Restaurant Food Serving Baskets",
            "url": "https://www.webstaurantstore.com/3041/restaurant-food-serving-baskets.html"
          },
          {
            "id": "",
            "name": "Serving and Display Bowls",
            "url": "https://www.webstaurantstore.com/41969/serving-and-display-bowls.html"
          },
          {
            "id": "",
            "name": "Reusable Milk & Juice Bottles",
            "url": "https://www.webstaurantstore.com/58849/milk-juice-bottles.html"
          },
          {
            "id": "",
            "name": "Coffee Mugs, Tea Cups, & Saucers",
            "url": "https://www.webstaurantstore.com/3793/coffee-mugs-tea-cups-cappuccino-cups-and-saucers.html"
          },
          {
            "id": "",
            "name": "Au Gratin Dishes / Rarebit Dishes",
            "url": "https://www.webstaurantstore.com/20313/au-gratin-dishes-platters.html"
          }
        ]
      },
      {
        "id": 195,
        "name": "Disposables",
        "url": "https://www.webstaurantstore.com/restaurant-disposable-supplies.html",
        "subcategories": [
          {
            "id": "",
            "name": "Foam Products",
            "url": "https://www.webstaurantstore.com/395/foam-products.html"
          },
          {
            "id": "",
            "name": "Disposable Concession Supplies",
            "url": "https://www.webstaurantstore.com/16199/disposable-concession-supplies.html"
          },
          {
            "id": "",
            "name": "Consumer Packaging",
            "url": "https://www.webstaurantstore.com/63661/consumer-packaging.html"
          },
          {
            "id": "",
            "name": "Disposable Gloves",
            "url": "https://www.webstaurantstore.com/261/disposable-gloves.html"
          },
          {
            "id": "",
            "name": "Disposable Plastic Cups",
            "url": "https://www.webstaurantstore.com/655/disposable-plastic-cups.html"
          },
          {
            "id": "",
            "name": "Paper Bags",
            "url": "https://www.webstaurantstore.com/15969/paper-bags.html"
          },
          {
            "id": "",
            "name": "Deli Containers",
            "url": "https://www.webstaurantstore.com/779/deli-take-out-containers.html"
          },
          {
            "id": "",
            "name": "Paper Take-Out Boxes",
            "url": "https://www.webstaurantstore.com/11987/paper-take-out-boxes.html"
          },
          {
            "id": "",
            "name": "Plastic To-Go Containers",
            "url": "https://www.webstaurantstore.com/803/plastic-microwaveable-take-out-containers.html"
          },
          {
            "id": "",
            "name": "Portion Cups & Lids",
            "url": "https://www.webstaurantstore.com/715/souffle-portion-cups-lids.html"
          },
          {
            "id": "",
            "name": "Paper Hot Cups",
            "url": "https://www.webstaurantstore.com/589/paper-hot-cups.html"
          },
          {
            "id": "",
            "name": "Plastic Cutlery / Utensils",
            "url": "https://www.webstaurantstore.com/54139/plastic-cutlery-utensils.html"
          },
          {
            "id": "",
            "name": "Disposable Soup Containers",
            "url": "https://www.webstaurantstore.com/11985/disposable-soup-containers.html"
          },
          {
            "id": "",
            "name": "Paper Napkins",
            "url": "https://www.webstaurantstore.com/547/paper-napkins.html"
          },
          {
            "id": "",
            "name": "Muffin & Cupcake Packaging",
            "url": "https://www.webstaurantstore.com/12949/cupcake-muffin-take-out-containers.html"
          },
          {
            "id": "",
            "name": "Foam Takeout Containers",
            "url": "https://www.webstaurantstore.com/47305/foam-hinged-take-out-containers.html"
          },
          {
            "id": "",
            "name": "Cake Boxes and Bakery Boxes",
            "url": "https://www.webstaurantstore.com/353/cake-boxes-and-bakery-boxes.html"
          },
          {
            "id": "",
            "name": "Clear Hinged Take-Out Containers",
            "url": "https://www.webstaurantstore.com/775/clear-hinged-take-out-containers.html"
          },
          {
            "id": "",
            "name": "Plastic Bags",
            "url": "https://www.webstaurantstore.com/323/plastic-bags.html"
          },
          {
            "id": "",
            "name": "Aluminum Foil Pans",
            "url": "https://www.webstaurantstore.com/197/aluminum-foil-pans.html"
          },
          {
            "id": "",
            "name": "Straws",
            "url": "https://www.webstaurantstore.com/753/straws.html"
          },
          {
            "id": "",
            "name": "Plastic Glassware & Barware",
            "url": "https://www.webstaurantstore.com/649/disposable-plastic-barware-and-cups.html"
          },
          {
            "id": "",
            "name": "Foam Cups and Lids",
            "url": "https://www.webstaurantstore.com/47237/foam-cups-and-lids.html"
          },
          {
            "id": "",
            "name": "Plastic Disposable Plates",
            "url": "https://www.webstaurantstore.com/45835/plastic-disposable-plates.html"
          }
        ]
      },
      {
        "id": 68015,
        "name": "Furniture",
        "url": "https://www.webstaurantstore.com/commercial-furniture.html",
        "subcategories": [
          {
            "id": "",
            "name": "Table Tops",
            "url": "https://www.webstaurantstore.com/42545/table-tops.html"
          },
          {
            "id": "",
            "name": "Outdoor Restaurant Tables",
            "url": "https://www.webstaurantstore.com/42561/outdoor-restaurant-tables.html"
          },
          {
            "id": "",
            "name": "Restaurant Bar Stools",
            "url": "https://www.webstaurantstore.com/42539/restaurant-bar-stools.html"
          },
          {
            "id": "",
            "name": "Restaurant Chairs",
            "url": "https://www.webstaurantstore.com/42529/restaurant-chairs.html"
          },
          {
            "id": "",
            "name": "Outdoor Restaurant Chairs",
            "url": "https://www.webstaurantstore.com/42559/outdoor-restaurant-chairs.html"
          },
          {
            "id": "",
            "name": "Tables and Chair Sets",
            "url": "https://www.webstaurantstore.com/45689/tables-and-dining-sets.html"
          },
          {
            "id": "",
            "name": "Restaurant Table Bases",
            "url": "https://www.webstaurantstore.com/42543/restaurant-table-bases.html"
          },
          {
            "id": "",
            "name": "Outdoor Restaurant Bar Stools",
            "url": "https://www.webstaurantstore.com/50381/outdoor-restaurant-bar-stools.html"
          },
          {
            "id": "",
            "name": "Commercial Patio Heaters",
            "url": "https://www.webstaurantstore.com/42565/commercial-patio-heaters.html"
          },
          {
            "id": "",
            "name": "Banquet Chairs",
            "url": "https://www.webstaurantstore.com/42535/banquet-chairs-and-stackable-chairs.html"
          },
          {
            "id": "",
            "name": "Restaurant Booths",
            "url": "https://www.webstaurantstore.com/42537/restaurant-booths.html"
          },
          {
            "id": "",
            "name": "Outdoor Table Umbrellas and Bases",
            "url": "https://www.webstaurantstore.com/42563/outdoor-table-umbrellas-and-bases.html"
          },
          {
            "id": "",
            "name": "High Chairs",
            "url": "https://www.webstaurantstore.com/45523/restaurant-high-chairs.html"
          },
          {
            "id": "",
            "name": "Filing Cabinets",
            "url": "https://www.webstaurantstore.com/52235/filing-cabinets.html"
          },
          {
            "id": "",
            "name": "Seminar Tables",
            "url": "https://www.webstaurantstore.com/42555/seminar-tables.html"
          },
          {
            "id": "",
            "name": "Lobby, Reception, and Lounge Seating",
            "url": "https://www.webstaurantstore.com/52493/lobby-reception-and-lounge-seating.html"
          },
          {
            "id": "",
            "name": "Office Chairs",
            "url": "https://www.webstaurantstore.com/49587/office-chairs.html"
          },
          {
            "id": "",
            "name": "Canopies and Canopy Accessories",
            "url": "https://www.webstaurantstore.com/54605/canopies-and-canopy-accessories.html"
          },
          {
            "id": "",
            "name": "Desks and Desk Bases",
            "url": "https://www.webstaurantstore.com/51211/desks-and-desk-bases.html"
          },
          {
            "id": "",
            "name": "Table Carts, Trucks, and Dollies",
            "url": "https://www.webstaurantstore.com/42557/table-carts-trucks-and-dollies.html"
          },
          {
            "id": "",
            "name": "Retail Shelving and Displays",
            "url": "https://www.webstaurantstore.com/63855/retail-shelving.html"
          },
          {
            "id": "",
            "name": "Commercial Lighting",
            "url": "https://www.webstaurantstore.com/67909/commercial-lighting.html"
          }
        ]
      },
      {
        "id": 3415,
        "name": "Storage & Transport",
        "url": "https://www.webstaurantstore.com/restaurant-storage-transport.html",
        "subcategories": [
          {
            "id": "",
            "name": "Sheet Pan Racks",
            "url": "https://www.webstaurantstore.com/45131/sheet-pan-racks.html"
          },
          {
            "id": "",
            "name": "Food Pan Carriers",
            "url": "https://www.webstaurantstore.com/3521/insulated-heated-food-pan-carriers.html"
          },
          {
            "id": "",
            "name": "Plastic Utility Carts and Bus Carts",
            "url": "https://www.webstaurantstore.com/25985/plastic-bussing-carts-and-transport-carts.html"
          },
          {
            "id": "",
            "name": "Glass Racks",
            "url": "https://www.webstaurantstore.com/39727/glass-racks-cup-racks-and-extenders.html"
          },
          {
            "id": "",
            "name": "Dunnage Racks",
            "url": "https://www.webstaurantstore.com/14877/dunnage-racks.html"
          },
          {
            "id": "",
            "name": "Hand Trucks",
            "url": "https://www.webstaurantstore.com/24885/hand-trucks.html"
          },
          {
            "id": "",
            "name": "Platform Trucks",
            "url": "https://www.webstaurantstore.com/24883/platform-trucks.html"
          },
          {
            "id": "",
            "name": "Dish and Flatware Racks",
            "url": "https://www.webstaurantstore.com/4205/dish-and-flatware-racks.html"
          },
          {
            "id": "",
            "name": "Outdoor Storage",
            "url": "https://www.webstaurantstore.com/54109/outdoor-storage.html"
          },
          {
            "id": "",
            "name": "Stock and Order Picking Carts",
            "url": "https://www.webstaurantstore.com/50831/stock-and-order-picking-carts.html"
          },
          {
            "id": "",
            "name": "Workbenches",
            "url": "https://www.webstaurantstore.com/65049/industrial-workbenches.html"
          },
          {
            "id": "",
            "name": "Metal Utility Carts",
            "url": "https://www.webstaurantstore.com/14369/metal-bussing-utility-transport-carts.html"
          },
          {
            "id": "",
            "name": "Trash Can and Recycling Dollies",
            "url": "https://www.webstaurantstore.com/24889/trash-can-dollies-and-recycling-dollies.html"
          },
          {
            "id": "",
            "name": "Cutlery & Flatware Holders",
            "url": "https://www.webstaurantstore.com/4227/flatware-holders-and-flatware-organizers.html"
          },
          {
            "id": "",
            "name": "Bakery Racks and Dollies",
            "url": "https://www.webstaurantstore.com/55389/bakery-racks-and-dollies.html"
          },
          {
            "id": "",
            "name": "Storage Bins",
            "url": "https://www.webstaurantstore.com/65879/industrial-storage-bins.html"
          },
          {
            "id": "",
            "name": "Bun Pan Rack Covers",
            "url": "https://www.webstaurantstore.com/16941/bun-pan-rack-covers.html"
          },
          {
            "id": "",
            "name": "Mobile Ice Bins",
            "url": "https://www.webstaurantstore.com/3511/mobile-ice-bins.html"
          },
          {
            "id": "",
            "name": "Bus Tubs and Bus Boxes",
            "url": "https://www.webstaurantstore.com/3425/bus-tubs-and-bus-boxes.html"
          },
          {
            "id": "",
            "name": "Gondola Shelving",
            "url": "https://www.webstaurantstore.com/68097/gondola-shelving.html"
          },
          {
            "id": "",
            "name": "Bun Pan Trucks & Dollies",
            "url": "https://www.webstaurantstore.com/45119/bun-pan-trucks-dollies.html"
          },
          {
            "id": "",
            "name": "Can Racks",
            "url": "https://www.webstaurantstore.com/24851/can-racks.html"
          },
          {
            "id": "",
            "name": "Boltless Shelving",
            "url": "https://www.webstaurantstore.com/64573/boltless-shelving.html"
          },
          {
            "id": "",
            "name": "Lockers",
            "url": "https://www.webstaurantstore.com/21921/lockers.html"
          },
          {
            "id": "",
            "name": "Ice Transport Buckets",
            "url": "https://www.webstaurantstore.com/3509/ice-transport-buckets-and-accessories.html"
          }
        ]
      },
      {
        "id": 875,
        "name": "Janitorial",
        "url": "https://www.webstaurantstore.com/restaurant-janitorial-supplies.html",
        "subcategories": [
          {
            "id": "",
            "name": "Hand Soap and Sanitizer",
            "url": "https://www.webstaurantstore.com/48577/hand-soap-and-sanitizer.html"
          },
          {
            "id": "",
            "name": "Floor Care Supplies",
            "url": "https://www.webstaurantstore.com/48563/floor-care-supplies.html"
          },
          {
            "id": "",
            "name": "Commercial Floor Mats",
            "url": "https://www.webstaurantstore.com/48581/commercial-floor-mats.html"
          },
          {
            "id": "",
            "name": "Anti-Fatigue Kitchen Mats",
            "url": "https://www.webstaurantstore.com/885/anti-fatigue-floor-mats.html"
          },
          {
            "id": "",
            "name": "Vacuum Cleaners",
            "url": "https://www.webstaurantstore.com/1241/vacuum-cleaners.html"
          },
          {
            "id": "",
            "name": "Traffic Doors",
            "url": "https://www.webstaurantstore.com/48587/traffic-doors.html"
          },
          {
            "id": "",
            "name": "Fire Extinguishers",
            "url": "https://www.webstaurantstore.com/973/fire-extinguishers.html"
          },
          {
            "id": "",
            "name": "Carpet Shampooers, Extractors, & Steamers",
            "url": "https://www.webstaurantstore.com/46043/carpet-shampooers-extraction-machines.html"
          },
          {
            "id": "",
            "name": "Commercial Paper Towel Dispensers",
            "url": "https://www.webstaurantstore.com/46165/commercial-paper-towel-dispensers.html"
          },
          {
            "id": "",
            "name": "Flying Insect Control Products",
            "url": "https://www.webstaurantstore.com/1091/flying-insect-control-products-and-bug-zappers.html"
          },
          {
            "id": "",
            "name": "Baby Changing Tables",
            "url": "https://www.webstaurantstore.com/889/baby-changing-stations-tables.html"
          },
          {
            "id": "",
            "name": "Wet Mop Buckets / Wringers",
            "url": "https://www.webstaurantstore.com/1059/wet-mop-buckets-wringers.html"
          },
          {
            "id": "",
            "name": "Electric Hand Dryers",
            "url": "https://www.webstaurantstore.com/1009/electric-hand-dryers.html"
          },
          {
            "id": "",
            "name": "All Purpose Cleaners",
            "url": "https://www.webstaurantstore.com/1019/all-purpose-cleaning-chemicals.html"
          },
          {
            "id": "",
            "name": "Commercial Brooms",
            "url": "https://www.webstaurantstore.com/909/lobby-brooms-and-warehouse-brooms.html"
          },
          {
            "id": "",
            "name": "Wet Mops",
            "url": "https://www.webstaurantstore.com/1061/wet-mops.html"
          },
          {
            "id": "",
            "name": "Chemical Portion Packs & Tabs",
            "url": "https://www.webstaurantstore.com/48901/ready-to-use-chemical-portion-packs-tabs.html"
          },
          {
            "id": "",
            "name": "Oven & Grill Cleaner",
            "url": "https://www.webstaurantstore.com/1001/oven-cleaner-grill-cleaner.html"
          },
          {
            "id": "",
            "name": "Toilet Paper Dispensers",
            "url": "https://www.webstaurantstore.com/1127/commercial-toilet-paper-dispensers-and-holders.html"
          },
          {
            "id": "",
            "name": "Scrubbers and Sponges",
            "url": "https://www.webstaurantstore.com/1175/scrubbers-sponges-and-wipers.html"
          },
          {
            "id": "",
            "name": "Air Curtains",
            "url": "https://www.webstaurantstore.com/881/air-curtains.html"
          },
          {
            "id": "",
            "name": "Plastic Utility Trash Cans",
            "url": "https://www.webstaurantstore.com/69145/plastic-utility-trash-cans.html"
          }
        ]
      },
      {
        "id": 57683,
        "name": "Industrial",
        "url": "https://www.webstaurantstore.com/industrial-supplies.html",
        "subcategories": [
          {
            "id": "",
            "name": "Hand Trucks",
            "url": "https://www.webstaurantstore.com/24885/hand-trucks.html"
          },
          {
            "id": "",
            "name": "Pallet Trucks",
            "url": "https://www.webstaurantstore.com/58099/pallet-trucks.html"
          },
          {
            "id": "",
            "name": "Loading Dock Equipment",
            "url": "https://www.webstaurantstore.com/58101/loading-dock-equipment.html"
          },
          {
            "id": "",
            "name": "Industrial Carts",
            "url": "https://www.webstaurantstore.com/37745/industrial-carts-and-maintenance-carts.html"
          },
          {
            "id": "",
            "name": "Trash Carts with Wheels",
            "url": "https://www.webstaurantstore.com/24887/wheeled-trash-cans-and-tilt-trucks.html"
          },
          {
            "id": "",
            "name": "Fire Extinguishers",
            "url": "https://www.webstaurantstore.com/973/fire-extinguishers.html"
          },
          {
            "id": "",
            "name": "Industrial Vacuums",
            "url": "https://www.webstaurantstore.com/65217/industrial-vacuums.html"
          },
          {
            "id": "",
            "name": "Packing Tables",
            "url": "https://www.webstaurantstore.com/42667/packing-tables.html"
          },
          {
            "id": "",
            "name": "Pallets",
            "url": "https://www.webstaurantstore.com/58941/pallets.html"
          },
          {
            "id": "",
            "name": "PPE Equipment",
            "url": "https://www.webstaurantstore.com/58759/ppe-equipment.html"
          },
          {
            "id": "",
            "name": "Industrial Fans",
            "url": "https://www.webstaurantstore.com/59513/industrial-fans.html"
          },
          {
            "id": "",
            "name": "Commercial Generators",
            "url": "https://www.webstaurantstore.com/57519/commercial-generators.html"
          },
          {
            "id": "",
            "name": "Industrial Shelving",
            "url": "https://www.webstaurantstore.com/57761/industrial-shelving-and-storage.html"
          },
          {
            "id": "",
            "name": "Industrial Workbenches",
            "url": "https://www.webstaurantstore.com/65049/industrial-workbenches.html"
          },
          {
            "id": "",
            "name": "Industrial Hoists and Cranes",
            "url": "https://www.webstaurantstore.com/64569/industrial-hoists-and-cranes.html"
          },
          {
            "id": "",
            "name": "Material Handling Equipment",
            "url": "https://www.webstaurantstore.com/65239/material-handling-equipment.html"
          },
          {
            "id": "",
            "name": "Drum Handling Equipment",
            "url": "https://www.webstaurantstore.com/58095/drum-handling-equipment.html"
          },
          {
            "id": "",
            "name": "Hot / Cold Packs",
            "url": "https://www.webstaurantstore.com/49203/hot-cold-packs.html"
          },
          {
            "id": "",
            "name": "Insulated Shipping Boxes and Packaging",
            "url": "https://www.webstaurantstore.com/44429/insulated-shipping-boxes.html"
          },
          {
            "id": "",
            "name": "Stretch Wrap, Stretch Film, and Pallet Wrap",
            "url": "https://www.webstaurantstore.com/3577/stretch-wrap-stretch-film-and-pallet-wrap.html"
          },
          {
            "id": "",
            "name": "Mini Splits",
            "url": "https://www.webstaurantstore.com/64719/mini-splits.html"
          },
          {
            "id": "",
            "name": "Mailing & Shipping Labels",
            "url": "https://www.webstaurantstore.com/64677/mailing-shipping-labels.html"
          },
          {
            "id": "",
            "name": "Maintenance Tools",
            "url": "https://www.webstaurantstore.com/56483/maintenance-tools.html"
          }
        ]
      },
      {
        "id": 53981,
        "name": "Business Type",
        "url": "https://www.webstaurantstore.com/categories.html",
        "subcategories": [
          {
            "id": "",
            "name": "Bakery Supplies",
            "url": "https://www.webstaurantstore.com/bakery-supplies.html"
          },
          {
            "id": "",
            "name": "Food Truck Supplies",
            "url": "https://www.webstaurantstore.com/food-truck-supplies.html"
          },
          {
            "id": "",
            "name": "Hotel Supplies",
            "url": "https://www.webstaurantstore.com/hotel-supplies.html"
          },
          {
            "id": "",
            "name": "Bar Supplies",
            "url": "https://www.webstaurantstore.com/bar-supplies.html"
          },
          {
            "id": "",
            "name": "Coffee Shop Supplies",
            "url": "https://www.webstaurantstore.com/coffee-shop-supplies.html"
          },
          {
            "id": "",
            "name": "Catering Supplies",
            "url": "https://www.webstaurantstore.com/catering-supplies.html"
          },
          {
            "id": "",
            "name": "Chef Supplies",
            "url": "https://www.webstaurantstore.com/chef-supplies.html"
          },
          {
            "id": "",
            "name": "Butcher Shop Supplies",
            "url": "https://www.webstaurantstore.com/butcher-shop-supplies.html"
          },
          {
            "id": "",
            "name": "Pizzeria Supplies",
            "url": "https://www.webstaurantstore.com/pizza-supplies.html"
          },
          {
            "id": "",
            "name": "Asian Restaurant Supplies",
            "url": "https://www.webstaurantstore.com/asian-restaurant-supplies.html"
          },
          {
            "id": "",
            "name": "Candy Making Supplies",
            "url": "https://www.webstaurantstore.com/candy-making-supplies.html"
          },
          {
            "id": "",
            "name": "Ice Cream Shop Supplies",
            "url": "https://www.webstaurantstore.com/ice-cream-shop-supplies.html"
          },
          {
            "id": "",
            "name": "Buffet & Serving Line Supplies",
            "url": "https://www.webstaurantstore.com/buffet-supplies.html"
          },
          {
            "id": "",
            "name": "Grocery Store Supplies",
            "url": "https://www.webstaurantstore.com/grocery-deli-supplies.html"
          },
          {
            "id": "",
            "name": "Concession Supplies",
            "url": "https://www.webstaurantstore.com/restaurant-concession-supplies.html"
          },
          {
            "id": "",
            "name": "Mexican Restaurant Supplies",
            "url": "https://www.webstaurantstore.com/mexican-restaurant-supplies.html"
          },
          {
            "id": "",
            "name": "Donut Shop Equipment",
            "url": "https://www.webstaurantstore.com/59257/donut-shop-equipment.html"
          },
          {
            "id": "",
            "name": "Day Care Supplies",
            "url": "https://www.webstaurantstore.com/day-care-supplies.html"
          },
          {
            "id": "",
            "name": "Sandwich Shop",
            "url": "https://www.webstaurantstore.com/sandwich-shop-supplies.html"
          },
          {
            "id": "",
            "name": "Retail Store Supplies",
            "url": "https://www.webstaurantstore.com/66409/retail-store-supplies.html"
          },
          {
            "id": "",
            "name": "Brewery Equipment and Supplies",
            "url": "https://www.webstaurantstore.com/59927/brewery-equipment.html"
          },
          {
            "id": "",
            "name": "Vending Machine Supplies",
            "url": "https://www.webstaurantstore.com/65095/vending-machine-supplies.html"
          },
          {
            "id": "",
            "name": "Farmer's Market Supplies",
            "url": "https://www.webstaurantstore.com/57103/farmers-market-supplies.html"
          },
          {
            "id": "",
            "name": "Banquet Supplies",
            "url": "https://www.webstaurantstore.com/59601/banquet-supplies.html"
          }
        ]
      }
    ]
  }
}
                    
		''')

	def __init__(self, options=None):
		super().__init__(firefox=True)
		# There are only 2 navigation categories we want to process and we only want to process 1 sub category
		self.options['test_categories'] = 8
		self.PRODUCT_DATA_SPEC = self.BASE_PRODUCT_DATA_SPEC.copy()
		for spec in self.DISTRIBUTOR_PRODUCT_DATA_SPEC:
			self.PRODUCT_DATA_SPEC[spec] = ''
		print(self.PRODUCT_DATA_SPEC)

	def bypass_cookie_consent(self, url):
		print("bypass_cookie_consent()")
		# try:
		# 	self.driver.get(url)
		# 	time.sleep(20)
		# 	modal = self.wait.until(
		# 		EC.presence_of_element_located((By.CSS_SELECTOR, '.cookie-notice'))
		# 	)
		# 	select = modal.find_element(By.CSS_SELECTOR, '.cookie-accept')
		# 	select.click()
		# 	print("Bypassed cookie consent")
		# except Exception as e:
		# 	print(f"Error: {e}")

	def scraping_setup(self):
		"""Scrape products from the website"""
		print("scraping_setup()")
		url = "https://www.wine-searcher.com/"
		self.bypass_cookie_consent(url)
		time.sleep(10)
		return

	@staticmethod
	def extract_unique_id_from_url(url):
		"""
		Get a unique identifier from the url.
		Standard version example https://website.com/4345353
		"""
		try:
			# get the last part of the url and remove any querystring parameters
			sku = url.split('/')[-1].split('?')[0]
			sku = sku.replace(".html", "")
		except Exception as e:
			print(f"⛔️⛔️⛔️Error saving URLs to CSV: {e}")
			sku = ''
		return sku

	# ************************************************************************
	# Utility Functions
	# ************************************************************************


	# ************************************************************************
	# 	Product Scraping Functions
	# ************************************************************************

	def get_product_data(self, data, row_spec):
		print("processing product data from response...")
		print(data)
		if data:
			try:
				row_spec['sku'] = ''
				row_spec["product_id"] = data.get("product_id", "")
				row_spec = self.parse_product_schema(data, row_spec)
				row_spec = self.get_price(data, row_spec)
			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing product data: {e}")

		print("processing get_product_data Complete...")
		return row_spec
	
	def get_more_extra_data(self, row_spec):
		print("processing product extra data from response...")
		data_2 = json.loads(row_spec['extra_data_2'])
		data_3 = json.loads(row_spec['extra_data_3'])
		if data_2:
			try:
				row_spec = self.parse_product_schema(data_2, row_spec)
				row_spec = self.get_price(data_2, row_spec)
			except Exception as e:
				print(f" ⛔️⛔️⛔️Error processing more product data: {e}")
			if data_2.get('@type') == 'ProductGroup' and 'hasVariant' in data_2:
				# Find the main product variant (the one that matches our URL)
				current_url = row_spec.get('content_url', '')
				for variant in data_2['hasVariant']:
					if isinstance(variant, dict) and variant.get('@type') == 'Product' and variant.get(
							'url') == current_url:
						# Found our product in the variants
						row_spec = self.parse_product_schema(variant, row_spec)
						row_spec = self.get_price(variant, row_spec)
						break

		print(row_spec['brand'])
		brand = row_spec['brand']
		if brand:
			row_spec['brand'] = row_spec['brand'].get('name', '')

		row_spec['id'] = self.extract_unique_id_from_url(row_spec['content_url'])

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
		"""Parse the navigation menu to extract categories and their subcategories."""
		print(f"{self.__class__}->build_categories_list()")
		url = "https://www.webstaurantstore.com/"
		self.driver.get(url)

		try:
			# Find all script tags
			script_elements = self.driver.find_elements(By.TAG_NAME, 'script')
			nav_data = None

			# Search for script containing navDataItems
			for script in script_elements:
				print("searching scripts")
				script_type = script.get_attribute('type')
				if script_type == 'application/json':
					print("found JSON")
					try:
						script_content = script.get_attribute('innerHTML').replace("<!--", "").replace("-->", "")
						print(script_content)
						if script_content and 'navDataItems' in script_content:
							json_data = json.loads(script_content)

							if 'navDataItems' in json_data:
								nav_data = json_data
								print("Found navigation data")
								break
					except json.JSONDecodeError:
						continue

			if not nav_data:
				print("No navigation data found in script tags")
				return json.dumps({
					'data': {
						'categories': [],
						'error': 'No navigation data found'
					}
				})

			# Process the navigation data
			all_categories = {
				'data': {
					'categories': []
				}
			}

			# Process each category in navDataItems
			for item in nav_data.get('navDataItems', []):
				link = self.BASE_URL + item.get('link', '')
				category = {
					'id': item.get('id', ''),
					'name': item.get('displayName', ''),
					'url': link,
					'subcategories': []
				}

				# Add subcategories from subResources
				for sub_item in item.get('subResources', []):
					link = self.BASE_URL + sub_item.get('link', '')
					subcategory = {
						'id': sub_item.get('id', ''),
						'name': sub_item.get('name', ''),
						'url': link
					}
					category['subcategories'].append(subcategory)

				all_categories['data']['categories'].append(category)

			return json.dumps(all_categories, indent=2)

		except Exception as e:
			print(f"Error processing navigation data: {e}")
			return json.dumps({
				'data': {
					'categories': [],
					'error': str(e)
				}
			})
		
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

	def build_products_list(self):
		"""Scrape products from the website"""
		html = ""
		all_urls = []
		process_urls = []

		# Use the options with fallback to module-level variables
		max_products = self.options.get('max_products', self.MAX_API_PRODUCTS)
		category_to_process = self.options.get('category_to_process', 0)
		chosen_category = int(self.options.get('chosen_category', 0))
		test_categories = self.options.get('test_categories', 100)
		category_count = 0
		categories = []
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
			subcategory_name = ''
			category_name = category['name']
			print(f"category: {category_name}")
			if 'subcategories' in category and category['subcategories']:
				sub_categories = category['subcategories']

				sub_category_found_count = len(sub_categories)
				print(f"Found {sub_category_found_count} sub categories to process...")
				for subcategory in sub_categories:
					subcategory_name = subcategory['name']
					print(f"Sub category: {subcategory_name}")
					url = self.get_category_url(subcategory)
					print(f"Subcategory Url: {url}")
					product_urls = self.process(url)
					process_urls = self.build_products_list_step_2(product_urls, category_name, subcategory_name)
			else:
				url = self.get_category_url(category)
				product_urls = self.process(url)
				process_urls = self.build_products_list_step_2(product_urls, category_name, subcategory_name)

			all_urls.extend(process_urls)

		html += f"<h2>Total products found: {total_products}</h2>"

		print(f"Total products found: {len(all_urls)}")
		return html

	def build_products_list_step_2(self, urls, category_name, subcategory_name):
		"""Visit deepest URLs in CATEGORIES and extract product URLs from children data."""
		print(f"{self.__class__}->build_products_list_step_2()")
		print(urls)
		category_urls = set()  # Using a set to avoid duplicates

		# for url in urls:
		product_found = False
		for url in urls:
			try:
				print(f"Visiting step 2: {url}")
				self.driver.get(url)

				# Find script tags that might contain the JSON data
				script_elements = self.driver.find_elements(By.TAG_NAME, 'script')

				for script in script_elements:
					# print(f"Script: {script}")
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
												category_urls.add(full_url)
												# print(f"Found product URL: {full_url}")
												product_found = True

								except json.JSONDecodeError:
									continue
						except Exception as e:
							print(f"Error processing script: {str(e)}")
							continue
				if not product_found:
					category_urls.add(url)

			except Exception as e:
				print(f"Error processing URL {url}: {str(e)}")
				continue
		all_urls = []

		for url in category_urls:
			print(f"Part 2 Url: {url}")
			detail_urls, html = self.get_category_page(url, category_name, subcategory_name, '')
			all_urls.extend(detail_urls)

		return list(category_urls)
	# Step Two: Get links to products
	def build_products_listx(self):
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

			url = self.get_category_url(category)
			print(f"Url: {url}")
			detail_urls, html = self.get_category_page(url, category_name, '', '')
			all_urls.extend(detail_urls)

		# html_table_to_csv(html_table)
		html += f"<h2>Total products found: {total_products}</h2>"

		print(f"Total products found: {len(all_urls)}")
		return html

	def _process_item_list(self, item_list):
		"""Process the ItemList and return formatted categories."""
		all_categories = {
			'data': {
				'categories': []
			}
		}

		for i, item in enumerate(item_list.get('itemListElement', []), 1):
			try:
				category_name = item.get('name', '')
				category_url = item.get('url', '')

				# Skip if no meaningful name
				if not category_name or category_name.lower() in ['all wines', 'all spirits', '']:
					continue

				category_data = {
					'name': category_name,
					'id': i,
					'url': category_url,
					'subcategories': []
				}

				all_categories['data']['categories'].append(category_data)

			except Exception as e:
				print(f"Error processing category {item.get('name', 'unknown')}: {e}")
				continue

		return json.dumps(all_categories, indent=2)

	def get_product_details(self, url, row_spec=None):
		"""
		Product detail pages are rendered server-side. Page must be manually scraped.
		Additional packages also need to be pulled or visited from the dropdown
		To get the product detail page, visit the product detail page and then pull the additional packages
		"""
		#  Wait for the product name element on the product page detail page
		if not row_spec: row_spec = self.PRODUCT_DATA_SPEC.copy()
		print(f"{self.__class__}->get_product_details()")

		print(f"Loading page: {url}")
		self.driver.get(url)

		data = ''
		# sku = row_spec['sku']
		row_spec['content_url'] = url
		row_spec['id'] = row_spec['content_url']

		print(f"Loading page...{url}")
		try:
			data, data_2 = self.get_product_detail_from_schema_in_html(row_spec=row_spec, target="application/ld+json")
			data_3 = self.get_product_detail_2_from_json_in_html(url, row_spec=row_spec, target="script[data-hypernova-key='ProductDetails']")
			row_spec["extra_data_1"] = json.dumps(data)
			row_spec["extra_data_2"] = json.dumps(data_2)
			row_spec["extra_data_3"] = json.dumps(data_3)

			row_spec = self.get_product_data(data, row_spec)
			row_spec = self.get_more_extra_data(row_spec)
			# row_spec = self.get_product_data(data, row_spec)
		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing get_product_details: {type(e)}")
			raise
		return row_spec

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
			if script_element:
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
	def get_category_page(self, url, category_name, sub_category_name, sub_sub_category_name):
		print("get_category_page()")
		main_window = self.driver.current_window_handle
		html = ''
		total_products = 0
		all_urls = []
		detail_urls = []
		page_count = 0
		try:
			self.driver.get(url)

			# Update URL from the redirect
			url = self.driver.current_url
			base_url = url
			print(f"Current URl: {self.driver.current_url}")

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
						html_line, detail_urls = self.get_products_from_json_in_html()
					products_found_count = len(detail_urls)
					all_urls.extend(detail_urls)
					html += f"<div>Found {products_found_count} products for category {category_name} page {page_count}</div>"
					print(f"Found {products_found_count} products for category {category_name} page {page_count}")
					total_products += products_found_count
					if products_found_count > 0 and products_found_count % 100 == 0:
						url = base_url + f"?page={page_count + 1}"
						self.driver.get(url)
					else:
						next_page = False
				# self.save_urls_to_csv(detail_urls, category_name, sub_category_name, sub_sub_category_name)

				except Exception as e:
					print(f"****************** ⛔️⛔️⛔️ Error getting details: {e}")
					html += f"<div>Name: {sub_category_name} (Error getting details)</div>"

		except Exception as e:
			print(f"⛔️⛔️⛔️Error processing category: {e}")

		html += f"<h2>Total products found: {total_products}</h2>"
		print(f"Total Products {len(all_urls)}")

		# write all the urls to file
		self.save_urls_to_csv(all_urls, category_name, sub_category_name, sub_sub_category_name)
		# return results to results page
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
