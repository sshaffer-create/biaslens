import gspread  # Imports the gspread library so Python can interact with Google Sheets

from oauth2client.service_account import ServiceAccountCredentials
# Imports the authentication class used to log in with a service account JSON key


SCOPE = [
    "https://spreadsheets.google.com/feeds",
    # Permission to read and write data in Google Sheets

    "https://www.googleapis.com/auth/drive"
    # Permission to access files in Google Drive (needed to open the sheet)
]

CREDS = ServiceAccountCredentials.from_json_keyfile_name("keys.json", SCOPE)
# Loads your service account credentials from the JSON file and applies the required permissions

client = gspread.authorize(CREDS)
# Uses the credentials to log in and create a client connection to Google APIs

sheet = client.open("BUS472")
# Opens the Google Spreadsheet named "BUS472" (must match the exact sheet name)

worksheet = sheet.sheet1
# Selects the first worksheet (tab) inside the spreadsheet so you can read/write data

#following lines are optional.
# __name__ is a built-in variable that tells how this file is being used
# "__main__" means this file is being run directly (not imported)
# So this condition means: only run the code below if this is the main file being executed
# In simple terms: "If I am the main program, then do this (e.g., print output)"
if __name__ == "__main__":
    print("Accessible Spreadsheets..BUS472.")
