from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("user__username", "product__name")
    inlines = [OrderProductInlineAdmin]
    list_per_page = 25


admin.site.register(Order, OrderAdmin)
