import csv
import glob
import importlib
import inspect
import json
import os
import uuid
from importlib import import_module
from io import StringIO
from django.shortcuts import render, redirect
from django.contrib import messages

from scrapers.city.empire_metro import EmpireMetroScraper
from .bigcommerce.meatsbylinz import MeatsByLinzScraper
from .bigcommerce.terraspice import TerraSpiceScraper
from .city._template import HiveTemplateScraper
from .city.archerliquor import ArcherLiquorScraper
from .city.cellar53 import Cellar53Scraper
from .city.empire_north import EmpireNorthScraper
from .city.maverick import MaverickBeverageScraper
from .city.morrellwine import MorrellWineScraper
from .city.sandr import SandRScraper
from .city.southillswine import ShortHillsWineScraper
from .city.twinliquors import TwinLiquorsScraper
from .misc.sysco import SyscoScraper
from .misc.webstaurant import WebstaurantScraper
from .misc.winesearcher import WineSearcherScraper
from .pepper.brotherfoodservice import BrothersFoodServiceScraper
from .pepper.cibo import CiboScraper
from .pepper.graves import GravesFoodsScraper
from .pepper.kuno import KunoScraper
from .pepper.piazza_produce import PiazzaProduceScraper
from .pepper.primesource import PrimeSourceScraper
from .pepper.sirnasonsproduce import SirnaSonsProduceScraper
from .shopify.allenbrothers import AllenBrothersScraper
from .shopify.alma import AlmaScraper
from .shopify.fultonfish import FultonFishScraper
from .thread_manager import thread_manager

import pandas as pd
import requests
from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.cache import cache
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from scrapers.cut.birite import BiRiteScraper
from scrapers.cut.cheese_importers import CheeseImportersScraper
from scrapers.cut.creamco import CreamCoScraper
from scrapers.cut.primizie_ny import PrimizieScraper
from scrapers.cut.sardilli import SardilliScraper
from scrapers.misc.breakthru import BreakthruScraper
from scrapers.misc.chefswarehouse import ChefWarehouseScraper
from scrapers.misc.sg import SouthernGlazierScraper
from scrapers.misc.usfoods import USFoodsScraper
from scrapers.shopify.melissas import MelissasScraper
from .pepper.getfreshproduce import GetFreshProduceScraper
from .pepper.expressfoods import ExpressFoodsScraper
from .csvProcessor import CSVProcessor
from .cut.ab import ABScraper
# Import all scraper classes
from .cut.acme_steak import AcmeSteakScraper
from .cut.all_fresh_seafood import AllFreshSeafoodScraper
from .cut.all_star_specialties import AllStarSpecialtiesScraper
from .cut.alpeake import AlpeakeScraper
from .cut.apito import ApitoScraper
from .cut.carmela import CarmelaScraper
from .cut.caruso import CarusoScraper
from .cut.chefs_kitchen import ChefsKitchenScraper
from .cut.christ_panos import ChristPanosScraper
from .cut.citylinefoods import CityLineFoodsScraper
from .cut.cooks import CooksCompanyScraper
from .cut.crookbros import CrookBrosScraper
from .cut.cusumanoandsons import CusumanoAndSonsScraper
from .cut.derstines import DerstinesScraper
from .cut.dicarlo import DiCarloScraper
from .cut.driscoll import DriscollScraper
from .cut.dwcspecialties import DWCSpecialtiesScraper
from .cut.food_paper import FoodAndPaperScraper
from .cut.food_pro import FoodProScraper
from .cut.fourstarmeat import FourStarMeatScraper
from .cut.hearty import HeartyScraper
from .cut.hooktofork import HookToForkScraper
from .cut.indianhead import IndianheadScraper
from .cut.jordanpaige import JordanPaigeScraper
from .cut.manson import MansonScraper
from .cut.maple_vale import MapleValeScraper
from .cut.market_406 import Market406Scraper
from .cut.misterproduce import MisterProduceScraper
from .cut.pacificprovisions import PacificProvisionsScraper
from .cut.prdeli import PRDeliScraper
from .cut.primesourcefoods import PrimeSourceFoodsScraper
from .cut.primizie_noca import PrimizieNoCaScraper
from .cut.rarefoods import RareFoodsScraper
from .cut.realityfoods import RealityFoodsScraper
from .cut.safradistribution import SafraDistributionScraper
from .cut.sandw import SandWScraper
from .cut.savalfoodservice import SavalFoodserviceScraper
from .cut.sierra_meat import SierraMeatScraper
from .cut.socomeatco import SoCoMeatCoScraper
from .cut.southwest_traders import SouthwestTradersScraper
from .cut.sunbelt import SunbeltScraper
from .cut.sutters import SuttersScraper
from .cut.thefishguys import TheFishGuysScraper
from .cut.tolteca import ToltecaScraper
from .cut.totalfoods import TotalFoodsScraper
from .cut.valleygold import ValleyGoldScraper
from .cut.vitco_foods import VitcoScraper
from .cut.wagner import WagnerScraper
from .cut.whatchefswant_central import WhatChefsWantCentralScraper
from .cut.whatchefswant_rockies import WhatChefsWantRockiesScraper
from .cut.whatchefswant_south import WhatChefsWantSouthScraper
from .cut.woolcofoods import WoolcoFoodsScraper
from .misc.cheneybrothers import CheneyBrothersScraper
from .misc.imperialdade import ImperialDadeScraper
from .other.application import ApplicationScraper
from .pepper.acc_endico import AceEndicoScraper
from .pepper.accdistributors import AccDistributorsScraper
from .pepper.city_produce import CityProduceScraper
from .pepper.dennis_foodservice import DennisFoodserviceScraper
from .pepper.farmart import FarmArtScraper
from .pepper.flanagan import FlanaganFoodserviceScraper
from .pepper.northeastspecialty import NortheastSpecialtyScraper
from .pepper.palmerfoods import PalmerFoodsScraper
from .pepper.perrone import PerroneScraper
from .pepper.seattlefish import SeattleFishScraper
from .pepper.testa import TestaProduceScraper
from .pepper.schenck import SchenckFoodsScraper
from .pepper.earthlygourmet import EarthlyGourmetScraper
from .pepper.euclidfish import EuclidFishScraper
from .scraper import Scraper
from .shopify.bittersbottles import BittersBottlesScraper
from .shopify.fourstarseafood import FourStarSeafoodScraper
from .shopify.pacificgourmet import PacificGourmetScraper
from .shopify.savorygourmet import SavoryGourmetScraper

# Import other scrapers here...

# List of all scraper classes
SCRAPER_CLASSES = [
]

# Get the directory containing the scrapers
scrapers_cut_dir = os.path.join(os.path.dirname(__file__), 'cut')
scrapers_misc_dir = os.path.join(os.path.dirname(__file__), 'misc')
scrapers_shop_dir = os.path.join(os.path.dirname(__file__), 'shopify')
scrapers_pepper_dir = os.path.join(os.path.dirname(__file__), 'pepper')
scrapers_city_dir = os.path.join(os.path.dirname(__file__), 'city')
bigcommerce_city_dir = os.path.join(os.path.dirname(__file__), 'bigcommerce')

# Import all Python files in the cut directory
for filename in os.listdir(scrapers_cut_dir):
    if filename.endswith('.py') and not filename.startswith('_') and filename != 'dry.py' and filename != 'dry_market.py':
        module_name = filename[:-3]  # Remove .py extension
        try:
            module = importlib.import_module(f'scrapers.cut.{module_name}')
            # Get all classes in the module that end with 'Scraper'
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if name.endswith('Scraper') and hasattr(obj, 'VENDOR_NAME') and hasattr(obj, 'DEFAULT_DIRECTORY') and name != 'CutScraper' and name != 'Scraper' and name != 'DryMarketScraper':
                    SCRAPER_CLASSES.append(obj)
        except Exception as e:
            print(f"Error importing {module_name}: {e}")
for filename in os.listdir(scrapers_misc_dir):
    if filename.endswith('.py') and not filename.startswith('_'):
        module_name = filename[:-3]  # Remove .py extension
        try:
            module = importlib.import_module(f'scrapers.misc.{module_name}')
            # Get all classes in the module that end with 'Scraper'
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if name.endswith('Scraper') and hasattr(obj, 'VENDOR_NAME') and hasattr(obj, 'DEFAULT_DIRECTORY') and name != 'CutScraper' and name != 'Scraper' and name != 'DryMarketScraper':
                    SCRAPER_CLASSES.append(obj)
        except Exception as e:
            print(f"Error importing {module_name}: {e}")
for filename in os.listdir(scrapers_shop_dir):
    # print(filename)
    if filename.endswith('.py') and not filename.startswith('_') and filename != 'shopify.py':
        module_name = filename[:-3]
        try:
            module = importlib.import_module(f'scrapers.shopify.{module_name}')
            # Get all classes in the module that end with 'Scraper'
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if name.endswith('Scraper') and hasattr(obj, 'VENDOR_NAME') and hasattr(obj, 'DEFAULT_DIRECTORY') and name != 'ShopifyScraper' and name != 'Scraper':
                    # print(name)
                    SCRAPER_CLASSES.append(obj)
        except Exception as e:
            print(f"Error importing {module_name}: {e}")
for filename in os.listdir(scrapers_pepper_dir):
    # print(filename)
    if filename.endswith('.py') and not filename.startswith('_') and filename != 'pepper.py':
        module_name = filename[:-3]
        try:
            module = importlib.import_module(f'scrapers.pepper.{module_name}')
            # Get all classes in the module that end with 'Scraper'
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if name.endswith('Scraper') and hasattr(obj, 'VENDOR_NAME') and hasattr(obj, 'DEFAULT_DIRECTORY') and name != 'PepperScraper' and name != 'Scraper':
                    # print(name)
                    SCRAPER_CLASSES.append(obj)
        except Exception as e:
            print(f"Error importing {module_name}: {e}")
for filename in os.listdir(scrapers_city_dir):
    # print(filename)
    if filename.endswith('.py') and not filename.startswith('_') and filename != 'hive.py':
        module_name = filename[:-3]
        try:
            module = importlib.import_module(f'scrapers.city.{module_name}')
            # Get all classes in the module that end with 'Scraper'
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if name.endswith('Scraper') and hasattr(obj, 'VENDOR_NAME') and hasattr(obj,
                                                                                        'DEFAULT_DIRECTORY') and name != 'HiveScraper' and name != 'Scraper':
                    # print(name)
                    SCRAPER_CLASSES.append(obj)
        except Exception as e:
            print(f"Error importing {module_name}: {e}")
