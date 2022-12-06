import uuid
from time import timezone
from django.db import models
from register.models import RegisterUser


# Create your models here.
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, null=False)
    user_email = models.EmailField(max_length=80, null=False, unique=True)
    user_dob = models.DateField(null=False)
    location = models.CharField(max_length=255, null=False)
    user_mobile = models.CharField(max_length=10, null=False)
