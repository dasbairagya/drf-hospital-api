from django.urls import path, include
from .views import RegisterCreateView, EditUserView

urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='patient_registration'),
    path('edit/<int:pk>', EditUserView.as_view(), name='patient_edit'),
    path('list/', EditUserView.as_view(), name='patient_list'),
    # path('view/<int:pk>', AppointmentViewPatient.as_view(), name='patient_view'),
    path('view/<int:pk>', EditUserView.as_view(), name='patient_view'),
    path('delete/<int:pk>', EditUserView.as_view(), name='patient_delete'),
]

# 8367823626