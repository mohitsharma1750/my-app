import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

completion = openai.ChatCompletion.create( # Change the function Completion to ChatCompletion
  model = 'gpt-3.5-turbo',
  messages = [ # Change the prompt parameter to the messages parameter
    {'role': 'user', 'content': 'Can you give me suggestion on my Resume'}
  ],
  temperature = 0  
)

print(completion['choices'][0]['message']['content']) # Change how you access the message conten