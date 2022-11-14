from django.urls import path, include
from . import views

urlpatterns = [
    path('signin/', views.index, name='index'),
    path('register/', views.index, name='index'),
    path('editprofile/', views.index, name='index'),
    path('viewprofile/', views.index, name='index'),
]
