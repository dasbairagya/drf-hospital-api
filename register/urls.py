from django.contrib import admin
from .views import RegisterCreateView, SigninRetrieveView, SingleUserView, EditUserView
from django.urls import path, include

urlpatterns = [
    path('app/register/', RegisterCreateView.as_view(), name='register'),
    path('app/signin/', SigninRetrieveView.as_view(), name='signin'),
    path('app/editprofile/<int:pk>', EditUserView.as_view(), name='editprofile'),
    path('app/viewprofile/<int:pk>', SingleUserView.as_view(), name='viewprofile'),
]
