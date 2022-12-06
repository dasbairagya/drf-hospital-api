# drf-hospital-api

This is an appointment booking API's based on Django REST Framework. This API has three features - Register/login, Patient and Appointment . For authenticating user, Django REST Framework custom token authentication is used. API endpoints and sample request/response are given below.




# Endpoints
![Swagger](https://user-images.githubusercontent.com/18226897/205968880-08608d62-34b4-4dcb-92b3-ef99861a7f66.png)


#### Register Endpoints: 'register/'
```
request: POST
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
request: POST
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
request: PUT
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
request: GET
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
request: POST
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
##### Edit : 'patients/edit/\<id\>'
```
request: GET

response:
{
    "profile_data": {
        "user_dob": "2022-11-15",
        "location": "chennai",
        "user_mobile": "8509848752"
    }
}

request: PUT
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
request: GET

response:
{
    "patients": [
        {
            "id": "2",
            "user_name": "patient1",
            "user_email": "patient1@gmail.com",
            "patient": {
                "user_dob": "2022-11-15T00:00:00Z",
                "location": "chennai",
                "user_mobile": "8509848751"
            }
        },
        {
            "id": "3",
            "user_name": "patient2",
            "user_email": "patient2@gmail.com",
            "patient": {
                "user_dob": "2022-11-15T00:00:00Z",
                "location": "chennai",
                "user_mobile": "8509848751"
            }
        },
        {
            "id": "4",
            "user_name": "patient3",
            "user_email": "patient3@gmail.com",
            "patient": {
                "user_dob": "2022-11-15T00:00:00Z",
                "location": "mumbai",
                "user_mobile": "8509848751"
            }
        }
    ]
}

```
##### View : 'patients/view/\<id\>'

```
request: GET

response:
{
    "patient_data": {
        "id": "3",
        "user_name": "patient3",
        "user_email": "patient3@gmail.com",
        "patient": {
            "user_dob": "2022-11-15T00:00:00Z",
            "location": "mumbai",
            "user_mobile": "8509848751"
        }
    },
    "bookappointments": [
        {
            "id": 1,
            "patient": 3,
            "disease": "Fever",
            "date": "2019-11-20",
            "timings": "02:00–03:00",
            "description": "Severe pain"
        },
        {
            "id": 3,
            "patient": 3,
            "disease": "Pain",
            "date": "2019-11-20",
            "timings": "04:00–05:00",
            "description": "Severe tooth pain"
        }
    ]
}

```

#### Appointments Endpoints:

##### Appointments : 'appointment/register/'
```
request: POST
{
"patient":2, 
"disease": "Fever",
"date": "2019-11-12",
"timings":"12.00-1.00",
"description":"Severe pain"
}

response:
{
    "appointments": {
        "id": 1,
        "patient": 2,
        "disease": "Fever",
        "date": "2019-11-12",
        "timings": "12.00-1.00",
        "description": "Severe pain"
    }
}

```
##### Appointments : 'appointment/list/'
```
request: GET

response:
{
    "appointments": [
        {
            "id": 1,
            "patient": 2,
            "disease": "Fever",
            "date": "2019-11-12",
            "timings": null,
            "description": "Severe pain"
        },
        {
            "id": 2,
            "patient": 3,
            "disease": "Fever",
            "date": "2019-11-12",
            "timings": null,
            "description": "Severe pain"
        }
    ]
}

```
##### Appointments : 'appointment/view/\<id\>'
```
request: GET

response:
{
    "appointments": {
        "id": 1,
        "patient": 3,
        "disease": "Fever",
        "date": "2019-11-20",
        "timings": "02:00–03:00",
        "description": "Severe pain"
    }
}

```
##### Appointments : 'appointment/edit/\<id\>'
```
request: PUT <- id=1

{
"appointment":{
    "disease": "Fever",
    "date": "2019-11-20",
    "timings":"04:00–05:00",
    "description":"Severe Pain"
    }
}

response:

{
    "appointment": {
        "id": 1,
        "patient": 3,
        "disease": "Fever",
        "date": "2019-11-20",
        "timings": "04:00–05:00",
        "description": "Severe Pain"
    }
}

```
##### Appointments : 'appointment/delete/\<id\>'
```
request: DELETE <- id=2

response:
{
    "message": "Appointment with id `2` has been deleted."
}

```

#### Generate API Documents:

[drf-spectacular](https://github.com/tfranzel/drf-spectacular/#installation)

#### Authentication
[source](https://python.plainenglish.io/django-custom-user-model-and-auth-using-jwt-simple-boilerplate-6acd78bf7767)

[Pkg: Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)

#### Migration and super user creation:
```
> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser
```