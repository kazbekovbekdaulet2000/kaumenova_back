from django.urls import path
from shop.views.card_view import CardList
from shop.views.category_view import ProductCategoryList
from shop.views.color_view import ColorList
from shop.views.product_view import ProductDetail, ProductDetailAddCard, ProductDetailRemoveCard, ProductList

urlpatterns = [
    # colors
    path('colors/', ColorList.as_view()),

    # categories
    path('categories/', ProductCategoryList.as_view()),

    # products
    path('products/', ProductList.as_view()),
    path('products/<int:id>/', ProductDetail.as_view()),
    path('products/<int:id>/card/add/', ProductDetailAddCard.as_view()),
    path('products/<int:id>/card/remove/', ProductDetailRemoveCard.as_view()),

    # card
    path('card/', CardList.as_view()),
]
