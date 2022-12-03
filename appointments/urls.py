from django.urls import path, include
from .views import RegisterAppointmentView, EditAppointmentView, ListAppointentView, AppointmentView, DeleteAppointView

urlpatterns = [
    path('register/', RegisterAppointmentView.as_view(), name='register_appointment'),
    path('edit/<int:pk>', EditAppointmentView.as_view(), name='edit_appointment'),
    path('list/', ListAppointentView.as_view(), name='list_appointment'),
    path('delete/<int:pk>/', DeleteAppointView.as_view(), name='delete_appointment'), # note ending slash should could cause test failure
    path('view/<int:pk>', AppointmentView.as_view(), name='view_appointment'),
]
