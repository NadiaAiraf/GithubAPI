from lib.display import Display
from lib.client_api import *

class Controller:

    def __init__(self, display=Display(), client_api=ClientApi()):
        self.display = display
        self.client_api = client_api


    def favourite_language(self, array):
        return max(array, key=array.count)

    def run_app(self):
        username = self.display.get_search_word()
        languages = self.client_api.return_repo_languages(username)
        favourite_language = self.favourite_language(languages)
        self.display.return_favourite_language(favourite_language)
