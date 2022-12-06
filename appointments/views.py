from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.core import serializers
from .models import BookAppointments


# Method to register a new user
class RegisterCreateView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = BookAppointments.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"message": "Appointment created successfully."}, status=status.HTTP_201_CREATED)
        return Response(data={"message": "Appointment policy failed."}, status=status.HTTP_400_BAD_REQUEST)


# Method to edit appointment details
class EditUserView(generics.RetrieveUpdateAPIView):
    serializer_class = RegisterSerializer
    queryset = BookAppointments.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# Method to list all the appointments
class ListUserView(generics.ListAPIView):
    serializer_class = RegisterSerializer
    queryset = BookAppointments.objects.all()


# Method to delete the appointments
class DeleteUserView(generics.DestroyAPIView):
    serializer_class = RegisterSerializer
    queryset = BookAppointments.objects.all()


# Method to list a particular appointment
class SingleUserView(generics.RetrieveAPIView):
    serializer_class = RegisterSerializer
    queryset = BookAppointments.objects.all()
