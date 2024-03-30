import unittest
import chatbot
from chatbot import respond


class TestRespond(unittest.TestCase):

    def test_respond_hello(self):
        input_text = "hello"
        expected = "Hello there! How can I help you today?"
        actual = respond(input_text)
        self.assertEqual(actual, expected)

    def test_respond_goodbye(self):
        input_text = "goodbye"
        expected = "Goodbye! Have a nice day." 
        actual = respond(input_text)
        self.assertEqual(actual, expected)

    def test_respond_empty_input(self):
        input_text = ""
        expected = "Sorry, I didn't get that. Could you please repeat?"
        actual = respond(input_text)
        self.assertEqual(actual, expected)

    def test_respond_unknown_input(self):
        input_text = "asdfjklasdfjklasdf" 
        expected = "Sorry, I don't understand. Could you rephrase your question?"
        actual = respond(input_text)
        self.assertEqual(actual, expected)

