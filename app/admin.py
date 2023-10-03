from django.contrib import admin
from .models import (
        Category,
        Product
    )
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('category_name', 'product_name', 'desc',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cate_name',)