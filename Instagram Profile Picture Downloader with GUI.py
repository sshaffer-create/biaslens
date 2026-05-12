#Instagram profile picture download with GUI

# We are importing the tkinter library, which helps us create windows and buttons.
import tkinter as tk
# Importing messagebox to show pop-up messages like success or error messages.
from tkinter import messagebox
# This is the library that helps us download Instagram profile pictures.
import instaloader


# This function will run when we click the "Download Profile Picture" button
def download_profile_pic():
   # 'entry.get()' gets whatever the user types in the text box (Instagram username)
   username = entry.get()

   # If the user typed something (if username is not empty)
   if username:
       try:
           # We create a new 'instaloader' object that helps us download things from Instagram
           ig = instaloader.Instaloader()
           # This command downloads the profile picture for the username entered
           ig.download_profile(username, profile_pic_only=True)
           # Show a pop-up message saying the picture was downloaded successfully
           messagebox.showinfo("Success", f"Profile picture of {username} downloaded successfully!")
       except Exception as e:
           # If there was an error (like no internet or wrong username), show an error message
           messagebox.showerror("Error", f"Error downloading profile picture: {str(e)}")
   else:
       # If the username field is empty, show a warning to the user
       messagebox.showwarning("Input Error", "Please enter a valid Instagram username.")


# Now we are creating the window where everything will be displayed
root = tk.Tk()
# This changes the title of the window (the top part of the window)
root.title("Instagram Profile Picture Downloader")
root.geometry("400x200")

# This is the label that asks the user to enter an Instagram username
label = tk.Label(root, text="Enter Instagram Username:")
# This puts the label on the window and adds some space around it
label.pack(pady=10)

# This creates a box where the user can type the Instagram username
entry = tk.Entry(root, width=40)
# This puts the text box on the window and adds some space around it
entry.pack(pady=5)

# This creates a button that says "Download Profile Picture"
# When the button is clicked, it will call the 'download_profile_pic' function
download_button = tk.Button(root, text="Download Profile Picture", command=download_profile_pic)
# This places the button on the window and adds some space around it
download_button.pack(pady=20)

# This starts the window and waits for the user to interact with it
root.mainloop()
