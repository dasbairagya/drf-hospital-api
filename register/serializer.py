from .models import RegisterUser
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
   class Meta:
        model = RegisterUser
        fields = ['user_name', 'user_email', 'first_name', 'last_name']