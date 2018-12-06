import unittest
from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none
from lib.client_api import ClientApi

class Interaction(unittest.TestCase):

    def test_make_api_request(mock_get):
        client_api = ClientApi()
        with patch('lib.client_api.requests.get') as mock_get:
            mock_get.return_value_ok = True
            response = client_api.make_api_request('nadiaairaf')
        assert_is_not_none(response)

    # def test_return_repo_languages(self):
    #     client_api = ClientApi()
    #     with patch('lib.client_api.requests.get') as mock_get:
    #         mock_get.text = '[{"language":"Javascript"}]'
    #         languages = client_api.return_repo_languages('nadiaairaf')
    #
    #     self.assertEqual(languages, ['hello'])


    def test_return_languages(self):
        client_api = ClientApi()
        json_string = '[{"language":"Javascript"}]'
        language = client_api.return_languages(json_string)
        self.assertEqual(language, ['Javascript'])

    def test_return_languages_multiple(self):
        client_api = ClientApi()
        json_string = '[{"language":"Javascript"}, {"language": "Ruby"}]'
        language = client_api.return_languages(json_string)
        self.assertEqual(language, ['Javascript', 'Ruby'])
