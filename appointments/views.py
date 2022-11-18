from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer

# Create your views here.
"""API endpoint for getting info of all/particular appointment,
 update/delete appointment - only accessible by Admin"""

class RegisterAppointmentView(APIView):
    """API endpoint for getting info of all/particular appointment"""
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'appointments': serializer.data,
            }, status=status.HTTP_201_CREATED)
        return Response({
            'appointments': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)


class ListAppointentView(APIView):
    """API endpoint for getting info of all appointments"""
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        all_appointment = Appointment.objects.filter()
        serializer = AppointmentSerializer(all_appointment, many=True)
        return Response({'appointments': serializer.data}, status=status.HTTP_200_OK)



class EditAppointmentView(APIView):
    """API endpoint for edit info of a particular appointment"""
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        saved_appointment= self.get_object(pk)
        serializer = AppointmentSerializer(
            instance=saved_appointment, data=request.data.get('appointment'), partial=True) #if want to pass only single json data then pass data=request.data only
        if serializer.is_valid():
            serializer.save()
            return Response({'appointment': serializer.data}, status=status.HTTP_200_OK)
        return Response({
            'appointments': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)



class AppointmentView(APIView):
    """API endpoint for getting info of a particular appointment"""
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        appointment_detail = self.get_object(pk)
        serializer = AppointmentSerializer(appointment_detail)
        if pk:
            return Response({'appointments': serializer.data}, status=status.HTTP_200_OK)
        return Response({'appointments': serializer.data}, status=status.HTTP_200_OK)



class DeleteAppointView(APIView):
    """API endpoint for delete particular appointment"""
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        saved_appointment= self.get_object(pk)
        saved_appointment.delete()
        return Response({"message": "Appointment with id `{}` has been deleted.".format(pk)}, status=status.HTTP_204_NO_CONTENT)
