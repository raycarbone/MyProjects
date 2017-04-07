# module engine.py

def start_game(action):
        print();
        print("Let's play...")
        new_player = input('Please enter your Name: ')
        guesses = 5
        while guesses:
            # sart a new game
            A = list("This Word")
            B = list("---------")
            guess = input('Enter a letter: ')
            check_letter(guess, A, B, guesses)

            print(B)


def check_letter(guess, A, B, guesses):

    k = 0
    for i in A:
        if i == guess:
            B[k] = i
        else:
            guesses = guesses -1
        k = k + 1
