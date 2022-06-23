# Generated by Django 4.0.5 on 2022-06-22 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_cake_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date Ordered')),
                ('time', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('E', 'Evening')], default='M', max_length=1)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.cake')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]