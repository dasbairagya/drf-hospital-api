from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth.models import User

from .views import RegisterCreateView, SingleUserView
from .models import RegisterUser


class RegisterView(TestCase):

    def setUp(self):
        self.client = Client()

        RegisterUser.objects.create(user_name='username3',
                                    user_email='email3@test.com',
                                    password='password3',
                                    user_dob='1996-10-11',
                                    location='location3',
                                    user_mobile=9874563210
                                    )

    def test_addAccount(self):
        response1 = self.client.post('/register/', {'user_name': 'username4', 'user_email': 'email4@test.com',
                                                    'password': 'password3', 'user_dob': '1996-10-11',
                                                    'location': 'location4',
                                                    'user_mobile': 9874563210})

        response2 = self.client.get('/viewprofile/1')


        self.assertEqual(response2.status_code, 200)

        self.assertEqual(response1.status_code, 201)


    def test_signinUser(self):

        response = self.client.post('/signin/', {'user_email': 'email3@test.com', 'password': 'password3'})
        # response = self.client.get('/register/')
        # response = self.client.get('/viewprofile/1')

        # @debug
        response_content = response.content.decode("utf-8")
        print(response_content) #..{"non_field_errors":["Unable to log in with provided credentials."]}

        self.assertEqual(response.status_code, 200)

    def test_viewProfile(self):

        response = self.client.get('/viewprofile/1')

        response_content = response.content.decode("utf-8")
        # print(response_content)

        self.assertJSONEqual(
            response_content,
            {'user_name': 'username3',
             'location': 'location3',
             'password': 'password3',
             'user_dob': '1996-10-11',
             'user_email': 'email3@test.com',
             'user_mobile': '9874563210',
             }

        )

        self.assertEqual(response.status_code, 200)

    def test_editUser(self):

        response = self.client.get('/editprofile/1')

        self.assertEqual(response.status_code, 200)
