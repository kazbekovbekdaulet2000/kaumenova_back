from rest_framework import serializers

from news.models import Broadcast


class SubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broadcast
        fields = "__all__"
