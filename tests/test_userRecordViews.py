from app import app
import unittest

testapp = app.test_client()

class Test_test(unittest.TestCase):
    def test_user_registration_valid_inputs(self):
        response = self.register(full_name='Hezron kimutai',
        email='kim@gmail.com',username='kim',password='HHeezziiee1357&%',
        repeat_password='HHeezziiee1357&%')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'')

    def register(self,full_name,email,username,password,repeat_password):
        return testapp.post('/users',data=dict(full_name=full_name,
        email=email,username=username,password=password,repeat_password=repeat_password),
        follow_redirects=True)
