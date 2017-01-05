#!/usr/bin/python3

#import contact_create
import sys
import pickle

def read_file():
  contact_list = 'contact.list'
  f = open(contact_list, 'rb')
  #f = open(contact_list, 'wb')
  try:
    List = pickle.load(f)
  except (IOError, EOFError):
    List = {}

  f.close()
  return (List, f)


def write_file(List, f):
  contact_list = 'contact.list'
  f = open(contact_list, 'wb')

  try:
    pickle.dump(List, f)
  except IOError:
    pass

  f.close()
  return


def create_contact(name, email, phone, category):

  List, f = read_file()
  print(List);print()
  List[name]={'name':name, 'email':email, 'phone':phone, 'category':category}
  write_file(List, f)

  print();print('Created a contact: {}'.format(name));print()
  return


def delete_contact(name):

  List, f = read_file()
  del List[name]
  write_file(List, f)
  print();print('Deleted a contact: {}'.format(name));print()
  return

def modify_contact(name, email, phone, category):

  List, f = read_file()
  old_List = List[name]
  if email == '':
    email = old_List['email']
  if phone == '':
    phone = old_List['phone']
  if category == '':
    category = old_List['category']

  List[name].update({'name':name, 'email':email, 'phone':phone, 'category':category})
  write_file(List, f)
  print();print('Modified a contact: {}'.format(name));print()
  return


def show_contact(name):

  List, f = read_file()

  try:
    print();print('The contact Name: {}'.format(List[name]['name']))
  except KeyError:
    print();print('The Contact {} not found!'.format(name));print()
    return

  print('The contact Email: {}'.format(List[name]['email']))
  print('The contact Phone: {}'.format(List[name]['phone']))
  print('The contact Caetgory: {}'.format(List[name]['category']));print()

  write_file(List, f)
  return

def main():

  while True:

    print();print('Online Contact List!');print()
    action = input('What would you like to do, [A]dd/[M]odify/[D]elete/[S]how a contact? Or [Q]uit: ')

    if action == 'A' or action == 'a':
      print(); print('Adding a new contact')
      new_name = input('Please enter the Name: ')
      new_email = input('Please enter the Email: ')
      new_phone = input('Please enter the Phone Number: ')
      new_category = input('Please enter the Contact Category [Friend/Family/Colleagues]: ')

      create_contact(new_name, new_email, new_phone, new_category)


    elif action == 'M' or action == 'm':
      print(); print('Modifying a contact')
      name = input('Please enter the Name of the contact to modify: ')
      show_contact(name);print()
      mod_email = input('Please enter the new Email for {} [Enter for default]: '.format(name))
      mod_phone = input('Please enter the new Phone for {} [Enter for default]: '.format(name))
      mod_category = input('Please enter the new Category for {} [Enter for default]: '.format(name))
      modify_contact(name, mod_email, mod_phone, mod_category)

    elif action == 'D' or action == 'd':
      print(); print('Deleting a contact')
      del_name  = input('Please enter the Name of the contact to delete: ')
      delete_contact(del_name)

    elif action == 'S' or action == 's':
      print(); print('Showing a contact')
      name = input('Please enter the Name of the contact to show: ')
      show_contact(name)

    elif action == 'Q' or action == 'q':
      exit(0)


if __name__ == '__main__':
  main()

