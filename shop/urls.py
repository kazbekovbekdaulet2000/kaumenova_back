from django.urls import path
from shop.views.category_view import ProductCategoryList
from shop.views.product_view import ProductDetail, ProductList

urlpatterns = [
  # categories
  path('categories/', ProductCategoryList.as_view()),
  
  # products
  path('products/', ProductList.as_view()),
  path('products/<int:id>/', ProductDetail.as_view())
]