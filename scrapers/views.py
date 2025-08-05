from django.shortcuts import render
from django.views.generic import TemplateView

from .usfoods import USFoodsScraper
from .chefswarehouse import ChefWarehouseScraper
from .breakthru import BreakthruScraper
from .sg import SouthernGlazierScraper

class ScrapeProductsPageView(TemplateView):
    template_name = "scrape_products/scrape_home.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)


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
    current_options['scrape_products'] = 'scrape_products' in post_data
    current_options['process_csv'] = 'process_csv' in post_data
    current_options['reprocess_csv'] = 'reprocess_csv' in post_data
    current_options['dedupe_csv'] = 'dedupe_csv' in post_data
    current_options['count_csv'] = 'count_csv' in post_data

    # Update numerical values with defaults
    current_options['test_products'] = int(post_data.get('test_products', current_options.get('test_products', 10)))
    current_options['test_categories'] = int(post_data.get('test_categories', current_options.get('test_categories', 10)))
    current_options['max_products'] = int(post_data.get('max_products', current_options.get('max_products', 500)))
    current_options['csv_start_row'] = int(post_data.get('start_row', current_options.get('csv_start_row', 0)))
    current_options['category_to_process'] = int(
        post_data.get('category_to_process', current_options.get('category_to_process', 0)))
    current_options['home_directory'] = str(post_data.get('home_directory', current_options.get('home_directory', '')))


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

