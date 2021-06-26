from django.shortcuts import render, redirect

from recipes.recipes_app.forms import RecipeForm, DeleteRecipeForm
from recipes.recipes_app.models import Recipe


def index(req):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(req, 'index.html', context)


def create(req):
    if req.method == 'POST':
        form = RecipeForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()
        context = {
            'form': form,
        }
        return render(req, 'create.html', context)


def edit(req, pk):
    recipe = Recipe.objects.get(pk=pk)
    if req.method == 'POST':
        form = RecipeForm(req.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm(instance=recipe)
        context = {
            'form': form,
        }
        return render(req, 'edit.html', context)


def delete(req, pk):
    recipe = Recipe.objects.get(pk=pk)
    if req.method == 'POST':
        recipe.delete()
        return redirect('index')
    else:
        form = DeleteRecipeForm(instance=recipe)
        context = {
            'form': form,
        }
        return render(req, 'delete.html', context)


def details(req, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(req, 'details.html', context)

