import os

from .ai.ai import AI

from dotenv import load_dotenv
from pathlib import Path

OPENAI_API_KEY =  os.getenv('OPENAI_API_KEY')
CONFIG_DIR =  os.getenv('CONFIG_DIR')

user_name = input("Username: ")
user_context = CONFIG_DIR + '/' + user_name + '_context.json'

ai = AI(OPENAI_API_KEY, user_context)

ai.hello(user_name)

while True:
    request = input("Question: ")
    response = ai.request(request)

    print("Assistant: " + response)

    if (request == "bye"):
        break
