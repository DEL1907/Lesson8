from django.shortcuts import render
from django.utils.timezone import now
from django.views.generic import ListView, TemplateView, DetailView, RedirectView, FormView
from . import models, forms


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


class ClassBasedIndex(TemplateView):
    template_name = 'core/ind.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['additional_info'] = now()
        return context


class RecipeList(ListView):
    model = models.Recipes
    context_object_name = "recipes"
    template_name = 'core/recipes_list.html'


class RecipeDetail(DetailView):
    model = models.Recipes
    context_object_name = 'recipe'
    template_name = 'core/recipes_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['additional_info'] = 'Делитесь вкусными рецептами'
        return context


class Redirect(RedirectView):
    query_string = True
    url = 'http://paranoia.com/'


class SimpleForm(FormView):
    template_name = 'core/form.html'
    form_class = forms.SimpleForm
    success_url = "/index_class/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
