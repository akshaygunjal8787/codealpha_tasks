import random

# Step 1: Predefined list of words
words = ["python", "computer", "science", "hangman", "program"]

# Step 2: Randomly choose a word
chosen_word = random.choice(words)
word_length = len(chosen_word)

# Step 3: Create a list of underscores for the hidden word
display = ["_"] * word_length

# Step 4: Initialize variables
attempts = 6
guessed_letters = []

print("Welcome to the Hangman Game!")
print("Guess the word one letter at a time.")
print(f"The word has {word_length} letters.\n")
print(" ".join(display))

# Step 5: Main game loop
while attempts > 0 and "_" in display:
    guess = input("\nEnter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter is already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in chosen_word:
        print("Good job! That letter is in the word.")
        # Reveal correct letters in display
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")

    # Show current progress
    print("\nWord:", " ".join(display))
    print("Guessed letters:", ", ".join(guessed_letters))

# Step 6: End of game messages
if "_" not in display:
    print("\n Congratulations! You guessed the word:", chosen_word)
else:
    print("\n Game Over! The word was:", chosen_word)
