import random

def hangman():
    # List of words for the game
    word_list = ["python", "hangman", "developer", "programming"]
    
    # Choose a random word
    word_to_guess = random.choice(word_list)
    word_display = "_" * len(word_to_guess)
    attempts = 6

    print("Welcome to Hangman!")
    print(f"Guess the word: {word_display}")

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        # Check if the guess is valid (single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        # Check if the letter is in the word
        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
            word_display = ''.join([guess if word_to_guess[i] == guess else word_display[i] for i in range(len(word_to_guess))])
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print(f"Current word: {word_display}")

        # Check if the player has guessed the word
        if word_display == word_to_guess:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"Sorry, you lost! The word was '{word_to_guess}'.")

# Run the game
hangman()
