from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.utils.translation import ugettext_lazy as _  
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def get_by_natural_key(self, user_email):
        return self.get(user_email=user_email)
    use_in_migrations = True
    def _create_user(self, user_email, password=None, **kwargs):
        user_email = self.normalize_email(user_email)
        is_staff = kwargs.pop('is_staff', False)
        is_superuser = kwargs.pop('is_superuser', False)
        user = self.model(user_email=user_email, is_active=True, is_staff=is_staff, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, user_email, password=None, **extra_fields):
        return self._create_user(user_email, password, **extra_fields)

    def create_superuser(self, user_email, password, **extra_fields):
        print(f"{user_email=} {password=} {extra_fields=}")
        return self._create_user(user_email, password, is_staff=True, is_superuser=True, **extra_fields)


class RegisterUser(AbstractBaseUser, PermissionsMixin):

    def natural_key(self):
         return (self.user_email,)

    user_name = models.CharField(max_length=150)
    user_email = models.EmailField(unique=True)
    # user_password = models.CharField()
    user_dob = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = UserManager()

    USERNAME_FIELD = 'user_email'
    # REQUIRED_FIELDS = ['user_name', 'user_password']

    def get_full_name(self):
        return self.user_name

    # def get_short_name(self):
    #     return self.user_name.split()[0]

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
