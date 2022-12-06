from rest_framework import serializers
from .models import Register


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register


class ViewSerializer(serializers.ModelSerializer):
    bookappointments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Register
