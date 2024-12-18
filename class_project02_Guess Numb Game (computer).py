import random

def guess_the_number():
    # Step 1: Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 5)
    
    # Step 2: Give instructions to the user
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 5. Try to guess it")
    
    # Step 3: Keep track of attempts
    attempts = 0
    
    while True:
        # Step 4: Ask the user to guess
        guess = int(input("Enter your guess"))
        attempts += 1
        
        # Step 5: Provide feedback based on the guess
        if guess < number_to_guess:
            print("Too low! Try again")
        elif guess > number_to_guess:
            print("Too high! Try again")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break  # Exit the loop when the guess is correct

# Call the function to start the game
guess_the_number()

