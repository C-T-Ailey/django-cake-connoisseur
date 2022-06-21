from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=100)
    flavor_base = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    image = models.CharField(default=None, blank=True, max_length=300, null=True)