from django.urls import path
from . import views
from core.views import index

urlpatterns = [
    path('api/products/', views.product_list, name='product-list'),
    path('', index),
]