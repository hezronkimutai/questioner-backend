
import pytest
import json
import unittest

from app import app

class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.user = {
            "username": "username",
            "email": "email@user.com",
            "password": "yourpassword",
            "repeat_password": "yourpassword"
        }

    def test_api_can_signup_user(self):
        response = self.client.post('/app/views', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
