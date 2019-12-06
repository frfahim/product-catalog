from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'code', 'is_available']
    search_ffields = ('name', 'code')
    filter_fields = ['is_available']

