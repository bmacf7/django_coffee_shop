from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order: {self.id}\nCreated By: {self.user.username} @ {self.created_at}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_price(self):
        self.price = self.product.price * self.quantity
        self.save()

    def save(self, *args, **kwargs):
        if not self.price:
            self.set_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order.user.username}\nProduct: {self.product.name} x{self.quantity}\Grand Total: {self.price}\n@ {self.created_at}"
