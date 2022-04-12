from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from shop.models.product import Product
from shop.serializers.product_serializer import ProductDetailSerializer, ProductSerializer
from django_filters import rest_framework as filters

def filter_by_ids(queryset, name, value):
    values = value.split(',')
    return queryset.filter(id__in=values)

class ProductFilter(filters.FilterSet):
   ids = filters.CharFilter(method=filter_by_ids)
    
   class Meta:
      model = Product
      fields = ['ids']

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        print(self.get_client_ip())
        return super().get_queryset()

    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

class ProductDetail(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer