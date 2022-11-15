# from django.contrib.auth.models import User

from .models import RegisterUser
from rest_framework import serializers
from .models import RegisterUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = '__all__'

    def create(self, validated_data):
        auth_user = RegisterUser.objects.create_user(**validated_data)
        return auth_user

