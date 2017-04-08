# module start_game.py

import sys
import modules.engine

def start_game(action):


        print();
        new_player = input('Please enter your Name: ')
        print("Ok "+new_player+", Let's play...")

        guesses = 5
        B = list("---------")
        A = list("This Word")

        while guesses:
            guess = input('Enter a letter: ')
            modules.engine.check_letter(guess, A, B, guesses)
            print(B)

        print("Sorry, you ran out of guesses. You lose.")
        exit()

