from django.shortcuts import get_object_or_404
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from shop.models.card import Card
from shop.models.product import Product
from shop.serializers.card_serializer import ProductCardSerializer
from shop.serializers.product_serializer import CardProductSerializer
from django_filters import rest_framework as filters
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


class CardList(generics.ListAPIView):
    serializer_class = CardProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    card_obj = None
    pagination_class = None

    def get_queryset(self):
        self.card_obj = Card.objects.filter(hash=self.get_client_ip())
        ids = self.card_obj.values_list('product__id', flat=True)
        return Product.objects.all() \
            .annotate(items_count=Count('items')) \
            .filter(items_count__gte=1, id__in=ids) \


    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip.replace(".", "")


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
