import random

def rock_paper_scissors():
    # List of options for the game
    choices = ["rock", "paper", "scissors"]
    
    # Welcome message
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        # Get user's choice
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # Check if the user input is valid
        if user_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Get computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Run the game
rock_paper_scissors()
