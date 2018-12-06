import unittest
from unittest import mock
from lib.controller import *

class ControllerTest(unittest.TestCase):

    def setUp(self):
        client_api_mock = mock.Mock()
        display_mock = mock.Mock()
        self.controller = Controller(display_mock, client_api_mock)

    def test_run_app(self):
        self.controller.run_app()
        self.controller.display.get_search_word.assert_called()
