from django.contrib import admin
from .views import RegisterCreateView, EditUserView, ListUserView, DeleteUserView, SingleUserView
from django.urls import path, include

urlpatterns = [
    path('appointment/register/', RegisterCreateView.as_view(), name='register_appointment'),
    path('appointment/edit/<int:pk>', EditUserView.as_view(), name='edit_appointment'),
    path('appointment/list/', ListUserView.as_view(), name='list_appointment'),
    path('appointment/delete/<int:pk>', DeleteUserView.as_view(), name='delete_appointment'), # note ending slash should could cause test failure
    path('appointment/view/<int:pk>', SingleUserView.as_view(), name='view_appointment'),
  ]