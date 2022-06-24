from django.contrib import admin
from .models import Cake, Order, Ingredient
# Register your models here.

admin.site.register(Cake)
admin.site.register(Order)
admin.site.register(Ingredient)