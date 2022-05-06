from django.urls import path

from news.views import NewsList

urlpatterns = [
  path('', NewsList.as_view())
]