from django.shortcuts import render
from django.views.generic import TemplateView

from .usfoods import USFoodsScraper

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