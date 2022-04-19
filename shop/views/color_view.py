from rest_framework import generics
from shop.models.color import Color

from shop.serializers.color_serializer import ColorSerializer


class ColorList(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    pagination_class = None
