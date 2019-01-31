from app import app
from .base_test import BaseTest
import unittest

testapp = app.test_client()

class Test_test(unittest.TestCase):
    def test_user_registration_valid_inputs(self):
        response = self.register(full_name='Hezron kimutai',
        email='kim@gmail.com',username='kim',password='HHeezziiee1357&%',
        repeat_password='HHeezziiee1357&%')
        self.assertEqual(response.status_code,201)
        '''self.assertIn(b'')'''

    def register(self,full_name,email,username,password,repeat_password):
        return testapp.post('/signup',data=dict(full_name=full_name,
        email=email,username=username,password=password,repeat_password=repeat_password),
        follow_redirects=True)


    def test_user_registration_invalid_password(self):
        response = self.pregister(full_name='Hezron kimutai',
        email='kim@gmail.com',username='kim',password='jkl',
        repeat_password='jkl')
        self.assertEqual(response.status_code,400)
        '''self.assertIn(b'')'''

    def pregister(self,full_name,email,username,password,repeat_password):
        return testapp.post('/signup',data=dict(full_name=full_name,
        email=email,username=username,password=password,repeat_password=repeat_password),
        follow_redirects=True)


    def test_user_registration_different_passwords(self):
        response = self.pregister(full_name='Hezron kimutai',
        email='kim@gmail.com',username='kim',password='HHeezziiee1357&%',
        repeat_password='HHeezziie')
        self.assertEqual(response.status_code,400)
        '''self.assertIn(b'')'''

    def pregister(self,full_name,email,username,password,repeat_password):
        return testapp.post('/signup',data=dict(full_name=full_name,
        email=email,username=username,password=password,repeat_password=repeat_password),
        follow_redirects=True)

    def test_user_registration_no_inputs(self):
        response = self.pregister(full_name='',
        email='',username='',password='',
        repeat_password='')
        self.assertEqual(response.status_code,400)
        '''self.assertIn(b'')'''

    def pregister(self,full_name,email,username,password,repeat_password):
        return testapp.post('/signup',data=dict(full_name=full_name,
        email=email,username=username,password=password,repeat_password=repeat_password),
        follow_redirects=True)
