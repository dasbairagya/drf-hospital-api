from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.index, name='index'),
    path('edit/', views.index, name='index'),
    path('list/', views.index, name='index'),
    path('view/', views.index, name='index'),
]