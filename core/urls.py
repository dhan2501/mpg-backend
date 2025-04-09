from django.urls import path
from . import views
from core.views import index

urlpatterns = [
    path('api/products/', views.product_list, name='product-list'),
    path('api/banners/', views.banner_list, name='banner-list'),
    path('api/categories/', views.category_list, name='category-list'),
    path('api/menuitems/', views.menu_list, name='menu-list'),
    path('api/blogs/', views.blog_list, name='blog-list'),
    path('', index),
]