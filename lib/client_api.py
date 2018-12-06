import requests
import json

class ClientApi:

    def __init__(self):
        self.response = None

    def return_repo_languages(self, username='nadiaairaf'):
        return self.return_languages(self.make_api_request(username))

    def make_api_request(self, username):
        url = "https://api.github.com/users/" + username + "/repos"
        self.response = requests.get(url)
        return self.response.text

    def return_languages(self, data):
        repositories = json.loads(data)
        languages = []
        for repo in repositories:
            languages.append(repo['language'])
        return languages
