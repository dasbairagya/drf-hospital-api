"""hospital URL Configuration
   Main router
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointment/', include('appointments.urls')),
    path('patients/', include('patients.urls')),
    path('', include('register.urls')),
]
