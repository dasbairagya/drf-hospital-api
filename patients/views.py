from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer
from patients.models import Patient
from register.models import RegisterUser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from patients.serializers import PatientRegistrationSerializer, PatientProfileSerializer, PatientDetailSerializer


# Create your views here.
class PatientRegistrationView(APIView):
    """"API endpoint for Patient Registration"""

    permission_classes = [AllowAny]

    def post(self, request):
        registrationSerializer = PatientRegistrationSerializer(data=request.data)
        checkregistration = registrationSerializer.is_valid()

        profileSerializer = PatientProfileSerializer(data=request.data)
        checkprofile = profileSerializer.is_valid()

        if checkregistration and checkprofile:
            patient = registrationSerializer.save()
            profileSerializer.save(user=patient)
            return Response({
                'user_data': registrationSerializer.data,
                'profile_data': profileSerializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
                'user_data': registrationSerializer.data,
                'profile_data': profileSerializer.data
            }, status=status.HTTP_400_BAD_REQUEST)

class PatientProfileView(APIView):
    """"API endpoint for Patient profile view"""

    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return RegisterUser.objects.get(id=pk) # as our model does not have a specified id as a primary key hence pk=pk with id=pk
        except RegisterUser.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            patient = self.get_object(pk)
            print(patient)
            serializer = PatientDetailSerializer(patient)
            # @todo
            # appointment = Appointment.objects.filter( patient=patient)
            # print(appointment)
            # appointmentSerializer = AppointmentSerializer(appointment, many=True)

            return Response({'patient_data': serializer.data}, status=status.HTTP_200_OK) #view single patient
            # return Response({'patient_data': serializer.data}, {'bookappointments': appointmentSerializer.data}, status=status.HTTP_200_OK) #view single patient

class PatientProfileListView(APIView):
    """"API endpoint for all patients"""

    permission_classes = [AllowAny]

    def get(self, request, pk=None, format=None):
        all_patient = RegisterUser.objects.filter(groups=1)
        serializer = PatientDetailSerializer(all_patient, many=True)
        return Response({'patients': serializer.data}, status=status.HTTP_200_OK) #view all patient

class PatientProfileEditView(APIView):
    """"API endpoint for Patient profile edit"""

    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return RegisterUser.objects.get(pk=pk)
        except RegisterUser.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = PatientProfileSerializer(
            instance=profile, data=request.data.get('profile_data'), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'profile_data': serializer.data}, status=status.HTTP_200_OK)
        return Response({
            'profile_data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class PatientProfileDeleteView(APIView):
    """"API endpoint for Patient profile delete"""

    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return RegisterUser.objects.get(pk=pk)
        except RegisterUser.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        saved_user = self.get_object(pk)
        saved_user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)}, status=status.HTTP_204_NO_CONTENT)


class AppointmentViewPatient(APIView):
    """"API endpoint for getting appointments details, creating appointment"""
    permission_classes = [AllowAny]

    def get(self, request, pk=None, format=None):
        user = request.user
        # user_patient = Patient.objects.filter(user=user).get()
        patient_email = Patient.objects.get(pk=pk) #get patient unique field(user_email) as model RegisterUser does not have any primary key by mistake
        user_email = RegisterUser.objects.get(user_email=patient_email, groups=1)
        # print(user_email) #patient3@gmail.com

        patientDetailSerializer = PatientDetailSerializer(user_email)

        appointment = Appointment.objects.filter(patient=patient_email)
        # print(appointment) # get mutiple appointment
        appointmentSerializer = AppointmentSerializer(appointment, many=True)

        return Response({'patient_data': patientDetailSerializer.data, 'bookappointments': appointmentSerializer.data}, status=status.HTTP_200_OK)  # view single patient
        # @todo: you can format response as you want for that you can create one centralize appointment view serializer