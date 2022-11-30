from django.contrib import admin

from baskin_robbins.product.models import (
    Flavor,
    Product,
    Recipe,
    RecipeIngredient,
    Transaction,
)


@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("slug",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sku", "price")
    list_filter = ("flavor", "branch")
    search_fields = ("sku",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "product")
    list_filter = ("product",)
    search_fields = ("product__name",)


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "recipe", "ingredient", "quantity")
    list_filter = ("recipe", "ingredient")
    search_fields = ("recipe__product__name", "ingredient__name")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "created_at")
    list_filter = ("product",)
    search_fields = ("product__name",)
    ordering = ("-created_at",)
