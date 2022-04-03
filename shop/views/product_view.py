from rest_framework import generics

from shop.models.item import Product
from shop.serializers.product_serializer import ProductDetailSerializer, ProductSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer