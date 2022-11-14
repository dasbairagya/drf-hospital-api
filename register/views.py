from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import UserSerializer

# Create your views here.
class RegisterView(APIView):

    permission_classes = []

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)