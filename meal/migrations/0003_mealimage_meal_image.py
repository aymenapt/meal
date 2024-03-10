# Generated by Django 4.1.7 on 2023-03-18 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0002_meal_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='image',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='meal.mealimage'),
            preserve_default=False,
        ),
    ]