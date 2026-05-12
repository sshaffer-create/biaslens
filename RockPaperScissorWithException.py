#Creating a simple Rock, Paper, and Scissor Game with Error Handling (Exception) option
# #with ANOTHER opportunity if user inputs non-existing words (without GUI)


#The code above doesn't give the user another chance if they input an invalid choice such as ABC or Rocker
# To fix that, we need to move the input() prompt inside the while loop, so it keeps asking the user until a valid input is provided. That’s what we do in this code below.

import random  # Imports the random module to allow the computer to make random choices.
# Defines the game logic function
def game():
   possible_action = ['rock', 'paper', 'scissors']  # List of valid choices

   while True:  # Start a loop that keeps asking for input until it's valid
       # Prompts the user to input their choice (either rock, paper, or scissors)
       user_action = input('Enter a choice of rock, paper, or scissors: ').lower()

       try:
 #The try block in your code above is used for error handling. It attempts to execute the code inside it,
# and if any error (exception) occurs, the except block catches it and displays an error message instead of crashing the program.

           # Checks if the user's input is valid
           if user_action not in possible_action:
               raise ValueError  # If invalid input, raises a ValueError to go to the except block
           break  # If input is valid, exit the loop
       except ValueError:
           print("You must enter rock, paper, or scissors.")  # Informs the user that their input is invalid

   # The computer randomly selects one of the possible actions
   computer_action = random.choice(possible_action)

   # Prints both the user's and the computer's choices
   print('You chose ' + user_action + '. Computer chose ' + computer_action + '.')

   # Compares the user's action with the computer's action to determine the result
   if user_action == computer_action:
       print(f'Both players selected {user_action}. It is a tie.')
   elif user_action == 'rock':
       if computer_action == 'scissors':
           print('Rock smashes scissors. You win.')
       else:
           print('Paper covers rock. You lose.')
   elif user_action == 'scissors':
       if computer_action == 'paper':
           print('Scissors cuts the paper. You win.')
       else:
           print('Rock smashes scissors. You lose.')
   elif user_action == 'paper':
       if computer_action == 'rock':
           print('Paper covers the rock. You win.')
       else:
           print('Scissors cut paper. You lose.')
# Start the game
game()
