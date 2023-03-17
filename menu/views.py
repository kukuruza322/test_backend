from django.db.models import Prefetch
from rest_framework import generics, viewsets
from .models import Food, FoodCategory
from menu.serializers import FoodSerializer, FilteredCategorySerializer
from django_filters.rest_framework import DjangoFilterBackend


class PublishFoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.filter(is_publish=True)
    serializer_class = FoodSerializer


class FilteredCategoryViewSet(generics.ListAPIView):
    queryset = FoodCategory.objects.prefetch_related(Prefetch('food_set',
                                                              queryset=Food.objects.filter(is_publish=True),
                                                              to_attr='filtered_menu_items')
                                                     )
    serializer_class = FilteredCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['food__is_vegan',
                        'food__is_special',
                        ]
