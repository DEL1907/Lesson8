from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('index_class/', views.ClassBasedIndex.as_view(), name='index_class'),
    path('category/<int:category_id>', get_category, name='category'),

    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('recipe/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('redirect/', views.Redirect.as_view(), name='redirect'),
    path('form_example/', views.SimpleForm.as_view(), name='form_example'),
]
