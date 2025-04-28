from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import Product, MenuItem, SocialMediaLink, Category, Banner, Blog, ProductReview

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'is_active')  # Columns to display in the admin list

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    # prepopulated_fields = {'slug': ('name',)}


# @admin.register(Logo)
# class LogoAdmin(admin.ModelAdmin):
#     list_display = ('title', 'image', 'alt_text')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'position','order', 'is_active')
    list_filter = ('parent', 'position', 'is_active')
    ordering = ('order',)


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'location', 'is_active')
    list_filter = ('location', 'is_active')
    search_fields = ('platform', 'url')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'enquiry_button_text', 'enquiry_button_link', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'image_tag')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'date_posted')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'email', 'comment')