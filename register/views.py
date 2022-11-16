from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, ProfileSerializer
from .models import RegisterUser
from rest_framework.permissions import AllowAny

# https://python.plainenglish.io/django-custom-user-model-and-auth-using-jwt-simple-boilerplate-6acd78bf7767
# Create your views here.
from .util import get_tokens_for_user


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = RegisterUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class LoginView(APIView):
    permission_classes = [AllowAny]  # To avoid msg:  Authentication credentials were not provided

    def post(self, request):
        if 'user_email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        user_email = request.POST['user_email']
        password = request.POST['password']
        user = authenticate(request, user_email=user_email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ProfileView(APIView):
    """"API endpoint for Patient profile view"""

    permission_classes = [AllowAny]

    def get(self, request):
        user = request.data
        profile = RegisterUser.objects.filter(user_email=user['user_email']).get()
        profileSerializer = ProfileSerializer(profile)
        return Response({
            'profile_data':profileSerializer.data,
        }, status=status.HTTP_200_OK)


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

