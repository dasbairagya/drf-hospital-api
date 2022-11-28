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
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = LoginSerializers(data=request.data, context={ 'request': self.request })
        # serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            # print(serializer.validated_data)
            user = serializer.validated_data['user']
            # print('login view => ',user)
            #return Response(None, status=status.HTTP_202_ACCEPTED)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Method to list/edit a particular user
class SingleUserView(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return RegisterUser.objects.get(id=pk)  # as our model does not have a specified id as a primary key hence pk=pk with id=pk
        except RegisterUser.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            user = self.get_object(pk)
            # print(user)
            serializer = RegisterUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None, format=None):
        if pk:
            user = self.get_object(pk)
            serializer = RegisterUserSerializer(user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


