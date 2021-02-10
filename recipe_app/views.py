from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from recipe_app.models import Author, Recipe
from recipe_app.forms import AddRecipeForm, AddAuthorForm, SignUpForm, LoginForm

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


@login_required
def add_recipe(request):
    context = {}
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe = Recipe.objects.create(
                title = data['title'],
                author = request.user.author,
                description = data['description'],
                time_required = data['time_required'],
                instructions = data['instructions']
            )
            context.update({'message': 'Submitted Recipe Successfully!'})
            return HttpResponseRedirect(reverse('recipe_detail', args=[recipe.id]))

    form = AddRecipeForm()
    context.update({'form':form})
    return render(
        request,
        'generic_form.html',
        context
    )

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usr = User.objects.create_user(
                username=data['username'],
                password = data['password']
            )
            newform = Author.objects.create(
                name = data['name'],
                user = usr 
            )

            newform.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()
    if request.user.is_staff:
        return render(request, 'generic_form.html', {'form': form})

    return render(request, 'error.html')

def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(
                # name = data['name'],
                # bio = data['bio'],
                username = data['username'],
                password = data['password']
            )
            user = authenticate(
                username = data['username'],
                password = data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
                return HttpResponseRedirect(reverse('homepage'))

    form = SignUpForm()
    return render(request, 'generic_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username = data['username'],
                password = data['password']
            )

            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
  