import unittest
from chatbot import get_response

class TestGetResponse(unittest.TestCase):

    def test_get_response_returns_string(self):
        response = get_response("Hello")
        self.assertIsInstance(response, str)

    def test_get_response_not_empty(self):
        response = get_response("How are you?")
        self.assertTrue(len(response) > 0)

    def test_get_response_varies(self):
        response1 = get_response("What is your name?")
        response2 = get_response("What is your name?")
        self.assertNotEqual(response1, response2)

