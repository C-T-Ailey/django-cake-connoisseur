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

    path('cakes/<int:cake_id>/add_order', views.add_order, name='add_order'),

    #Ingredients paths
    path('ingredients/', views.IngredientList.as_view(), name='ingredients_index'),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredients_detail'),
    path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredients_create'),
    path('ingredients/<int:pk>/update', views.IngredientUpdate.as_view(), name='ingredients_update'),
    path('ingredients/<int:pk>/delete', views.IngredientDelete.as_view(), name='ingredients_delete'),

    path('cakes/<int:cake_id>/assoc_ingredient/<int:ingredient_id>/', views.assoc_ingredient, name='assoc_ingredient'),
    path('cakes/<int:cake_id>/unassoc_ingredient/<int:ingredient_id>/', views.unassoc_ingredient, name='unassoc_ingredient'),

    path('accounts/signup', views.signup, name='signup')
]