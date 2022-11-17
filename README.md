# drf-hospital-api

![](./endpoints.png)

#### Register Endpoints: 'register/'
```
request: post
{
    "user_name": "gopal",
    "user_email": "gopal@gmail.com",
    "password": "gopal@123",
    "user_dob": "2022-11-15",
    "location": "kokata",
    "user_mobile": "8509848755"
}

response:
{
    "id": 4,
    "password": "pbkdf2_sha256$390000$AWKJfIVoIrBEzZ8OfwzAhs$jJHBKKH+Nn/1+WHh6nbR17WhH1TyVWZ5efdCuIyMBhU=",
    "last_login": null,
    "is_superuser": false,
    "user_name": "gopal",
    "user_email": "gopal@gmail.com",
    "user_dob": "2022-11-15T00:00:00Z",
    "location": "kokata",
    "user_mobile": "8509848755",
    "is_staff": false,
    "is_active": true,
    "groups": [],
    "user_permissions": []
}
```
#### Login endpoint: 'signin/'
````
request: post
{
    "user_email":"gopal@gmail.com",
    "password":"gopal@123"
}

response:
{
    "msg": "Login Success",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2ODcwMDI2MywiaWF0IjoxNjY4NjEzODYzLCJqdGkiOiIzZThlYTI1NDZkNjg0ZGZkOWNiMGUyODRjOWQzMjYwMiIsInVzZXJfaWQiOjJ9.oCvlAp5k7robOXHVxihdli7JxY6Quo0niVbfebnY34s",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4NzAwMjYzLCJpYXQiOjE2Njg2MTM4NjMsImp0aSI6IjQ2MDdiNWUwMGJjNTRkZjdiZDdhMWNmYzNiNmJhODFkIiwidXNlcl9pZCI6Mn0.2ERjms3IIGl213ouD-zDZnLr8lir4nxP-l9f54hYJ4c"
}
````

#### Edit Profile Endpoint: 'editprofile/'
```
request: put
{
    "user_email":"gopal@gmail.com",
     "profile_data": {
        "user_dob": "2022-11-15T00:00:00Z",
        "location": "Kolkata",
        "user_mobile": "8509848755"
    }
}

response:
{
     "profile_data": {
        "user_dob": "2022-11-15T00:00:00Z",
        "location": "Kolkata",
        "user_mobile": "8509848755"
    }
}
```
#### View Profile Endpoint: 'viewprofile/'
```
request: get
{
    "user_email":"gopal@gmail.com"
}

response:
{
    "profile_data": {
        "user_dob": "2022-11-15T00:00:00Z",
        "location": "Kolkata",
        "user_mobile": "8509848755"
    }
}

```

#### Patients Endpoints:

##### Register : 'patients/register/'
```
request: post
{
    "user_name": "patient1",
    "user_email": "patient1@gmail.com",
    "password": "password",
    "user_dob": "2022-11-15",
    "location": "chennai",
    "user_mobile": "8509848751"
}

response:
{
    "user_data": {
        "id": 2,
        "password": "pbkdf2_sha256$390000$IUxZIeOi8hthHyj9pP8I2n$qthIIL0c/o3Y8SehSb0sGGkO3SlhpC1Ko5V/O4pQ7bc=",
        "last_login": null,
        "is_superuser": false,
        "user_name": "patient1",
        "user_email": "patient1@gmail.com",
        "user_dob": "2022-11-15T00:00:00Z",
        "location": "chennai",
        "user_mobile": "8509848751",
        "is_staff": false,
        "is_active": true,
        "groups": [
            1
        ],
        "user_permissions": []
    },
    "profile_data": {
        "user_dob": "2022-11-15T00:00:00Z",
        "location": "chennai",
        "user_mobile": "8509848751"
    }
}

```
##### Edit : 'patients/edit/<id>'
```
request: get

response:
{
    "profile_data": {
        "user_dob": "2022-11-15",
        "location": "chennai",
        "user_mobile": "8509848752"
    }
}
----------------------------------------------------------

request: put
{
    "profile_data":{
        "user_dob": "2022-11-16",
        "location": "kolkata",
        "user_mobile": "8509848752"
    }
}
response:
{
    "profile_data":{
        "user_dob": "2022-11-16",
        "location": "kolata",
        "user_mobile": "8509848752"
    }
}



```
##### List : 'patients/list/'
```
request: post

response:

```
##### View : 'patients/view/'

```
request: post

response:

```

#### Appointments Endpoints:
```
# To register the appointment = 'appointment/register/'
# To edit a single appointment = 'appointment/edit/'
# To list all appointments = 'appointment/list/'
# To delete a single appointment = ('appointment/delete/'
# To view a single appointment = ('appointment/view/'
```

#### Generate API Documents:

[drf-spectacular](https://github.com/tfranzel/drf-spectacular/#installation)

#### Authentication
[source](https://python.plainenglish.io/django-custom-user-model-and-auth-using-jwt-simple-boilerplate-6acd78bf7767)

[Pkg: Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)

#### Create super user:
```
python manage.py createsuperuser

```