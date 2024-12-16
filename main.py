import random
import os
from country_list import get_countries

# ASCII Art for Hangman stages
HANGMAN_ART = [
    """
      +---+
          |
          |
          |
         ===
    """,
    """
      +---+
      O   |
          |
          |
         ===
    """,
    """
      +---+
      O   |
      |   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\ |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\ |
     /    |
         ===
    """,
    """
      +---+
      O   |
     /|\\ |
     / \\ |
         ===
    """
]

def display_word(word, guessed_letters):
    """Display the current state of the word with guessed letters."""
    return ' '.join([letter if letter.lower() in guessed_letters else '_' for letter in word])

def display_ascii_art(lives):
    """Display the ASCII art for the current number of lives."""
    return HANGMAN_ART[len(HANGMAN_ART) - lives - 1]

def play_game(word, max_lives):
    """Main function to play the game."""
    guessed_letters = set()
    wrong_guesses = set()
    lives = max_lives

    print("Welcome to Hangman!")
    print(display_ascii_art(lives))
    print(display_word(word, guessed_letters))

    while lives > 0:
        guess = input("\nGuess a letter (or type 'quit' to exit): ").lower()
        if guess == 'quit':
            print("Goodbye!")
            break

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        if guess in word.lower():
            guessed_letters.add(guess)
            print(f"Correct! '{guess}' is in the word.")
        else:
            wrong_guesses.add(guess)
            lives -= 1
            print(f"Wrong! '{guess}' is not in the word. Lives left: {lives}")

        print(display_ascii_art(lives))
        print(display_word(word, guessed_letters))
        print(f"Wrong guesses: {', '.join(sorted(wrong_guesses))}")

        if all(letter.lower() in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was: {word}")

def main():
    """Main menu and difficulty selection."""
    words = get_countries()
    print("Choose a difficulty level:")
    print("1. Easy (7 lives)")
    print("2. Medium (5 lives)")
    print("3. Hard (3 lives)")

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                max_lives = 7
                break
            elif choice == 2:
                max_lives = 5
                break
            elif choice == 3:
                max_lives = 3
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

    word = random.choice(words)
    play_game(word, max_lives)

if __name__ == "__main__":
    main()