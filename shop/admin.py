from django.contrib import admin
from shop.models.color import Color
from shop.models.image import Image

from shop.models.item import Product, ProductAvailability
from shop.models.product_type import ProductType
from shop.models.size import Size


class ProductImageAdmin(admin.TabularInline):
    model = Image
    extra = 1


class ProductItemsAdmin(admin.TabularInline):
    model = ProductAvailability
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    exclude = ('set_sizes', 'set_colors')
    search_fields = ('name', 'description')
    inlines = [ProductItemsAdmin, ProductImageAdmin]


class SizeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "gender")
    list_filter = ("gender", )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType)
admin.site.register(Size, SizeAdmin)
# admin.site.register(Image)
admin.site.register(Color)
