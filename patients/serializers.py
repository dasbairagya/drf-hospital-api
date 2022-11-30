from rest_framework import serializers

# from appointments.models import Appointment
# from appointments.serializers import AppointmentSerializer
from .models import Register
from django.contrib.auth.models import Group


class PatientRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ["user_name", "user_email", "password", "user_dob", "location", "user_mobile"]

    def create(self, validated_data):
        patient = Register.objects.create(**validated_data)
        patient.save()

        # group_patient, created = Group.objects.get_or_create(name='patient')
        # group_patient.user_set.add(patient)
        return patient


class PatientProfileSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    user_name = serializers.CharField(max_length=150)
    user_email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    user_dob = serializers.DateField()
    location = serializers.CharField(max_length=50)
    user_mobile = serializers.CharField(max_length=50)

    def update(self, instance, validated_data):
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.password = validated_data.get('password', instance.user_name)
        instance.user_dob = validated_data.get('user_dob', instance.user_dob)
        instance.location = validated_data.get('location', instance.location)
        instance.user_mobile = validated_data.get('user_mobile', instance.user_mobile)
        instance.save()
        return instance


class PatientDetailSerializer(serializers.Serializer):  # get list of patients
    id = serializers.UUIDField(read_only=True)
    user_name = serializers.CharField(label='user_name:', read_only=True)
    user_email = serializers.CharField(label='user_email:', required=False)
    patient = PatientProfileSerializer(label='patient')
