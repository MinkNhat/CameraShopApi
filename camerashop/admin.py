from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import *


class MyCameraShopAdmin(admin.AdminSite):
    site_header = 'Camera Shop'


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'subcategory', 'manufacturer', 'price', 'stock')
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" width="100" height="100" style="border-radius: 10px;" />', obj.main_image.url)
        return "(No Image)"


admin_site = MyCameraShopAdmin(name='camerashop')

admin_site.register(Product, ProductAdmin)
admin_site.register(Category)
admin_site.register(SubCategory, SubCategoryAdmin)
admin_site.register(Manufacturer)
admin_site.register(Order)
admin_site.register(User)
admin_site.register(ProductImage)


