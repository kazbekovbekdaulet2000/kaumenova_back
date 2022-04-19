from rest_framework import serializers
from shop.models.product_type import ProductType
from django.db.models import Count

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ["id", "name", "year", "have_size"]


class ProductTypeDetailSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField(read_only = True)

    def get_products_count(self, obj):
        return obj.category_products.all().annotate(items_count=Count('items')).filter(items_count__gte=1).count()

    class Meta:
        model = ProductType
        fields = ["id", "name", "year", "have_size", "products_count"]
