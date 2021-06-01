from django.shortcuts import render

from rest_framework import viewsets

from .serializers import  FoodSerializer, MealSerializer
from .models import Food, Meal

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all().order_by('title')
    serializer_class = FoodSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all().order_by('id')
    serializer_class = MealSerializer
