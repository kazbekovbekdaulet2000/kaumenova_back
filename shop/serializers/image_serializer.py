from rest_framework import serializers
from shop.models.image import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["image", "color", "image_thumb"]