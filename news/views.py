from rest_framework import generics
from rest_framework import permissions

from news.models import Collection, News
from news.serializers.collection_serializer import CollectionSerializer
from news.serializers.news_serializer import NewsSerializer
from news.serializers.subs_serializer import SubsSerializer


class NewsList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    pagination_class = None
    serializer_class = NewsSerializer
    queryset = News.objects.filter(active=True)


class SubsCreate(generics.CreateAPIView):
    serializer_class = SubsSerializer


class ListCollections(generics.ListAPIView):
    serializer_class = CollectionSerializer
    pagination_class = None
    queryset = Collection.objects.filter(active=True)

class ListCollectionItem(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = CollectionSerializer
    queryset = Collection.objects.filter(active=True)