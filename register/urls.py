from django.urls import path, include
from .views import LoginView, RegisterView

app_name = 'register'

urlpatterns = [
    path('signin/', LoginView.as_view(), name='signin'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('editprofile/', views.index, name='index'),
    # path('viewprofile/', views.index, name='index'),
]
