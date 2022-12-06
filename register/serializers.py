from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from .models import RegisterUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = '__all__'


class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['user_email', 'password']

    def validate(self, data):
        email = data.get('user_email', None)
        password = data.get('password', None)

        """
        user = authenticate(user_email=email, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')

        return user
        """

        user = RegisterUser.objects.filter(user_email=email)

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("This username/email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Invalid credentials.")

            data['user'] = user_obj
            return data