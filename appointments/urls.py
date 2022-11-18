from django.urls import path, include
from .views import RegisterAppointmentView, EditAppointmentView, ListAppointentView, AppointmentView, DeleteAppointView

urlpatterns = [
    path('register/', RegisterAppointmentView.as_view(), name='register_appointment'),
    path('edit/<int:pk>/', EditAppointmentView.as_view(), name='index'),
    path('list/', ListAppointentView.as_view(), name='index'),
    path('delete/<int:pk>/', DeleteAppointView.as_view(), name='index'),
    path('view/<int:pk>/', AppointmentView.as_view(), name='index'),
]
