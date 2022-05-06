from rest_framework import generics
from rest_framework import permissions

from news.models import News
from news.serializers.news_serializer import NewsSerializer


class NewsList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    pagination_class = None
    serializer_class = NewsSerializer
    queryset = News.objects.filter(active=True)
