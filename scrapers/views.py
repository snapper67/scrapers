import json
import os

import requests
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from scrapers.cut.birite import BiRiteScraper
from scrapers.cut.primizie import PrimizieScraper
from scrapers.cut.sardilli import SardilliScraper
from scrapers.misc.breakthru import BreakthruScraper
from scrapers.misc.chefswarehouse import ChefWarehouseScraper
from scrapers.misc.sg import SouthernGlazierScraper
from scrapers.misc.usfoods import USFoodsScraper
from .csvProcessor import CSVProcessor
from .cut.ab import ABScraper
from .cut.carmela import CarmelaScraper
from .cut.caruso import CarusoScraper
from .cut.chefs_kitchen import ChefsKitchenScraper
from .cut.christ_panos import ChristPanosScraper
from .cut.cooks import CooksCompanyScraper
from .cut.derstines import DerstinesScraper
from .cut.driscoll import DriscollScraper
from .cut.food_paper import FoodAndPaperScraper
from .cut.food_pro import FoodProScraper
from .cut.indianhead import IndianheadScraper
from .cut.manson import MansonScraper
from .cut.maple_vale import MapleValeScraper
from .cut.sandw import SandWScraper
from .cut.sierra_meat import SierraMeatScraper
from .cut.southwest_traders import SouthwestTradersScraper
from .cut.sunbelt import SunbeltScraper
from .cut.vitco_foods import VitcoScraper
from .cut.wagner import WagnerScraper
from .scraper import Scraper


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
	from scrapers.misc.chefswarehouse import ChefWarehouseScraper

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
	from scrapers.misc.chefswarehouse import ChefWarehouseScraper
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
	# Update boolean flags
	scraper = BreakthruScraper()
	category_ids = scraper.get_category_ids()
	category_names = scraper.get_category_names()
	category_urls = scraper.get_category_urls()
	print(post_data)

	# Update category and file names if category changes
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
		success, message = scraper.clean_data_file()
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
		# Generate a task ID immediately
		import uuid
		task_id = str(uuid.uuid4())

		print(f"Got - Task ID: {task_id}")

		# Store the necessary options in cache instead of the scraper instance
		from django.core.cache import cache
		cache_key = f'scraper_options_{task_id}'
		print(f"setting options in cache: {options}")
		# Store only the options we need for the scraper
		cache.set(cache_key, {
			'home_directory': options.get('home_directory', ''),
			'csv_start_row': options.get('csv_start_row', 0),
			'test_products': options.get('test_products', 0),
			'url_output_file': options.get('url_output_file', ''),
			'data_output_file': options.get('data_output_file', ''),
			'process_csv': options.get('process_csv', ''),
			'attempts': options.get('attempts', 40)
		}, timeout=3600)  # 1 hour timeout

		# Start the scraper in a background thread
		import threading
		from importlib import import_module

		def run_scraper_async(task_id, module_name, class_name):
			print(f"run_scraper_async()")
			try:
				# Import the scraper class dynamically
				module = import_module(module_name)
				ScraperClass = getattr(module, class_name)
				print(f"Imported scraper class: {ScraperClass}")
				# Create a new scraper instance in the background thread
				with ScraperClass() as scraper:  # Create a new instance of the ScraperClass()
					scraper.current_task_id = task_id

					# Get the options from cache
					options = cache.get(f'scraper_options_{task_id}', {})
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
					'task_id': task_id
				}
				cache.set(f'product_processing_progress_{task_id}', progress_data, timeout=3600)

		# Get the module and class name for dynamic import
		scraper_module = scraper.__class__.__module__
		scraper_class = scraper.__class__.__name__

		# Start the scraper in a background thread
		thread = threading.Thread(
			target=run_scraper_async,
			args=(task_id, scraper_module, scraper_class),
			daemon=True  # Allow the thread to be terminated when the main thread exits
		)
		print("Starting thread")
		thread.start()

		# Return the task ID to the client immediately
		print(f"Returning task ID: {task_id}")
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
