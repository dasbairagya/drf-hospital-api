from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, ViewSerializer
from django.core import serializers
from .models import Register


# Method to register a new user
class RegisterCreateView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = Register.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.check_details(request.data):
            serializer.save()
            return Response(data={"message": "Patient created successfully."}, status=status.HTTP_201_CREATED)
        return Response(data={"message": "Username policy failed."}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def check_details(data):
        return len(data['user_name']) < 11


# Method to edit patient details
class EditUserView(generics.RetrieveUpdateAPIView):
    serializer_class = RegisterSerializer
    queryset = Register.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# Method to list all the patients
class ListUserView(generics.ListAPIView):
    serializer_class = RegisterSerializer
    queryset = Register.objects.all()


class SingleUserView(generics.RetrieveAPIView):
    serializer_class = RegisterSerializer
    queryset = Register.objects.all()

    # def get(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


class DeleteUserView(generics.DestroyAPIView):
    serializer_class = RegisterSerializer
    queryset = Register.objects.all()
