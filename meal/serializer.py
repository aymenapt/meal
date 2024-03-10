from rest_framework import serializers
from .models import Meal, Ingredient, Recipe, Category,MealImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealImage
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
   
    categories = CategorySerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)
    recipes = RecipeSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Meal
        fields = '__all__'
