import unittest
from unittest import mock
from lib.controller import *

class ControllerTest(unittest.TestCase):

    def setUp(self):
        self.client_api_mock = mock.MagicMock()
        self.client_api_mock.return_repo_languages.return_value = 'nadiaairaf'

        self.display_mock = mock.MagicMock()
        self.display_mock.get_search_word.return_value = ['python', 'ruby', 'python']
        self.controller = Controller(self.display_mock, self.client_api_mock)

    def test_run_app(self):
        self.controller.run_app()
        self.controller.display.get_search_word.assert_called()
        self.controller.client_api.return_repo_languages.assert_called()
        self.controller.display.return_favourite_language.assert_called()

    def test_favourite_language(self):
        array_of_languages = ['ruby', 'python', 'python', 'javascript']
        language = self.controller.favourite_language(array_of_languages)
        self.assertEqual(language, 'python')
