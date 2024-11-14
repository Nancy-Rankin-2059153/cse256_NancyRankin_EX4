#Nancy Rankin
#CIS256 Fall 2024
# EX 4 Testing with pytest and Git Manipulation

import random
from glob import magic_check

import guess_the_word
from guess_the_word import word_dic, guesses, word_to_guess, user_guess


def test_word_in_list():
       test_word = random.choice(word_dic)
       assert test_word in word_dic,"Test word not in word list"

def test_correct_guesses():
    word_to_guess = "magic"
    user_guess = ["_"] * 5
    guess = 'm'

    if guess == word_to_guess[0]:
        user_guess[0] = word_to_guess[0]

    assert user_guess == (f"[\"m\"][\"_\"][\"_\"][\"_\"][\"_\"]"),"Correct guess not processed correctly"



