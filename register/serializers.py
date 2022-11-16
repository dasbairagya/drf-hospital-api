from time import timezone
from rest_framework import serializers
from .models import RegisterUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = '__all__'

    def create(self, validated_data):
        user = RegisterUser.objects.create_user(**validated_data)
        return user


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