from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from rest_framework.test import RequestsClient
from django.contrib.auth.models import User
from .views import RegisterCreateView, EditUserView, ListUserView, DeleteUserView, SingleUserView
from .models import BookAppointments
from patients.models import Register


class AppointmentsView(TestCase):

    def setUp(self):
        p = Register.objects.create(user_name='username1',
                                    user_email='email1@test.com',
                                    password='password1',
                                    user_dob='1995-10-11',
                                    location='location1',
                                    user_mobile=9874563210
                                    )

        BookAppointments.objects.create(patients=p,
                                        disease='disease2',
                                        date='2019-11-25',
                                        timings='12.00-1.00',
                                        description='description2'
                                        )

    def test_registerAppointment(self):
        response = self.client.post('/appointment/register/',
                                    {'patients': 1, 'disease': 'disease2', 'date': '2019-11-25',
                                     'timings': '12.00-1.00', 'description': 'description2'})

        self.assertEqual(response.status_code, 201)

    def test_listappointments(self):
        response = self.client.get('/appointment/list/')

        self.assertEqual(response.status_code, 200)

    def test_viewSingleapppointment(self):

        response = self.client.get('/appointment/view/1')
        print('response', response)

        # self.assertEqual(response.status_code, 200)

    def test_editAppointment(self):
        response = self.client.get('/appointment/edit/1')

        self.assertEqual(response.status_code, 200)

    def test_deleteAppointment(self):
        response = self.client.delete('/appointment/delete/1')

        self.assertEqual(response.status_code, 204)




