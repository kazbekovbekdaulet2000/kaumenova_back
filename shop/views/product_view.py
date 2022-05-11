from django.shortcuts import get_object_or_404
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from shop.models.card import Card
from shop.models.product import Product
from shop.serializers.card_serializer import ProductCardSerializer
from shop.serializers.product_serializer import ProductDetailSerializer, ProductSerializer
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from django.db.models import Count


def filter_by_ids(queryset, name, value):
    values = value.split(',')
    return queryset.filter(id__in=values)


class ProductFilter(filters.FilterSet):
    ids = filters.CharFilter(method=filter_by_ids)
    type = filters.NumberFilter()
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['ids', 'name', 'type']


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all().annotate(
        items_count=Count('items')).filter(items_count__gte=1, active=True)
    serializer_class = ProductSerializer
    search_fields = ('type__tags', )
    'name', 'type__name',
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter


class ProductDetail(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Product.objects.all().annotate(
        items_count=Count('items')).filter(items_count__gte=1, active=True)
    serializer_class = ProductDetailSerializer


class ProductDetailAddCard(generics.CreateAPIView):
    serializer_class = ProductCardSerializer


class ProductDetailRemoveCard(generics.DestroyAPIView):
    serializer_class = ProductCardSerializer

    def get_object(self):
        obj = get_object_or_404(
            Card, **{'product': self.kwargs['id'], 'hash': self.get_client_ip()})
        return obj

    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip.replace(".", "")
