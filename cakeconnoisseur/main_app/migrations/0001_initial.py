# Generated by Django 4.0.5 on 2022-06-21 14:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('flavor_base', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('rating', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('image', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
    ]