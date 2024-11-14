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
        pass

    elif guess == letter2:
        pass

    elif guess == letter3:
       pass

    elif guess == letter4:
        pass

    elif guess == letter5:
       pass

    else:
        print(f"{guess} is not in the word.")


    if user_guess == word_to_guess:
        print(f"You guessed the word {word_to_guess}")

else:
    if user_guess != word_to_guess:
        print(f"\n You did not guess the word. (And now you'll never know)")