for filename in os.listdir(bigcommerce_city_dir):
    print(filename)
    if filename.endswith('.py') and not filename.startswith('_') and filename != 'bigcommerce.py':
        module_name = filename[:-3]
        try:
            module = importlib.import_module(f'scrapers.bigcommerce.{module_name}')
            # Get all classes in the module that end with 'Scraper'
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if name.endswith('Scraper') and hasattr(obj, 'VENDOR_NAME') and hasattr(obj,
                                                                                        'DEFAULT_DIRECTORY') and name != 'BigCommerceScraper' and name != 'Scraper':
                    # print(name)
                    SCRAPER_CLASSES.append(obj)
        except Exception as e:
            print(f"Error importing {module_name}: {e}")
print(SCRAPER_CLASSES)


class ScrapeProductsPageView(TemplateView):
    template_name = "scrape_products/scrape_home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



# ****************************************************
# Common
# ****************************************************

def process_common_post(options, request, scraper):
    # Handle clean_datas option
    if options.get('clean_data'):
        clean_field = request.POST.get('clean_field', 'name')  # Default to 'name' if not specified
        file_type = request.POST.get('file_type', 'url')  # Default to 'url' if not specified

        # Determine which file to clean based on selection
        if file_type == 'data':
            input_file = os.path.join(options.get('home_directory', ''), options.get('data_output_file', ''))
        else:  # 'url' or default
            input_file = os.path.join(options.get('home_directory', ''), options.get('url_output_file', ''))

        success, message = scraper.clean_data_file(input_file=input_file, field=clean_field)
        if success:
            result = f"<div class='alert alert-success'>{message}</div>"
        else:
            result = f"<div class='alert alert-danger'>{message}</div>"
        return result

    # Run the scraper if not just cleaning URLs
    scraper.set_options(options)
    print(f"checking request {options}")
    # Check if this is an AJAX request for processing CSV or reprocessing a CSV
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and (
            options.get('process_csv') or options.get('reprocess_csv')):
        # Define the scraper function that will run in the background
        def run_scraper(module_name, class_name, options):
            print(f"🧵 Starting scraper in background()")
            try:
                # Import the scraper class dynamically
                module = import_module(module_name)
                ScraperClass = getattr(module, class_name)
                print(f"Imported scraper class: {ScraperClass}")

                # Create a new scraper instance in the background thread
                with ScraperClass() as scraper:
                    scraper.current_task_id = task_id
                    scraper.set_options(options)

                    # Run the scraper
                    print(f"Starting scraper with options: {options}")
                    scraper.run()

            except Exception as e:
                # Update progress with error
                print(f"Error running scraper: {e}")
                progress_data = {
                    'status': 'error',
                    'error': str(e),
                    'message': f'Error: {str(e)}',
                    'task_id': task_id
                }
                from django.core.cache import cache
                cache.set(f'product_processing_progress_{task_id}', progress_data, timeout=3600)

        # Prepare the scraper options
        scraper_options = {
            'home_directory': options.get('home_directory', ''),
            'csv_start_row': options.get('csv_start_row', 0),
            'test_products': options.get('test_products', 0),
            'url_output_file': options.get('url_output_file', ''),
            'data_output_file': options.get('data_output_file', ''),
            'process_csv': options.get('process_csv', ''),
            'reprocess_csv': options.get('reprocess_csv', ''),
            'attempts': options.get('attempts', 40)
        }

        # Get the module and class name for dynamic import
        scraper_module = scraper.__class__.__module__
        scraper_class = scraper.__class__.__name__

        # Generate a task ID
        task_id = str(uuid.uuid4())

        # Initialize progress data in cache
        initial_progress = {
            'status': 'starting',
            'message': 'Starting processing...',
            'current': 0,
            'total': 0,
            'current_sku': '',
            'processed_skus': [],
            'not_found_skus': []
        }
        cache.set(f'product_processing_progress_{task_id}', initial_progress, 3600)

        # Start the task in a background thread
        thread_manager.start_thread(
            target=run_scraper,
            task_id=task_id,
            args=(scraper_module, scraper_class, scraper_options),
            timeout=3600  # 1 hour timeout
        )

        print(f"Started background task with ID: {task_id}")
        return task_id

def update_common_options(post_data, current_options):
    # Update boolean flags
    current_options['get_categories'] = 'get_categories' in post_data
    current_options['scrape_products'] = 'scrape_products' in post_data
    current_options['process_csv'] = 'process_csv' in post_data
    current_options['reprocess_csv'] = 'reprocess_csv' in post_data
    current_options['process_extra'] = 'process_extra' in post_data
    current_options['search_requests'] = 'search_requests' in post_data
    current_options['dedupe_csv'] = 'dedupe_csv' in post_data
    current_options['format_csv'] = 'format_csv' in post_data
    current_options['scan_csv'] = 'scan_csv' in post_data
    current_options['format_csv'] = 'format_csv' in post_data
    current_options['count_csv'] = 'count_csv' in post_data

    current_options['test_products'] = int(post_data.get('test_products', current_options.get('test_products', 10)))
    current_options['test_categories'] = int(
        post_data.get('test_categories', current_options.get('test_categories', 10)))
    current_options['max_products'] = int(post_data.get('max_products', current_options.get('max_products', 500)))
    current_options['csv_start_row'] = int(post_data.get('start_row', current_options.get('csv_start_row', 0)))
    current_options['category_to_process'] = int(
        post_data.get('category_to_process', current_options.get('category_to_process', 0)))
    current_options['home_directory'] = str(post_data.get('home_directory', current_options.get('home_directory', '')))
    # Search Requests options
    current_options['url'] = str(post_data.get('url', ''))
    current_options['search_term'] = str(post_data.get('search_term', ''))

    # This is not implemented yet
    skus_to_check = post_data.get('skus', '').split(',')  # Get SKUs from form input
    skus_to_check = [sku.strip() for sku in skus_to_check if sku.strip()]
    current_options['skus_to_check'] = skus_to_check

    current_options['clean_data'] = post_data.get('clean_data') == 'on'
    # Add directory for CSV row counting
    csv_dir = post_data.get('csv_dir', '')
    if csv_dir and os.path.isdir(csv_dir):
        current_options['csv_dir'] = csv_dir

    return current_options

def set_defaults(distributor_options):
    # Update boolean flags
    defaults = {
        'home_directory': distributor_options.get('home_directory', '.'),
        'get_categories': distributor_options.get('get_categories'),
        'scrape_products': distributor_options.get('scrape_products'),
        'process_csv': distributor_options.get('process_csv'),
        'process_extra': distributor_options.get('process_extra'),
        'reprocess_csv': distributor_options.get('reprocess_csv'),
        'dedupe_csv': distributor_options.get('dedupe_csv'),
        'format_csv': distributor_options.get('format_csv'),
        'scan_csv': distributor_options.get('scan_csv'),
        'count_csv': distributor_options.get('count_csv'),
        'start_row': distributor_options.get('csv_start_row'),
        'max_products': distributor_options.get('max_products'),
        'test_products': distributor_options.get('test_products'),
        'test_categories': distributor_options.get('test_categories'),
        'category_to_process': distributor_options.get('category_to_process'),
        'search_requests': distributor_options.get('search_requests'),
        'url': distributor_options.get('url'),
        'search_term': distributor_options.get('search_term'),
        'base_url': distributor_options.get('base_url'),
        'crm_url': distributor_options.get('crm_url'),
        # 'url_file': f"{usfoods_options.get('category_name').lower()}_product_urls.csv",
        # 'data_file': f"{usfoods_options.get('category_name').lower()}_product_data.csv"
    }
    return defaults
# ****************************************************
# Big Commerce
# ****************************************************
def scrape_bigcommerce(request, scraper_class):
    print("scrape_bigcommerce()")
    options = {}
    if request.method == 'POST':
        with scraper_class(options) as scraper:
            distributor_options = scraper.get_options()
            # Create a copy of options for this request
            options = update_shopify_options(request.POST, distributor_options, scraper)
            options = update_common_options(request.POST, options)
            # Run the scraper
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                print(f"skipping processing CSV")
                # Normal synchronous processing
                result = scraper.run()
                return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = scraper_class()
    distributor_options = scraper.get_options()
    category_ids = scraper.get_category_ids()

    categories_scraped = scraper.get_categories()
    categories = []
    categories.append({
        'id': 0,
        'name': 'All',
        'url_file': f"product_urls.csv",
        'data_file': f"product_data.csv"
    })
    for category in categories_scraped:
        categories.append({
            'id': category['id'],
            'name': category['name'],
            'url_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_urls.csv",
            'data_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_data.csv"
        })

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_misc2.html', {
        'categories': categories,
        'name': scraper.get_name(),
        'defaults': defaults,
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })

def scrape_terra_spice(request):
    scraper_class = TerraSpiceScraper
    return scrape_bigcommerce(request, scraper_class)

def scrape_meats_linz(request):
    scraper_class = MeatsByLinzScraper
    return scrape_bigcommerce(request, scraper_class)

# ****************************************************
# Misc
# ****************************************************
def update_usfoods_options(post_data, current_options):
    """
    Update usfoods_options based on form POST data.

    Args:
        post_data: request.POST dictionary
        current_options: Current usfoods_options to update

    Returns:
        Updated usfoods_options dictionary
    """
    # Update boolean flags
    scraper = USFoodsScraper()
    category_ids = scraper.get_category_ids()
    category_names = scraper.get_category_names()
    print(post_data)

    # Update category and file names if category changes
    category_id = post_data.get('category_id')
    if category_id:
        current_options['chosen_category'] = category_id
        category_id_lookup = category_ids[category_id]
        category_name = category_names[category_id_lookup]
        current_options['category_name'] = category_name
        current_options['url_output_file'] = str(post_data.get('url_file', ''))
        current_options['data_output_file'] = str(post_data.get('data_file', ''))
    print(current_options)
    return current_options

