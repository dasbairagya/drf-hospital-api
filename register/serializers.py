from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import RegisterUser

#Write the serializer for Registering the user
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        # fields = '__all__'
        fields = ["user_name", "user_email", "password","user_dob","location", "user_mobile"]

    def create(self, validated_data):
        user = RegisterUser.objects.create_user(**validated_data)
        return user


#Write the serializer for Signin

class LoginSerializers(serializers.Serializer):
    user_email = serializers.CharField(max_length=255)
    password = serializers.CharField(
        max_length=128,
        write_only=True
    )

    def validate(self, data):
        # print(data)
        user_email = data.get('user_email')
        password = data.get('password')
        # print()
        # print(user_email)
        # print(password)
        if user_email and password:
            user = authenticate(request=self.context.get('request'), user_email=user_email, password=password)
            # print(user) #print email id of the user
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
        fields = ["user_email", "password"]


class ProfileSerializer(serializers.Serializer):

    user_dob = serializers.DateTimeField()
    location = serializers.CharField(max_length=50)
    user_mobile = serializers.CharField(max_length=50)

    def validate_mobile(self, user_mobile):
        if user_mobile.isdigit() == False:
            raise serializers.ValidationError('Please Enter a valid mobile number!')
        return user_mobile

    def create(self, validated_data):
        new_patient = RegisterUser.objects.create(
            user_dob=validated_data['user_dob'],
            location=validated_data['location'],
            user_mobile=validated_data['user_mobile'],
            user=validated_data['user']
        )
        return new_patient

    def update(self, instance, validated_data):
        instance.user_dob = validated_data.get('user_dob', instance.user_dob)
        instance.location = validated_data.get('location', instance.location)
        instance.user_mobile = validated_data.get('user_mobile', instance.user_mobile)
        instance.save()
        return instance