def scrape_home(request):
    options = {}
    from .usfoods import USFoodsScraper

    if request.method == 'POST':
        with USFoodsScraper(options) as scraper:
            usfoods_options = scraper.get_options()
            # Create a copy of options for this request
            options = update_usfoods_options(request.POST, usfoods_options)

            skus_to_check = request.POST.get('skus', '').split(',')  # Get SKUs from form input
            skus_to_check = [sku.strip() for sku in skus_to_check if sku.strip()]
            options['skus_to_check'] = skus_to_check
            # Run the scraper
            scraper.set_options(options)
            result = scraper.run()
            return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    from .usfoods import USFoodsScraper
    scraper = USFoodsScraper()
    usfoods_options = scraper.get_options()
    category_ids = scraper.get_category_ids()
    categories = []
    for category_id, category_name in category_ids.items():
        categories.append({
            'id': category_id,
            'name': category_name,
            'url_file': f"{category_id.lower()}_urls.csv",
            'data_file': f"{category_id.lower()}_data.csv"
        })

    categories = [{'id': k, 'name': v} for k, v in category_ids.items()]

    return render(request, 'scrape_products/scrape_usfoods.html', {
        'categories': categories,
        'defaults': {
            'home_directory': usfoods_options.get('home_directory', '.'),
            'scrape_products': usfoods_options.get('scrape_products'),
            'process_csv': usfoods_options.get('process_csv'),
            'reprocess_csv': usfoods_options.get('reprocess_csv'),
            'dedupe_csv': usfoods_options.get('dedupe_csv'),
            'count_csv': usfoods_options.get('count_csv'),
            'start_row': usfoods_options.get('csv_start_row'),
            'max_products': usfoods_options.get('max_products'),
            'test_products': usfoods_options.get('test_products'),
            'test_categories': usfoods_options.get('test_categories'),
            'category_to_process': usfoods_options.get('category_to_process'),
            # 'url_file': f"{usfoods_options.get('category_name').lower()}_product_urls.csv",
            # 'data_file': f"{usfoods_options.get('category_name').lower()}_product_data.csv"
        }
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
    current_options['scrape_products'] = 'scrape_products' in post_data
    current_options['process_csv'] = 'process_csv' in post_data
    current_options['process_extra'] = 'process_extra' in post_data
    current_options['reprocess_csv'] = 'reprocess_csv' in post_data
    current_options['dedupe_csv'] = 'dedupe_csv' in post_data
    current_options['count_csv'] = 'count_csv' in post_data

    # Update numerical values with defaults
    current_options['test_products'] = int(post_data.get('test_products', current_options.get('test_products', 10)))
    current_options['test_categories'] = int(post_data.get('test_categories', current_options.get('test_categories', 10)))
    current_options['max_products'] = int(post_data.get('max_products', current_options.get('max_products', 500)))
    current_options['csv_start_row'] = int(post_data.get('start_row', current_options.get('csv_start_row', 0)))
    current_options['category_to_process'] = int(
        post_data.get('category_to_process', current_options.get('category_to_process', 0)))
    current_options['home_directory'] = str(post_data.get('home_directory', current_options.get('home_directory', '')))


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
    from .chefswarehouse import ChefWarehouseScraper

    if request.method == 'POST':
        with ChefWarehouseScraper(options) as scraper:
            cw_options = scraper.get_options()
            # Create a copy of options for this request
            options = update_cw_options(request.POST, cw_options)

            skus_to_check = request.POST.get('skus', '').split(',')  # Get SKUs from form input
            skus_to_check = [sku.strip() for sku in skus_to_check if sku.strip()]
            options['skus_to_check'] = skus_to_check
            # Run the scraper
            scraper.set_options(options)
            result = scraper.run()
            return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    from .chefswarehouse import ChefWarehouseScraper
    scraper = ChefWarehouseScraper()
    cw_options = scraper.get_options()
    category_ids = scraper.get_category_ids()
    categories = []
    for category_id, category_name in category_ids.items():
        categories.append({
            'id': category_id,
            'name': category_name,
            'url_file': f"{category_id.lower()}_urls.csv",
            'data_file': f"{category_id.lower()}_data.csv"
        })

    categories = [{'id': k, 'name': v} for k, v in category_ids.items()]

    return render(request, 'scrape_products/scrape_cw.html', {
        'categories': categories,
        'defaults': {
            'home_directory': cw_options.get('home_directory', '.'),
            'scrape_products': cw_options.get('scrape_products'),
            'process_csv': cw_options.get('process_csv'),
            'process_extra': cw_options.get('process_extra'),
            'reprocess_csv': cw_options.get('reprocess_csv'),
            'dedupe_csv': cw_options.get('dedupe_csv'),
            'count_csv': cw_options.get('count_csv'),
            'start_row': cw_options.get('csv_start_row'),
            'max_products': cw_options.get('max_products'),
            'test_products': cw_options.get('test_products'),
            'test_categories': cw_options.get('test_categories'),
            'category_to_process': cw_options.get('category_to_process'),
            # 'url_file': f"{usfoods_options.get('category_name').lower()}_product_urls.csv",
            # 'data_file': f"{usfoods_options.get('category_name').lower()}_product_data.csv"
        }
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
    current_options['scrape_products'] = 'scrape_products' in post_data
    current_options['process_csv'] = 'process_csv' in post_data
    current_options['process_extra'] = 'process_extra' in post_data
    current_options['reprocess_csv'] = 'reprocess_csv' in post_data
    current_options['dedupe_csv'] = 'dedupe_csv' in post_data
    current_options['count_csv'] = 'count_csv' in post_data
    current_options['get_categories'] = 'get_categories' in post_data

    # Update numerical values with defaults
    current_options['test_products'] = int(post_data.get('test_products', current_options.get('test_products', 10)))
    current_options['test_categories'] = int(post_data.get('test_categories', current_options.get('test_categories', 10)))
    current_options['max_products'] = int(post_data.get('max_products', current_options.get('max_products', 500)))
    current_options['csv_start_row'] = int(post_data.get('start_row', current_options.get('csv_start_row', 0)))
    current_options['category_to_process'] = int(
        post_data.get('category_to_process', current_options.get('category_to_process', 0)))
    current_options['home_directory'] = str(post_data.get('home_directory', current_options.get('home_directory', '')))


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

            skus_to_check = request.POST.get('skus', '').split(',')  # Get SKUs from form input
            skus_to_check = [sku.strip() for sku in skus_to_check if sku.strip()]
            options['skus_to_check'] = skus_to_check
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
            'url_file': f"{scraper.make_filename_safe(category['id'])}_product_urls.csv",
            'data_file': f"{scraper.make_filename_safe(category['id'])}_product_data.csv"
        })

    # categories = [{'id': k, 'name': v} for k, v in category_ids.items()]

    return render(request, 'scrape_products/scrape_breakthru.html', {
        'categories': categories,
        'defaults': {
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
            # 'url_file': f"{usfoods_options.get('category_name').lower()}_product_urls.csv",
            # 'data_file': f"{usfoods_options.get('category_name').lower()}_product_data.csv"
        }
    })
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
    return current_options

def update_sg_options(post_data, current_options):
    """
    Update usfoods_options based on form POST data.

    Args:
        post_data: request.POST dictionary
        current_options: Current usfoods_options to update

    Returns:
        Updated usfoods_options dictionary
    """
    # Update boolean flags
    scraper = SouthernGlazierScraper()

    # current_options['scrape_products'] = 'scrape_products' in post_data
    # current_options['process_csv'] = 'process_csv' in post_data
    # current_options['process_extra'] = 'process_extra' in post_data
    # current_options['reprocess_csv'] = 'reprocess_csv' in post_data
    # current_options['search_requests'] = 'search_requests' in post_data
    # current_options['dedupe_csv'] = 'dedupe_csv' in post_data
    # current_options['count_csv'] = 'count_csv' in post_data
    # current_options['get_categories'] = 'get_categories' in post_data

    # Update numerical values with defaults
    # current_options['test_products'] = int(post_data.get('test_products', current_options.get('test_products', 10)))
    # current_options['test_categories'] = int(post_data.get('test_categories', current_options.get('test_categories', 10)))
    # current_options['max_products'] = int(post_data.get('max_products', current_options.get('max_products', 500)))
    # current_options['csv_start_row'] = int(post_data.get('start_row', current_options.get('csv_start_row', 0)))
    # current_options['category_to_process'] = int(
    #     post_data.get('category_to_process', current_options.get('category_to_process', 0)))
    # current_options['home_directory'] = str(post_data.get('home_directory', current_options.get('home_directory', '')))
    #
    # current_options['url'] = str(post_data.get('url', ''))
    # current_options['search_term'] = str(post_data.get('search_term', ''))

    # Update category and file names if category changes
    category_id = post_data.get('category_id')
    if category_id and int(category_id) != 0:
        categories = scraper.get_categories()
        # for category in categories:
        #     if category['id'] == int(category_id):
        #         category_name = category['name']
        #         break
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
def scrape_sg(request):
    options = {}

    if request.method == 'POST':
        with SouthernGlazierScraper(options) as scraper:
            print(request.POST)
            distributor_options = scraper.get_options()

            options = update_sg_options(request.POST, distributor_options)
            options = update_common_options(request.POST, options)

            # This is not implemented yet
            skus_to_check = request.POST.get('skus', '').split(',')  # Get SKUs from form input
            skus_to_check = [sku.strip() for sku in skus_to_check if sku.strip()]
            options['skus_to_check'] = skus_to_check

            # Run the scraper
            scraper.set_options(options)
            result = scraper.run()
            return render(request, 'scrape_products/scrape_results.html', {'result': result})

    # GET request - show form
    scraper = SouthernGlazierScraper()
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
            'name': category['name'],
            'url_file': f"{scraper.make_filename_safe(category['name'])}_product_urls.csv",
            'data_file': f"{scraper.make_filename_safe(category['name'])}_product_data.csv"
        })

    # categories = [{'id': k, 'name': v} for k, v in category_ids.items()]

    return render(request, 'scrape_products/scrape_sg.html', {
        'categories': categories,
        'defaults': {
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
    })