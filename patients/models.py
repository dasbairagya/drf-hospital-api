from time import timezone
from django.db import models
from register.models import RegisterUser

# Create your models here.
class Patient(models.Model):
    user_dob = models.DateTimeField()
    location = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=50)
    user = models.OneToOneField(RegisterUser, on_delete=models.CASCADE, primary_key=True) #field name 'user' of Patient table is the Foregn key of RegisterUser table

    @property
    def get_name(self):
        return self.user.user_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.user_email