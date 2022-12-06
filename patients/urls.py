from django.contrib import admin
from .views import RegisterCreateView, EditUserView, ListUserView, SingleUserView, DeleteUserView
from django.urls import path, include

urlpatterns = [
    path('patients/register/', RegisterCreateView.as_view(), name='patient_registration'),
    path('patients/edit/<int:pk>', EditUserView.as_view(), name='patient_edit'),
    path('patients/list/', ListUserView.as_view(), name='patient_list'),
    path('patients/view/<int:pk>', SingleUserView.as_view(), name='patient_view'),
    path('patients/delete/<int:pk>', DeleteUserView.as_view(), name='patient_delete'),
  ]

