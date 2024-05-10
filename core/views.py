from django.shortcuts import render, get_object_or_404

from . import models
from .models import Category


def index(request):
    res = models.Recipes.objects.all()
    categories = models.Category.objects.all()
    context = {
        'res': res,
        'categories': categories,
        'title': 'Список рецептов',
    }
    return render(request, template_name='core/index.html', context=context)


def get_category(request, category_id):
    res = models.Recipes.objects.filter(category=category_id)
    categories = models.Category.objects.all()
    category = models.Category.objects.get(pk=category_id)
    context = {
        'res': res,
        'categories': categories,
        'category': category,
    }
    return render(request, template_name='core/category.html', context=context)


def show_category(request, category_slug):
    cat = get_object_or_404(Category, slug=category_slug)
    res = models.Recipes.objects.filter(slug=category_slug)
    category = models.Category.objects.get(pk=category_slug)
    data = {
        'title': Category.title,
        'res': res,
        'cat': cat,
        'category': category,
    }

    return render(request, 'core/category.html', context=data)
