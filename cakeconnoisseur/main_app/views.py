from ast import Delete
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cake
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import OrderForm

# Create your views here.

class CakeCreate(CreateView):
    model = Cake
    fields = '__all__'

class CakeUpdate(UpdateView):
    model = Cake
    fields = ['flavor_base', 'description', 'rating', 'image']

class CakeDelete(DeleteView):
    model = Cake
    success_url = '/cakes/'

def home(request):
    #return HttpResponse('<h1> The château du gâteau <br> Home of the Cake Connoisseur </h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cakes_index(request):
    cakes = Cake.objects.all
    return render(request, 'cakes/index.html', {'cakes': cakes})

def cakes_detail(request, cake_id):
    order_form = OrderForm()
    cake = Cake.objects.get(id=cake_id)
    return render(request, 'cakes/details.html', {'cake': cake, 'order_form': order_form})

def add_order(request, cake_id):
    form = OrderForm(request.POST)
    print(form)
    if form.is_valid():
        new_order = form.save(commit=False)
        new_order.cake_id = cake_id
        new_order.save()
        return redirect('detail', cake_id = cake_id)
