# 2. Applying GUI to Create a PDF Merging APP
# Earlier we learned how to merge PDFs together. Now, we extend that using GUI.
# GUI should allow users to select as many and whichever PDF users want.

import tkinter as tk  # Import the tkinter module for GUI
from tkinter import filedialog, messagebox  # Import dialog and messagebox for file selection and alerts
from PyPDF2 import PdfMerger  # Import PdfMerger to merge multiple PDF

# Initialize the Tkinter window (WITHOUT using a function)
root = tk.Tk()  # Create the main application window
root.title("PDF Merger")  # Set window title
root.geometry("300x150")  # Set window size


# Function to merge selected PDF files
def merge_pdfs():

    # Open a new file dialog window which allows you to select multiple PDF files.
    files = filedialog.askopenfilenames(title="Select PDF file/s", filetypes=[("PDF Files", "*.pdf")])

    # Check if no files were selected
    if not files:
        messagebox.showwarning("No Files Selected", "Please select some PDF files.")
        return

    # Open a new "SAVE as" dialog window
    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")], title="Save Merged PDF As")

    # Check if no output file was specified
    if not output_file:
        return

    merger = PdfMerger()

    for pdf in files:
        merger.append(pdf)

    merger.write(output_file)
    merger.close()

    messagebox.showinfo("Success", f"PDFs merged successfully into {output_file}")


# Create and add a button to merge PDFs
merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs, padx=30, pady=25)

# The padx and pady specify internal padding INSIDE the button itself.
# padx adds space on the left and right of the button’s text.
# pady adds space above and below the button's text.

merge_button.pack(padx=10, pady=50, expand=True)

# expand=True ensures the widget will expand and center within the window.
# padx=10 and pady=50 provide spacing OUTSIDE of the button.

# Start the main event loop
root.mainloop()
