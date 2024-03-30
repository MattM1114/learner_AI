import unittest
from app import home_page

class HomePageTestCase(unittest.TestCase):

    def test_home_page(self):
        response = home_page()
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_content(self):
        response = home_page()
        self.assertIn(b'Welcome', response.data)

