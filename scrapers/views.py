import os
import importlib
import inspect
from pathlib import Path
import requests
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from scrapers.cut.birite import BiRiteScraper
from scrapers.cut.cheese_importers import CheeseImportersScraper
from scrapers.cut.creamco import CreamCoScraper
from scrapers.cut.primizie import PrimizieScraper
from scrapers.cut.sardilli import SardilliScraper
from scrapers.misc.breakthru import BreakthruScraper
from scrapers.misc.chefswarehouse import ChefWarehouseScraper
from scrapers.misc.sg import SouthernGlazierScraper
from scrapers.misc.usfoods import USFoodsScraper
from .csvProcessor import CSVProcessor
from .cut.ab import ABScraper
from .cut.acme_steak import AcmeSteakScraper
from .cut.all_fresh_seafood import AllFreshSeafoodScraper
from .cut.alpeake import AlpeakeScraper
from .cut.apito import ApitoScraper
from .cut.carmela import CarmelaScraper
from .cut.caruso import CarusoScraper
from .cut.chefs_kitchen import ChefsKitchenScraper
from .cut.christ_panos import ChristPanosScraper
from .cut.cooks import CooksCompanyScraper
from .cut.crookbros import CrookBrosScraper
from .cut.cusumanoandsons import CusumanoAndSonsScraper
from .cut.derstines import DerstinesScraper
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
from .cut.whatchefswant_south import WhatChefsWantSouthScraper
from .cut.woolcofoods import WoolcoFoodsScraper
from .misc.cheneybrothers import CheneyBrothersScraper
from .scraper import Scraper

# List of all scraper classes
SCRAPER_CLASSES = [
]

# Get the directory containing the scrapers
scrapers_cut_dir = os.path.join(os.path.dirname(__file__), 'cut')
scrapers_misc_dir = os.path.join(os.path.dirname(__file__), 'misc')

# Import all Python files in the cut directory
for filename in os.listdir(scrapers_cut_dir):
    if filename.endswith('.py') and not filename.startswith('_') and filename != 'dry.py':
        module_name = filename[:-3]  # Remove .py extension
        try:
            module = importlib.import_module(f'scrapers.cut.{module_name}')
            # Get all classes in the module that end with 'Scraper'
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if name.endswith('Scraper') and hasattr(obj, 'VENDOR_NAME') and hasattr(obj, 'DEFAULT_DIRECTORY') and name != 'CutScraper':
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
                if name.endswith('Scraper') and hasattr(obj, 'VENDOR_NAME') and hasattr(obj, 'DEFAULT_DIRECTORY') and name != 'CutScraper':
                    SCRAPER_CLASSES.append(obj)
        except Exception as e:
            print(f"Error importing {module_name}: {e}")
print(SCRAPER_CLASSES)


class ScrapeProductsPageView(TemplateView):
    template_name = "scrape_products/scrape_home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


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


def update_common_options(post_data, current_options):
    # Update boolean flags
    current_options['get_categories'] = 'get_categories' in post_data
    current_options['scrape_products'] = 'scrape_products' in post_data
    current_options['process_csv'] = 'process_csv' in post_data
    current_options['reprocess_csv'] = 'reprocess_csv' in post_data
    current_options['process_extra'] = 'process_extra' in post_data
    current_options['search_requests'] = 'search_requests' in post_data
    current_options['dedupe_csv'] = 'dedupe_csv' in post_data
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

    # Add directory for CSV row counting
    csv_dir = post_data.get('csv_dir', '')
    if csv_dir and os.path.isdir(csv_dir):
        current_options['csv_dir'] = csv_dir

    return current_options


