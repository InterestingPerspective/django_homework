from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, ProductCreateView, VersionUpdateView, \
    VersionCreateView, ProductListView, ProductUpdateView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('version/<int:pk>/update/', VersionUpdateView.as_view(), name='update_version'),
    path('version/', VersionCreateView.as_view(), name='create_version'),
    path('product/', ProductCreateView.as_view(), name='create_product'),
    path('categories/', CategoryListView.as_view(), name='categories')
]
