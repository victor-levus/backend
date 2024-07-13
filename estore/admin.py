from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'updatedAt']


# @admin.register(models.Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['id', 'sku', 'name', 'description', 'category', 'price', 'image', 'createdAt',
#                   'updatedAt']

