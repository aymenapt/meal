# Generated by Django 4.1.7 on 2023-03-18 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0004_rename_image_meal_mealimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='mealimage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meal.mealimage'),
        ),
    ]