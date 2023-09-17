from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogPostCreateView, BlogPostListView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('', BlogPostListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogPostDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete')
]
