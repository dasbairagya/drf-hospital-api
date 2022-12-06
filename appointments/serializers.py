from rest_framework import serializers
from .models import BookAppointments


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAppointments
        fields = '__all__'
