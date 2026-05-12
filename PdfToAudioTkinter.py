#Creating audio book out of PDF
#We are creating an audio book that reads PDF but allows choosing the PDF using GUI

import tkinter as tk
from tkinter import filedialog, messagebox  # filedialog opens file chooser; messagebox displays popup alerts
from gtts import gTTS  # gTTS converts text into spoken audio (MP3 format)
from PyPDF2 import PdfReader  # PdfReader reads and extracts text from PDF files
import os  # os allows interaction with the operating system (e.g., opening files)

# Create the main Tkinter window
root = tk.Tk()  # Creates the main application window
root.title("PDF to Audiobook Converter")  # Sets the window title
root.geometry("400x200")  # Sets window size (width x height)

# Function to select PDF and convert it to audiobook
def convert_to_audiobook():

   pdf_path = filedialog.askopenfilename(
       title="Select a PDF file",
       filetypes=[("PDF Files", "*.pdf")]
   )  # Opens file selection dialog restricted to PDF files

   if not pdf_path:
       messagebox.showwarning("No file selected", "Please select a PDF file to convert.")
       return  # Stops execution if user cancels selection

   try:
       with open(pdf_path, 'rb') as book:  # Opens selected PDF in binary read mode
           pdfReader = PdfReader(book)  # Loads PDF into PdfReader object
           pages = len(pdfReader.pages)  # Counts total number of pages in the PDF
           full_text = ""  # This string will store text from all pages combined

           for num in range(pages):  # Loops through pages using index numbers (0, 1, 2, ...)
               page = pdfReader.pages[num]  # Retrieves one page at a time
               text = page.extract_text()  # Extracts readable text from that page
               if text:
                   full_text += text  # This does NOT increase page numbers; the for loop controls page movement. This line simply appends each page’s extracted text to full_text, building one large combined text string page by page.

       tts = gTTS(text=full_text, lang='en')  # Creates a text-to-speech object using the complete extracted PDF text. The argument text=full_text sends all combined content, and lang='en' sets English pronunciation.

       output_mp3 = pdf_path.rsplit('.', 1)[0] + "_audiobook.mp3"
       # rsplit('.', 1) splits the filename from the right at the last dot and removes the .pdf extension. For example, if the file is "March.pdf", rsplit returns ["March", "pdf"], we take [0] which is "March", and then add "_audiobook.mp3", resulting in "March_audiobook.mp3".

       tts.save(output_mp3)  # Converts text into speech and saves it as the new MP3 file

       messagebox.showinfo("Success", f"Audiobook has been created and saved as {output_mp3}")
       os.startfile(output_mp3)  # Opens the generated MP3 using the system’s default media player (Windows only)

   except Exception as e:
       messagebox.showerror("Error", f"An error occurred: {e}")  # Displays error message if something fails

convert_button = tk.Button(
    root,
    text="Convert PDF to Audiobook",
    command=convert_to_audiobook,
    padx=20,
    pady=10
)

convert_button.pack(expand=True)  # Places button in center of window

root.mainloop()  # Starts event loop and keeps window running