
import random

words = ["python", "apple", "computer", "tiger", "coding"]
word = random.choice(words)

guessed_letters = []
attempts = 6

print(" Welcome to Hangman!")
print("_ " * len(word))

while attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    if all(letter in guessed_letters for letter in word):
        print(" Congratulations! You won!")
        break

else:
    print(" Game over! The word was:", word)


        