# module engine.py

import sys


def check_letter(guess, A, B, guesses):
    k = 0
    guessed = False
    print(guesses)
    for i in A:
        if i == guess:
            B[k] = i
            guessed = True
        k = k + 1
    if not guessed:
        guesses = guesses - 1
        print(guesses)
    return B, guesses