def scrape_usfoods(request):
    options = {}
    from scrapers.misc.usfoods import USFoodsScraper

    if request.method == 'POST':
        with USFoodsScraper(options) as scraper:
            distributor_options = scraper.get_options()
            # Create a copy of options for this request
            options = update_usfoods_options(request.POST, distributor_options)
            options = update_common_options(request.POST, options)
            # Run the scraper
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                print(f"skipping processing CSV")
                # Normal synchronous processing
                result = scraper.run()
                return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    from scrapers.misc.usfoods import USFoodsScraper
    scraper = USFoodsScraper()
    scraper_class = USFoodsScraper
    distributor_options = scraper.get_options()
    category_ids = scraper.get_category_ids()

    categories = [{'id': k, 'name': v} for k, v in category_ids.items()]

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_usfoods.html', {
        'categories': categories,
        'defaults': defaults,
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })

def update_cw_options(post_data, current_options):
    """
    Update usfoods_options based on form POST data.

    Args:
        post_data: request.POST dictionary
        current_options: Current usfoods_options to update

    Returns:
        Updated usfoods_options dictionary
    """
    # Update boolean flags
    scraper = ChefWarehouseScraper()
    category_ids = scraper.get_category_ids()
    category_names = scraper.get_category_names()
    category_urls = scraper.get_category_urls()
    print(post_data)

    # Update category and file names if category changes
    category_id = post_data.get('category_id')
    if category_id:
        current_options['chosen_category'] = category_id
        category_id_lookup = category_ids[category_id]
        category_name = category_names[category_id_lookup]
        current_options['category_url_part'] = category_urls[category_id_lookup]
        current_options['category_name'] = category_name
        current_options['url_output_file'] = str(post_data.get('url_file', ''))
        current_options['data_output_file'] = str(post_data.get('data_file', ''))

    print(current_options)
    return current_options

def scrape_cw(request):
    options = {}

    if request.method == 'POST':
        with ChefWarehouseScraper(options) as scraper:
            distributor_options = scraper.get_options()
            # Create a copy of options for this request
            options = update_cw_options(request.POST, distributor_options)
            options = update_common_options(request.POST, options)
            # Run the scraper
            scraper.set_options(options)
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                result = scraper.run()
                return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form

    scraper = ChefWarehouseScraper()
    scraper_class = ChefWarehouseScraper
    distributor_options = scraper.get_options()
    category_ids = scraper.get_category_ids()
    categories = []
    for category_id, category_name in category_ids.items():
        categories.append({
            'id': category_id,
            'name': category_name,
            'url_file': f"{category_id.lower()}_product_urls.csv",
            'data_file': f"{category_id.lower()}_product_data.csv"
        })

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_cw.html', {
        'categories': categories,
        'defaults': defaults,
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })

def update_breakthru_options(post_data, current_options):
    """
    Update usfoods_options based on form POST data.

    Args:
        post_data: request.POST dictionary
        current_options: Current usfoods_options to update

    Returns:
        Updated usfoods_options dictionary
    """
    # Update category and file names if category
    # changes
    scraper = BreakthruScraper()
    category_id = post_data.get('category_id')
    if category_id and int(category_id) != 0:
        categories = scraper.get_categories()
        for category in categories:
            if category['id'] == int(category_id):
                category_name = category['name']
                current_options['category_url'] = category['url']
                break
        current_options['chosen_category'] = category_id
        category_name = ''
        current_options['category_url'] = ''
        current_options['url_output_file'] = str(post_data.get('url_file', ''))
        current_options['data_output_file'] = str(post_data.get('data_file', ''))
    else:
        category_name = 'All'
        current_options['chosen_category'] = 0
        current_options['url_output_file'] = current_options['home_directory']
        current_options['data_output_file'] = ''

    current_options['category_name'] = category_name

    print(current_options)
    return current_options

def scrape_breakthru(request):
    options = {}

    if request.method == 'POST':
        with BreakthruScraper(options) as scraper:
            distributor_options = scraper.get_options()
            # Create a copy of options for this request
            options = update_breakthru_options(request.POST, distributor_options)
            options = update_common_options(request.POST, options)
            # Run the scraper
            scraper.set_options(options)
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                result = scraper.run()
                return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = BreakthruScraper()
    scraper_class = BreakthruScraper
    distributor_options = scraper.get_options()
    category_ids = scraper.get_category_ids()
    categories_scraped = scraper.get_categories()
    categories = []
    categories.append({
        'id': 0,
        'name': 'All',
        'url_file': f"product_urls.csv",
        'data_file': f"product_data.csv"
    })
    for category in categories_scraped:
        categories.append({
            'id': category['number'],
            'name': category['id'],
            'url_file': f"{scraper.make_filename_safe(category['id']).lower()}_product_urls.csv",
            'data_file': f"{scraper.make_filename_safe(category['id']).lower()}_product_data.csv"
        })

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_breakthru.html', {
        'categories': categories,
        'defaults': defaults,
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })

def update_misc_options(post_data, current_options):
    """
    Update usfoods_options based on form POST data.

    Args:
        post_data: request.POST dictionary
        current_options: Current usfoods_options to update

    Returns:
        Updated usfoods_options dictionary
    """
    # Update category and file names if category
    # changes
    category_id = post_data.get('category_id')
    if category_id and int(category_id) != 0:
        current_options['chosen_category'] = category_id
        category_name = ''
        current_options['category_url'] = ''
        current_options['url_output_file'] = str(post_data.get('url_file', ''))
        current_options['data_output_file'] = str(post_data.get('data_file', ''))
    else:
        category_name = 'All'
        current_options['chosen_category'] = 0
        current_options['url_output_file'] = current_options['home_directory']
        current_options['data_output_file'] = ''
    current_options['category_name'] = category_name
    current_options['direct_category_to_process'] = str(post_data.get('direct_category_to_process', ''))

    print(current_options)
    return current_options

def scrape_cheney_brothers(request):
    print("scrape_cheney_brothers()")
    options = {}

    if request.method == 'POST':
        with CheneyBrothersScraper(options) as scraper:
            distributor_options = scraper.get_options()
            # Create a copy of options for this request
            options = update_misc_options(request.POST, distributor_options)
            options = update_common_options(request.POST, options)
            # Run the scraper
            scraper.set_options(options)
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                print("running scraper")
                result = scraper.run()
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
    # GET request - show form
    print("GET Form")
    scraper = CheneyBrothersScraper()
    scraper_class = CheneyBrothersScraper
    distributor_options = scraper.get_options()
    category_ids = scraper.get_category_ids()
    categories = []
    for category in category_ids:
        categories.append({
            'id': category["Id"],
            'name': category["Name"],
            'url_file': f"{category['Name'].lower()}_urls.csv",
            'data_file': f"{category['Name'].lower()}_data.csv"
        })

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_cheney_brothers.html', {
        'categories': categories,
        'defaults': defaults,
        'name': 'Cheney Brothers',
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })


def scrape_wine_searcher(request):
    options = {}
    print("scrape_wine_searcher()")

    if request.method == 'POST':
        with WineSearcherScraper(options) as scraper:
            print(request.POST)
            distributor_options = scraper.get_options()
            options = update_misc_options(request.POST, distributor_options)
            options = update_common_options(request.POST, options)
            # Run the scraper
            scraper.set_options(options)
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                print("running scraper")
                result = scraper.run()
                print("scraper finished")
                return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = WineSearcherScraper()
    scraper_class = WineSearcherScraper
    distributor_options = scraper.get_options()
    categories_scraped = scraper.get_categories()
    categories = []
    categories.append({
        'id': 0,
        'name': 'All',
        'url_file': f"product_urls.csv",
        'data_file': f"product_data.csv"
    })
    for category in categories_scraped:
        print(category)
        categories.append({
            'id': category['id'],
            'name': category['name'],
            'url_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_urls.csv",
            'data_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_data.csv"
        })

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_misc2.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })

def scrape_webstaurant(request):
    options = {}
    print("scrape_webstaurant()")

    if request.method == 'POST':
        with WebstaurantScraper(options) as scraper:
            print(request.POST)
            distributor_options = scraper.get_options()
            options = update_misc_options(request.POST, distributor_options)
            options = update_common_options(request.POST, options)
            # Run the scraper
            scraper.set_options(options)
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                print("running scraper")
                result = scraper.run()
                print("scraper finished")
                return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = WebstaurantScraper()
    scraper_class = WebstaurantScraper
    distributor_options = scraper.get_options()
    categories_scraped = scraper.get_categories()
    categories = []
    categories.append({
        'id': 0,
        'name': 'All',
        'url_file': f"product_urls.csv",
        'data_file': f"product_data.csv"
    })
    for category in categories_scraped:
        print(category)
        categories.append({
            'id': category['id'],
            'name': category['name'],
            'url_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_urls.csv",
            'data_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_data.csv"
        })

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_misc2.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })

def scrape_sysco(request):
    options = {}
    print("scrape_sysco()")

    if request.method == 'POST':
        with SyscoScraper(options) as scraper:
            print(request.POST)
            distributor_options = scraper.get_options()
            options = update_misc_options(request.POST, distributor_options)
            options = update_common_options(request.POST, options)
            # Run the scraper
            scraper.set_options(options)
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                print("running scraper")
                result = scraper.run()
                print("scraper finished")
                return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = SyscoScraper()
    scraper_class = SyscoScraper
    distributor_options = scraper.get_options()
    categories_scraped = scraper.get_categories()
    categories = []
    categories.append({
        'id': 0,
        'name': 'All',
        'url_file': f"product_urls.csv",
        'data_file': f"product_data.csv"
    })
    for category in categories_scraped:
        print(category)
        categories.append({
            'id': category['id'],
            'name': category['name'],
            'url_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_urls.csv",
            'data_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_data.csv"
        })

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_misc2.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })

def scrape_sg(request):
    options = {}
    print("scrape_sg()")

    if request.method == 'POST':
        with SouthernGlazierScraper(options) as scraper:
            print(request.POST)
            distributor_options = scraper.get_options()
            options = update_misc_options(request.POST, distributor_options)
            options = update_common_options(request.POST, options)
            # Run the scraper
            scraper.set_options(options)
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                print("running scraper")
                result = scraper.run()
                print("scraper finished")
                return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = SouthernGlazierScraper()
    scraper_class = SouthernGlazierScraper
    distributor_options = scraper.get_options()
    categories_scraped = scraper.get_categories()
    categories = []
    categories.append({
        'id': 0,
        'name': 'All',
        'url_file': f"product_urls.csv",
        'data_file': f"product_data.csv"
    })
    for category in categories_scraped:
        categories.append({
            'id': category['number'],
            'name': category['name'],
            'url_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_urls.csv",
            'data_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_data.csv"
        })

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_sg.html', {
        'categories': categories,
        'defaults': defaults,
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })

