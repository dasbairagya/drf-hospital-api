from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer, SigninSerializer
from rest_framework.authtoken.models import Token
import jwt
import datetime
from django.conf import settings
from django.core import serializers
from rest_framework import status
from .models import RegisterUser


# Method to register a new user
class RegisterCreateView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = RegisterUser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        if self.check_details(request.data):
            serializer.save()
            return Response(data={"message": "User created successfully."}, status=status.HTTP_201_CREATED)

            # return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(data={"message": "Password or username policy failed."}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def check_details(data):
        return len(data['user_name']) < 11 and len(data['password']) < 10


# Method to check login credentials
class SigninRetrieveView(generics.CreateAPIView):
    serializer_class = SigninSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Method to list a particular user
class SingleUserView(generics.RetrieveAPIView):
    serializer_class = RegisterSerializer
    queryset = RegisterUser.objects.all()
    #
    # def get(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


# Method to edit details of a particular user
class EditUserView(generics.RetrieveUpdateAPIView):
    serializer_class = RegisterSerializer
    queryset = RegisterUser.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
