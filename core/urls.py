from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.product_list, name='product-list'),
]
