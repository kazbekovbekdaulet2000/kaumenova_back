from rest_framework import generics

from orders.models import Order
from shop.serializers.order_serializer import OrderCreateSerializer

class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer