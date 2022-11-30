from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView

# from appointments.models import Appointment
# from appointments.serializers import AppointmentSerializer
from patients.models import Register
from register.models import RegisterUser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from patients.serializers import PatientRegistrationSerializer, PatientProfileSerializer, PatientDetailSerializer


# Create your views here.
from register.serializers import RegisterUserSerializer


class RegisterCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PatientRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditUserView(APIView):
    """"API endpoint for Patient profile view"""

    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Register.objects.get(pk=pk) # as our model does not have a specified id as a primary key hence pk=pk with id=pk
        except Register.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk: #view single patient
            patient = self.get_object(pk)
            # print(patient)
            serializer = PatientProfileSerializer(patient)
            # @todo
            # appointment = Appointment.objects.filter( patient=patient)
            # print(appointment)
            # appointmentSerializer = AppointmentSerializer(appointment, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK) #view single patient
            # return Response({'patient_data': serializer.data}, {'bookappointments': appointmentSerializer.data}, status=status.HTTP_200_OK) #view single patient

        #list all the patients
        all_patient = Register.objects.all()
        serializer = PatientProfileSerializer(all_patient, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  # view all patient

    #Edit single patient
    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = PatientProfileSerializer(instance=profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        saved_user = self.get_object(pk)
        saved_user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)}, status=status.HTTP_204_NO_CONTENT)

# class AppointmentViewPatient(APIView):
#     """"API endpoint for getting appointments details, creating appointment"""
#     permission_classes = [AllowAny]
#
#     def get(self, request, pk=None, format=None):
#         user = request.user
#         # user_patient = Patient.objects.filter(user=user).get()
#         patient_email = Register.objects.get(pk=pk) #get patient unique field(user_email) as model RegisterUser does not have any primary key by mistake
#         user_email = RegisterUser.objects.get(user_email=patient_email, groups=1)
#         # print(user_email) #patient3@gmail.com
#
#         patientDetailSerializer = PatientProfileSerializer(user_email)
#
#         appointment = Appointment.objects.filter(patient=patient_email)
#         # print(appointment) # get mutiple appointment
#         appointmentSerializer = AppointmentSerializer(appointment, many=True)
#
#         return Response({'patient_data': patientDetailSerializer.data, 'bookappointments': appointmentSerializer.data}, status=status.HTTP_200_OK)  # view single patient
#         # @todo: you can format response as you want for that you can create one centralize appointment view serializer

