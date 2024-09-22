from .models import Product
from .forms import ProductForm
from django.views.generic import ListView, FormView, DetailView
from django.urls import reverse_lazy

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductFormView(FormView):
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
