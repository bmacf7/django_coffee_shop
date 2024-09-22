from django.urls import path
from .views import OrderDetailView, CreateOrderProductView

urlpatterns = [
    path("<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path(
        "add-order-product",
        CreateOrderProductView.as_view(),
        name="create_order_product",
    ),
]
