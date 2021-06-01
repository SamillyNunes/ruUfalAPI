
from rest_framework import serializers
from .models import Food, Meal

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'title', 'category', 'urlField', 'isVegeterian', 'isVegan')


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'type', 'food', 'date')