from django.forms import ValidationError
from rest_framework import serializers

from orders.models import Order, ProductOrder
from orders.task import send_reminder
from shop.models.product import ProductAvailability


class ProductOrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        exclude = ('order', )


class OrderCreateSerializer(serializers.ModelSerializer):
    products = ProductOrderCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user_name', 'phone_num', 'products')

    def validate(self, attrs):
        products_attrs = attrs['products']
        for product in products_attrs:
            if(not ProductAvailability.objects.filter(size=product['size'], color=product['color'], product=product['product']).exists()):
                raise ValidationError('Таких данных нету на складе')
        return super().validate(attrs)

    def create(self, validated_data):
        products = validated_data.pop('products')
        validated_data['total_price'] = 0
        order = Order.objects.create(**validated_data)
        price = 0
        for product in products:
            prod = ProductOrder.objects.create(order=order, **product)
            price += prod.product.price * product['count']
        order.total_price = price
        send_reminder(price, validated_data['phone_num'])
        order.save()
        return order
