from django.urls import path
from . import views

from .views import ScrapeProductsPageView

# app_name = 'machine'
urlpatterns = [
    path("scrape_products/", ScrapeProductsPageView.as_view(), name="scrape_products"),
    # path("sysco_api/", SyscoApiPageView.as_view(), name="sysco_api"),
    path("usfoods/", views.scrape_usfoods, name="usfoods"),
    path("cw/", views.scrape_cw, name="cw"),
    path("breakthru/", views.scrape_breakthru, name="breakthru"),
    path("sg/", views.scrape_sg, name="sg"),
    path("birite/", views.scrape_birite, name="birite"),
    path("primizie/", views.scrape_primizie, name="primizie"),
    path("sardilli/", views.scrape_sardilli, name="sardilli"),
    path("maple_valley/", views.scrape_maple_valley, name="maple_valley"),
    path("wagner/", views.scrape_wagner, name="wagner"),
    path("carmela/", views.scrape_carmela, name="carmela"),
    path("indianhead/", views.scrape_indianhead, name="indianhead"),
    path("ab/", views.scrape_ab, name="ab"),
    path("scrapers/count-csv-rows/", views.count_csv_rows, name="count_csv_rows"),
    path("scrapers/update-distributor/", views.update_distributor, name="update_distributor"),
    path("scrapers/search-requests/", views.search_requests, name="search_requests"),

]
