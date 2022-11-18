from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
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
            return RegisterUser.objects.get(pk=pk)
        except RegisterUser.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            patient_detail = self.get_object(pk)
            serializer = PatientDetailSerializer(patient_detail)
            return Response({'patient_data': serializer.data}, status=status.HTTP_200_OK) #view single patient

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
