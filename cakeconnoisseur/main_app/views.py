from ast import Delete
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cake, Ingredient
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#
from django.views.generic import ListView, DetailView
from .forms import OrderForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os

# Create your views here.

class CakeCreate(LoginRequiredMixin, CreateView):
    model = Cake
    fields = ['name', 'flavor_base', 'description', 'rating', 'image']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CakeUpdate(LoginRequiredMixin, UpdateView):
    model = Cake
    fields = ['flavor_base', 'description', 'rating', 'image']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CakeDelete(LoginRequiredMixin, DeleteView):
    model = Cake
    success_url = '/cakes/'

def home(request):
    #return HttpResponse('<h1> The château du gâteau <br> Home of the Cake Connoisseur </h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cakes_index(request):
    # filter the returned list of cakes by the user submitting the request
    cakes = Cake.objects.filter(user=request.user)
    return render(request, 'cakes/index.html', {'cakes': cakes})

@login_required
def cakes_detail(request, cake_id):
    order_form = OrderForm()
    cake = Cake.objects.get(id=cake_id)
    ingredients_not_incl = Ingredient.objects.exclude(id__in = cake.ingredients.all().values_list('id'))
    return render(request, 'cakes/details.html', {'cake': cake, 'order_form': order_form, 'ingredients': ingredients_not_incl})

@login_required
def add_order(request, cake_id):
    form = OrderForm(request.POST)
    print(form)
    if form.is_valid():
        new_order = form.save(commit=False)
        new_order.cake_id = cake_id
        new_order.save()
        return redirect('detail', cake_id = cake_id)

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient

class IngredientDetail(LoginRequiredMixin, DetailView):
    model = Ingredient

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = '__all__'

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    fields = ['name','color']

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    success_url = '/ingredients/'

@login_required
def assoc_ingredient(request, cake_id, ingredient_id):
    Cake.objects.get(id=cake_id).ingredients.add(ingredient_id)
    return redirect('detail', cake_id = cake_id)

@login_required
def unassoc_ingredient(request, cake_id, ingredient_id):
    Cake.objects.get(id=cake_id).ingredients.remove(ingredient_id)
    return redirect('detail', cake_id = cake_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
        else:
            error_message = 'Invalid signup credentials - Please try again later.'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
