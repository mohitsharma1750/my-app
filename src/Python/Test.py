import PyPDF2
import pyautogui

# Open the PDF file
with open('MohitSharma-Resume.pdf', 'rb') as pdf_file:
    # Read the PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # Get the first page of the PDF
    page = pdf_reader.pages[0]
    # Extract the text from the page
    text = page.extract_text()

# Split the text into lines
lines = text.split('\n')

# Define a dictionary to store the values
values = {}

# Iterate through each line
for line in lines:
    # Check if the line contains a label followed by a value
    if ':' in line:
        # Split the line into label and value
        label, value, *_ = line.split(':')
        # Remove any leading or trailing spaces
        label = label.strip()
        value = value.strip()
        # Add the label and value to the dictionary
        values[label] = value
      
print(values)
# Fill out the form
pyautogui.click(100, 100)  # Click on the first field
pyautogui.typewrite(values['Contact'])  # Fill out the Name field
pyautogui.press('tab')  # Move to the next field
pyautogui.typewrite(values['Email'])  # Fill out the Email field
pyautogui.press('tab')  # Move to the next field
pyautogui.typewrite(values['Contact'])  # Fill out the Phone field
