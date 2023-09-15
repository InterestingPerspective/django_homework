from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, view_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('view/<int:pk>/', view_product, name='view_product')
]
