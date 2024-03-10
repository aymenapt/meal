from django.urls import path
from .views import CategoryListCreateView,MealListCreateView



urlpatterns = [
    path('meals/', MealListCreateView.as_view(), name="meals"),
    path('category/', CategoryListCreateView.as_view(),
         name='category')
]