def count_csv_rows(request):
    """
    Count rows in all CSV files with 'data' or 'urls' in their names across subdirectories.
    Returns JSON response with the results.
    """
    if request.method == 'POST':
        directory = request.POST.get('directory', '')
        if not directory or not os.path.isdir(directory):
            return JsonResponse(
                {'error': 'Invalid or missing directory'},
                status=400
            )

        try:
            # Get row counts using CSVProcessor
            results = CSVProcessor.count_rows_in_data_csvs(directory)

            # The results are already in the correct format from CSVProcessor
            # Calculate the total number of rows across all directories
            total_data_rows = sum(directory_data.get('data_rows', 0)
                                  for directory_data in results.values())

            total_url_rows = sum(directory_data.get('url_rows', 0)
                                 for directory_data in results.values())

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

        if not directory or not distributor_name:
            return JsonResponse(
                {'success': False, 'error': 'Both directory and distributor name are required'},
                status=400
            )

        try:
            # Call the CSV processor to update distributor names
            results = CSVProcessor.update_distributor_in_csvs(directory, distributor_name)
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
        # 'url_file': f"{usfoods_options.get('category_name').lower()}_product_urls.csv",
        # 'data_file': f"{usfoods_options.get('category_name').lower()}_product_data.csv"
    }
    return defaults


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
            scraper.set_options(options)
            result = scraper.run()
            return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    from scrapers.misc.usfoods import USFoodsScraper
    scraper = USFoodsScraper()
    distributor_options = scraper.get_options()
    category_ids = scraper.get_category_ids()

    categories = [{'id': k, 'name': v} for k, v in category_ids.items()]

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_usfoods.html', {
        'categories': categories,
        'defaults': defaults,
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
            result = scraper.run()
            return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form

    scraper = ChefWarehouseScraper()
    distributor_options = scraper.get_options()
    category_ids = scraper.get_category_ids()
    categories = []
    for category_id, category_name in category_ids.items():
        categories.append({
            'id': category_id,
            'name': category_name,
            'url_file': f"{category_id.lower()}_urls.csv",
            'data_file': f"{category_id.lower()}_data.csv"
        })

    defaults = set_defaults(distributor_options)

    return render(request, 'scrape_products/scrape_cw.html', {
        'categories': categories,
        'defaults': defaults,
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


def scrape_cheney_brothers(request):
    print("scrape_cheney_brothers()")
    options = {}

    if request.method == 'POST':
        with CheneyBrothersScraper(options) as scraper:
            distributor_options = scraper.get_options()
            # Create a copy of options for this request
            options = update_cheney_brothers(request.POST, distributor_options)
            options = update_common_options(request.POST, options)
            # Run the scraper
            scraper.set_options(options)
            print("running scraper")
            result = scraper.run()
            return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form

    scraper = CheneyBrothersScraper()
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
        'name': 'Cheney Brothers'
    })


def update_cheney_brothers(post_data, current_options):
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
            result = scraper.run()
            return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = BreakthruScraper()
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
    })


def update_sg_options(post_data, current_options):
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


def scrape_sg(request):
    options = {}

    if request.method == 'POST':
        with SouthernGlazierScraper(options) as scraper:
            print(request.POST)
            distributor_options = scraper.get_options()

            options = update_sg_options(request.POST, distributor_options)
            options = update_common_options(request.POST, options)
            # Run the scraper
            scraper.set_options(options)
            result = scraper.run()
            return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = SouthernGlazierScraper()
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
    })


def process_cut_post(request, scraper):
    print(request.POST)
    print("process_cut_post()")
    distributor_options = scraper.get_options()

    # Update options from form data
    options = update_cut_options(request.POST, distributor_options)
    options = update_common_options(request.POST, options)

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
    # Check if this is an AJAX request for processing CSV
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and options.get('process_csv'):
        # Import the thread manager
        from .thread_manager import start_background_task
        from importlib import import_module

        # Define the scraper function that will run in the background
        def run_scraper(module_name, class_name, options):
            print(f"Starting scraper in background()")
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
            'attempts': options.get('attempts', 40)
        }

        # Get the module and class name for dynamic import
        scraper_module = scraper.__class__.__module__
        scraper_class = scraper.__class__.__name__

        import uuid
        task_id = str(uuid.uuid4())

        # Start the scraper in a background thread using the thread manager
        task_id = start_background_task(
            target=run_scraper,
            task_id=task_id,
            args=(scraper_module, scraper_class, scraper_options),
            timeout=3600  # 1 hour timeout
        )

        print(f"Started background task with ID: {task_id}")
        return JsonResponse({'task_id': task_id}, status=200)

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


