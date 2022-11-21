import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.utils.translation import ugettext_lazy as _  
from django.utils import timezone


# Create your models here.
class UserManager(BaseUserManager):
    def get_by_natural_key(self, user_email):
        return self.get(user_email=user_email)

    use_in_migrations = True

    def create_user(self, user_email, password, **extra_fields):

        if not user_email:
            raise ValueError('The Email must be set')
        user_email = self.normalize_email(user_email)
        user = self.model(user_email=user_email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_email, password, **extra_fields):

        # print(f"{user_email=} {password=} {extra_fields=}")
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(user_email, password, **extra_fields)


class RegisterUser(AbstractBaseUser, PermissionsMixin):

    def natural_key(self):
        return self.user_email,

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_name = models.CharField(max_length=150)
    user_email = models.EmailField(max_length=255, unique=True)
    user_dob = models.DateField()
    location = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'user_email'

    # REQUIRED_FIELDS = ['user_name', 'user_password']

    def __str__(self):
        return self.user_email