def scrape_imperial_dade(request):
    options = {}
    if request.method == 'POST':
        with ImperialDadeScraper(options) as scraper:
            print(request.POST)
            distributor_options = scraper.get_options()

            options = update_misc_options(request.POST, distributor_options)
            options = update_common_options(request.POST, options)
            # Run the scraper
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                print(f"skipping processing CSV")
                # Normal synchronous processing
                result = scraper.run()
                return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = ImperialDadeScraper()
    scraper_class = ImperialDadeScraper
    distributor_options = scraper.get_options()
    categories_scraped = scraper.get_categories()
    categories = []
    categories.append({
        'id': 0,
        'name': 'All',
        'url_file': f"product_urls.csv",
        'data_file': f"product_data.csv"
    })
    for category in categories_scraped:
        categories.append({
            'id': category['id'],
            'name': category['name'],
            'url_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_urls.csv",
            'data_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_data.csv"
        })

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_misc2.html', {
        'categories': categories,
        'defaults': defaults,
        'name': 'Imperial Dade',
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })
# ****************************************************
# City Hive
# ****************************************************
def scrape_city_hive(request, scraper_class):
    options = {}
    print("scrape_city_hive()")

    if request.method == 'POST':
        with scraper_class(options) as scraper:
            print(request.POST)
            distributor_options = scraper.get_options()
            options = update_misc_options(request.POST, distributor_options)
            options = update_common_options(request.POST, options)
            # Run the scraper
            scraper.set_options(options)
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                print("running scraper")
                result = scraper.run()
                print("scraper finished")
                return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = scraper_class()
    distributor_options = scraper.get_options()
    categories_scraped = scraper.get_categories()
    categories = []
    categories.append({
        'id': 0,
        'name': 'All',
        'url_file': f"product_urls.csv",
        'data_file': f"product_data.csv"
    })
    for category in categories_scraped:
        print(category)
        categories.append({
            'id': category['id'],
            'name': category['name'],
            'url_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_urls.csv",
            'data_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_data.csv"
        })

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_misc2.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })

def scrape_archer_liquor(request):
    scraper_class = ArcherLiquorScraper
    return scrape_city_hive(request, scraper_class)
def scrape_cellar_53(request):
    scraper_class = Cellar53Scraper
    return scrape_city_hive(request, scraper_class)
def scrape_empire_metro(request):
    scraper_class = EmpireMetroScraper
    return scrape_city_hive(request, scraper_class)
def scrape_empire_north(request):
    scraper_class = EmpireNorthScraper
    return scrape_city_hive(request, scraper_class)
def scrape_maverick_beverage(request):
    scraper_class = MaverickBeverageScraper
    return scrape_city_hive(request, scraper_class)
def scrape_morrell_wine(request):
    scraper_class = MorrellWineScraper
    return scrape_city_hive(request, scraper_class)
def scrape_sandr_liquors(request):
    scraper_class = SandRScraper
    return scrape_city_hive(request, scraper_class)
def scrape_south_hills_wine(request):
    scraper_class = ShortHillsWineScraper
    return scrape_city_hive(request, scraper_class)
def scrape_twin_liquors(request):
    scraper_class = TwinLiquorsScraper
    return scrape_city_hive(request, scraper_class)
def scrape_hive_template(request):
    scraper_class = HiveTemplateScraper
    return scrape_city_hive(request, scraper_class)

# ****************************************************
# Shopify
# ****************************************************
def update_shopify_options(post_data, current_options, scraper):
    """
    Update bitters_options based on form POST data.

    Args:
        post_data: request.POST dictionary
        current_options: Current bitters_options to update

    Returns:
        Updated bitters_options dictionary
    """
    # Update boolean flags
    print(post_data)

    # Update category and file names if category changes
    category_id = post_data.get('category_id')
    if category_id and int(category_id) != 0:
        current_options['chosen_category'] = category_id
        category_name = ''
        current_options['category_url'] = ''
        current_options['url_output_file'] = str(post_data.get('url_file', ''))
        current_options['data_output_file'] = str(post_data.get('data_file', ''))
    else:
        category_name = 'All'
        current_options['chosen_category'] = 0
        current_options['url_output_file'] = current_options['home_directory']
        current_options['data_output_file'] = ''

    # Update clean_data option
    current_options['clean_data'] = post_data.get('clean_data') == 'on'
    current_options['category_name'] = category_name
    current_options['direct_category_to_process'] = str(post_data.get('direct_category_to_process', ''))
    current_options['attempts'] = int(post_data.get('attempts', 40))

    return current_options

def scrape_shopify(request, scraper_class):
    options = {}
    if request.method == 'POST':
        with scraper_class(options) as scraper:
            distributor_options = scraper.get_options()
            # Create a copy of options for this request
            options = update_shopify_options(request.POST, distributor_options, scraper)
            options = update_common_options(request.POST, options)
            # Run the scraper
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                print(f"skipping processing CSV")
                # Normal synchronous processing
                result = scraper.run()
                return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = scraper_class()
    distributor_options = scraper.get_options()
    category_ids = scraper.get_category_ids()

    categories_scraped = scraper.get_categories()
    categories = []
    categories.append({
        'id': 0,
        'name': 'All',
        'url_file': f"product_urls.csv",
        'data_file': f"product_data.csv"
    })
    for category in categories_scraped:
        categories.append({
            'id': category['id'],
            'name': category['name'],
            'url_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_urls.csv",
            'data_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_data.csv"
        })

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_misc2.html', {
        'categories': categories,
        'name': scraper.get_name(),
        'defaults': defaults,
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })

def scrape_melissas(request):
    scraper_class = MelissasScraper
    return scrape_shopify(request, scraper_class)
def scrape_bitters_bottles(request):
    scraper_class = BittersBottlesScraper
    return scrape_shopify(request, scraper_class)
def scrape_savory_gourmet(request):
    scraper_class = SavoryGourmetScraper
    return scrape_shopify(request, scraper_class)
def scrape_pacific_gourmet(request):
    scraper_class = PacificGourmetScraper
    return scrape_shopify(request, scraper_class)
def scrape_four_star_seafood(request):
    scraper_class = FourStarSeafoodScraper
    return scrape_shopify(request, scraper_class)
def scrape_alma(request):
    scraper_class = AlmaScraper
    return scrape_shopify(request, scraper_class)
def scrape_allen_brothers(request):
    scraper_class = AllenBrothersScraper
    return scrape_shopify(request, scraper_class)
def scrape_fulton_fish(request):
    scraper_class = FultonFishScraper
    return scrape_shopify(request, scraper_class)

# ****************************************************
# Cut+Dry
# ****************************************************
def process_cut_post(request, scraper):
    print(request.POST)
    print("process_cut_post()")
    distributor_options = scraper.get_options()

    # Update options from form data
    options = update_cut_options(request.POST, distributor_options)
    options = update_common_options(request.POST, options)

    task_id = process_common_post(options, request, scraper)
    if task_id:
        return JsonResponse({
            'task_id': task_id,
            'status': 'started',
            'message': 'Task started successfully'
        }, status=200)
    else:
        print(f"skipping processing CSV")
        # Normal synchronous processing
        result = scraper.run()
    return result

def update_cut_options(post_data, current_options):
    """
    Update birite_options based on form POST data.

    Args:
        post_data: request.POST dictionary
        current_options: Current birite_options to update

    Returns:
        Updated birite_options dictionary
    """
    # Update category and file names if category changes
    category_id = post_data.get('category_id')
    if category_id and int(category_id) != 0:
        current_options['chosen_category'] = category_id
        category_name = ''
        current_options['category_url'] = ''
        current_options['url_output_file'] = str(post_data.get('url_file', ''))
        current_options['data_output_file'] = str(post_data.get('data_file', ''))
    else:
        category_name = 'All'
        current_options['chosen_category'] = 0
        current_options['url_output_file'] = current_options['home_directory']
        current_options['data_output_file'] = ''

    # Update clean_data option
    current_options['clean_data'] = post_data.get('clean_data') == 'on'
    current_options['category_name'] = category_name
    current_options['direct_category_to_process'] = str(post_data.get('direct_category_to_process', ''))
    current_options['attempts'] = int(post_data.get('attempts', 40))

    print(current_options)
    return current_options

def update_cut_categories(post_data, scraper):
    categories_scraped = scraper.get_categories()
    categories = []
    categories.append({
        'id': 0,
        'name': 'All',
        'url_file': f"product_urls.csv",
        'data_file': f"product_data.csv"
    })
    for category in categories_scraped:
        categories.append({
            'id': category['id'],
            'name': category['name'],
            'url_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_urls.csv",
            'data_file': f"{scraper.make_filename_safe(category['name']).lower()}_product_data.csv"
        })

    # Calculate total product count from top-level categories
    total_products = 0
    if hasattr(scraper, 'CATEGORIES') and 'data' in scraper.CATEGORIES:
        for category in scraper.CATEGORIES['data'].get('catalogCategoryOptions', []):
            if 'productCount' in category and isinstance(category['productCount'], (int, float)):
                total_products += category['productCount']
    return categories, total_products

