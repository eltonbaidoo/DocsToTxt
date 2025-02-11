from docx import Document

# Load the .docx file
doc = Document('HW1 Introduction 2.docx')
#replace the file name with the file you want to convert

# Extract and print the text
for paragraph in doc.paragraphs:
    print(paragraph.text)