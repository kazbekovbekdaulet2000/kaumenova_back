from django.shortcuts import get_object_or_404
from rest_framework import serializers
from shop.models.card import Card
from shop.models.product import Product, ProductAvailability
from shop.serializers.category_serializer import ProductTypeSerializer
from shop.serializers.color_serializer import ColorSerializer
from shop.serializers.image_serializer import ImageSerializer
from shop.serializers.size_serializer import SizeSerializer


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAvailability
        fields = ['id', 'size', 'color', 'count']


class ProductItemDetailSerializer(serializers.ModelSerializer):
    size = SizeSerializer()
    color = ColorSerializer()
    class Meta:
        model = ProductAvailability
        fields = ['id', 'size', 'color', 'count']


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    colors = ColorSerializer(source="set_colors", many=True, read_only=True)
    sizes = SizeSerializer(source="set_sizes", many=True, read_only=True)
    type = ProductTypeSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'created_at', 'price',
                  'type', 'images', 'colors', 'sizes']


class ProductDetailSerializer(ProductSerializer):
    items = ProductItemSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'created_at', 'price', 'description',
                  'type', 'items', 'images', 'colors', 'sizes']


class CardProductSerializer(ProductSerializer):
    count = serializers.SerializerMethodField(read_only=True)
    total_price = serializers.SerializerMethodField(read_only=True)
    selected_size = serializers.SerializerMethodField(read_only=True)

    def get_count(self, obj):
        obj = get_object_or_404(Card, **{'product': obj, 'hash': self.get_client_ip()})
        return obj.count

    def get_total_price(self, obj):
        return ((self.get_count(obj) * obj.price) * (100 - obj.discount))/100

    def get_selected_size(self, obj):
        product_size_ids = self.context['view'].card_obj.values_list('product_size', flat=True).distinct()
        data = ProductAvailability.objects.filter(id__in=product_size_ids)
        return ProductItemDetailSerializer(data, many=True).data

    class Meta:
        model = Product
        fields = ['id', 'name', 'created_at', 'price',
                  'type', 'images', 'colors', 'sizes', 'count', 'total_price', 'selected_size']

    def get_client_ip(self):
        x_forwarded_for = self.context['request'].META.get(
            'HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.context['request'].META.get('REMOTE_ADDR')
        return ip.replace(".", "")
