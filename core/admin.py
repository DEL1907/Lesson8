from django.contrib import admin

from core.models import Recipes, Category


class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'ingredients', 'created_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'descriptions', 'ingredients')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Recipes)
admin.site.register(Category)
