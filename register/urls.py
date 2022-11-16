from django.urls import path, include
from .views import LoginView, RegisterView, ProfileView, EditProfileView

app_name = 'register'

urlpatterns = [
    path('signin/', LoginView.as_view(), name='signin'),
    path('register/', RegisterView.as_view(), name='register'),
    path('editprofile/', EditProfileView.as_view(), name='editprofile'),
    path('viewprofile/', ProfileView.as_view(), name='viewprofile'),
]
