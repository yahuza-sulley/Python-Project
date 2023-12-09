import random

def choose_word():
    words = ["python", "hangman", "programming", "code", "challenge", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    incorrect_guesses = 0
    guessed_letters = []
    word_to_guess = choose_word()

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while incorrect_guesses < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            incorrect_guesses += 1
            print(f"Incorrect guesses: {incorrect_guesses}/{max_attempts}")

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You guessed the word!")
            break

    if "_" in current_display:
        print(f"Sorry, you ran out of attempts. The word was {word_to_guess}.")

if __name__ == "__main__":
    hangman()
