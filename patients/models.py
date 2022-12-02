import uuid
from time import timezone
from django.db import models
from register.models import RegisterUser


# Create your models here.
class Register(models.Model):

    user_name = models.CharField(max_length=150)
    user_email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    user_dob = models.DateField(null=True)
    location = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=50)

    def create(self, user_email, password=password, **extra_fields):
        if not user_email:
            raise ValueError('The Email must be set')
        user_email = self.normalize_email(user_email)
        user = self.model(user_email=user_email, password=password, **extra_fields)
        user.save(using=self._db)
        return user

    @property
    def get_name(self):
        return self.user_name

    # @property
    # def get_id(self):
    #     return self.id

    def __str__(self):
        return self.user_email
