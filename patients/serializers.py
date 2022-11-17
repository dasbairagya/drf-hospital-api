from rest_framework import serializers
from .models import RegisterUser, Patient
from django.contrib.auth.models import Group


class PatientRegistrationSerializer(serializers.ModelSerializer):

    # user_name = serializers.CharField(max_length=150)
    # user_email = serializers.EmailField(max_length=255, unique=True)
    # password = serializers.CharField(min_length=8)
    # #
    # def validate_username(self, user_email):
    #     user_email_exists=RegisterUser.objects.filter(user_email__iexact=user_email)
    #     if user_email_exists:
    #         raise serializers.ValidationError({'user_email':'This username already exists'})
    #     return user_email
    # #
    # def validate_password(self, password):
    #     if password.isdigit():
    #         raise serializers.ValidationError('Your password should contain letters!')
    #     return password

    class Meta:
        model = RegisterUser
        fields = ['user_email', 'user_name', 'password']

    def create(self, validated_data):
        user = RegisterUser.objects.create_user(
            user_email=validated_data['user_email'],
            user_name=validated_data['user_name'],
            password=validated_data['password'],
        )
        user.save()

        group_patient, created = Group.objects.get_or_create(name='patient')
        group_patient.user_set.add(user)
        return user



class PatientProfileSerializer(serializers.Serializer):

    user_dob = serializers.DateTimeField()
    location = serializers.CharField(max_length=50)
    user_mobile = serializers.CharField(max_length=50)

    def validate_mobile(self, user_mobile):
        if user_mobile.isdigit() == False:
            raise serializers.ValidationError('Please Enter a valid mobile number!')
        return user_mobile

    def create(self, validated_data):
        new_patient = Patient.objects.create(
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