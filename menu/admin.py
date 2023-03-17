from django.contrib import admin
from .models import Food, FoodCategory, Topping


@admin.register(FoodCategory, Topping)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Food)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name', 'description', 'price')
