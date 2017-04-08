#!/usr/bin/python3

import sys, pickle
import modules.start_game

def main():
    print()
    print('Hang-Man Game!')
    print()

    while True:
        action = input('What would you like to do, [S]tart a new game? Or [Q]uit: ')
        if action == 'S' or action == 's':
            modules.start_game.start_game(action)
        if action == 'Q' or action == 'q':
            print();print("Good Bye!");print()
            exit()





if __name__ == '__main__':
    main()


