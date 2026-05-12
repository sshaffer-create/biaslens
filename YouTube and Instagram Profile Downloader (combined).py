#Youtube Video Downloader and Instagram Profile Downloader Combined with GUI

#Combined GUI for downloading YouTube video and Instagram Profile picture

import tkinter as tk  # This helps us create windows (like magic drawing paper)
from tkinter import messagebox  # This shows pop-up messages (like "Yay! Downloaded!")
import instaloader  # This is a tool to get Instagram pictures
import os  # This helps us work with files and folders
import pytube  # This helps us download YouTube videos (like saving your favorite cartoons!)


# Function to download Instagram profile picture
def download_instagram_profile_pic():
   username = entrybox1.get()  # Get the Instagram username from the box

   if username:  # Check if the box is not empty
       try:
           ig = instaloader.Instaloader()  # Create an Instagram downloader

           ig.download_profile(username, profile_pic_only=True)  # Download the profile picture only

           folder_name = username  # Instagram saves pictures in a folder named after the username
           old_file_path = os.path.join(folder_name, 'profile_pic.jpg')  # Find the downloaded picture

           new_file_name = f"{username}_profile_pic.jpg"  # Give it a new name

           if os.path.exists(old_file_path):  # Check if the picture really exists
               os.rename(old_file_path, new_file_name)  # Rename the picture
               os.rmdir(folder_name)  # Remove the empty folder (clean up)
               messagebox.showinfo("Success", f"Profile picture of {username} downloaded as {new_file_name}!")  # Show success pop-up
           else:
               messagebox.showerror("Error", "Error downloading the profile picture.")  # Show error pop-up if picture is missing
       except Exception as e:
           messagebox.showerror("Error", f"Error downloading Instagram profile picture: {str(e)}")  # Show error if something went wrong
   else:
       messagebox.showwarning("Input Error", "Please enter a valid Instagram username.")  # Warn if the user didn’t type anything


# Function to download YouTube video
def download_youtube_video():
   url = entrybox1.get()  # Get the YouTube link from the box

   if url:  # Check if the box is not empty
       try:
           yt = pytube.YouTube(url)  # Get the YouTube video
           stream = yt.streams.get_highest_resolution()  # Choose the best quality
           stream.download()  # Download the video
           messagebox.showinfo("Success", "YouTube video downloaded successfully!")  # Show success pop-up
       except Exception as e:
           messagebox.showerror("Error", f"Error downloading YouTube video: {str(e)}")  # Show error pop-up if it fails
   else:
       messagebox.showwarning("Input Error", "Please enter a valid YouTube link.")  # Warn if the user didn’t type anything


# Function to update the screen when switching between Instagram and YouTube
def update_gui_for_selection():
   if option_var.get() == "Instagram":  # If "Instagram" is selected
       label1.config(text="Enter Instagram Username Below:")  # Change the label text
       action_button.config(text="Download Profile Picture", command=download_instagram_profile_pic)  # Change button action
   elif option_var.get() == "YouTube":  # If "YouTube" is selected
       label1.config(text="Enter YouTube Video URL Below:")  # Change the label text
       action_button.config(text="Download YouTube Video", command=download_youtube_video)  # Change button action


# Create the main window for GUI
root = tk.Tk()  # Make a new window
root.title("Download Media (Instagram or YouTube)")  # Give the window a title
root.geometry("400x200")  # Set the size of the window

# The following line is used to create a variable that will store the user's selection from the radio buttons.
#So option_var basically stores people's choice of what they selected
# #It helps Tkinter "track" the currently selected option.
# value = Instagram chooses a default value as Instagram
option_var = tk.StringVar(value="Instagram")  # Make a variable to store the selection. Value from below comes and saves in this option_var

# Create a radio button for Instagram
instagram_radio = tk.Radiobutton(root, text="Instagram", variable=option_var, value="Instagram", command=update_gui_for_selection)
instagram_radio.place(x=75, y=25)  # Put it on the screen

# Create a radio button for YouTube
youtube_radio = tk.Radiobutton(root, text="YouTube", variable=option_var, value="YouTube", command=update_gui_for_selection)
youtube_radio.place(x=210, y=25)


# Create a label (text) to tell the user what to enter
label1 = tk.Label(root, text="Enter Instagram Username Below:")
label1.place(x=120, y=60)

# Create an entry box where users can type their Instagram username or YouTube link
entrybox1 = tk.Entry(root, width=45)
entrybox1.place(x=90, y=90)

# Create a button to download the profile picture or video
action_button = tk.Button(root, text="Download Profile Picture", command=download_instagram_profile_pic)
action_button.place(x=120, y=125)

# Start the program (keep the window open)
root.mainloop()
