import tkinter as tk
from tkinter import messagebox
import json
import os

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

class DogCareApp:
    def __init__(self, root):
        # Save the main window in self.root so the whole class can use it
        self.root = root

        # Set the window title
        self.root.title("PawPal: Dog Care Simulator and Health Tracker")

        # Set the window size
        self.root.geometry("700x800")

        # This will store the dog's information later
        self.dog = None

        # This list stores messages about what happened in the game
        self.history = []

        # Show the first screen when the program starts
        self.show_profile_screen()

    def clear_screen(self):
        # Remove everything currently on the window
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_profile_screen(self):
        # Clear the window before drawing the profile screen
        self.clear_screen()

        # Title at the top of the screen
        title_label = tk.Label(self.root, text="Create Your Dog Profile", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)

        # Create a frame to hold the labels and entry boxes
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)

        # Labels for the input fields
        tk.Label(form_frame, text="Dog Name:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(form_frame, text="Breed:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(form_frame, text="Age:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(form_frame, text="Weight (lbs):", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
        tk.Label(form_frame, text="Size Category:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=10, sticky="e")

        # Entry box for the dog's name
        self.name_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Entry box for the breed
        self.breed_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.breed_entry.grid(row=1, column=1, padx=10, pady=10)

        # Entry box for the age
        self.age_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.age_entry.grid(row=2, column=1, padx=10, pady=10)

        # Entry box for the weight
        self.weight_entry = tk.Entry(form_frame, font=("Arial", 12))
        self.weight_entry.grid(row=3, column=1, padx=10, pady=10)

        # Dropdown menu for the dog size
        self.size_var = tk.StringVar(value="Small")
        size_menu = tk.OptionMenu(form_frame, self.size_var, "Small", "Medium", "Large")
        size_menu.grid(row=4, column=1, padx=10, pady=10, sticky="we")

        # Small help message so the user knows how to type age
        age_help_label = tk.Label(
            self.root,
            text="Age examples: 7 months, 2 years, 1.5",
            font=("Arial", 10)
        )
        age_help_label.pack()

        # Button to create the dog profile
        create_button = tk.Button(
            self.root,
            text="Create Dog",
            font=("Arial", 12, "bold"),
            command=self.create_dog
        )
        create_button.pack(pady=20)

        # Button to load a saved dog
        load_button = tk.Button(
            self.root,
            text="Load Saved Dog",
            font=("Arial", 11),
            command=self.load_dog
        )
        load_button.pack()

    def parse_age(self, age_text):
        # Make the text lowercase and remove extra spaces
        age_text = age_text.lower().strip()

        try:
            # If the user types just a number like 2 or 1.5, use it as years
            return float(age_text)
        except ValueError:
            # If it is not just a number, keep checking other formats
            pass

        if "month" in age_text:
            # If the user types something like "7 months", convert months into years
            number = float(age_text.split()[0])
            return number / 12

        if "year" in age_text:
            # If the user types something like "2 years", keep that number as years
            number = float(age_text.split()[0])
            return number

        # If the format does not match anything we expect, show an error
        raise ValueError("Invalid age format")

    def get_age_display(self):
        # If the dog is younger than one year, show months instead of decimals
        if self.dog["age"] < 1:
            months = round(self.dog["age"] * 12)
            return f"{months} months"

        # Otherwise show age in years
        return f"{self.dog['age']} years"

    def validate_dog_inputs(self, name, breed, age, weight):
        # This function checks if the user's inputs are realistic

        if len(name) < 2:
            messagebox.showerror("Input Error", "Dog name must be at least 2 characters long.")
            return False

        if len(breed) < 2:
            messagebox.showerror("Input Error", "Breed must be at least 2 characters long.")
            return False

        if age <= 0:
            messagebox.showerror("Input Error", "Age must be greater than 0.")
            return False

        if age > 25:
            messagebox.showerror("Input Error", "Please enter a realistic dog age (25 years or less).")
            return False

        if weight <= 0:
            messagebox.showerror("Input Error", "Weight must be greater than 0.")
            return False

        if weight > 250:
            messagebox.showerror("Input Error", "Please enter a realistic dog weight (250 lbs or less).")
            return False

        # If nothing is wrong, return True
        return True

    def create_dog(self):
        # Get the text the user typed into each box
        name = self.name_entry.get().strip()
        breed = self.breed_entry.get().strip()
        age_text = self.age_entry.get().strip()
        weight_text = self.weight_entry.get().strip()
        size = self.size_var.get()

        # Make sure no box is empty
        if not name or not breed or not age_text or not weight_text:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            # Convert age input into a number
            age = self.parse_age(age_text)

            # Convert weight input into a number
            weight = float(weight_text)
        except ValueError:
            # Show an error if the format is wrong
            messagebox.showerror(
                "Input Error",
                "Enter age like: 2, 1.5, 7 months, or 2 years. Weight must be a number."
            )
            return

        # Check if the values are realistic
        if not self.validate_dog_inputs(name, breed, age, weight):
            return

        # Create the dog dictionary with starting values
        self.dog = {
            "name": name,
            "breed": breed,
            "age": age,
            "weight": weight,
            "size": size,
            "hunger": 70,
            "happiness": 70,
            "energy": 70,
            "health": 80,
            "feed_count": 0,
            "walk_count": 0,
            "play_count": 0,
            "rest_count": 0,
            "vet_count": 0,
            "care_score": 50,
            "day": 1,
           "room_x": 250,
            "room_y": 110
        }

        # Start the history log
        self.history = [f"Created profile for {name}."]

        # Go to the main game screen
        self.show_main_screen()

    def get_human_age(self):
        # If no dog exists yet, return 0
        if not self.dog:
            return 0

        age = self.dog["age"]
        size = self.dog["size"]

        # Use a simple dog-to-human age estimate
        if age <= 2:
            human_age = age * 10.5
        else:
            if size == "Small":
                human_age = 21 + (age - 2) * 4
            elif size == "Medium":
                human_age = 21 + (age - 2) * 5
            else:
                human_age = 21 + (age - 2) * 6

        return round(human_age, 1)

    def get_life_stage(self):
        # Return a life stage based on age
        age = self.dog["age"]

        if age < 2:
            return "Puppy"
        elif age < 7:
            return "Adult"
        else:
            return "Senior"

    def get_dog_mood(self):
        # Decide the dog's mood using its health, energy, and happiness
        if self.dog["health"] < 40:
            return "Sick", "🤒🐶"
        elif self.dog["energy"] < 30:
            return "Tired", "😴🐶"
        elif self.dog["happiness"] > 85:
            return "Very Happy", "😄🐶"
        elif self.dog["happiness"] < 40:
            return "Sad", "🥺🐶"
        else:
            return "Content", "🐶"

    def update_health_status(self):
        # This function changes health based on how the dog is being treated

        if self.dog["feed_count"] > self.dog["walk_count"] + 2:
            self.dog["health"] -= 3
            self.history.append("Too much feeding without enough exercise lowered health.")

        if self.dog["energy"] < 20:
            self.dog["health"] -= 2
            self.history.append("Low energy lowered health.")

        if self.dog["happiness"] < 30:
            self.dog["health"] -= 2
            self.history.append("Low happiness lowered health.")

        if self.dog["walk_count"] >= 3 and self.dog["play_count"] >= 2:
            self.dog["health"] += 2
            self.history.append("Good activity improved health.")

        self.limit_stats()

    def limit_stats(self):
        # Keep the stats between 0 and 100
        for key in ["hunger", "happiness", "energy", "health"]:
            if self.dog[key] < 0:
                self.dog[key] = 0
            if self.dog[key] > 100:
                self.dog[key] = 100

    def move_dog_in_room(self, x, y):
        # Save the dog's position in the room
        self.dog["room_x"] = x
        self.dog["room_y"] = y

    def show_main_screen(self):
        # Clear the screen before drawing the main game screen
        self.clear_screen()

        # Show the dog's name at the top
        top_label = tk.Label(
            self.root,
            text=f"Taking Care of {self.dog['name']}",
            font=("Arial", 20, "bold")
        )
        top_label.pack(pady=10)

        # Get the dog's mood label and emoji
        mood_text, dog_character = self.get_dog_mood()

        # Show dog details
        info_text = (
            f"Breed: {self.dog['breed']}\n"
            f"Age: {self.get_age_display()}\n"
            f"Size: {self.dog['size']}\n"
            f"Human Age: {self.get_human_age()} years\n"
            f"Life Stage: {self.get_life_stage()}\n"
            f"Mood: {mood_text}"
            f"Day: {self.dog['day']}"
        )
        info_label = tk.Label(self.root, text=info_text, font=("Arial", 12), justify="left")
        info_label.pack(pady=5)


        # Show the current main stats
        stats_text = (
            f"Hunger: {self.dog['hunger']}\n"
            f"Happiness: {self.dog['happiness']}\n"
            f"Energy: {self.dog['energy']}\n"
            f"Health: {self.dog['health']}"
        )
        self.stats_label = tk.Label(self.root, text=stats_text, font=("Arial", 13, "bold"))
        self.stats_label.pack(pady=10)

        # Title for the visual room
        room_title = tk.Label(self.root, text="Dog Room", font=("Arial", 14, "bold"))
        room_title.pack()

        # Create a canvas to draw the room
        self.room_canvas = tk.Canvas(self.root, width=500, height=220, bg="lightblue")
        self.room_canvas.pack(pady=10)

        # Floor
        self.room_canvas.create_rectangle(0, 160, 500, 220, fill="tan", outline="tan")

        # Bed area
        self.room_canvas.create_rectangle(30, 130, 120, 180, fill="pink", outline="black")
        self.room_canvas.create_text(75, 155, text="Bed")

        # Food area
        self.room_canvas.create_oval(190, 150, 240, 180, fill="orange", outline="black")
        self.room_canvas.create_text(215, 135, text="Food")

        # Toy area
        self.room_canvas.create_oval(360, 145, 410, 185, fill="yellow", outline="black")
        self.room_canvas.create_text(385, 135, text="Toy")

        # Door area
        self.room_canvas.create_rectangle(450, 70, 490, 160, fill="brown", outline="black")
        self.room_canvas.create_text(470, 50, text="Door")

        # Vet area
        self.room_canvas.create_rectangle(255, 35, 330, 95, fill="lightgreen", outline="black")
        self.room_canvas.create_text(292, 25, text="Vet")

        # Draw the dog character at its saved position
        self.dog_canvas_item = self.room_canvas.create_text(
            self.dog["room_x"],
            self.dog["room_y"],
            text=dog_character,
            font=("Arial", 28)
        )

        # Create a frame for the action buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Buttons for the dog actions
        tk.Button(button_frame, text="Feed", width=12, command=self.feed_dog).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(button_frame, text="Walk", width=12, command=self.walk_dog).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(button_frame, text="Play", width=12, command=self.play_with_dog).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(button_frame, text="Rest", width=12, command=self.rest_dog).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(button_frame, text="Vet", width=12, command=self.vet_visit).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(button_frame, text="Health Summary", width=12, command=self.show_summary_screen).grid(row=1, column=2, padx=10, pady=10)
        tk.Button(button_frame, text="Save", width=12, command=self.save_dog).grid(row=2, column=1, padx=10, pady=10)

        # Title for the recent history log
        history_title = tk.Label(self.root, text="Recent Activity", font=("Arial", 14, "bold"))
        history_title.pack(pady=(10, 5))

        # Show the last 6 history messages
        history_text = "\n".join(self.history[-6:])
        self.history_label = tk.Label(self.root, text=history_text, font=("Arial", 11), justify="left")
        self.history_label.pack()

    def refresh_main_screen(self):
        # Update health logic, then redraw the main screen
        self.update_health_status()
        self.show_main_screen()

    def feed_dog(self):
        self.dog["day"] += 1
        # Feeding helps hunger and happiness
        self.dog["hunger"] += 15
        self.dog["happiness"] += 5
        self.dog["energy"] += 2
        self.dog["feed_count"] += 1


        self.history.append(f"You fed {self.dog['name']}.")
        self.move_dog_in_room(215, 120)
        self.limit_stats()
        self.refresh_main_screen()

    def walk_dog(self):
        self.dog["day"] += 1
        # Walking improves health and happiness, but uses energy
        self.dog["health"] += 8
        self.dog["happiness"] += 10
        self.dog["energy"] -= 12
        self.dog["hunger"] -= 5
        self.dog["walk_count"] += 1
        self.history.append(f"You walked {self.dog['name']}.")
        self.move_dog_in_room(460, 110)
        self.limit_stats()
        self.refresh_main_screen()

    def play_with_dog(self):
        self.dog["day"] += 1
        # Playing raises happiness, but uses energy and hunger
        self.dog["happiness"] += 15
        self.dog["energy"] -= 10
        self.dog["hunger"] -= 4
        self.dog["play_count"] += 1
        self.history.append(f"You played with {self.dog['name']}.")
        self.move_dog_in_room(385, 115)
        self.limit_stats()
        self.refresh_main_screen()

    def rest_dog(self):
        self.dog["day"] += 1
        # Resting gives the dog more energy
        self.dog["energy"] += 20
        self.dog["happiness"] -= 2
        self.dog["rest_count"] += 1
        self.history.append(f"{self.dog['name']} took a rest.")
        self.move_dog_in_room(75, 110)
        self.limit_stats()
        self.refresh_main_screen()

    def vet_visit(self):
        self.dog["day"] += 1
        # The vet helps if the dog's health is low
        if self.dog["health"] < 50:
            self.dog["health"] += 25
            self.dog["energy"] -= 10
            self.dog["happiness"] -= 5
            self.dog["vet_count"] += 1
            self.history.append(f"{self.dog['name']} visited the vet and feels better.")
        else:
            self.history.append("Your dog is healthy and does not need a vet visit.")

        self.move_dog_in_room(292, 105)
        self.limit_stats()
        self.refresh_main_screen()

    def get_weight_status(self):
        # Give a simple weight message based on dog size
        weight = self.dog["weight"]
        size = self.dog["size"]

        if size == "Small":
            if weight < 10:
                return "Underweight for a small dog"
            elif weight <= 25:
                return "Healthy range for a small dog"
            else:
                return "Overweight for a small dog"

        if size == "Medium":
            if weight < 25:
                return "Underweight for a medium dog"
            elif weight <= 55:
                return "Healthy range for a medium dog"
            else:
                return "Overweight for a medium dog"

        if weight < 50:
            return "Underweight for a large dog"
        elif weight <= 90:
            return "Healthy range for a large dog"
        else:
            return "Overweight for a large dog"

    def get_care_recommendation(self):
        # Give a recommendation based on the dog's current stats
        if self.dog["health"] < 40:
            return "Your dog needs better daily care. Try more walks, balanced feeding, rest, or a vet visit."
        elif self.dog["energy"] < 30:
            return "Your dog is tired. Let your dog rest before more activity."
        elif self.dog["happiness"] < 40:
            return "Your dog needs attention. Playing more can improve happiness."
        else:
            return "Your dog is doing well. Keep a good balance of food, play, walks, and rest."

    def get_activity_summary(self):
        # This function collects the action totals and finds the action used the most

        actions = {
            "Feed": self.dog["feed_count"],
            "Walk": self.dog["walk_count"],
            "Play": self.dog["play_count"],
            "Rest": self.dog["rest_count"],
            "Vet": self.dog["vet_count"]
        }

        total_actions = sum(actions.values())

        if total_actions == 0:
            most_used_action = "No actions yet"
        else:
            most_used_action = max(actions, key=actions.get)

        return actions, total_actions, most_used_action

    def update_care_score(self):
        # This function calculates how well the user is caring for the dog

        score = 50

        if self.dog["health"] >= 80:
            score += 20
        elif self.dog["health"] >= 60:
            score += 10
        elif self.dog["health"] < 40:
            score -= 15

        if self.dog["happiness"] >= 80:
            score += 15
        elif self.dog["happiness"] < 40:
            score -= 10

        if self.dog["energy"] >= 50:
            score += 10
        elif self.dog["energy"] < 20:
            score -= 10

        if self.dog["vet_count"] >= 3:
            score -= 5

        if score < 0:
            score = 0
        if score > 100:
            score = 100

        self.dog["care_score"] = score

    def get_owner_rank(self):
        # This function gives the user a title based on the care score

        score = self.dog["care_score"]

        if score >= 85:
            return "Expert Dog Parent"
        elif score >= 65:
            return "Caring Owner"
        elif score >= 45:
            return "Learning Owner"
        else:
            return "Beginner Owner"

    def show_summary_screen(self):
        # Clear the screen before showing the summary
        self.clear_screen()

        # Update care score before showing it
        self.update_care_score()

        # Get the analytics information
        actions, total_actions, most_used_action = self.get_activity_summary()

        title_label = tk.Label(self.root, text="Dog Health Summary", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)

        summary_text = (
            f"Name: {self.dog['name']}\n"
            f"Breed: {self.dog['breed']}\n"
            f"Age: {self.get_age_display()}\n"
            f"Human Age Equivalent: {self.get_human_age()}\n"
            f"Life Stage: {self.get_life_stage()}\n"
            f"Weight Status: {self.get_weight_status()}\n"
            f"Health Score: {self.dog['health']}\n"
            f"Care Score: {self.dog['care_score']}\n"
            f"Owner Rank: {self.get_owner_rank()}\n\n"
            f"Activity Analytics:\n"
            f"Feed Count: {actions['Feed']}\n"
            f"Walk Count: {actions['Walk']}\n"
            f"Play Count: {actions['Play']}\n"
            f"Rest Count: {actions['Rest']}\n"
            f"Vet Visits: {actions['Vet']}\n"
            f"Total Actions: {total_actions}\n"
            f"Most Used Action: {most_used_action}\n\n"
            f"Recommendation:\n{self.get_care_recommendation()}"
        )

        summary_label = tk.Label(self.root, text=summary_text, font=("Arial", 13), justify="left")
        summary_label.pack(pady=20)

        back_button = tk.Button(
            self.root,
            text="Back to Main Screen",
            font=("Arial", 12),
            command=self.show_main_screen
        )
        back_button.pack(pady=10)
    def get_sheets_service(self):
        # This function connects the program to Google Sheets
        # using the service account JSON file.

        scopes = ["https://www.googleapis.com/auth/spreadsheets"]

        credentials = Credentials.from_service_account_file(
            "pawpal-494021-e14aeb559ac9",
            scopes=scopes
        )

        service = build("sheets", "v4", credentials=credentials)
        return service

    def save_to_google_sheet(self):
        # This function sends the dog's data to a Google Sheet.

        # Replace this with your real spreadsheet ID
        spreadsheet_id = "1HFPCkUz8BqrhwQxuPCjdXZBiH2VYo4YzXrUlCxfzLgY"

        # This is the tab name and range in the sheet
        range_name = "DogData!A:P"

        # Put the dog's information into one row
        values = [[
            self.dog["name"],
            self.dog["breed"],
            self.dog["age"],
            self.dog["weight"],
            self.dog["size"],
            self.dog["health"],
            self.dog["happiness"],
            self.dog["energy"],
            self.dog["day"],
            self.dog["care_score"],
            self.dog["feed_count"],
            self.dog["walk_count"],
            self.dog["play_count"],
            self.dog["rest_count"],
            self.dog["vet_count"],
            self.get_owner_rank()
        ]]

        body = {
            "values": values
        }

        service = self.get_sheets_service()

        service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="RAW",
            insertDataOption="INSERT_ROWS",
            body=body
        ).execute()

    def save_dog(self):
        # Save the dog's information and history to a JSON file
        save_data = {
            "dog": self.dog,
            "history": self.history
        }

        with open("dog_save.json", "w") as file:
            json.dump(save_data, file, indent=4)

        messagebox.showinfo("Saved", "Your dog data has been saved successfully.")

    def load_dog(self):
        # Make sure the save file exists before loading it
        if not os.path.exists("dog_save.json"):
            messagebox.showerror("Load Error", "No saved dog file was found.")
            return
        if "day" not in self.dog:
            self.dog["day"] = 1

        # Read the saved JSON file
        with open("dog_save.json", "r") as file:
            save_data = json.load(file)

        self.dog = save_data["dog"]
        self.history = save_data["history"]
        self.history.append(f"Loaded saved profile for {self.dog['name']}.")

        # Add missing values for older save files
        if "feed_count" not in self.dog:
            self.dog["feed_count"] = 0
        if "walk_count" not in self.dog:
            self.dog["walk_count"] = 0
        if "play_count" not in self.dog:
            self.dog["play_count"] = 0
        if "rest_count" not in self.dog:
            self.dog["rest_count"] = 0
        if "vet_count" not in self.dog:
            self.dog["vet_count"] = 0
        if "care_score" not in self.dog:
            self.dog["care_score"] = 50
        if "room_x" not in self.dog:
            self.dog["room_x"] = 250
        if "room_y" not in self.dog:
            self.dog["room_y"] = 110

        self.show_main_screen()


root = tk.Tk()
app = DogCareApp(root)
root.mainloop()