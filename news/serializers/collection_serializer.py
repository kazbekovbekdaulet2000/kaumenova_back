from rest_framework import serializers

from news.models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    product_list = serializers.PrimaryKeyRelatedField(
        source="products", read_only=True, many=True)

    class Meta:
        model = Collection
        fields = "__all__"
