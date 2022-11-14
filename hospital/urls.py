"""hospital URL Configuration
   Main router

   check at: https://betterprogramming.pub/learn-django-rest-framework-in-minutes-ef5159dc60ab
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointment/', include('appointments.urls')),
    path('patients/', include('patients.urls')),
    path('', include('register.urls')),

    # API Documentaion:
    # Schema Generation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI: 
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
urlpatterns = format_suffix_patterns(urlpatterns)