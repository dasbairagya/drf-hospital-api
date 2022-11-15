# drf-hospital-api

## Register Endpoints:
```
# To register the user = 'register/'
sample data:
{
    "user_name": "gopal",
    "user_email": "gopal@gmail.com",
    "password": "gopal@123",
    "user_dob": "2022-11-15",
    "location": "kokata",
    "user_mobile": "8509848755"
}

# To signin the user = 'signin/'
# To edit all user = 'editprofile/'
# To view a single user = 'viewprofile/'

```

## Patients Endpoints:
```
# To register the patient = 'patients/register/'
# To edit a single patients = 'patients/edit/'
# To list all patients = 'patients/list/'
# To view a single patients = ('patients/view/'
```

## Appointments Endpoints:
```
# To register the appointment = 'appointment/register/'
# To edit a single appointment = 'appointment/edit/'
# To list all appointments = 'appointment/list/'
# To delete a single appointment = ('appointment/delete/'
# To view a single appointment = ('appointment/view/'
```

## Generate API Documents:

[drf-spectacular](https://github.com/tfranzel/drf-spectacular/#installation)

## Authentication
[source](https://python.plainenglish.io/django-custom-user-model-and-auth-using-jwt-simple-boilerplate-6acd78bf7767)

[Pkg: Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)

## Create super user:
```
python manage.py createsuperuser

```