from django.contrib import admin
from .models import Product, Logo, MenuItem, SocialMediaLink


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'alt_text')

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