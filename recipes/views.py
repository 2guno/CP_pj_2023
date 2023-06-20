import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Recipe


@csrf_exempt
def recipe_list(request):
    if request.method == 'POST':
        ingredients = request.POST.get('ingredients', '').split(',')

        # CSV 파일 경로
        csv_path = 'recipes/data/recipes.csv'

        # CSV 파일을 pandas DataFrame으로 읽어옴
        df = pd.read_csv(csv_path)

        # 요리명과 재료 컬럼 추출
        recipe_names = df['요리명'].tolist()
        recipe_ingredients = df['재료'].tolist()

        # 재료와 일치하는 요리 목록 필터링
        matching_recipes = []
        for name, ingredients_list in zip(recipe_names, recipe_ingredients):
            if all(ingredient.lower() in ingredients for ingredient in ingredients_list.split(',')):
                matching_recipes.append({'name': name})

        return JsonResponse({'recipes': matching_recipes})
    else:
        return JsonResponse({'error': 'Invalid request method.'})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def recipe_recommendation(request):
    if request.method == 'POST':
        #ingredients = request.POST.get('ingredients', '').strip()
        # 추천 로직을 구현합니다.
        # 적절한 요리를 찾아서 결과를 반환합니다.
        ingredients = '참깨'
    else:
        ingredients = '고추장'

    return render(request, 'recipes/recommendation.html', {'ingredients': ingredients})
