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

]
