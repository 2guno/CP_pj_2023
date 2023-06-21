from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def recommendation(request):
    if request.method == 'POST':
        ingredients = request.POST.get('ingredients', '').split(',')
        recipes = Recipe.objects.filter(ingredients__icontains=ingredients[0])
        for ingredient in ingredients[1:]:
            recipes = recipes.filter(ingredients__icontains=ingredient)
        return render(request, 'recipes/recommendation.html', {'recipes': recipes})
    return render(request, 'recipes/recommendation.html')


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipes': recipe})


def add_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        description = request.POST.get('description')

        recipe = Recipe(name=name, ingredients=ingredients, description=description)
        recipe.save()

        return redirect('recipes:recipe_list')

    return render(request, 'recipes/add_recipe.html')


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return redirect('recipes:recipe_list')
