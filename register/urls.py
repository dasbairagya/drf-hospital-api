from django.urls import path, include
from .views import LoginView, RegisterCreateView, SingleUserView

app_name = 'register'

urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('editprofile/<int:pk>', SingleUserView.as_view(), name='editprofile'),
    path('viewprofile/<int:pk>', SingleUserView.as_view(), name='viewprofile'),
]
