from django.urls import path
from .views import BannerAPIView, category_list, BlogListAPIView  # replace as needed

urlpatterns = [
    path('banners/', BannerAPIView.as_view(), name='banner-api'),
    path('categories/', category_list, name='category-list'),
    path('blogs/', BlogListAPIView.as_view(), name='blog-list'),
]
