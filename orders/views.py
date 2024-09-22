from decimal import Decimal
from django.db.models import Sum
from django.views.generic import DetailView, CreateView
from .models import Order, OrderProduct
from .forms import OrderProductForm
from django.urls import reverse_lazy


class OrderDetailView(DetailView):
    model = Order
    template_name = "orders/order_detail.html"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        grand_total = order.orderproduct_set.aggregate(total=Sum("price"))["total"]
        if grand_total is not None:
            grand_total = Decimal(grand_total).quantize(Decimal("0.01"))
        else:
            grand_total = Decimal("0.00")
        context["grand_total"] = grand_total
        return context


class CreateOrderProductView(CreateView):
    model = OrderProduct
    form_class = OrderProductForm
    template_name = "orders/create_order_product.html"
    success_url = reverse_lazy("order_detail")

    def form_valid(self, form):
        order = Order.objects.get_or_create(
            is_active=True, user=self.request.user, id=self.kwargs["pk"]
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.instance.price = form.instance.product.price
        return super().form_valid(form)
