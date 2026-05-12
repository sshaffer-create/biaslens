#we are creating an app that reads the PDF in a voice
#Simply put this is our Alexa for our PDF

import pyttsx3
import PyPDF2

book = open('mislead.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()

for num in range(3, pages):
    page =pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
