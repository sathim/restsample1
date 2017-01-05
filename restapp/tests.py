# -*- coding: cp1252 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from rest_framework.test import APIClient
from django.test.client import encode_multipart, RequestFactory
import requests
import json

# Create your tests here.
class UserListTestCase(TestCase):
    # Get user details and check the response
    def test_getUserList(self):
        c = Client()
        response = c.get('/user/1')
        self.assertEqual(response.status_code,200)
        
    # Insert data into the database
    '''def test_getUserDetails(self):
        url = 'http://localhost:8000/user/'
        data = {"username": "Ramu", "first_name": "Ram", "last_name": "Ram", "email": "ram@techtreeit.com"}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        self.assertEqual(r.status_code,201)'''

class UserDetailTestCase(TestCase):
    # Check the response for User details
    def test_getUser(self):
        try:
            data = {"first_name": "Raja"}
            headers = {'Content-Type': 'application/json'}
            response = requests.get('http://localhost:8000/users/2/', headers)            
            self.assertEqual(response.status_code,200)
        except AttributeError:
            raise Http404

    # Update the user details    
    def test_putUser(self):
        url = 'http://localhost:8000/users/3/'
        headers = {'Content-Type': 'application/json'}
        r = requests.put(url, {"username": "Asha", "last_name": "Avis"})
        self.assertEqual(r.status_code,200)

    # Delete user
    def test_delUser(self):
        url = 'http://localhost:8000/users/7/'
        headers = {'Content-Type': 'application/json'}
        re = requests.delete(url)
        self.assertEqual(re.status_code,204)

    '''if __name__ == '__main__':
        HTMLTestRunner.main()'''

        


        
        
