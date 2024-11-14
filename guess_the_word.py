#Nancy Rankin
#CIS256 Fall 2024
# EX 4 Testing with pytest and Git Manipulation

import random
word_dic = ["phase" "magic", "flash", "globe", "usage", "shall", "unity", "drove", "water", "sharp"]

print("Welcome to Guess the Word! In this program you will get 25 chances to guess a 5 letter word")

word_to_guess = random.choice(word_dic)

letter1 = word_to_guess[0]
letter2 = word_to_guess[1]
letter3 = word_to_guess[2]
letter4 = word_to_guess[3]
letter5 = word_to_guess[4]

user_guess = ["_"]*5
guesses = 25

while guesses > 0 and user_guess != word_to_guess:
    print(f"\nWord to guess{user_guess}")
    print(f"You have {guesses} attempts left.")

    guess = input("Guess a letter: ").lower()


    if guess == letter1:
        user_guess[0] = letter1

    elif guess == letter2:
        user_guess[1] = letter2

    elif guess == letter3:
       user_guess[2] = letter3

    elif guess == letter4:
        user_guess[3] = letter4

    elif guess == letter5:
       user_guess[4] = letter5

    else:
        print(f"{guess} is not in the word.")
        guesses -= 1


    if user_guess == word_to_guess:
        print(f"You guessed the word {word_to_guess}")

else:
    if user_guess != word_to_guess:
        print(f"\n You did not guess the word. (And now you'll never know)")