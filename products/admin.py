from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("name", "price", "created_at", "available")
    search_fields = ("name", "description")


admin.site.register(Product, ProductAdmin)
