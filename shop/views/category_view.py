from rest_framework import generics

from shop.models.product_type import ProductType
from shop.serializers.category_serializer import ProductTypeSerializer


class ProductCategoryList(generics.ListAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer