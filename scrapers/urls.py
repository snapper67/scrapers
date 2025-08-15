from django.urls import path
from . import views

from .views import ScrapeProductsPageView, get_processing_progress

# app_name = 'machine'
urlpatterns = [
    path("scrape_products/", ScrapeProductsPageView.as_view(), name="scrape_products"),
    path("get_processing_progress/", get_processing_progress, name="get_processing_progress"),
    # path("sysco_api/", SyscoApiPageView.as_view(), name="sysco_api"),
    path("usfoods/", views.scrape_usfoods, name="usfoods"),
    path("cw/", views.scrape_cw, name="cw"),
    path("breakthru/", views.scrape_breakthru, name="breakthru"),
    path("sg/", views.scrape_sg, name="sg"),
    path("birite/", views.scrape_birite, name="birite"),
    path("driscoll/", views.scrape_driscoll, name="driscoll"),
    path("primizie/", views.scrape_primizie, name="primizie"),
    path("sardilli/", views.scrape_sardilli, name="sardilli"),
    path("maple_vale/", views.scrape_maple_vale, name="maple_vale"),
    path("wagner/", views.scrape_wagner, name="wagner"),
    path("carmela/", views.scrape_carmela, name="carmela"),
    path("manson/", views.scrape_manson, name="manson"),
    path("indianhead/", views.scrape_indianhead, name="indianhead"),
    path("ab/", views.scrape_ab, name="ab"),
    path("sandw/", views.scrape_sandw, name="sandw"),
    path("southwest_traders/", views.scrape_southwest_traders, name="southwest_traders"),
    path("caruso/", views.scrape_caruso, name="caruso"),
    path("chefs_kitchen/", views.scrape_chefs_kitchen, name="chefs_kitchen"),
	path("cooks_company/", views.scrape_cooks_company, name="cooks_company"),
    path("christ_panos/", views.scrape_christ_panos, name="christ_panos"),
    path("derstines/", views.scrape_derstines, name="derstines"),
	path("scrapers/count-csv-rows/", views.count_csv_rows, name="count_csv_rows"),
    path("scrapers/update-distributor/", views.update_distributor, name="update_distributor"),
    path("scrapers/search-requests/", views.search_requests, name="search_requests"),

]
