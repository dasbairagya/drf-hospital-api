from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.index, name='index'),
    path('edit/<int:pk>/', views.index, name='index'),
    path('list/', views.index, name='index'),
    path('delete/<int:pk>/', views.index, name='index'),
    path('view/<int:pk>/', views.index, name='index'),
]
