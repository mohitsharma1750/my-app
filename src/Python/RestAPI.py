from flask import Flask,request,jsonify
import PyPDF2
import pyautogui
from flask_cors import CORS
import json
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello():
    return 'Hello, World!'
    
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request', 500
    file = request.files['file']
    return pdfFunction(file)
    if file.filename == '':
        return 'No file selected', 500
    # Do something with the file, such as save it to disk or process its contents
    print(file.filename)
    response = jsonify({'message': 'File uploaded Mohit'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.headers.add('Content-Type', 'application/json')
    return response, 200


def pdfFunction(file):
    pdf_reader = PyPDF2.PdfReader(file)
    page = pdf_reader.pages[0]
    text = page.extract_text()
    # words = text.split()
    # print ("Number of words"+ str (len(words)) )
    # text = text.replace("\n","")
    # words = text.split()
    # num_words = len(words)
    # print(num_words)
   #   text = getPrompt()
    text = callOpenAPI(text)
    response = {
    'text': text
}
    return response


def getPrompt():
    return "ddgg"
# Open the PDF file
    # with open(file.filename, 'rb') as pdf_file:
    #     # Read the PDF file
    #     pdf_reader = PyPDF2.PdfReader(pdf_file)
    #     # Get the first page of the PDF
    #     page = pdf_reader.pages[0]
    #     # Extract the text from the page
    #     text = page.extract_text()

    # # Split the text into lines
    # lines = text.split('\n')

    # # Define a dictionary to store the values
    # values = {}

    # # Iterate through each line
    # for line in lines:
    #     # Check if the line contains a label followed by a value
    #     if ':' in line:
    #         # Split the line into label and value
    #         label, value, *_ = line.split(':')
    #         # Remove any leading or trailing spaces
    #         label = label.strip()
    #         value = value.strip()
    #         # Add the label and value to the dictionary
    #         values[label] = value
        
   #    print(text)


def callOpenAPI(text):
    completion = openai.ChatCompletion.create( # Change the function Completion to ChatCompletion
    model = 'gpt-3.5-turbo',
    messages = [ # Change the prompt parameter to the messages parameter
        {'role': 'user', 'content': 'Can you give me suggestion on my Resume'+  text}
    ],
    temperature = 0  
    )
    return completion['choices'][0]['message']['content']
# Change how you access the message conten
if __name__ == '__main__':
    app.run(debug=True)

    
