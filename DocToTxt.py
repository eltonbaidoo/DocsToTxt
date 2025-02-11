from docx import Document

# Load the .docx file
doc = Document('Name of File.docx')
#replace the file name with the file you want to convert
#Inlcude the path in it does not have a file 

# Extract and print the text
option = int(input("1. Print in Console \n 2. Export to Txt file "))

for paragraph in doc.paragraphs:
    print(paragraph.text)
