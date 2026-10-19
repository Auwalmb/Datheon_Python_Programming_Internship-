# ==================================================
# PROJECT: Hangman Word Guessing Game
# INTERNSHIP: Datheon Python Programming Internship
# DEVELOPER: Auwal Mohammed Bello
# LANGUAGE: Python
# ==================================================

import random

WORDS = [
    "python",
    "cybersecurity",
    "computer",
    "network",
    "programming",
    "security",
    "internet"
]

HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def play_game():
    word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_letters = set()
    max_attempts = 6

    print("\n" + "=" * 35)
    print("       HANGMAN WORD GAME")
    print("=" * 35)
    print("Guess the hidden word one letter at a time.")

    while len(incorrect_letters) < max_attempts:
        print(HANGMAN_STAGES[len(incorrect_letters)])

        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in word
        )

        print("Word:", display_word)
        print("Incorrect guesses:", sorted(incorrect_letters))
        print(
            "Attempts remaining:",
            max_attempts - len(incorrect_letters)
        )

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

        guess = input("\nEnter one letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one alphabetic letter.")
            continue

        if guess in guessed_letters or guess in incorrect_letters:
            print("You already guessed that letter. Try another.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            incorrect_letters.add(guess)
            print("Wrong guess!")

    print(HANGMAN_STAGES[max_attempts])
    print("\nGame over! The word was:", word)


def main():
    while True:
        play_game()

        again = input(
            "\nWould you like to play again? (yes/no): "
        ).lower().strip()

        if again not in ("yes", "y"):
            print("Thank you for playing Hangman. Goodbye!")
            break


if __name__ == "__main__":
    main()
