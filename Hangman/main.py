import os
import random
import word_list 
import stages, logo2, logo3

# Function to clear the screen (works on most systems)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Print logo and instructions
print(logo3)
print("\nTo win, guess the word before the person is hung.\n")

# Create blanks for the word
display = []
for _ in range(word_length):
    display += "_"

# Track incorrect guesses
wrong_guesses = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    # Check if the letter has been guessed before
    if guess in display or guess in wrong_guesses:
        print(f"{' '.join(display)}")
        print(stages[lives])
        print(f"You've already guessed the letter '{guess}', pick another one.")
    else:
        # If the guess is in the chosen word
        if guess in chosen_word:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
        else:
            # If the guess is incorrect
            wrong_guesses.append(guess)
            lives -= 1
            print(f"'{guess}' is not in the word, you lost 1 life.")

        # Print current state of the word
        print(f"{' '.join(display)}")

        # Check if the game is won
        if "_" not in display:
            end_of_game = True
            print("\nGenius, genius, genius! You won!")
            print(logo2)

        # Check if the game is lost
        if lives == 0:
            end_of_game = True
            print("The man has been hung, you lose.")
            print(f"\nThe word was '{chosen_word}'")

        # Display current stage of the hangman
        if not end_of_game:
            print(stages[lives])
