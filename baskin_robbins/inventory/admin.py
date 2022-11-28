from django.contrib import admin

from baskin_robbins.inventory.models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "quantity", "branch")
    list_filter = ("branch",)
    search_fields = ("name", "description")
    ordering = ("name",)
