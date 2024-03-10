from django.contrib import admin


from .models import Meal, Ingredient, Recipe, Category,MealImage

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Category)
class RecipeAdmin(admin.StackedInline):
    model = Recipe
class MealImageAdmin(admin.StackedInline):
    model = MealImage

class MealAdmin(admin.ModelAdmin):
    inlines = [MealImageAdmin]

    class Meta:
        model = Meal

admin.site.register(Meal,MealAdmin)