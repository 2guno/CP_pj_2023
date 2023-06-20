from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipe_list, name='list'),
    path('recipes/<int:pk>/', views.recipe_detail, name='detail'),
    path('recommendation/', views.recipe_recommendation, name='recommendation'),
]