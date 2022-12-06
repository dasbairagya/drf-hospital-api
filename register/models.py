from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class RegisterUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, null=False)
    user_email = models.EmailField(unique=True)
    password = models.CharField(max_length=30, null=False)
    user_dob = models.DateField(null=False)
    location = models.CharField(max_length=255, null=False)
    user_mobile = models.CharField(max_length=10, null=False)

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = []
