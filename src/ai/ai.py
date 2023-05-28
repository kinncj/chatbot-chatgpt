import openai
import json

class AI:
    def __init__(self, api_key, context_file):
        self.cli = openai
        self.cli.api_key = api_key
        self.context_file = context_file
        self.messages = self.read()

    def hello(self, name):
        if (len(self.messages) == 0):
            self.request("Hi, you can call me " + name)
    
    # API Calls to OpenAI
    def request(self, prompt, model='gpt-3.5-turbo'):
        message = {'role': 'user', 'content': prompt}
        self.write(message)
        response = openai.ChatCompletion.create(model=model, messages=self.messages)
        self.write(response['choices'][0]['message'])
        return response['choices'][0]['message']['content']
    
    def read(self):
        file = open(file=self.context_file, mode="a+", encoding="UTF8")
        file.close()
        file = open(file=self.context_file, mode="r", encoding="UTF8")
        try:
            message = file.read()
            file.close()
            messages = json.loads(message)
        except Exception as e:
            messages = []
            
        return messages

    def write(self, message):
        self.messages.append(message)
        file = open(file=self.context_file, mode="w", encoding="UTF8")
        file.write(json.dumps(self.messages))
        file.close()
