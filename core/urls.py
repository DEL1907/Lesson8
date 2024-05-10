from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cat/<slug:category_slug>/', show_category, name='cat')
]
