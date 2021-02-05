from django.shortcuts import render, HttpResponseRedirect

from recipe_app.models import Author, Recipe
from recipe_app.forms import AddRecipeForm

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

def add_recipe(request):
    context = {}
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe = Recipe.objects.create(
                title = data['title'],
                author = data['author'],
                description = data['description'],
                time_required = data['time_required'],
                instructions = data['instructions']
            )
            context.update({'message': 'Submitted Recipe Successfully!'})

    form = AddRecipeForm()
    context.update({'form':form})
    return render(
        request,
        'add_recipe.html', 
        # {'form': form},
        context
    )


