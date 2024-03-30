import json
from unittest.mock import patch
from flask import Flask
from app import handle_query

import unittest

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_handle_query(self):
        query_data = {'query': 'math 3**4'}
        with patch('app.chat') as mock_chat:
            mock_chat.return_value = 'ResearchBot: Result = 81.0000000000000'
            response = self.client.post('/query', json=query_data)
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(data['response'], 'Hello! How can I help you?')

if __name__ == '__main__':
    unittest.main()