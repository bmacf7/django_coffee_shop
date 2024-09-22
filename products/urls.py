from django.urls import path
from .views import ProductListView, ProductFormView, ProductDetailView, ProductAPIView

urlpatterns = [
    path("product-list/", ProductListView.as_view(), name="product_list"),
    path("create-product/", ProductFormView.as_view(), name="product_form"),
    path(
        "product-detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),
    path("api/", ProductAPIView.as_view(), name="product_api"),
]
