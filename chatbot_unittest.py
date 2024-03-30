import unittest
from unittest.mock import patch, Mock
from io import StringIO
import sys
import chatbot  # Assuming your chatbot functions are defined in a module named chatbot

class TestChatbot(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['search quantum computing', 'exit'])
    def test_academic_search(self, mock_input, mock_stdout):
        # Mock the search function to avoid making actual requests to Google Scholar
        with patch('chatbot.academic_search') as mock_search:
            chatbot.chat()  # Run the chatbot
            mock_search.assert_called_with('quantum computing')

        # Check if the chatbot displays the correct output
        expected_output = "Top 10 relevant results for 'quantum computing' from "
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['explain quantum computing', 'exit'])
    def test_explain(self, mock_input, mock_stdout):
        # Mock the explanation function
        with patch('chatbot.explain') as mock_explain:
            chatbot.chat()  # Run the chatbot
            mock_explain.assert_called_with('quantum computing')

        # Check if the chatbot displays the correct output
        expected_output = "Title:"
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['summary quantum computing', 'exit'])
    def test_summarize_google_scholar(self, mock_input, mock_stdout):
        # Mock the summarize function
        with patch('chatbot.summarize_google_scholar') as mock_summarize:
            chatbot.chat()  # Run the chatbot
            mock_summarize.assert_called_with('quantum computing')

        # Check if the chatbot displays the correct output
        expected_output = "Summaries for search results on 'quantum computing':"
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['quiz physics', 'exit'])
    def test_conduct_quiz_and_flashcards(self, mock_input, mock_stdout):
        # Mock the quiz function
        with patch('chatbot.conduct_quiz_and_flashcards') as mock_quiz:
            chatbot.chat()  # Run the chatbot
            mock_quiz.assert_called_with('physics')

        # Check if the chatbot displays the correct output
        expected_output = "Generating quiz and flashcards for the topic: physics"
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['math 2+2', 'exit'])
    def test_calculate(self, mock_input, mock_stdout):
        # Mock the calculate function
        with patch('chatbot.calculate') as mock_calculate:
            chatbot.chat()  # Run the chatbot
            mock_calculate.assert_called_with('2+2')

        # Check if the chatbot displays the correct output
        expected_output = "Result = 4.0"
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['invalid input', 'exit'])
    def test_invalid_input(self, mock_input, mock_stdout):
        # Check if the chatbot handles invalid input gracefully
        with patch('chatbot.input', side_effect=['invalid input', 'exit']), patch('sys.stdout', new_callable=StringIO) as mock_output:
            chatbot.chat()

        # Check if the chatbot displays the correct output
        expected_output = "I'm sorry, I don't understand."
        self.assertIn(expected_output, mock_output.getvalue())

if __name__ == '__main__':
    unittest.main()
