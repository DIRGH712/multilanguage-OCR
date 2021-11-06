import pdf2image          # Convert a PDF to a seqeunce of PIL image objects.
from PIL import Image     # Convert PIL image objects into png or jpg file formats   
import os 
import pytesseract
import subprocess
import shutil             # to delete folder


#Converting PDF to Images

resolution = 600
pdf_path = "source.pdf"
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\patel\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Updatings the path to poppler 
pil_images = pdf2image.convert_from_path(pdf_path, dpi=resolution, poppler_path= r'C:\Users\patel\AppData\poppler-21.10.0\Library\bin')


#Convert a sequnce of PIL image objects to required image format and store the images at the required location

os.chdir("E:/projects/multilanguage-OCR") #change path 
file_path="E:/projects/multilanguage-OCR/input_images"

if os.path.exists(file_path):
    shutil.rmtree(file_path)

new_folder_name = "input" + "_images"
subprocess.call("mkdir " + new_folder_name, shell = True)

index=1
for image in pil_images:
    print("Converting page", index)
    image.save("input_images/" + "page_" + str(index) + ".PNG")
    index += 1


#Extracting text from images

total_pages = index - 1
text = ""

#Language is set to "English" in lang.
for i in range(total_pages):
    print("Extracting text from page", i + 1)
    im = Image.open("input_images/page_" + str(i + 1) + ".PNG")
    text = text + pytesseract.image_to_string(im, lang = 'eng')

# Store broken sentences of a paragraph as they appear in the PDF to a text file. 
with open("unformatted.txt", "w", encoding="utf-8") as myfile:
    myfile.write(text)


#Formatting extracted text. Combines segments of a paragraph (broken sentences) in the unformatted text into a single paragraph.
	
edited_text = ""

for i in range(len(text)):
    if text[i] == "\n" and text[i+1] != "\n" and text[i-1] != "\n":
        edited_text = edited_text + " "
    else:
        edited_text = edited_text + text[i]
        
# Storing to a text file
with open("formatted.txt", "w", encoding="utf-8") as myfile:
    myfile.write(edited_text)

#open unformatted extracted txt file
file=r'E:\projects\multilanguage-OCR\unformatted.txt'
os.startfile(file)