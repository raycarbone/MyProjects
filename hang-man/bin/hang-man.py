#!/usr/bin/python3

#import contact_create
import sys
import pickle


def main():

  while True:

    print();print('Hang-Man Game!');print()
    action = input('What would you like to do, [S]tart a new game? Or [Q]uit: ')


    if action == 'S' or action == 's':
      print(); print("Let's play...")
      new_player = input('Please enter your Name: ')

      # sart a new game
      #create_contact(new_name, new_email, new_phone, new_category)
      A = list("This Word")
      B = list("---------")

    guess = input('Enter a letter: ')
    k = 0
    for i in A:
        if i == guess:
            B[k] = i
        k=k+1
    print(B)







    #elif action == 'Q' or action == 'q':
    #  exit(0)


if __name__ == '__main__':
  main()


