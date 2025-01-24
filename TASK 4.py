import random

# Function to display the instructions
def display_instructions():
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose one of the following:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("The rules are:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock\n")

# Function to get user's choice
def get_user_choice():
    while True:
        try:
            user_input = int(input("Enter your choice (1: Rock, 2: Paper, 3: Scissors): "))
            if user_input in [1, 2, 3]:
                return user_input
            else:
                print("Invalid input! Please choose 1 for Rock, 2 for Paper, or 3 for Scissors.")
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice([1, 2, 3])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        return "User"
    else:
        return "Computer"

# Function to display choices
def display_choices(user_choice, computer_choice):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"Your choice: {choices[user_choice]}")
    print(f"Computer's choice: {choices[computer_choice]}")

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0
    play_again = True

    while play_again:
        display_instructions()

        # Get user and computer choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Display choices
        display_choices(user_choice, computer_choice)

        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)

        if winner == "Tie":
            print("It's a tie!")
        elif winner == "User":
            user_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")

        # Display scores
        print(f"Score: You - {user_score}, Computer - {computer_score}\n")

        # Ask if the user wants to play again
        play_again_input = input("Do you want to play again? (y/n): ").lower()
        if play_again_input != 'y':
            play_again = False
            print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