# def scrape_prdeli(request):
#     """View for scraping PRDeli"""
#     if request.method == 'POST':
#         return process_cut_post(request, PRDeliScraper)
#
#     # For GET request, show the form with current options
#     context = {
#         'title': 'PRDeli Scraper',
#         'distributor_name': 'PRDeli',
#         'distributor_slug': 'prdeli',
#         'options': PRDeliScraper.DEFAULT_OPTIONS,
#         'categories': getattr(PRDeliScraper, 'CATEGORIES', None),
#         'is_cut_scraper': True,
#     }
#     return render(request, 'scrape_products/scrape_form.html', context)
def scrape_market_406(request):
    """View for scraping 406 Market"""
    print("Calling scrape_market_406()")
    scraper_class = Market406Scraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_ab(request):
    scraper_class = ABScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_acme_steak(request):
    print("Calling scrape_acme_steak()")
    scraper_class = AcmeSteakScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_all_fresh_seafood(request):
    print("Calling scrape_all_fresh_seafood()")
    scraper_class = AllFreshSeafoodScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_all_star_specialties(request):
    print("Calling scrape_all_fresh_seafood()")
    scraper_class = AllStarSpecialtiesScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_alpeake(request):
    """View for scraping 406 Market"""
    print("Calling scrape_foodpro()")
    scraper_class = AlpeakeScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_apito(request):
    print("Calling scrape_foodpro()")
    scraper_class = ApitoScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_birite(request):
    scraper_class = BiRiteScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_carmela(request):
    scraper_class = CarmelaScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_caruso(request):
    scraper_class = CarusoScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_chefs_kitchen(request):
    scraper_class = ChefsKitchenScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_cheese_importers(request):
    """View for scraping Cheese Importers"""
    print("Calling scrape_cheese_importers()")
    scraper_class = CheeseImportersScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_christ_panos(request):
    scraper_class = ChristPanosScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_citylinefoods(request):
    """View for scraping Woolco Foods"""
    print("Calling scrape_citylinefoods()")
    scraper_class = CityLineFoodsScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_cooks_company(request):
    scraper_class = CooksCompanyScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_creamco(request):
    """View for scraping CreamCo"""
    print("Calling scrape_creamco()")
    scraper_class = CreamCoScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_crookbros(request):
    """View for scraping Crook & Co."""
    print("Calling scrape_crookbros()")
    scraper_class = CrookBrosScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_cusumanoandsons(request):
    """View for scraping Cusumano & Sons"""
    print("Calling scrape_cusumanoandsons()")
    scraper_class = CusumanoAndSonsScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_dicarlo(request):
    print("Calling scrape_all_fresh_seafood()")
    scraper_class = DiCarloScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_derstines(request):
    print("Calling scrape_derstines()")
    scraper_class = DerstinesScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_driscoll(request):
    scraper_class = DriscollScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_dwcspecialties(request):
    """View for scraping DWC Specialties"""
    print("Calling scrape_dwcspecialties()")
    scraper_class = DWCSpecialtiesScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_foodandpaper(request):
    print("Calling scrape_foodandpaper()")
    scraper_class = FoodAndPaperScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_foodpro(request):
    print("Calling scrape_foodpro()")
    scraper_class = FoodProScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_fourstarmeat(request):
    """View for scraping Four Star Meat"""
    print("Calling scrape_fourstarmeat()")
    scraper_class = FourStarMeatScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_hearty(request):
    """View for scraping Hearty"""
    print("Calling scrape_hearty()")
    scraper_class = HeartyScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_hooktofork(request):
    """View for scraping Hook to Fork"""
    print("Calling scrape_hooktofork()")
    scraper_class = HookToForkScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_indianhead(request):
    scraper_class = IndianheadScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_jordanpaige(request):
    """View for scraping Jordan Paige"""
    print("Calling scrape_jordanpaige()")
    scraper_class = JordanPaigeScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_manson(request):
    scraper_class = MansonScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_maple_vale(request):
    scraper_class = MapleValeScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_misterproduce(request):
    """View for scraping Mister Produce"""
    print("Calling scrape_misterproduce()")
    scraper_class = MisterProduceScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_pacificprovisions(request):
    """View for scraping Pacific Provisions"""
    print("Calling scrape_pacificprovisions()")
    scraper_class = PacificProvisionsScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_prdeli(request):
    """View for scraping Pacific Provisions"""
    print("Calling scrape_prdeli()")
    scraper_class = PRDeliScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_primizie_noca(request):
    scraper_class = PrimizieNoCaScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_primizie_ny(request):
    scraper_class = PrimizieScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_rarefoods(request):
    """View for scraping Rare Foods"""
    print("Calling scrape_rarefoods()")
    scraper_class = RareFoodsScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_realityfoods(request):
    """View for scraping Reality Foods"""
    print("Calling scrape_realityfoods()")
    scraper_class = RealityFoodsScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_safradistribution(request):
    """View for scraping Safra Distribution"""
    print("Calling scrape_safradistribution()")
    scraper_class = SafraDistributionScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_sardilli(request):
    scraper_class = SardilliScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_savalfoodservice(request):
    """View for scraping Saval Foodservice"""
    print("Calling scrape_savalfoodservice()")
    scraper_class = SavalFoodserviceScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_sandw(request):
    scraper_class = SandWScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_sierra_meat(request):
    print("Calling scrape_derstines()")
    scraper_class = SierraMeatScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_southwest_traders(request):
    scraper_class = SouthwestTradersScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_socomeatco(request):
    """View for scraping SoCo Meat Co"""
    print("Calling scrape_socomeatco()")
    scraper_class = SoCoMeatCoScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_sunbelt(request):
    print("Calling scrape_sunbelt()")
    scraper_class = SunbeltScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_sutters(request):
    """View for scraping Sutter's Food Group"""
    print("Calling scrape_sutters()")
    scraper_class = SuttersScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_thefishguys(request):
    """View for scraping The Fish Guys"""
    print("Calling scrape_thefishguys()")
    scraper_class = TheFishGuysScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_tolteca(request):
    """View for scraping Tolteca"""
    print("Calling scrape_tolteca()")
    scraper_class = ToltecaScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_valleygold(request):
    """View for scraping Valley Gold"""
    print("Calling scrape_valleygold()")
    scraper_class = ValleyGoldScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_vitco_foods(request):
    print("Calling scrape_vitco_foods()")
    scraper_class = VitcoScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_wagner(request):
    scraper_class = WagnerScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_whatchefswant_south(request):
    """View for scraping What Chefs Want - South"""
    print("Calling scrape_whatchefswant_south()")
    scraper_class = WhatChefsWantSouthScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_whatchefswant_central(request):
    """View for scraping What Chefs Want - South"""
    print("Calling scrape_whatchefswant_south()")
    scraper_class = WhatChefsWantCentralScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_whatchefswant_rockies(request):
    """View for scraping What Chefs Want - South"""
    print("Calling scrape_whatchefswant_south()")
    scraper_class = WhatChefsWantRockiesScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_totalfoods(request):
    """View for scraping Total Foods"""
    print("Calling scrape_totalfoods()")
    scraper_class = TotalFoodsScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_woolcofoods(request):
    """View for scraping Woolco Foods"""
    print("Calling scrape_woolcofoods()")
    scraper_class = WoolcoFoodsScraper
    return scrape_cut_and_dry(request, scraper_class)

def scrape_primesourcefoods(request):
    """View for scraping Woolco Foods"""
    print("Calling scrape_primesourcefoods()")
    scraper_class = PrimeSourceFoodsScraper
    return scrape_cut_and_dry(request, scraper_class)


def scrape_cut_and_dry(request, scraper):
    """View for scraping Woolco Foods"""
    print("Calling scrape_cut_and_dry()")
    options = {}
    scraper_class = scraper
    if request.method == 'POST':
        with scraper_class(options) as scraper:
            print("Calling process_cut_post from scrape_woolcofoods()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = scraper_class()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products,
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })


# ****************************************************
# Pepper
# ****************************************************

def scrape_pepper(request, scraper):
    options = {}
    scraper_class = scraper
    if request.method == 'POST':
        with scraper_class(options) as scraper:
            distributor_options = scraper.get_options()
            # Create a copy of options for this request
            options = {}
            options = update_common_options(request.POST, options)
            # Run the scraper
            task_id = process_common_post(options, request, scraper)
            if task_id:
                return JsonResponse({
                    'task_id': task_id,
                    'status': 'started',
                    'message': 'Task started successfully'
                }, status=200)
            else:
                print(f"skipping processing CSV")
                # Normal synchronous processing
                result = scraper.run()
                return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = scraper_class()
    distributor_options = scraper.get_options()

    categories = []
    categories.append({
        'id': 0,
        'name': 'All',
        'url_file': "product_urls.csv",
        'data_file': getattr(scraper, 'OUTPUT_FILE', 'Output_file.csv')
    })

    defaults = set_defaults(distributor_options)
    defaults['data_file'] = getattr(scraper, 'OUTPUT_FILE', 'Output_file.csv')

    return render(request, 'scrape_products/scrape_pepper.html', {
        'categories': categories,
        'name': scraper.get_name(),
        'defaults': defaults,
        'scraper_class': scraper_class.__name__,
        'module_name': scraper_class.__module__
    })
def scrape_acc_distributors(request):
    scraper_class = AccDistributorsScraper
    return scrape_pepper(request, scraper_class)

def scrape_cibo(request):
    scraper_class = CiboScraper
    return scrape_pepper(request, scraper_class)

def scrape_city_produce(request):
    scraper_class = CityProduceScraper
    return scrape_pepper(request, scraper_class)

def scrape_earthly_gourmet(request):
    scraper_class = EarthlyGourmetScraper
    return scrape_pepper(request, scraper_class)

def scrape_euclid_fish(request):
    scraper_class = EuclidFishScraper
    return scrape_pepper(request, scraper_class)

def scrape_ace_endico(request):
    scraper_class = AceEndicoScraper
    return scrape_pepper(request, scraper_class)

def scrape_brothers_food(request):
    scraper_class = BrothersFoodServiceScraper
    return scrape_pepper(request, scraper_class)

def scrape_dennis_foodservice(request):
    scraper_class = DennisFoodserviceScraper
    return scrape_pepper(request, scraper_class)

def scrape_farmart(request):
    scraper_class = FarmArtScraper
    return scrape_pepper(request, scraper_class)

def scrape_get_fresh_produce(request):
    options = {}
    scraper_class = GetFreshProduceScraper
    return scrape_pepper(request, scraper_class)

def scrape_northeast_specialty(request):
    scraper_class = NortheastSpecialtyScraper
    return scrape_pepper(request, scraper_class)

def scrape_palmer_foods(request):
    scraper_class = PalmerFoodsScraper
    return scrape_pepper(request, scraper_class)

def scrape_perrone(request):
    scraper_class = PerroneScraper
    return scrape_pepper(request, scraper_class)

def scrape_graves_foods(request):
    scraper_class = GravesFoodsScraper
    return scrape_pepper(request, scraper_class)

def scrape_kuno(request):
    scraper_class = KunoScraper
    return scrape_pepper(request, scraper_class)

def scrape_piazza(request):
    scraper_class = PiazzaProduceScraper
    return scrape_pepper(request, scraper_class)

def scrape_prime_source(request):
    scraper_class = PrimeSourceScraper
    return scrape_pepper(request, scraper_class)

def scrape_sirna_sons(request):
    scraper_class = SirnaSonsProduceScraper
    return scrape_pepper(request, scraper_class)

def scrape_seattle_fish(request):
    scraper_class = SeattleFishScraper
    return scrape_pepper(request, scraper_class)

