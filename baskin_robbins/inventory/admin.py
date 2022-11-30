from django.contrib import admin

from baskin_robbins.inventory.models import Ingredient, Inventory


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "quantity", "branch")
    list_filter = ("branch",)
    search_fields = ("name", "description")
    ordering = ("name",)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "created_at")
    list_filter = ("product",)
    search_fields = ("product__name",)
    ordering = ("-created_at",)
