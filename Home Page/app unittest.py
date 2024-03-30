import unittest
from app import homepage

class TestHomepage(unittest.TestCase):

    def test_homepage(self):
        response = homepage()
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_content_type(self):
        response = homepage()
        self.assertEqual(response.content_type, 'text/html')

