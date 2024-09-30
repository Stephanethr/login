from django.urls import path
from . import views

urlpatterns = [
    path('', views.objet_list, name='objet_list'),
    path('create/', views.objet_create, name='objet_create'),
    path('update/<int:pk>/', views.objet_update, name='objet_update'),
    path('delete/<int:pk>/', views.objet_delete, name='objet_delete'),
]
