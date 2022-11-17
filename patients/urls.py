from django.urls import path, include
from .views import PatientRegistrationView, PatientProfileView

urlpatterns = [
    path('register/', PatientRegistrationView.as_view(), name='patient_registration'),
    path('edit/<int:pk>', PatientProfileView.as_view(), name='patient_edit'),
    path('list/', PatientProfileView.as_view(), name='patient_list'),
    path('view/<int:pk>', PatientProfileView.as_view(), name='patient_view'),
]