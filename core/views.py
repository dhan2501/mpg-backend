from django.http import JsonResponse
from .models import Product, Banner, Category, MenuItem, Blog, ProductReview
from django.shortcuts import render, redirect
from .models import ProductReview
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductReviewSerializer
from django.utils.decorators import method_decorator

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

@csrf_exempt
@api_view(['GET'])
def reviews_list(request):
    reviews = list(ProductReview.objects.values())
    return JsonResponse(reviews, safe=False)

# csrf_exempt
# @api_view(['POST'])
# def reviews_list(request):
#     print("POST DATA:", request.data)  # 👈 Debug
#     serializer = ProductReviewSerializer(data=request.data)
#     if serializer.is_valid():
#         review = serializer.save()
#         print("Saved Review:", review)  # 👈 Debug
#         return Response({'message': 'Review submitted successfully!'}, status=status.HTTP_201_CREATED)
#     else:
#         print("Serializer errors:", serializer.errors)  # 👈 Debug
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt  # Exempt CSRF for frontend JS forms
@api_view(['GET', 'POST'])
def reviews_list(request):
    if request.method == 'GET':
        reviews = ProductReview.objects.all()
        serializer = ProductReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Review submitted!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# without popup thankyou page
# def submit_review(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         comment = request.POST.get('comment')

#         ProductReview.objects.create(
#             name=name,
#             email=email,
#             comment=comment,
#             is_active=False  # Default; can be omitted
#         )
#         return redirect('thank_you')  # Redirect after submission

#     return render(request, 'reviews/review_form.html')

# With popup
def submit_review(request):
    success = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        ProductReview.objects.create(
            name=name,
            email=email,
            comment=comment,
            is_active=False
        )
        success = True  # trigger popup

    return render(request, 'reviews/review_form.html', {'success': success})

def thank_you(request):
    return render(request, 'thank_you.html')



from django.shortcuts import render
from .models import Blog

def create_blog(request):
    success = False

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        meta_title = request.POST.get('meta_title')
        meta_description = request.POST.get('meta_description')
        content = request.POST.get('content')

        Blog.objects.create(
            title=title,
            description=description,
            image=image,
            meta_title=meta_title,
            meta_description=meta_description,
            content=content
        )

        success = True

    return render(request, 'blog/blog_form.html', {'success': success})

# def blog_success(request):
#     return render(request, 'blog/blog_success.html')
