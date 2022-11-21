from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .views import RegisterCreateView, EditUserView
from .models import Register


class PatientsView(TestCase):

    def setUp(self):
        self.client = Client()

        Register.objects.create(user_name='username2',
                                user_email='email2@test.com',
                                password='password3',
                                user_dob='1995-10-11',
                                location='location1',
                                user_mobile=9874563210
                                )

    def test_addPatient(self):
        response = self.client.post('/patients/register/',
                                    {'user_name': 'username1', 'user_email': 'email1@test.com', 'password': 'password2',
                                     'user_dob': '1995-10-11', 'location': 'location1',
                                     'user_mobile': 9874563210})

        self.assertEqual(response.status_code, 201)

    def test_listPatientsDetails(self):
        response = self.client.get('/patients/list/')

        self.assertEqual(response.status_code, 200)

    def test_viewPatientsDetails(self):
        response = self.client.get('/patients/view/1')

        response_content = response.content.decode("utf-8")

        self.assertEqual(response.status_code, 200)

    def test_editPatientsDetails(self):
        response = self.client.get('/patients/edit/1')

        self.assertEqual(response.status_code, 200)
