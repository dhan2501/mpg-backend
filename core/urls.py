from django.urls import path
from . import views
from core.views import index

urlpatterns = [
    path('api/products/', views.product_list, name='product-list'),
    path('api/banners/', views.banner_list, name='banner-list'),
    path('api/categories/', views.category_list, name='category-list'),
    path('api/menuitems/', views.menu_list, name='menu-list'),
    path('api/blogs/', views.blog_list, name='blog-list'),
    path('api/reviews/', views.reviews_list, name='reviews-list'),
    path('submit-review/', views.submit_review, name='submit_review'),
    # path('thank-you/', views.thank_you, name='thank_you'),  # Add this if you want a thank-you page
    path('create-blog/', views.create_blog, name='create_blog'),
    # path('blog-success/', views.blog_success, name='blog_success'),  # Optional success page
]