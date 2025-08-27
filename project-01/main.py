''' Snake beats Water (snake drinks water),
    Water beats Gun (gun sinks in water),
   and Gun beats Snake (gun shoots snake). 
'''
# Snake, Water, and Gun game
import random

def play_game():
    """Plays a game of Snake, Water, Gun against the computer."""
    choices = ["Snake", "Water", "Gun"]
    user_choice = input("Enter your choice (snake, water, gun): ").capitalize()

    # Validate user input
    if user_choice not in choices:
        print("Invalid choice.")
        return  # Exit the function if the choice is invalid

    computer_choice = random.choice(choices)
    print(f"Computer choice: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Snake" and computer_choice == "Water") or \
         (user_choice == "Water" and computer_choice == "Gun") or \
         (user_choice == "Gun" and computer_choice == "Snake"):
        print("You win!")
    else:
        print("You lose!")

# Start the game
play_game()
