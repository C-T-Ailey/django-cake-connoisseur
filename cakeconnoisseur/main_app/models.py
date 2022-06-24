from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredients_detail', kwargs={'pk':self.id})

# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=100)
    flavor_base = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    image = models.CharField(default=None, blank=True, max_length=300, null=True)
    ingredients = models.ManyToManyField(Ingredient)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'cake_id': self.id})

    def __str__(self):
        return f"{self.name}"

    def eaten_today(self):
        return self.order_set.filter(date=date.today()).count() >= 1

class Order(models.Model):
    date = models.DateField("Date Ordered")
    time = models.CharField(max_length=1, choices=TIMES, default=TIMES[0][0])
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['date']

#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    favorite_color = models.CharField(max_length=50)