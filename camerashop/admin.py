from django.contrib import admin
from .models import *


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'price', 'stock')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Manufacturer)
admin.site.register(Order)
admin.site.register(User)