def scrape_testa_produce(request):
    scraper_class = TestaProduceScraper
    return scrape_pepper(request, scraper_class)

def scrape_schenck_foods(request):
    scraper_class = SchenckFoodsScraper
    return scrape_pepper(request, scraper_class)

def scrape_express_foods(request):
    scraper_class = ExpressFoodsScraper
    return scrape_pepper(request, scraper_class)

def scrape_flanagan_foodservice(request):
    options = {}
    scraper_class = FlanaganFoodserviceScraper
    return scrape_pepper(request, scraper_class)

# ****************************************************
# General
# ****************************************************

@csrf_exempt
@require_http_methods(["POST"])
def get_processing_progress(request):
    """
    Endpoint to get the current progress of product processing.
    Expected POST data: {"task_id": "unique_task_id"}
    """
    try:
        data = json.loads(request.body)
        task_id = data.get('task_id')
        print("checking progress for task_id:", task_id)
        if not task_id:
            return JsonResponse({'error': 'task_id is required'}, status=400)

        progress = cache.get(f'product_processing_progress_{task_id}', {})
        return JsonResponse({
            'status': 'success',
            'progress': progress
        })
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def stop_processing(request):
    """
    Endpoint to stop a running processing task.
    Expected POST data: {"task_id": "unique_task_id"}
    """
    print("stop_processing() called")
    try:
        data = json.loads(request.body)
        task_id = data.get('task_id')
        print(f"[DEBUG] Stopping task: {task_id}")

        if not task_id:
            return JsonResponse({'success': False, 'error': 'task_id is required'}, status=400)

        # Import thread manager components
        from .thread_manager import thread_manager, stop_background_task, get_task_status

        # Get detailed debug information
        print(f"[DEBUG] All active threads: {thread_manager.get_all_threads()}")
        print(f"[DEBUG] Stop events: {thread_manager._stop_events}")

        # Get task status
        status = get_task_status(task_id)
        print(f"[DEBUG] Task Status: {status}")

        # Try to stop the task
        stopped = stop_background_task(task_id)
        print(f"[DEBUG] Stop result: {stopped}")

        # Get updated status after stop attempt
        updated_status = get_task_status(task_id)
        print(f"[DEBUG] Updated task status: {updated_status}")

        # Get progress from cache
        progress = cache.get(f'product_processing_progress_{task_id}', {})
        print(f"[DEBUG] Task progress: {progress}")

        if not stopped:
            return JsonResponse({
                'success': False,
                'error': 'Task not found or already stopped',
                'task_id': task_id,
                'debug': {
                    'threads': thread_manager.get_all_threads(),
                    'status': status,
                    'updated_status': updated_status,
                    'progress': progress
                }
            }, status=404)

        return JsonResponse({
            'success': True,
            'message': 'Stop signal sent to the task',
            'task_id': task_id,
            'debug': {
                'status': status,
                'updated_status': updated_status,
                'progress': progress
            }
        })

    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

