# Mystery Word Game (Wordle-style)
# Author: hajar1010
# Description: A fun terminal game where the user has 6 tries to guess a 5-letter mystery word, with color-coded hints.

import random

# 1. Define a list of valid 5-letter words
word_list= ["apple", "grape", "stone", "brain", "zebra"]

# 2. Randomly pick one word from the list as the mystery word
chosen=random.choice(word_list)

# 3. Create a loop to allow max 6 guesses from the user
guesses=0
print("Welcome to the Mystery Word Game!")
#    - Ask the user to enter a 5-letter word
while guesses<6 :
    _5letter=input(" enter a 5-letter word").lower()
    if len(_5letter) != 5 or _5letter not in word_list:
        print(" Invalid word.")
        continue
#  Give feedback:
    feedback = ""
    for i in range(5):
        if _5letter[i] == chosen[i]:
            feedback += _5letter[i].upper()  # Correct position
        elif _5letter[i] in chosen:
            feedback += _5letter[i].lower()  # Wrong position
        else:
            feedback += "_"  # Not in the word

    print("Hint: ", feedback)
    guesses += 1
    if _5letter== chosen:
        print("Congraaatss! You guessed the word:", chosen)
        break
if _5letter!= chosen:
    print("\n Game over. The correct word was:", chosen)
