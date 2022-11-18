from django.urls import path, include
from .views import PatientRegistrationView, PatientProfileView, PatientProfileListView, PatientProfileEditView, \
    PatientProfileDeleteView

urlpatterns = [
    path('register/', PatientRegistrationView.as_view(), name='patient_registration'),
    path('edit/<int:pk>', PatientProfileEditView.as_view(), name='patient_edit'),
    path('list/', PatientProfileListView.as_view(), name='patient_list'),
    path('view/<int:pk>', PatientProfileView.as_view(), name='patient_view'),
    path('delete/<int:pk>', PatientProfileDeleteView.as_view(), name='patient_delete'),
]