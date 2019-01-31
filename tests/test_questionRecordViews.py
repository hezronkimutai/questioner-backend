from app import app
from .base_test import BaseTest
import unittest

testapp = app.test_client()

class Test_test(unittest.TestCase):
    def test_questions_valid_inputs(self):
        response = self.question1(title='Andela',
        body='This is andela')
        self.assertEqual(response.status_code,201)
        '''self.assertIn(b'')'''

    def question1(self,title, body):
        return testapp.post('/questions',data=dict(title=title,
        body=body),
        follow_redirects=True)

    def test_questions_invalid_inputs(self):
        response = self.question2(title='',
        body='')
        self.assertEqual(response.status_code,400)
        '''self.assertIn(b'')'''

    def question2(self,title, body):
        return testapp.post('/questions',data=dict(title=title,
        body=body),
        follow_redirects=True)
