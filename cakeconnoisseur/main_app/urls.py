from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cakes/', views.cakes_index, name='index'),
    path('cakes/<int:cake_id>', views.cakes_detail, name='detail'),
    path('cakes/create', views.CakeCreate.as_view(), name='cakes_create'),

    path('cakes/<int:pk>/update/', views.CakeUpdate.as_view(), name='cakes_update'),
    path('cakes/<int:pk>/delete/', views.CakeDelete.as_view(), name='cakes_delete'),

    path('cakes/<int:cake_id>/add_order', views.add_order, name='add_order')
]