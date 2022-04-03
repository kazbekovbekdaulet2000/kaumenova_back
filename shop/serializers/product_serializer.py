from rest_framework import serializers
from shop.models.item import Product, ProductAvailability
from shop.models.product_type import ProductType
from shop.serializers.color_serializer import ColorSerializer
from shop.serializers.image_serializer import ImageSerializer
from shop.serializers.size_serializer import SizeSerializer


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAvailability
        fields = ['id', 'size', 'color', 'count']


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['name', 'have_size']


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    colors = ColorSerializer(source="set_colors", many=True, read_only=True)
    sizes = SizeSerializer(source="set_sizes", many=True, read_only=True)
    type = ProductTypeSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'created_at', 'price',
                  'type', 'images', 'colors', 'sizes']


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    colors = ColorSerializer(source="set_colors", many=True, read_only=True)
    sizes = SizeSerializer(source="set_sizes", many=True, read_only=True)
    type = ProductTypeSerializer()
    items = ProductItemSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'created_at', 'price', 'description',
                  'type', 'items', 'images', 'colors', 'sizes']