def count_csv_rows(request):
    """
    Count rows in all CSV files with 'data' or 'urls' in their names across subdirectories.
    Returns JSON response with the results.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            directory = data.get('directory')
            module_name = data.get('module_name')
            scraper_class_name = data.get('scraper_class')
            print(directory)
            import urllib.parse
            directory = urllib.parse.unquote(directory)
            print(directory)
            # Your existing directory validation code
            if not directory or not os.path.isdir(directory):
                return JsonResponse({'error': 'Invalid directory'}, status=400)


            # Get row counts using CSVProcessor
            results = CSVProcessor.count_rows_in_data_csvs(directory)

            # The results are already in the correct format from CSVProcessor
            # Calculate the total number of rows across all directories
            total_data_rows = sum(directory_data.get('data_rows', 0)
                                  for directory_data in results.values())

            total_url_rows = sum(directory_data.get('url_rows', 0)
                                 for directory_data in results.values())

            module = __import__(module_name, fromlist=[scraper_class_name])
            scraper_class = getattr(module, scraper_class_name)
            scraper = scraper_class()
            print(f"scraper_class: {scraper_class}")
            print(f"scraper: {scraper}")
            if hasattr(scraper, 'CRM_NOTE_ID') and scraper.CRM_NOTE_ID:
                print(f"Updating product count for {scraper.CRM_NOTE_ID}")
                scraper.update_product_count(total_data_rows, total_url_rows)
            return JsonResponse({
                'results': results,
                'total_data_rows': total_data_rows,
                'total_url_rows': total_url_rows,
                'status': 'success'
            })

        except Exception as e:
            import traceback
            traceback.print_exc()  # This will print the full traceback to the console
            return JsonResponse(
                {'error': f'Error counting CSV rows: {str(e)}'},
                status=500
            )

    return JsonResponse(
        {'error': 'Only POST method is allowed'},
        status=405
    )

def update_distributor(request):
    """
    Update distributor name in all CSV files in the specified directory
    """
    print("update_distributor()")
    print(request.POST)
    if request.method == 'POST':
        directory = request.POST.get('directory', '').strip()
        distributor_name = request.POST.get('distributor_name', '').strip()
        distributor_address = request.POST.get('distributor_address', '').strip()
        distributor_city = request.POST.get('distributor_city', '').strip()
        distributor_state = request.POST.get('distributor_state', '').strip()
        distributor_zip = request.POST.get('distributor_zip', '').strip()

        if not directory or not distributor_name:
            return JsonResponse(
                {'success': False, 'error': 'Both directory and distributor name are required'},
                status=400
            )

        try:
            # Call the CSV processor to update distributor names
            results = CSVProcessor.update_distributor_in_csvs(directory, distributor_name, distributor_address, distributor_city, distributor_state, distributor_zip)
            return JsonResponse(results)

        except Exception as e:
            return JsonResponse(
                {'success': False, 'error': f'Error updating distributor: {str(e)}'},
                status=500
            )

    return JsonResponse(
        {'success': False, 'error': 'Only POST method is allowed'},
        status=405
    )

def search_requests(request):
    """
    Handle search requests via AJAX
    """
    if request.method == 'POST':
        url = request.POST.get('url', '').strip()
        search_term = request.POST.get('search_term', '').strip()

        if not url or not search_term:
            return JsonResponse({
                'success': False,
                'error': 'Both URL and search term are required'
            }, status=400)

        try:

            with Scraper() as scraper:
                scraper.options['search_term'] = search_term
                scraper.options['url'] = url
                result, found = scraper.search_requests()

            return JsonResponse({
                'success': True,
                'found': found,
                'sample': result,
                'url': url,
                'search_term': search_term
            })

        except requests.RequestException as e:
            return JsonResponse({
                'success': False,
                'error': f'Error making request: {str(e)}',
                'url': url,
                'search_term': search_term
            }, status=500)

    return JsonResponse({
        'success': False,
        'error': 'Only POST method is allowed'
    }, status=405)
def scraper_status(request):
    """
    Display a status page showing summary information for all scrapers.
    """
    print("scraper_status()")
    # Get data for all scrapers
    scraper_data = []

    for scraper_class in SCRAPER_CLASSES:
        data = get_scraper_data(scraper_class)
        if data:
            scraper_data.append(data)

    # Sort by status (In Progress first) then by name
    scraper_data.sort(key=lambda x: (x['status'] == 'Complete', x['name']))

    # Calculate totals
    total_data = sum(d['data_rows'] for d in scraper_data)
    total_urls = sum(d['url_rows'] for d in scraper_data)
    total_percent = min(100, int((total_data / total_urls * 100))) if total_urls > 0 else 0

    context = {
        'scrapers': scraper_data,
        'total_data': total_data,
        'total_urls': total_urls,
        'total_percent': total_percent,
        'formatted_total_data': intcomma(total_data),
        'formatted_total_urls': intcomma(total_urls),
    }

    return render(request, 'scrape_products/status.html', context)

def get_scraper_data(scraper_class):
    """Get data for a single scraper class"""
    try:
        # Create an instance of the scraper
        scraper = scraper_class()
        
        # Get the directory and vendor name
        directory = getattr(scraper, 'DEFAULT_DIRECTORY', None)
        vendor_name = getattr(scraper, 'VENDOR_NAME', scraper_class.__name__)
        scraper_type = scraper.get_type()
        print(vendor_name)

        if not directory or not os.path.exists(directory):
            return None
            
        # Find data and URL files
        data_files = glob.glob(os.path.join(directory, '*_data.csv'))
        url_files = glob.glob(os.path.join(directory, '*_urls.csv'))
        only_data = getattr(scraper, 'ONLY_DATA', None)
        if only_data:
            url_files = data_files
        
        # Count rows in data files
        data_rows = 0
        has_prices = False
        for file in data_files:
            try:
                df = pd.read_csv(file, on_bad_lines='skip', dtype={'38': str})
                data_rows += len(df)
                # Check if any row has retail_price > 0
                if 'retail_price' in df.columns:
                    # Convert to numeric, coerce errors to NaN
                    df['retail_price'] = pd.to_numeric(df['retail_price'], errors='coerce')
                    has_prices = has_prices or (df['retail_price'] > 1).any()
            except Exception as e:
                print(f"Error reading {file}: {e}")

        # Count rows in URL files
        url_rows = 0
        for file in url_files:
            try:
                df = pd.read_csv(file, on_bad_lines='skip')
                url_rows += len(df)
            except Exception as e:
                print(f"Error reading {file}: {e}")
        
        # Calculate percentage complete
        percent_complete = 0
        if url_rows > 0:
            percent_complete = min(100, int((data_rows / url_rows) * 100))

        return {
            'name': vendor_name,
            'directory': directory,
            'scraper_type': scraper_type,
            'data_rows': data_rows,
            'url_rows': url_rows,
            'percent_complete': percent_complete,
            'status': 'Complete' if url_rows > 0 and data_rows >= url_rows else 'In Progress',
            'class_name': scraper_class.__name__,
            'has_prices': has_prices,
        }
        
    except Exception as e:
        print(f"Error processing {scraper_class.__name__}: {e}")
        return None

def task_status(request):
    """View to display the status of all background tasks."""
    # Get all active tasks from the thread manager
    active_tasks = thread_manager.get_all_tasks()
    
    # Format task data for the template
    tasks = []
    for task_id, task_info in active_tasks.items():
        tasks.append({
            'id': task_id,
            'name': task_info.get('name', 'Unnamed Task'),
            'status': task_info.get('status', 'unknown'),
            'start_time': task_info.get('start_time'),
            'progress': task_info.get('progress', {}),
            'is_alive': task_info.get('thread', {}).is_alive() if task_info.get('thread') else False
        })
    
    # Sort tasks by start time (newest first)
    tasks.sort(key=lambda x: x.get('start_time') or '', reverse=True)
    
    context = {
        'tasks': tasks,
        'total_tasks': len(tasks),
        'active_tasks': sum(1 for task in tasks if task.get('is_alive')),
    }
    
    return render(request, 'scrape_products/task_status.html', context)

def display_sample_data(request):
    """
    Display sample product data from a CSV file.
    Expected GET parameter: file (path to the CSV file)
    """
    print("display_sample_data()")
    print(request)
    scraper_class_name = request.POST.get('scraper_class', 'Scraper')
    print(f"Scraper Class: {scraper_class_name}")

    # Import the appropriate scraper module and get the class
    module_name =  request.POST.get('module_name', 'scraper')
    print(f"Module: {module_name}")
    module = __import__(module_name, fromlist=[scraper_class_name])
    scraper_class = getattr(module, scraper_class_name)
    scraper = scraper_class()
    file_path = request.POST.get('data_file', 'product_data_url.csv')
    file_path = scraper.get_file_path(file_path, home_dir=getattr(scraper, 'DEFAULT_DIRECTORY', None))
    print(file_path)
    
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            return JsonResponse({'error': f'File not found: {file_path}'})
        
        # Read the CSV file
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Get the first 3 rows
            rows = []
            for i, row in enumerate(reader):
                if i >= 3:  # Only take first 3 rows
                    break
                rows.append(row)
            
            if not rows:
                return JsonResponse({
                    'error': f'No data found in {file_path}'
                }, status=404)
            
            # Generate HTML for the sample data
            html = ['<div class="row g-4">']  # Increased gutter for better spacing
            
            for row in rows:
                # Get the fields we want to display
                name = row.get('name', 'No name available')
                sku = row.get('sku', 'N/A')
                image_url = row.get('image', '')
                # if isinstance(row['retail_price'], str):
                #     retail_price = int(row.get('retail_price', 0)) / 100
                # else:
                #     retail_price = int(float(row['retail_price']))
                # if int(retail_price) == 0:
                #     retail_price = 'NA'
                retail_price = row.get('retail_price', 'N/A')
                link = row.get('content_url', '')
                pack_size = row.get('pack_size', 'N/A')
                description = row.get('description', 'No description available')
                
                # Image HTML - handle separately to avoid f-string issues
                image_html = ''
                if image_url:
                    image_html = f'<img src="{image_url}" class="img-fluid rounded-top h-100 w-100 object-fit-cover" onerror="this.onerror=null; this.src=\'/static/images/no-image.png\'" alt="{name}">'
                else:
                    image_html = '<div class="d-flex align-items-center justify-content-center h-100 text-muted">No image available</div>'
                
                # Create product card with modern theme
                html.append(f'''
                <div class="col-12 col-md-6 col-lg-4">
                    <div class="card h-100 shadow-sm border-0">
                        <div class="position-relative overflow-hidden" style="height: 200px; background-color: #f8f9fa;">
                            {image_html}
                            <div class="position-absolute top-0 end-0 m-2">
                                <span class="badge bg-primary">New</span>
                            </div>
                        </div>
                        <div class="card-body d-flex flex-column">
                            <div class="d-flex justify-content-between align-items-start mb-2">
                                <h5 class="card-title mb-0 text-truncate" title="{name}">{name}</h5>
                                <span class="badge bg-light text-dark">SKU: {sku}</span>
                            </div>
                            
                            <p class="card-text text-muted small flex-grow-1" style="min-height: 60px; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical;">
                                {description}
                            </p>
                            
                            <div class="d-flex justify-content-between align-items-center mt-3 pt-2 border-top">
                                <div>
                                    <span class="text-muted small">Pack Size:</span>
                                    <span class="fw-bold ms-1">{pack_size}</span>
                                </div>
                                <div class="text-end">
                                    <div class="text-muted small">Price</div>
                                    <h5 class="mb-0 text-primary">{retail_price}</h5>
                                </div>
                            </div>
                            
                            <div class="d-grid gap-2 mt-3">
                                <a class="btn btn-outline-primary btn-sm" href="{link}">View Details</a>
                            </div>
                        </div>
                    </div>
                </div>
                ''')
            
            html.append('</div>')  # Close row
            
            # Add some custom CSS for better styling
            html.append('''
            <style>
                .card {
                    transition: transform 0.2s ease, box-shadow 0.2s ease;
                    border-radius: 0.75rem;
                    overflow: hidden;
                }
                .card:hover {
                    transform: translateY(-5px);
                    box-shadow: 0 0.5rem 1.5rem rgba(0, 0, 0, 0.1) !important;
                }
                .object-fit-cover {
                    object-fit: cover;
                }
                .card-title {
                    font-weight: 600;
                    color: #2c3e50;
                }
                .text-truncate-2 {
                    display: -webkit-box;
                    -webkit-line-clamp: 2;
                    -webkit-box-orient: vertical;
                    overflow: hidden;
                }
            </style>
            ''')
            
            return JsonResponse({
                'html': '\n'.join(html)
            })
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({
            'error': f'Error reading file: {str(e)}'
        }, status=500)



def stop_task(request, task_id):
    """View to stop a running task."""
    if request.method == 'POST':
        stopped = thread_manager.stop_thread(task_id)
        if stopped:
            messages.success(request, f'Task {task_id} has been stopped.')
        else:
            messages.error(request, f'Failed to stop task {task_id} or task was not found.')

    return redirect('task_status')

@require_http_methods(["GET"])
def task_progress(request, task_id):
    """
    View to get the progress of a background task.
    """
    import logging
    from django.core.cache import cache
    from django.utils import timezone

    # Set up logging
    logger = logging.getLogger(__name__)

    # Log the incoming request
    logger.info("\n" + "=" * 80)
    logger.info(f"TASK PROGRESS REQUEST")
    logger.info(f"Time: {timezone.now().isoformat()}")
    logger.info(f"Task ID: {task_id}")
    logger.info(f"Request path: {request.path}")
    logger.info(f"Request method: {request.method}")
    logger.info(f"Request GET params: {dict(request.GET)}")

    # Validate task_id
    if not task_id:
        logger.error("ERROR: No task_id provided in the URL")
        return JsonResponse({
            'status': 'error',
            'message': 'Task ID not provided',
            'request_path': request.path,
            'provided_task_id': str(task_id)
        }, status=400)

    # Get the progress from cache
    cache_key = f'product_processing_progress_{task_id}'
    logger.info(f"Looking up cache with key: {cache_key}")

    try:
        # Get the progress data from cache
        progress = cache.get(cache_key)

        if progress is None:
            logger.warning(f"No progress found in cache for task_id: {task_id}")

            # Try to list all cache keys (works with some backends)
            try:
                if hasattr(cache, '_cache') and hasattr(cache._cache, 'keys'):
                    all_keys = list(cache._cache.keys())
                    logger.info(f"Found {len(all_keys)} total cache keys")

                    # Look for any keys that might be related to our task
                    related_keys = [k for k in all_keys if 'progress' in str(k).lower()]
                    if related_keys:
                        logger.info(f"Found {len(related_keys)} related cache keys:")
                        for key in related_keys[:10]:  # Show first 10 to avoid log spam
                            logger.info(f"  - {key}")
            except Exception as e:
                logger.error(f"Error listing cache keys: {e}")

            return JsonResponse({
                'status': 'not_found',
                'message': f'Task {task_id} not found or has expired',
                'cache_key_used': cache_key,
                'current': 0,
                'total': 0,
                'current_sku': '',
                'processed_skus': [],
                'not_found_skus': []
            })

        # Log successful progress retrieval
        logger.info(f"Successfully retrieved progress for task_id: {task_id}")
        logger.debug(f"Progress data: {progress}")

        # Ensure the response includes the task_id for debugging
        if isinstance(progress, dict):
            progress['task_id'] = task_id
            progress['cache_key_used'] = cache_key

        return JsonResponse(progress)

    except Exception as e:
        logger.exception(f"ERROR in task_progress view for task_id {task_id}")
        return JsonResponse({
            'status': 'error',
            'message': f'Internal server error: {str(e)}',
            'task_id': str(task_id),
            'cache_key': cache_key
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def stop_task(request, task_id):
    """
    View to stop a running task.
    """
    try:
        # Set a flag in cache to signal the task to stop
        cache.set(f'task_cancelled_{task_id}', True, timeout=3600)

        # Try to stop the thread if it's still running
        thread_manager.stop_thread(task_id)

        # Update the progress to reflect the cancellation
        progress = cache.get(f'product_processing_progress_{task_id}', {})
        progress.update({
            'status': 'cancelled',
            'message': 'Task was cancelled by user',
        })
        cache.set(f'product_processing_progress_{task_id}', progress, timeout=3600)

        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def get_scraper_class(distributor_name):
    """
    Helper function to get the scraper class by distributor name.
    """
    # Import all scraper classes

    # Get all scraper classes
    scraper_classes = [cls for name, cls in globals().items()
                      if name.endswith('Scraper') and hasattr(cls, 'VENDOR_NAME')]

    # Find the scraper class that matches the distributor name
    for cls in scraper_classes:
        if cls.VENDOR_NAME.lower() == distributor_name.lower():
            return cls

    return None

def application(request):
    """View for scraping UniPro Foodservice distributor directory."""
    context = {
        'title': 'Application Launcher',
        'distributors': [],
        'zip_code': '',
        'distributor_type': 'Broadline Foodservice',
        'radius': 1000,
        'error': None
    }

    if request.method == 'POST':
        scraper = ApplicationScraper()
        # scraper.setup_driver()
        scraper.launch()

        print("Done")
        # with ApplicationScraper() as scraper:
        #     scraper.launch()
        #     time.sleep(50000)


    return render(request, 'scrape_products/application.html', context)


def scrape_unipro(request):
    """View for scraping UniPro Foodservice distributor directory."""
    from .other.unipro import UniProScraper
    
    if request.method == 'POST':
        print(request.POST)
        zip_code = request.POST.get('zip_code', '').strip()
        market_name = request.POST.get('market_name', '').strip()
        distributor_type = request.POST.get('distributor_type', 'Broadline Foodservice')
        radius = int(request.POST.get('radius', 100))
        print("Here 2")
        if not zip_code:
            return render(request, 'scrape_products/unipro.html', {
                'error': 'Please enter a zip code or select a market',
                'zip_code': zip_code,
                'market_name': market_name,
                'distributor_type': distributor_type,
                'radius': radius,
                'market': UniProScraper.MARKETS,
            })
        
        scraper = UniProScraper()
        print("Here 3")
        # Add market name to each distributor if available
        distributors = []
        try:
            results = scraper.get_distributors(zip_code, radius, distributor_type)
            print("Here 1")
            for dist in results:
                if market_name:
                    dist['market'] = market_name
                distributors.append(dist)
            print("Here 4")
            # Check if this is an export request
            print(distributors)
            if 'export_csv' in request.POST:
                # Create a safe filename with zip code and distributor type
                safe_zip = zip_code.replace(' ', '_')
                safe_type = distributor_type.lower().replace(' ', '_')
                filename = f"unipro_distributors_{safe_zip}_{safe_type}.csv"
                response = HttpResponse(
                    content_type='text/csv',
                    headers={'Content-Disposition': f'attachment; filename="{filename}"'},
                )
                response.write(export_unipro_csv(distributors))
                return response
            
            # request.session['unipro_distributors'] = results
            # request.session['unipro_zip_code'] = zip_code
            # request.session['unipro_market_name'] = market_name
            # request.session['unipro_distributor_type'] = distributor_type
            # request.session['unipro_radius'] = radius
            
            return render(request, 'scrape_products/unipro.html', {
                'distributors': distributors,
                'zip_code': zip_code,
                'market_name': market_name,
                'distributor_type': distributor_type,
                'radius': radius,
                'markets': UniProScraper.MARKETS
            })
            
        except Exception as e:
            return render(request, 'scrape_products/unipro.html', {
                'error': str(e),
                'zip_code': zip_code,
                'market_name': market_name,
                'distributor_type': distributor_type,
                'radius': radius,
                'markets': UniProScraper.MARKETS
            })
    
    # GET request - show form
    return render(request, 'scrape_products/unipro.html', {
        'markets': UniProScraper.MARKETS
    })


def export_unipro_csv(distributors):
    """Helper function to generate CSV data from distributors list."""
    print("export_unipro_csv()")
    output = StringIO()
    writer = csv.writer(output)

    # Write header
    writer.writerow([
        'Name', 'City', 'State', 'Zip', 'Type', 'Distance',
        'Address', 'Phone', 'Website', 'Logo URL', 'Unipro Market', 'Unipro'
    ])

    # Write data rows
    for dist in distributors:
        address = ''
        phone = ''
        website = ''
        logo_url = ''

        if dist.get('details'):
            details = dist['details']
            if details.get('address'):
                addr = details['address']
                address_parts = [
                    addr.get('address_1', ''),
                    addr.get('address_2', ''),
                    f"{addr.get('city', '')}, {addr.get('state', '')} {addr.get('zip', '')}"
                ]
                address = ' '.join(filter(None, address_parts))
                phone = addr.get('phone', '')
            website = details.get('website', '')
            if details.get('logo'):
                logo_url = f"https://www.uniprofoodservice.com/{details['logo']}"

        # market = dist.get('market', '').split(',')[0]
        market = dist.get('market', '')

        writer.writerow([
            dist.get('name', ''),
            dist.get('city', ''),
            dist.get('state', ''),
            dist.get('zip', ''),
            dist.get('type', ''),
            dist.get('distance', ''),
            address,
            phone,
            website,
            logo_url,
            market,
            1,
        ])

    return output.getvalue()


def json_to_csv(request):
    print("json_to_csv()")
    context = {
        'title': 'JSON to CSV Converter',
        'error': None
    }

    if request.method == 'POST':
        try:
            json_data = ""

            # Check if JSON was uploaded as a file
            if 'json_file' in request.FILES:
                file = request.FILES['json_file']
                if file.name.endswith('.json'):
                    # Read the uploaded file
                    json_data = file.read().decode('utf-8')
                else:
                    raise ValueError('Please upload a valid .json file')
            else:
                # Get JSON data from textarea
                json_data = request.POST.get('json_data', '').strip()
                if not json_data:
                    raise ValueError('Please enter some JSON data or upload a JSON file')

            # Parse the JSON
            data = json.loads(json_data)

            # Check if the data is in the expected format
            if not isinstance(data, dict) or 'Items' not in data or 'ShortItems' not in data:
                raise ValueError('Invalid JSON format. Expected format: {"Items": [...], "ShortItems": [...]}')

            items = data['Items']
            short_items = data['ShortItems']

            if not items:
                raise ValueError('No items found in the JSON data')

            # Create a CSV in memory
            output = StringIO()
            writer = csv.writer(output)

            # Get all unique field names from both Items and ShortItems
            fieldnames = set()

            # Add all fields from Items
            if items:
                fieldnames.update(items[0].keys())

            # Add all fields from ShortItems
            if short_items:
                fieldnames.update(short_items[0].keys())

            # Convert set to list and sort for consistent column order
            fieldnames = sorted(list(fieldnames))

            # Write header row
            writer.writerow(fieldnames)

            # Write data rows
            for item in items:
                # Create a new row with all fields
                row = {}

                # Add all fields from the main item
                row.update(item)

                # Add matching fields from short item if exists
                short_item = short_items_map.get(item.get('Number'))
                if short_item:
                    row.update(short_item)

                # Write the row with all fields in the correct order
                writer.writerow([row.get(field, '') for field in fieldnames])

            # Create the response with the CSV file
            response = HttpResponse(
                content_type='text/csv',
                headers={'Content-Disposition': 'attachment; filename="converted_data.csv"'},
            )
            response.write(output.getvalue())
            return response

            # Rest of your existing code remains the same...
            # [Previous code for processing JSON and generating CSV...]

        except json.JSONDecodeError:
            context['error'] = 'Invalid JSON format. Please check your input.'
        except Exception as e:
            context['error'] = f'Error: {str(e)}'

    return render(request, 'scrape_products/json_to_csv.html', context)

# In views.py, add this new view
def find_zero_skus(request):
    if request.method == 'POST':
        directory = request.POST.get('directory', '').strip()
        scraper_class_name = request.POST.get('scraper_class', '').strip()
        module_name = request.POST.get('module_name', '').strip()
        column = request.POST.get('column', 'Sku').strip()

        if not directory:
            return JsonResponse({'error': 'Directory path is required'}, status=400)

        try:
            csv_processor = CSVProcessor()
            results = csv_processor.find_skus_starting_with_zero(directory, column)

            # Get the scraper class from the form if provided
            print(f"Update Note {scraper_class_name}")
            if scraper_class_name:
                try:
                    # Import the scraper class dynamically
                    module = __import__(module_name, fromlist=[scraper_class_name])
                    scraper_class = getattr(module, scraper_class_name)

                    # Create an instance of the scraper
                    scraper = scraper_class()

                    # If the scraper has a CRM_NOTE_ID, update the CRM
                    if hasattr(scraper, 'CRM_NOTE_ID') and scraper.CRM_NOTE_ID:
                        note_content = f"Found {len(results)} products with leading zero SKUs"
                        result = len(results) > 0
                        print(f"Update Note: {result}")

                        scraper.update_crm_note(scraper.CRM_NOTE_ID, result)

                except (ImportError, AttributeError, ValueError) as e:
                    print(f"⚠️ Could not import scraper class: {e}")

            return JsonResponse({
                'status': 'success',
                'results': results,
                'total_matches': sum(len(rows) for rows in results.values())
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

from django.urls import get_resolver

def list_all_urls(request):
    urlconf = __import__('scrapers.urls', {}, None, [''])
    url_patterns = get_resolver(urlconf).url_patterns
    urls = []

    def extract_urls(patterns, prefix=''):
        for pattern in patterns:
            if hasattr(pattern, 'url_patterns'):
                extract_urls(pattern.url_patterns, prefix + str(pattern.pattern))
            else:
                print(pattern)
                urls.append({
                    'url': prefix + str(pattern.pattern),
                    'name': pattern.name or '',
                    'view': str(pattern.callback.__module__ + '.' + pattern.callback.__name__)
                })

    extract_urls(url_patterns)
    print(urls)
    return render(request, 'scrape_products/url_list.html', {'urls': sorted(urls, key=lambda x: x['url'])})

from django.shortcuts import render
from django.contrib import messages
import os
from .parse import process_distributor_files
def process_distributor_directory(request):
    """
    View for processing a directory containing distributor CSV files
    """
    if request.method == 'POST':
        print("Processing distributor directory")
        directory_path = request.POST.get('directory_path', '').strip()
        if not directory_path:
            messages.error(request, 'Please provide a directory path')
            return render(request, 'scrape_products/process_directory.html')

        if not os.path.isdir(directory_path):
            messages.error(request, f'Directory not found: {directory_path}')
            return render(request, 'scrape_products/process_directory.html')

        try:
            result = process_distributor_files(directory_path)
            return render(request, 'scrape_products/process_directory.html',
                          {'result': result})
        except Exception as e:
            messages.error(request, f'Error processing directory: {str(e)}')

    return render(request, 'scrape_products/process_directory.html')


@csrf_exempt
def add_column_to_csv(request):
    print("add_column_to_csv()")
    """
    View to add a column to a CSV file if it doesn't exist
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            csv_file = data.get('csv_file')
            column_name = data.get('column_name')
            scraper_class_name = data.get('scraper_class')
            module_name = data.get('module_name')

            print("scraper: ", scraper_class_name)
            print("column_name: ", column_name)
            print("csv_file: ", csv_file)
            print("module_name: ", module_name)
            module = __import__(module_name, fromlist=[scraper_class_name])
            scraper_class = getattr(module, scraper_class_name)
            scraper = scraper_class()
            if not csv_file or not column_name:
                return JsonResponse({
                    'success': False,
                    'message': 'CSV file path and column name are required'
                }, status=400)

            csv_file = scraper.get_file_path(csv_file)

            # Add the column using CSVProcessor
            result = CSVProcessor.add_column_if_missing(csv_file, column_name)

            if result:
                return JsonResponse({
                    'success': True,
                    'message': f'Successfully added column "{column_name}" to {os.path.basename(csv_file)}'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': f'Column "{column_name}" already exists in {os.path.basename(csv_file)} or an error occurred'
                })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error adding column: {str(e)}'
            }, status=500)

    return JsonResponse({
        'success': False,
        'message': 'Only POST requests are allowed'
    }, status=405)
