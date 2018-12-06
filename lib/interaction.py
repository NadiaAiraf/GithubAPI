import requests

class Interaction:

    def __init__(self):
        self.response = None

    def get_data(self, username):
        data = make_api_request(username)

    def make_api_request(self, username):
        url = "https://api.github.com/users/" + username + "/repos"
        self.response = requests.get(url)
        return self.response
