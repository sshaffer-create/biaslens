from tkinter import *
import datetime

# ===================== NEW ADDED SECTION =====================
from google_auth import worksheet
# THIS is NEW added section
# Imports the Google Sheet connection (worksheet) from google_auth.py that you created above
# ===========================================================


root = Tk()
root.title("Age Calculator")
root.geometry("400x250")

NameVariable = StringVar()
YearVariable = StringVar()
MonthVariable = StringVar()
DayVariable = StringVar()

output_label = Label(root, text="")
output_label.grid(row=6, column=1, columnspan=2)

error_label = Label(root, text="", fg="red")

error_label.grid(row=7, column=1, columnspan=2)


def calculateage():

    error_label.config(text="")
    output_label.config(text="")

    if (YearVariable.get().strip() == "" or
        MonthVariable.get().strip() == "" or
        DayVariable.get().strip() == ""):
        error_label.config(text="Please fill all date fields")
        return

    if (not YearVariable.get().strip().isdigit() or
        not MonthVariable.get().strip().isdigit() or
        not DayVariable.get().strip().isdigit()):
        error_label.config(text="Year, Month and Day must be numeric")
        return

    name = NameVariable.get().strip()
    year = int(YearVariable.get().strip())
    month = int(MonthVariable.get().strip())
    day = int(DayVariable.get().strip())

    if month < 1 or month > 12:
        error_label.config(text="Month must be between 1 and 12")
        return

    if day < 1 or day > 31:
        error_label.config(text="Day must be between 1 and 31")
        return

    try:
        birthdate = datetime.datetime(year, month, day)
    except ValueError:
        error_label.config(text="Invalid calendar date")
        return

    today = datetime.datetime.now()
    age_days = (today - birthdate).days
    age_years = round(age_days / 365, 2)

    output_label.config(text=f"{name} your age is {age_years} years")


    # ===================== NEW ADDED SECTION =====================
    try:
        worksheet.append_row([
            name,
            year,
            month,
            day,
            age_years,
            today.strftime("%Y-%m-%d %H:%M:%S")
        ])
        # THIS is NEW added section
        # Saves user input + calculated age into Google Sheet as a new row

    except Exception as e:
        error_label.config(text=f"Could not save to Google Sheet: {e}")
        # THIS is NEW added section
        # Shows error if Google Sheet saving fails
    # ===========================================================


Label(root, text="Your Name").grid(row=1, column=1, padx=90)
Label(root, text="Year").grid(row=2, column=1, padx=90)
Label(root, text="Month").grid(row=3, column=1, padx=90)
Label(root, text="Day").grid(row=4, column=1, padx=90)

Entry(root, textvariable=NameVariable).grid(row=1, column=2)
Entry(root, textvariable=YearVariable).grid(row=2, column=2)
Entry(root, textvariable=MonthVariable).grid(row=3, column=2)
Entry(root, textvariable=DayVariable).grid(row=4, column=2)

Button(root, text="Submit", command=calculateage).grid(row=5, column=1)

root.mainloop()




