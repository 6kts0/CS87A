"""
Python is a dynamically typed, object oriented programming language.
Faba Kouyate, Fall 2025
"""
import random
from time import sleep

def guessing_game():

    # Set a random value to be guessed
    # Take players name
    rnge_value = random.randint(1, 101)
    player_1 = input("Enter Player 1 name: ")

    """
    Initialized guess variable to zero so python doesnt get confused before starting the while loop, not sure if this can be optimized, but if it aint broke dont fix it right?
    """
    user_guess = 0

    # Introduce the user to the game
    print("Time to test your guessing skills") ; sleep(1.5)   
    print(f"Good luck {player_1}, you'll need it!") ; sleep(1.5) 
    print("-+" * 30) ; sleep(1)



# Start while loop
    while user_guess != rnge_value:
        # Get input value 
        user_guess = input("\nPick a number (1 - 100): ")
        
        try:
            # Convert input to integer within while loop
            guess_int = int(user_guess)
            # When a guess is correct this code is returned
            if guess_int == rnge_value:
                print("Nice! you got it correct!")
                break # 'Break' acts similar to 'return' but only ends the while or for loop its inside of 
            # When a guess is greater than the guess value this code is returned
            elif guess_int > rnge_value:
                print("Try again... Your guess was too high.")
            # When a guess is neither correct nor greater than the guess value this code is returned
            else:
                print("Try again... Your guess was too low.")
        except ValueError:
            # If an error is called because the datatype of the input this code will execute
            print("That is not a valid entry, try again.")

# Run the function to start game
guessing_game()
            