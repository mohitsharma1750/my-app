import PyPDF2
import re

# Open the PDF file in read-binary mode
pdf_file = open('MohitSharma-Resume.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the first page of the PDF file
page = pdf_reader.pages[0]

# Extract text from the page
text = page.extract_text()

# Define regular expressions to match headings
heading_regex = re.compile(r'\n([A-Z][a-z ]+)\n')

# Find all headings and their positions in the text
headings = [(match.group(1), match.start()) for match in heading_regex.finditer(text)]
print(headings)

# Add end position of last section
headings.append(('End', len(text)))

# Extract sections based on the headings
sections = {}
for i, heading in enumerate(headings[:-1]):
    section_title, start_pos = heading
    next_section_title, end_pos = headings[i+1]
    section_content = text[start_pos:end_pos].strip()
    sections[section_title] = section_content

# Print the sections
print( sections)
for title, content in sections.items():
    print(title + ':\n' + content + '\n')
    
# Close the PDF file
print( "end")
pdf_file.close()
