import tkinter as tk   # Imports Tkinter library to create GUI applications

# Create main window
root = tk.Tk()   # Creates the main application window
root.title("Dog Age Calculator")   # Sets the title of the window
root.geometry("400x400")   # Sets the size of the window (width x height)
###^^^ My code
# Function to parse age input (handles "7 months", "2 years", etc.)
def parse_age(age_text):
    age_text = age_text.lower()   # Converts input to lowercase so "Months" and "months" both work

    number = ""   # Empty string to store numbers found in the input

    for char in age_text:   # Loop through each character in the input text
        if char.isdigit() or char == ".":   # Check if character is a number or decimal point
            number += char   # Add valid characters to the number string
### ^^^ source from Geeks for Geeks
    if number == "":
        return None   # If no number is found, return None (invalid input)

    age = float(number)   # Convert extracted number into a decimal (float)
### My code below
    if "month" in age_text:   # Check if user typed "month" or "months"
        age = age / 12   # Convert months into years

    return age   # Return the final age in years
### My source

# Function to calculate dog age and display result
def calculate_age():
    name = name_entry.get()   # Gets text entered in name input box
    age_text = age_entry.get()   # Gets raw text entered for age
    age = parse_age(age_text)   # Calls parse_age function to convert input into number
    size = size_var.get()   # Gets selected value from dropdown menu

    if not name or age is None:   # Check if name is empty or age is invalid
        result_label.config(text="Please enter valid information.")   # Show error message
        return   # Stop the function

    # Calculate human age based on dog size
    if size == "Small":
        human_age = age * 6   # Small dogs age slower
    elif size == "Medium":
        human_age = age * 7   # Medium dogs use standard
    else:
        human_age = age * 8   # Large dogs age faster
### My codes from class and myself
    # Determine life stage and care tip
    if age < 2:
        stage = "Puppy"   # Young dogs
        tip = "Focus on training and nutrition."
    elif age < 6:
        stage = "Young Adult"
        tip = "Keep up exercise and playtime."
    elif age < 10:
        stage = "Adult"
        tip = "Regular vet checkups are important."
    else:
        stage = "Senior"
        tip = "Provide comfort and monitor health closely."
    ### My codes from class and myself
    # Display results
    result_label.config(
        text=f"{name} is about {human_age:.1f} human years old.\nLife stage: {stage}\nTip: {tip}"
    )
    # .config updates the label text; f-string inserts variables into the message


# Function to clear all inputs and results
def clear_fields():
    name_entry.delete(0, tk.END)   # Removes text from name input box
    age_entry.delete(0, tk.END)   # Removes text from age input box
    result_label.config(text="")   # Clears the result label


# Title label
title_label = tk.Label(root, text="Dog Age & Care Calculator", font=("Arial", 16))
# Creates a label with larger font for the app title
title_label.pack(pady=10)   # Displays it with vertical spacing

# Dog name label and input
name_label = tk.Label(root, text="Dog Name:")   # Label asking for dog name
name_label.pack()
name_entry = tk.Entry(root)   # Input box for name
name_entry.pack()

# Dog age label and input
age_label = tk.Label(root, text="Dog Age:")   # Label asking for age
age_label.pack()
age_entry = tk.Entry(root)   # Input box for age
age_entry.pack()

# Dog size label and check mark
size_label = tk.Label(root, text="Dog Size:")
# Creates a label to tell the user what the options are
size_label.pack()

# Variable to store selected size
size_var = tk.StringVar()
# StringVar is used to store the selected value from radio buttons

size_var.set("Medium")
# Sets the default selected option to "Medium"

# Radio button for Small
small_radio = tk.Radiobutton(root, text="Small", variable=size_var, value="Small")
# Creates a radio button labeled "Small"
# variable=size_var connects it to the shared variable
# value="Small" is what gets stored when selected
small_radio.pack()

# Radio button for Medium
medium_radio = tk.Radiobutton(root, text="Medium", variable=size_var, value="Medium")
# Another option that shares the same variable
medium_radio.pack()

# Radio button for Large dog
large_radio = tk.Radiobutton(root, text="Large", variable=size_var, value="Large")
# Third option
large_radio.pack()
####^^ Above is source code
# Result label
result_label = tk.Label(root, text="", wraplength=300)
# Label where output will be shown; wraplength keeps text inside window
result_label.pack(pady=10)

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate_age)
# Button that runs calculate_age function when clicked
calc_button.pack(pady=5)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_fields)
# Button that clears all inputs and results
clear_button.pack()

# Run the app
root.mainloop()   # Keeps the window open and running