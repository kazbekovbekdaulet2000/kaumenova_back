from rest_framework import serializers
from shop.models.size import Size


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'size', 'type', 'size_global', 'bust', 'waist', 'hips']
