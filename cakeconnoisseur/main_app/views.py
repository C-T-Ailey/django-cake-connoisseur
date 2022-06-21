from django.shortcuts import render
from django.http import HttpResponse
from .models import Cake

# Create your views here.

def home(request):
    #return HttpResponse('<h1> The château du gâteau <br> Home of the Cake Connoisseur </h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cakes_index(request):
    cakes = Cake.objects.all
    return render(request, 'cakes/index.html', {'cakes': cakes})

def cakes_detail(request, cake_id):
    cake = Cake.objects.get(id=cake_id)
    return render(request, 'cakes/details.html', {'cake': cake})