from lib.display import *
from lib.client_api import *

class Controller:

    def __init__(self, display=Display, client_api=ClientApi):
        self.display = display
        self.client_api = ClientApi

    def run_app(self):
        username = self.display.get_search_word()
        languages = self.client_api.return_repo_languages(username)
