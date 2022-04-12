from django.contrib import admin

from orders.models import Order, ProductOrder


class ProductOrderAdmin(admin.TabularInline):
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    model = ProductOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    list_display = ("user_name", "phone_num", "done", "total_price")
    list_filter = ("done", )
    readonly_fields = ("user_name", "phone_num", "total_price")
    inlines = [ProductOrderAdmin]


# admin.site.register(ProductOrder)
admin.site.register(Order, OrderAdmin)
