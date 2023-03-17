from django.urls import path, include
from rest_framework import routers
from menu import views
from menu.views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'food', views.PublishFoodViewSet)


urlpatterns = [
    path('categories/', CategoryViewSet.as_view(), name='categories'),
]
