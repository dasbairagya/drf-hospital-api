from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

# Create your views here.
class RegisterView(APIView):
    def post(self,)