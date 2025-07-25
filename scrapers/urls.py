from django.urls import path
from . import views

from .views import ScrapeProductsPageView

# app_name = 'machine'
urlpatterns = [
    # path("scrape_products/", ScrapeProductsPageView.as_view(), name="scrape_products"),
    # path("sysco_api/", SyscoApiPageView.as_view(), name="sysco_api"),
    path("usfoods/", views.scrape_home, name="usfoods"),

]
