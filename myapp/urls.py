from django.urls import path

from .views import ProductCreateList, ProductGetDelete
urlpatterns = [

    path("product/createlist", ProductCreateList.as_view(),name="product_create_list"),
    path("product/productgetdelete/<int:pk>", ProductGetDelete.as_view(), name="product_get_delete"),
]