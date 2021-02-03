from django.shortcuts import render

from recipe_app.models import Author, Recipe

def index_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'heading':'Recipe Box.', 'recipes': recipes})

def recipe_detail(request, post_id):
    recipe_obj = Recipe.objects.get(id=post_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe_obj})



def author_detail(request, author_id):
    author_obj = Author.objects.get(id=author_id)
    recipes = Recipe.objects.filter(author=author_obj)
    return render(request, 'author_detail.html', {
        'author': author_obj, 
        'recipes': recipes,
        })
