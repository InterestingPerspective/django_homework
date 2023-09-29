from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, ProductCreateView, VersionListView, VersionUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', VersionListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('edit/<int:pk>/', VersionUpdateView.as_view(), name='edit_version'),
    path('create/', ProductCreateView.as_view(), name='create_product')
]
