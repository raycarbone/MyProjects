# module contact_create

import pickle
contact_list = {}


class Contact:


    def __init__(self, name, email, phone, category):
        #contact_list = {}
        self.name =  name
        self.email = email
        self.phone = phone
        self.category = category

        contact_list[self.name]={'name':self.name, 'email':self.email, 'phone':self.phone, 'category':self.category}

        print();print('Created a contact: {}'.format(self.name));print()
        #self.category = category



class Friend(Contact):

    def __init__(self, name, email, phone, category):
        Contact.__init__(self, name, email, phone)
        self.category = category


class Family(Contact):

    def __init__(self, name, email, phone, category):
        Contact.__init__(self, name, email, phone)
        self.category = category

class Colleagues(Contact):

    def __init__(self, name, email, phone, category):
        Contact.__init__(self, name, email, phone)
        self.category = category