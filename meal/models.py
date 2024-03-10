from django.db import models


from PIL import Image

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)



class Meal(models.Model):
    name=models.CharField(max_length=76,blank=False)
    description=models.CharField(max_length=255)
    cooking_time=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient)
    
    
    cooking_level_choises = (
        ('easy', 'easy'),
        ('meduim', 'meduim'),
        ('hard', 'hard'),
        ('chef', 'chef'),
    )
    cooking_level = models.CharField(max_length=25, choices=cooking_level_choises)

class MealImage(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='uploads/')