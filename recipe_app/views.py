from django.shortcuts import render

from recipe_app.models import Author, Recipe

def index_view(requests):
    recipes = Recipe.objects.all()
    return render(requests, 'index.html', {'heading':'Recipe Box.', 'recipes': recipes})
