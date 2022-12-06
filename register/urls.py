from django.contrib import admin
from .views import RegisterCreateView, SigninRetrieveView, SingleUserView, EditUserView
from django.urls import path, include



urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('signin/', SigninRetrieveView.as_view(), name='signin'),
    path('editprofile/<int:pk>', EditUserView.as_view(), name='editprofile'),
    path('viewprofile/<int:pk>', SingleUserView.as_view(), name='viewprofile'),
]
