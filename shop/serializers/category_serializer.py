from rest_framework import serializers
from shop.models.product_type import ProductType

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ["name", "year", "have_size"]