def scrape_birite(request):
    options = {}

    if request.method == 'POST':
        with BiRiteScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = BiRiteScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_primizie(request):
    options = {}

    if request.method == 'POST':
        with PrimizieScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = PrimizieScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_sardilli(request):
    options = {}

    if request.method == 'POST':
        with SardilliScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = SardilliScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_maple_vale(request):
    options = {}

    if request.method == 'POST':
        with MapleValeScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = MapleValeScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_wagner(request):
    options = {}

    if request.method == 'POST':
        with WagnerScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = WagnerScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_carmela(request):
    options = {}

    if request.method == 'POST':
        with CarmelaScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = CarmelaScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_manson(request):
    options = {}

    if request.method == 'POST':
        with MansonScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = MansonScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_indianhead(request):
    options = {}

    if request.method == 'POST':
        with IndianheadScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = IndianheadScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_ab(request):
    options = {}

    if request.method == 'POST':
        with ABScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = ABScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_sandw(request):
    options = {}

    if request.method == 'POST':
        with SandWScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = SandWScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_southwest_traders(request):
    options = {}

    if request.method == 'POST':
        with SouthwestTradersScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = SouthwestTradersScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_caruso(request):
    options = {}

    if request.method == 'POST':
        with CarusoScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = CarusoScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_chefs_kitchen(request):
    options = {}

    if request.method == 'POST':
        with ChefsKitchenScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = ChefsKitchenScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_cooks_company(request):
    options = {}

    if request.method == 'POST':
        with CooksCompanyScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = CooksCompanyScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_christ_panos(request):
    options = {}

    if request.method == 'POST':
        with ChristPanosScraper(options) as scraper:
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = ChristPanosScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_derstines(request):
    print("Calling scrape_derstines()")
    options = {}

    if request.method == 'POST':
        with DerstinesScraper(options) as scraper:
            print("Calling process_cut_post from scrape_derstines()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = DerstinesScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_driscoll(request):
    options = {}

    if request.method == 'POST':
        with DriscollScraper(options) as scraper:
            print("Calling process_cut_post from ()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = DriscollScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_foodandpaper(request):
    print("Calling scrape_derstines()")
    options = {}

    if request.method == 'POST':
        with FoodAndPaperScraper(options) as scraper:
            print("Calling process_cut_post from scrape_derstines()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = FoodAndPaperScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_vitco_foods(request):
    print("Calling scrape_derstines()")
    options = {}

    if request.method == 'POST':
        with VitcoScraper(options) as scraper:
            print("Calling process_cut_post from scrape_derstines()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = VitcoScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })


def scrape_sunbelt(request):
    print("Calling scrape_derstines()")
    options = {}

    if request.method == 'POST':
        with SunbeltScraper(options) as scraper:
            print("Calling process_cut_post from scrape_derstines()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = SunbeltScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_prdeli(request):
    """View for scraping PRDeli"""
    if request.method == 'POST':
        return process_cut_post(request, PRDeliScraper)
    
    # For GET request, show the form with current options
    context = {
        'title': 'PRDeli Scraper',
        'distributor_name': 'PRDeli',
        'distributor_slug': 'prdeli',
        'options': PRDeliScraper.DEFAULT_OPTIONS,
        'categories': getattr(PRDeliScraper, 'CATEGORIES', None),
        'is_cut_scraper': True,
    }
    return render(request, 'scrape_products/scrape_form.html', context)

def scrape_alpeake(request):
    """View for scraping 406 Market"""
    print("Calling scrape_foodpro()")
    options = {}

    if request.method == 'POST':
        with AlpeakeScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = AlpeakeScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_apito(request):
    print("Calling scrape_foodpro()")
    options = {}

    if request.method == 'POST':
        with ApitoScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = ApitoScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_sierra_meat(request):
    print("Calling scrape_derstines()")
    options = {}

    if request.method == 'POST':
        with SierraMeatScraper(options) as scraper:
            print("Calling process_cut_post from scrape_derstines()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = SierraMeatScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_foodpro(request):
    print("Calling scrape_foodpro()")
    options = {}

    if request.method == 'POST':
        with FoodProScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = FoodProScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_market_406(request):
    """View for scraping 406 Market"""
    print("Calling scrape_market_406()")
    options = {}

    if request.method == 'POST':
        with Market406Scraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = Market406Scraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })
def scrape_acme_steak(request):
    print("Calling scrape_acme_steak()")
    options = {}

    if request.method == 'POST':
        with AcmeSteakScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = AcmeSteakScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_all_fresh_seafood(request):
    print("Calling scrape_all_fresh_seafood()")
    options = {}

    if request.method == 'POST':
        with AllFreshSeafoodScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = AllFreshSeafoodScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_cheese_importers(request):
    """View for scraping Cheese Importers"""
    print("Calling scrape_cheese_importers()")
    options = {}

    if request.method == 'POST':
        with CheeseImportersScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = CheeseImportersScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_creamco(request):
    """View for scraping CreamCo"""
    print("Calling scrape_creamco()")
    options = {}

    if request.method == 'POST':
        with CreamCoScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = CreamCoScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_crookbros(request):
    """View for scraping Crook & Co."""
    print("Calling scrape_crookbros()")
    options = {}

    if request.method == 'POST':
        with CrookBrosScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = CrookBrosScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_cusumanoandsons(request):
    """View for scraping Cusumano & Sons"""
    print("Calling scrape_cusumanoandsons()")
    options = {}

    if request.method == 'POST':
        with CusumanoAndSonsScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = CusumanoAndSonsScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_dwcspecialties(request):
    """View for scraping DWC Specialties"""
    print("Calling scrape_dwcspecialties()")
    options = {}

    if request.method == 'POST':
        with DWCSpecialtiesScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = DWCSpecialtiesScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_fourstarmeat(request):
    """View for scraping Four Star Meat"""
    print("Calling scrape_fourstarmeat()")
    options = {}

    if request.method == 'POST':
        with FourStarMeatScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = FourStarMeatScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_hooktofork(request):
    """View for scraping Hook to Fork"""
    print("Calling scrape_hooktofork()")
    options = {}

    if request.method == 'POST':
        with HookToForkScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = HookToForkScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_jordanpaige(request):
    """View for scraping Jordan Paige"""
    print("Calling scrape_jordanpaige()")
    options = {}

    if request.method == 'POST':
        with JordanPaigeScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = JordanPaigeScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_misterproduce(request):
    """View for scraping Mister Produce"""
    print("Calling scrape_misterproduce()")
    options = {}

    if request.method == 'POST':
        with MisterProduceScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = MisterProduceScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_pacificprovisions(request):
    """View for scraping Pacific Provisions"""
    print("Calling scrape_pacificprovisions()")
    options = {}

    if request.method == 'POST':
        with PacificProvisionsScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = PacificProvisionsScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_prdeli(request):
    """View for scraping Pacific Provisions"""
    print("Calling scrape_prdeli()")
    options = {}

    if request.method == 'POST':
        with PRDeliScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = PRDeliScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_rarefoods(request):
    """View for scraping Rare Foods"""
    print("Calling scrape_rarefoods()")
    options = {}

    if request.method == 'POST':
        with RareFoodsScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = RareFoodsScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_realityfoods(request):
    """View for scraping Reality Foods"""
    print("Calling scrape_realityfoods()")
    options = {}

    if request.method == 'POST':
        with RealityFoodsScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = RealityFoodsScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_safradistribution(request):
    """View for scraping Safra Distribution"""
    print("Calling scrape_safradistribution()")
    options = {}

    if request.method == 'POST':
        with SafraDistributionScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = SafraDistributionScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_savalfoodservice(request):
    """View for scraping Saval Foodservice"""
    print("Calling scrape_savalfoodservice()")
    options = {}

    if request.method == 'POST':
        with SavalFoodserviceScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = SavalFoodserviceScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_socomeatco(request):
    """View for scraping SoCo Meat Co"""
    print("Calling scrape_socomeatco()")
    options = {}

    if request.method == 'POST':
        with SoCoMeatCoScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = SoCoMeatCoScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_sutters(request):
    """View for scraping Sutter's Food Group"""
    print("Calling scrape_sutters()")
    options = {}

    if request.method == 'POST':
        with SuttersScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = SuttersScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_thefishguys(request):
    """View for scraping The Fish Guys"""
    print("Calling scrape_thefishguys()")
    options = {}

    if request.method == 'POST':
        with TheFishGuysScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = TheFishGuysScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_tolteca(request):
    """View for scraping Tolteca"""
    print("Calling scrape_tolteca()")
    options = {}

    if request.method == 'POST':
        with ToltecaScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = ToltecaScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_valleygold(request):
    """View for scraping Valley Gold"""
    print("Calling scrape_valleygold()")
    options = {}

    if request.method == 'POST':
        with ValleyGoldScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = ValleyGoldScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_whatchefswant_south(request):
    """View for scraping What Chefs Want - South"""
    print("Calling scrape_whatchefswant_south()")
    options = {}

    if request.method == 'POST':
        with WhatChefsWantSouthScraper(options) as scraper:
            print("Calling process_cut_post from scrape_foodpro()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = WhatChefsWantSouthScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_hearty(request):
    """View for scraping Hearty"""
    print("Calling scrape_hearty()")
    options = {}

    if request.method == 'POST':
        with HeartyScraper(options) as scraper:
            print("Calling process_cut_post from scrape_hearty()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = HeartyScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_totalfoods(request):
    """View for scraping Total Foods"""
    print("Calling scrape_totalfoods()")
    options = {}

    if request.method == 'POST':
        with TotalFoodsScraper(options) as scraper:
            print("Calling process_cut_post from scrape_totalfoods()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = TotalFoodsScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scrape_woolcofoods(request):
    """View for scraping Woolco Foods"""
    print("Calling scrape_woolcofoods()")
    options = {}

    if request.method == 'POST':
        with WoolcoFoodsScraper(options) as scraper:
            print("Calling process_cut_post from scrape_woolcofoods()")
            result = process_cut_post(request, scraper)
            if isinstance(result, str):
                return render(request, 'scrape_products/scrape_results.html', {'result': result})
            else:
                return result

    # GET request - show form
    scraper = WoolcoFoodsScraper()
    distributor_options = scraper.get_options()
    categories, total_products = update_cut_categories(request.POST, scraper)

    defaults = set_defaults(distributor_options)
    defaults.update({'attempts': 40})

    return render(request, 'scrape_products/scrape_cut.html', {
        'categories': categories,
        'defaults': defaults,
        'name': scraper.get_name(),
        'total_products': total_products
    })

def scraper_status(request):
    """
    Display a status page showing summary information for all scrapers.
    """
    # Base directory where scraper data is stored
    base_dir = '/Users/mark/Downloads/scrapers'
    
    # Get all subdirectories (each represents a scraper)
    try:
        scraper_dirs = [d for d in os.listdir(base_dir) 
                      if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith('.')]
    except FileNotFoundError:
        return render(request, 'scrape_products/status.html', {
            'error': f'Directory not found: {base_dir}'
        })
    
    scraper_data = []
    
    for scraper_dir in sorted(scraper_dirs):
        dir_path = os.path.join(base_dir, scraper_dir)
        data_files = glob.glob(os.path.join(dir_path, '*_data.csv'))
        url_files = glob.glob(os.path.join(dir_path, '*_urls.csv'))
        
        # Count rows in data files
        data_rows = 0
        for file in data_files:
            try:
                df = pd.read_csv(file, on_bad_lines='skip')
                data_rows += len(df)
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
        
        scraper_data.append({
            'name': scraper_dir,
            'data_rows': data_rows,
            'url_rows': url_rows,
            'percent_complete': percent_complete,
            'status': 'Complete' if url_rows > 0 and data_rows >= url_rows else 'In Progress',
            'formatted_data_rows': intcomma(data_rows),
            'formatted_url_rows': intcomma(url_rows)
        })
    
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

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.humanize.templatetags.humanize import intcomma
import os
import json
import glob
import pandas as pd

# Import all scraper classes
from .cut.acme_steak import AcmeSteakScraper
from .cut.ab import ABScraper
from .cut.alpeake import AlpeakeScraper
# Import other scrapers here...


def get_scraper_data(scraper_class):
    """Get data for a single scraper class"""
    try:
        # Create an instance of the scraper
        scraper = scraper_class()
        
        # Get the directory and vendor name
        directory = getattr(scraper, 'DEFAULT_DIRECTORY', None)
        vendor_name = getattr(scraper, 'VENDOR_NAME', scraper_class.__name__)
        
        if not directory or not os.path.exists(directory):
            return None
            
        # Find data and URL files
        data_files = glob.glob(os.path.join(directory, '*_data.csv'))
        url_files = glob.glob(os.path.join(directory, '*_urls.csv'))
        
        # Count rows in data files
        data_rows = 0
        for file in data_files:
            try:
                df = pd.read_csv(file, on_bad_lines='skip')
                data_rows += len(df)
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
            'data_rows': data_rows,
            'url_rows': url_rows,
            'percent_complete': percent_complete,
            'status': 'Complete' if url_rows > 0 and data_rows >= url_rows else 'In Progress',
            'class_name': scraper_class.__name__,
        }
        
    except Exception as e:
        print(f"Error processing {scraper_class.__name__}: {e}")
        return None

def scraper_status(request):
    """
    Display a status page showing summary information for all scrapers.
    """
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

from django.shortcuts import render
from .thread_manager import thread_manager

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

from django.shortcuts import render, redirect
from django.contrib import messages
from .thread_manager import thread_manager

def stop_task(request, task_id):
    """View to stop a running task."""
    if request.method == 'POST':
        stopped = thread_manager.stop_thread(task_id)
        if stopped:
            messages.success(request, f'Task {task_id} has been stopped.')
        else:
            messages.error(request, f'Failed to stop task {task_id} or task was not found.')
    
    return redirect('task_status')
