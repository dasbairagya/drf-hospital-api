from django.urls import path, include
from . import views


urlpatterns = [
    # path('signin/', views.SnippetList.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='index'),
    # path('editprofile/', views.index, name='index'),
    # path('viewprofile/', views.index, name='index'),
]
