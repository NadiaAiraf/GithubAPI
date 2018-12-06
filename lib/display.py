import getpass

class Display:
    def __init__(self):
        self.username = None

    def get_search_word(self):
        print('To find a github users preferred language, please enter their username: ')
        self.username = raw_input()
        return self.username

    def return_favourite_language(self, string):
        print(self.username + "'s favourite language is " + string)
