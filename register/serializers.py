from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import RegisterUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = '__all__'


class SigninSerializer(serializers.ModelSerializer):
    # this two field is very important other wise it will work as a registration
    # and "register user with this user email already exists." will tigger
    user_email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def authenticate(self, **kwargs):
        return authenticate(**kwargs)

    def validate(self, data):
        user_email = data.get('user_email')
        password = data.get('password')
        user = None
        if user_email and password:
            # user = authenticate(ser_email=user_email, password=password)  # use this if you have hashed the password during registration
            # user = self.authenticate(user_email=user_email, password=password)
            user = get_object_or_404(RegisterUser, user_email=user_email, password=password) #additional import
            if not user:
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data

    class Meta:
        model = RegisterUser
        fields = ['user_email', 'password']