import unittest
from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none
from lib.interaction import Interaction

class InteractionTest(unittest.TestCase):

    def test_make_api_request(mock_get):
        interaction = Interaction()
        with patch('lib.interaction.requests.get') as mock_get:
            mock_get.return_value_ok = True
            response = interaction.make_api_request('nadiaairaf')
        assert_is_not_none(response)
