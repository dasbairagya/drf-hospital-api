from rest_framework import serializers
from .models import Register


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'


class ViewSerializer(serializers.ModelSerializer):
    bookappointments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Register
        fields = ["id", "user_name", "user_email", "user_dob", "location", "user_mobile", "bookappointments"]
