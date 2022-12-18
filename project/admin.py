from django.contrib import admin

# Register your models here.
from .models import ProductModel

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'stock', 'image']

admin.site.register(ProductModel)