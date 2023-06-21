from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('detail/<int:recipe_id>/', views.recipe_detail, name='detail'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]
