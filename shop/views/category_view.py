from rest_framework import generics

from shop.models.product_type import ProductType
from shop.serializers.category_serializer import ProductTypeDetailSerializer
from django.db.models import Count


class ProductCategoryList(generics.ListAPIView):
    queryset = ProductType.objects.all().annotate(
        items_count=Count('category_products')).filter(items_count__gte=1).order_by('order')
    serializer_class = ProductTypeDetailSerializer
    pagination_class = None