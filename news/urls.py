from django.urls import path

from news.views import ListCollectionItem, ListCollections, NewsList, SubsCreate

urlpatterns = [
    path('', NewsList.as_view()),
    path('subsribe/', SubsCreate.as_view()),
    path('collections/', ListCollections.as_view()),
    path('collections/<int:id>/', ListCollectionItem.as_view())
]
