from django.contrib import admin
from shop.models.color import Color
from shop.models.image import Image

from shop.models.product import Product, ProductAvailability
from shop.models.product_type import ProductType
from shop.models.size import Size


class ProductImageAdmin(admin.TabularInline):
    model = Image
    extra = 0


class ProductItemsAdmin(admin.TabularInline):
    model = ProductAvailability
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    exclude = ('set_sizes', 'set_colors')
    search_fields = ('name', 'description')
    inlines = [ProductItemsAdmin, ProductImageAdmin]


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "year")
    search_fields = ('name', )


class SizeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "gender")
    list_filter = ("gender", )


class ColorAdmin(admin.ModelAdmin):
    list_display = ("name", "color", "color_code")
    search_fields = ("name", )

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
