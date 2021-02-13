import pickle
import os
import pathlib


class Phonebook:
    # class variables
    first = ''
    last = ''
    num = 0

    def addNum(self):
        self.first = input('enter first name: ')
        self.last = input('enter last name: ')
        self.num = int(input('enter phone number: '))


def create():
    book = Phonebook()
    book.addNum()
    writedatatofile(book)


def writedatatofile(book):
    file = pathlib.Path('Phonebook.data')

    if file.exists():
        infile = open('Phonebook.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(book)
        infile.close()
        os.remove('Phonebook.data')
    else:
        oldlist = [book]
    outfile = open('newphonebook.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newphonebook.data', 'Phonebook.data')


def showcontacts():
    file = pathlib.Path('Phonebook.data')

    if file.exists():
        infile = open('Phonebook.data', 'rb')
        mylist = pickle.load(infile)

        for item in mylist:
            print('first name    lastname      number')
            print(item.first, ' ', item.last, ' ', item.num)

        infile.close()
    else:
        print('no data found')


def modifycontact(name):
    file = pathlib.Path('Phonebook.data')
    if file.exists():
        infile = open('Phonebook.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('Phonebook.data')

        for item in oldlist:
            if item.first == name:
                item.first = input('enter first name: ')
                item.last = input('enter last name: ')
                item.num = int(input('enter phone number'))
            else:
                print('no data found')

        outfile = open('newphonebook.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newphonebook.data', 'Phonebook.data')


def searchcontact(name):
    file = pathlib.Path('Phonebook.data')
    infile = open('Phonebook.data', 'rb')
    mylist = pickle.load(infile)
    infile.close()
    found = False

    for item in mylist:
        if item.first == name:
            print('number: ', item.num)
            found = True
        else:
            print('no data found')


def deletecontact(name, lastname):
    file = pathlib.Path('Phonebook.data')
    infile = open('Phonebook.data', 'rb')
    oldlist = pickle.load(infile)
    infile.close()

    newlist = []
    for item in oldlist:
        if item.first != name and item.last != lastname:
            newlist.append(item)
        os.remove('Phonebook.data')
        outfile = open('newphonebook.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newphonebook.data', 'Phonebook.data')


select = ''
while select != 6:
    print('welcome to phoenbook')
    print('\t1. add contact')
    print('\t2. show contacts')
    print('\t3. edit contact')
    print('\t4. search contact')
    print('\t5. delete contact')
    print('\t6. exit')
    select = input()

    if select == '1':
        create()
        print('contact create successfully')
    elif select == '2':
        showcontacts()
    elif select == '3':
        name = input('enter name of the contact: ')
        modifycontact(name)
        print('contact modified successfully')
    elif select == '4':
        name = input('enter name of the contact: ')
        searchcontact(name)
    elif select == '5':
        name = input('enter first name: ')
        lastname = input('enter last name: ')
        deletecontact(name, lastname)
        print('contact delete successfully')
    elif select == '6':
        print('thank you')
        break
