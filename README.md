# Github Tech Test

The aim for this tech test is to create an application that uses Githubs REST API to take a username and return your best guess at their favourite programming language.

I don't have a huge amount of experience with Python but I decided to use it to create this app in order to test myself. This came with plenty of it's own problems (see the testing section further on) but also greatly helped my understanding of Python in general.

## How to run

This assumes you already have python installed, if not you can find instructions [here](https://www.python.org/downloads/):

1. save these files locally
2. navigate into the folder on the command line
3. install any packages you need `pip install -r requirements.txt`
4. enter into the command line `python run_app`
5. enter the Github username you would like information on

## Example

```
$ python run_app.py
To find a github users preferred language, please enter their username:
NadiaAiraf
---
NadiaAiraf's favourite language is Ruby
```

## Approach to the problem

I decided to have 3 separate objects for this project. My ClientApi is responsible for returning all of the languages used by any given user, done by interacting with Githubs API. My Display class deals with everything relating to the command line input/outputs and finally the Controller class connects the two.

## Testing

In order to run the tests use the following command:
```
coverage run --source=lib -m unittest && coverage report
```

## Problems to overcome

- More work is needed on how to use mocks in Python. Calls to Githubs API were successfully mocked during tests which is great. However, mocking of instance methods in the controller class specifically gave issues. There is an instance of one of the tests that gave me trouble with mocks in the `test_controller.py` file.
- The Github API only gives you a certain number of calls per day without authentication. I had planned to add functionality that would ask you to authenticate if it reached it's limit for the day but ran out of time with the mock testing.
- If given an actual user name the program works, if given a username that doesn't exist the program crashes. Again I had planned to add edge cases for this but was hindered by testing on the MVP.
