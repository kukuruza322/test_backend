from django.urls import path, include
from rest_framework import routers
from menu import views
from menu.views import FilteredCategoryViewSet

router = routers.DefaultRouter()
router.register(r'food', views.PublishFoodViewSet)


urlpatterns = [
    path('categories/', FilteredCategoryViewSet.as_view(), name='filtered_categories'),
]
