from django.urls import path, include
from . import views

app_name = 'main_pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', include('recipes.urls')),
]