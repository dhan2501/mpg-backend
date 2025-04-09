from django.http import JsonResponse
from .models import Product, Banner, Category, MenuItem, Blog
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def menu_list(request):
    menuitems = list(MenuItem.objects.values())
    return JsonResponse(menuitems, safe=False)

def product_list(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)

def category_list(request):
    categories = list(Category.objects.values())
    return JsonResponse(categories, safe=False)

def banner_list(request):
    banners = list(Banner.objects.values())
    return JsonResponse(banners, safe=False)

def blog_list(request):
    blogs = list(Blog.objects.values())
    return JsonResponse(blogs, safe=False)

