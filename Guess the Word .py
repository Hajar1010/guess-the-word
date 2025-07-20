# Mystery Word Game (Wordle-style)
# Author: hajar1010
# Description: A fun terminal game where the user has 6 tries to guess a 5-letter mystery word, with color-coded hints.

import random

word_list = [
    "apple", "grape", "stone", "brain", "zebra", "tiger", "light", "cloud", "spice", "candy",
    "plant", "sugar", "glass", "flame", "brave", "crane", "dream", "frost", "globe",
    "honey", "jelly", "knife", "lemon", "melon", "noble", "ocean", "pearl", "queen", "river",
    "storm", "table", "urban", "vivid", "whale", "xenon", "youth", "woman", "charm", "blaze",
    "bloom", "climb", "daisy", "eagle", "fable", "grind", "haste", "image", "jumpy", "karma"
]

chosen = random.choice(word_list)
guesses = 0

print("Welcome to the Mystery Word Game!")
print("Guess the 5-letter word. You have 6 tries.")
print("🟩 = correct place | 🟨 = in word wrong place | ⬜ = not in word")

while guesses < 6:
    guess = input("Enter a 5-letter word: ").lower()

    if len(guess) != 5 or guess not in word_list:
        print("Invalid word .")
        continue


    feedback = ""
    for i in range(5):
        if guess[i] == chosen[i]:
            feedback += "🟩"
        elif guess[i] in chosen:
            feedback += "🟨"
        else:
            feedback += "⬜"

    print("Hint:", feedback)
    guesses += 1

    if guess == chosen:
        print("\nCongratulations! You guessed the word:", chosen.upper())
        break

if guess != chosen:
    print("\nGame over. The correct word was:", chosen.upper())

