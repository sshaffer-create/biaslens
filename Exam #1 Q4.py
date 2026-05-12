from tkinter import *  # Import everything from the Tkinter library. no need to install this library
root = Tk()  # Create the main application window (root window)
root.title("Grade Checker App")  # Set the window title
root.geometry("400x400")  # Set window size as a string "widthxheight"
#root.resizeable(0,0) or root.resizable(width=False, height=False) to not allow people to expand GUI window

def check_grade():
    grade= float(entry.get())
    if grade >= 90:
        result_label.config(text="You got an A")
    else:
        result_label.config(text="You got an B or less")

label = Label(root, text="Enter your numeric grade: ")
label.grid(row=0, column=0)

entry = Entry(root, bd=5, bg="white", fg="black")
entry.grid(row=0, column=1, padx=10, pady=10)

button = Button(root, text="Submit", command=check_grade)
button.grid(row=1, column=2, padx=10, pady=10)

result_label = Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

























print(root)  # Print the reference of the Tkinter window object in the console
root.mainloop()  # Use root.mainloop() instead of mainloop()




