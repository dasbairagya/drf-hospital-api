from django.contrib.auth import login, authenticate
from django.contrib.auth.models import update_last_login
from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer, RegisterUserSerializer, LoginSerializers
from .models import RegisterUser
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token


# https://python.plainenglish.io/django-custom-user-model-and-auth-using-jwt-simple-boilerplate-6acd78bf7767
# Create your views here.
from .util import get_tokens_for_user


# Method to register a new user
class RegisterCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = RegisterUser.objects.all()
        serializer = RegisterUserSerializer(users, many=True)
        return Response(serializer.data)


# Method to check login credentials
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"status": status.HTTP_200_OK, "Token": token.key})


# Method to list a particular user
class SingleUserView(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return RegisterUser.objects.get(
                id=pk)  # as our model does not have a specified id as a primary key hence pk=pk with id=pk
        except RegisterUser.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            user = self.get_object(pk)
            # print(user)
            serializer = RegisterUserSerializer(user)
            return Response({
                'response': serializer.data,
            }, status=status.HTTP_200_OK)


# Method to edit details of a particular user

class EditProfileView(APIView):
    """"API endpoint for Patient profile update"""

    permission_classes = [AllowAny]

    def put(self, request, format=None):
        user = request.data
        profile = RegisterUser.objects.filter(user_email=user['user_email']).get()
        profileSerializer = ProfileSerializer(
            instance=profile, data=request.data.get('profile_data'), partial=True)
        if profileSerializer.is_valid():
            profileSerializer.save()
            return Response({
                'profile_data': profileSerializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'profile_data': profileSerializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
