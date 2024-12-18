import random

def guess_the_number():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100

    # Generate a random number within the range
    number_to_guess = random.randint(lower_bound, upper_bound)

    # Set the initial number of attempts
    attempts = 0

    print(f"Welcome to Guess the Number Game!")
    print(f"Guess the number between {lower_bound} and {upper_bound}.")

    # Loop until the user guesses the number correctly
    while True:
        try:
            # Prompt user to input their guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1  # Increment the attempt counter

            # Check if the guess is correct
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break  # End the game when the guess is correct

        except ValueError:
            # Handle the case where the user doesn't enter a valid number
            print("Please enter a valid integer.")

# Run the game
guess_the_number()



