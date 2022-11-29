from django.contrib import admin

from baskin_robbins.product.models import Flavor, Product


@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("slug",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sku", "price")
    list_filter = ("flavor", "branch")
    search_fields = ("sku",)
