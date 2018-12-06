import getpass

class Display:

    def get_search_word(self):
        print('To find a github users preferred language, please enter their username: ')
        username = raw_input()
        return username
