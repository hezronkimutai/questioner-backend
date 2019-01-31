from app import app
from .base_test import BaseTest
import unittest

testapp = app.test_client()

class Test_test(unittest.TestCase):
    def test_meetup_valid_inputs(self):
        response = self.meetup1(meetup_title='Flask',
        meetup_body='Flask is very good')
        self.assertEqual(response.status_code,201)
        '''self.assertIn(b'')'''

    def meetup1(self,meetup_title, meetup_body):
        return testapp.post('/meetups',data=dict(meetup_title=meetup_title,
        meetup_body=meetup_body),
        follow_redirects=True)

    def test_meetup_invalid_inputs(self):
        response = self.meetup2(meetup_title='',
        meetup_body='')
        self.assertEqual(response.status_code,400)
        '''self.assertIn(b'')'''

    def meetup2(self,meetup_title, meetup_body):
        return testapp.post('/meetups',data=dict(meetup_title=meetup_title,
        meetup_body=meetup_body),
        follow_redirects=True)
