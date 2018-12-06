import unittest
from unittest import mock
from lib.controller import *

class ControllerTest(unittest.TestCase):

    def setUp(self):
        client_api_mock = mock.Mock()
        display_mock = mock.Mock()
        self.controller = Controller(display_mock, client_api_mock)

    # def test_run_app(self):
    #     self.controller.main()
    #     self.controller.display.get_search_word.assert_called()
    #     self.controller.client_api_mock.get_search_word.assert_called()

    def test_favourite_language(self):
        array_of_languages = ['ruby', 'python', 'python', 'javascript']
        language = self.controller.favourite_language(array_of_languages)
        self.assertEqual(language, 'python')
