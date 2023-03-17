from .models import Food, FoodCategory, Topping
from rest_framework import serializers


class FoodSerializer(serializers.ModelSerializer):
    toppings = serializers.StringRelatedField(many=True)

    class Meta:
        model = Food
        fields = ['name',
                  'description',
                  'price',
                  'is_vegan',
                  'is_special',
                  'toppings',
                  ]


class FilteredCategorySerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True, source='filtered_menu_items')

    class Meta:
        model = FoodCategory
        fields = [
            "id",
            "name",
            "foods",
        ]
