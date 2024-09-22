from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label="Nombre")
    description = forms.CharField(max_length=200, label="Descripcion")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = forms.BooleanField(initial=True, label="Disponible", required=True)
    image = forms.ImageField(label="Foto", required=False)

    class Meta:
        model = Product
        fields = ["name", "description", "price", "available", "image"]

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            image=self.cleaned_data["image"],
        )
