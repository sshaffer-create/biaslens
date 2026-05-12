#Code 7: Same as Code 6 but validating dates (so people don’t put anything in year, date, day).
#Also, have two labels one for correct output and other for error output.
from tkinter import *  # Imports all classes and functions from tkinter (Tk, Label, Entry, Button, StringVar, etc.) for GUI creation
import datetime  # Imports datetime module to work with dates and times (datetime class, now(), etc.)

# Create the main application window and set its title and size
root = Tk()  # Tk() creates the main root window that holds all GUI widgets
root.title("Age Calculator")  # title() sets the window title shown in the title bar
root.geometry("400x250")  # geometry() sets window size in width x height format (400px by 250px)

# Create Tkinter StringVar objects to store user input from Entry widgets
NameVariable = StringVar()  # StringVar() creates a Tkinter-managed string variable linked to input fields
YearVariable = StringVar()  # Stores year input as a dynamic string variable
MonthVariable = StringVar()  # Stores month input as a dynamic string variable
DayVariable = StringVar()  # Stores day input as a dynamic string variable

# Create a label that will display the calculated age result
output_label = Label(root, text="")  # Label() creates a text display widget inside root; text="" initializes it empty
output_label.grid(row=6, column=1, columnspan=2)  # grid() places widget in row 6, column 1; columnspan=2 makes it span two columns

# Create a label that will display validation error messages in red
error_label = Label(root, text="", fg="red")  # fg="red" sets foreground (text) color to red
error_label.grid(row=7, column=1, columnspan=2)  # Positions error label at row 7, spanning two columns


# Define a function that validates input, calculates age, and updates the GUI
def calculateage():  # Defines function calculateage() executed when button is clicked

    # Clear any previous result or error message before running new validation
    error_label.config(text="")  # config() updates widget properties; clears error message
    output_label.config(text="")  # Clears previous output result

    # If any date field is empty, show an error and stop the function
    if (YearVariable.get().strip() == "" or  # get() retrieves value from StringVar; strip() removes spaces; checks if empty
        MonthVariable.get().strip() == "" or
        DayVariable.get().strip() == ""):
        error_label.config(text="Please fill all date fields")  # Displays validation message
        return  # return stops function execution immediately

    # If any date field contains non-numeric characters, show an error and stop
    if (not YearVariable.get().strip().isdigit() or  # isdigit() checks if string contains only digits; not reverses result
        not MonthVariable.get().strip().isdigit() or
        not DayVariable.get().strip().isdigit()):
        error_label.config(text="Year, Month and Day must be numeric")  # Displays numeric validation error
        return

    # Convert the validated string inputs into integer values
    year = int(YearVariable.get().strip())  # int() converts string to integer
    month = int(MonthVariable.get().strip())  # Converts month string to integer
    day = int(DayVariable.get().strip())  # Converts day string to integer

    # If month is outside the valid range 1–12, show an error and stop
    if month < 1 or month > 12:  # Checks numeric range for valid month
        error_label.config(text="Month must be between 1 and 12")
        return

    # If day is outside the valid range 1–31, show an error and stop
    if day < 1 or day > 31:  # Checks numeric range for valid day
        error_label.config(text="Day must be between 1 and 31")
        return

    # Attempt to create a datetime object and catch invalid calendar dates
    try:
        birthdate = datetime.datetime(year, month, day)  # datetime.datetime() creates date object; raises ValueError if invalid date
    except ValueError:  # Catches invalid calendar dates like Feb 30
        error_label.config(text="Invalid calendar date")
        return

    # Calculate the difference in days between today and the birthdate
    today = datetime.datetime.now()  # now() returns current date and time as datetime object
    age_days = (today - birthdate).days  # Subtracting datetime objects gives timedelta; .days extracts total days

    # Convert total days into approximate years
    age_years = round(age_days / 365, 2)  # Divides days by 365; round(value, 2) rounds to 2 decimal places

    # Display the calculated age inside the output label
    output_label.config(text=f"{NameVariable.get()} your age is {age_years} years")  # f-string inserts name and age; config() updates label text


# Create static text labels for the input fields
Label(root, text="Your Name").grid(row=1, column=1, padx=90)  # padx adds horizontal padding space
Label(root, text="Year").grid(row=2, column=1, padx=90)
Label(root, text="Month").grid(row=3, column=1, padx=90)
Label(root, text="Day").grid(row=4, column=1, padx=90)

# Create Entry widgets linked to their respective StringVar variables
Entry(root, textvariable=NameVariable).grid(row=1, column=2)  # Entry() creates input box; textvariable links it to StringVar
Entry(root, textvariable=YearVariable).grid(row=2, column=2)
Entry(root, textvariable=MonthVariable).grid(row=3, column=2)
Entry(root, textvariable=DayVariable).grid(row=4, column=2)

# Create a button that runs calculateage() when clicked
Button(root, text="Submit", command=calculateage).grid(row=5, column=1)  # command attaches function reference (no parentheses)

# Start the Tkinter event loop to keep the window running
root.mainloop()  # mainloop() starts event loop and keeps window responsive to user actions