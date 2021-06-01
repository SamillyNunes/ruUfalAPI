from django.urls import path, include

from django.urls import path, include
from rest_framework import routers
from .views import FoodViewSet, MealViewSet

router = routers.DefaultRouter()
router.register(r'foods', FoodViewSet)
router.register(r'meals', MealViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]