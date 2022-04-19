from django.forms import ValidationError
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from shop.models.card import Card
from shop.models.product import Product


class ProductCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ["count", "product_size"]
        read_only_fields = ('id', 'product')

    def validate_product_size(self, attrs):
        product_id = self.context['view'].kwargs['id']
        if(not product_id == attrs.product.id):
            raise ValidationError('id не совподает')
        return attrs

    def create(self, validated_data):
        h = self.get_client_ip()
        validated_data['product'] = get_object_or_404(Product, **{
            "id": self.context['view'].kwargs['id']
        })
        validated_data['hash'] = h

        card_item = Card.objects.filter(
            hash=h, product=validated_data["product"])

        if card_item.count() == 1:
            card = card_item.last()
            if (validated_data['product_size']):
                card.product_size = validated_data['product_size']
            if(validated_data['count']):
                card.count = validated_data['count']
            else:
                card.count += 1
            card.save()
            return card

        if(not validated_data['count']):
            validated_data['count'] = 1

        return super().create(validated_data)

    def get_client_ip(self):
        x_forwarded_for = self.context['request'].META.get(
            'HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.context['request'].META.get('REMOTE_ADDR')
        return ip.replace(".", "")
