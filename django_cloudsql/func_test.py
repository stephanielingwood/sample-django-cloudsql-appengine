import unittest
from django.test.client import Client

class IntegrationTest(unittest.TestCase):
  def test_index(self):
    c = Client()
    response = c.get('/')
    self.assertRegexpMatches(response.content, r'Hello world, [0-9]+!')
