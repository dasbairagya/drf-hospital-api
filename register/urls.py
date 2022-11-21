from django.urls import path, include
from .views import LoginView, EditProfileView, RegisterCreateView, SingleUserView

app_name = 'register'

urlpatterns = [
    path('signin/', LoginView.as_view(), name='signin'),
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('editprofile/<int:pk>', EditProfileView.as_view(), name='editprofile'),
    path('viewprofile/<int:pk>', SingleUserView.as_view(), name='viewprofile'),
]
