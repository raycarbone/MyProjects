#!/usr/bin/python3

import sys, pickle
import modules.engine

def main():

  while True:

    print();print('Hang-Man Game!');print()
    action = input('What would you like to do, [S]tart a new game? Or [Q]uit: ')
    if action == 'S' or action == 's':
        modules.engine.start_game(action)


if __name__ == '__main__':
  main()


