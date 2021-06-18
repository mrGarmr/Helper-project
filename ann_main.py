#from ClassBook import *
from annClasses import *
#from notes_book import NotesBook
import pickle


def error_handler(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except:
            print('я внутри error_handler ')
            result = input_error()
            return result
    return inner


@error_handler
def main():
    # global path, book, esc_e
    global path, book, notes_book, esc_e
    esc_e = True
    while True:
        print('What do you want to do?\nYou can use commands: "load" to load Adress Book and "new" to create new Book or "exit"/"close" to close application:')
        command = str(input())
        if command == "load":
            print(r'Please write the full path to file. Example: "d:\test\book.txt":')
            path = str(input())
            try:
                with open(path, 'rb') as fh:
                    book = pickle.load(fh)
                    notes_book = pickle.load(fh)
                    break
            except:
                print('Please write wright path to file! This file is empty!')

        elif command == 'new':
            print(
                r'Please write the full path where to create file. Example: "d:\test\book.txt":')
            path = str(input())
            book = AddressBook()
            notes_book = NotesBook()
            break

        elif command == 'exit' or command == 'esc' or command == 'close':
            esc = False
            break
        else:
            print('Wrong command.')

    while esc_e:
        user_input = input(
            'What do you want to do? Type "help" for additional commands.\n')
        result = handler(user_input)
        if result:
            print(result)
        elif result == None:
            pass
        else:
            break


@error_handler
def add():
    global esc_e, book
    print('Input Name:')
    name = Name(str(input()))
    record1 = Record(name)
    esc = True
    while True:
        print('Do you want to add phone-number? "y" (YES) or n (NO). Type "exit" to exit')
        decicion = str(input())
        decicion = decicion.lower()
        if decicion == 'y' or decicion == 'yes':
            print('Input Phone Number. Example: +380501234567')
            phone = str(input())
            '''if len(phone) < 13:
                print('This phone-number is too short. Try again')
            elif phone[0] != '+':
                print('Wrong format! First simbol have to be "+". Please try again')'''
            record1.add_phone(phone)
        elif decicion == 'exit' or decicion == 'esc' or decicion == 'close':
            esc_e = False
            break
        elif decicion == 'n' or decicion == 'not':
            break
    while esc:
        print('Do you want to add Birthday? "y" (YES) or n (NO). Type "exit" to exit')
        decicion = str(input())
        decicion = decicion.lower()
        if decicion == 'y' or decicion == 'yes':
            print('Input Birthday. Expected day.month.year(Example:25.12.1970)')
            birthday = str(input())
            record1.user['Birthday'] = birthday
            book.add_record(record1.user)
            esc = False
            say = 'Successfully changed! Save your record - type "save"'
            return say

        elif decicion == 'exit' or decicion == 'esc' or decicion == 'close':
            book.add_record(record1.user)
            esc_e = False
            return 'Good Bye'

        elif decicion == 'n' or decicion == 'not':
            book.add_record(record1.user)
            say = 'Successfully changed! Save your record - type "save"'
            return say


@error_handler
def change():
    global book, esc_e
    print('To change name: type "name", to change phone: type "phone", to change birthday: type "birthday"')
    decicion = str(input())
    decicion = decicion.lower()
    if decicion == 'name':
        print('Type name you want to change')
        old_name = str(input())
        old_name = old_name.lower()
        print('Type new name')
        new_name = str(input())
        for i in book:
            if i['Name'].lower() == old_name:
                i['Name'] = new_name
                say = 'Successfully changed'
                return say
            else:
                print(f'{old_name} not in Adress Book')

    elif decicion == 'phone':
        print('Type phone you want to change')
        old_name = str(input())
        print('Type new phone')
        new_name = str(input())
        for i in book:
            for j in i['Phones']:
                if j == old_name:
                    i['Phones'].remove(j)
                    i['Phones'].append(new_name)
                    say = 'Successfully changed'
                    return say
            else:
                print(f'{old_name} not in Adress Book')
    elif decicion == 'birthday':
        print(
            'Type birthday you want to change. Expected day.month.year(Example:25.12.1970)')
        old_name = str(input())
        print('Type new birthday. Expected day.month.year(Example:25.12.1970)')
        new_name = str(input())
        for i in book:
            if i['Birthday'] == old_name:
                i['Birthday'] = new_name
                say = 'Successfully changed'
                return say
            else:
                print(f'{old_name} not in Adress Book')

    elif decicion == 'exit' or decicion == 'esc' or decicion == 'close':
        esc_e = False
        return esc_e


@error_handler
def find():
    global path, book
    print('Put information you want to find')
    find_v = str(input())
    result = book.find_value(find_v)
    return result


def exit():
    global esc_e
    save()
    esc_e = False
    return "Good Bye"


def save():
    global path, book, notes_book
    with open(path, 'wb') as fh:
        pickle.dump(book, fh)
        pickle.dump(notes_book, fh)
        return 'Successfully saved'


@error_handler
def show():
    # counter=0
    print(79*'_')
    print('|                  Name                   |       Phones         |  Birthday  |')
    print(79*'_')
    for i in book:
        print(f'| {i["Name"]:<40}| { i["Phones"][0] if len(i["Phones"])>=1 else " ":<20} | {i["Birthday"]if i["Birthday"] else " ":<11}|')
        if len(i["Phones"]) > 1:
            for elem in i["Phones"][1:]:
                print(
                    f'|                                         | {elem: <20} |            |')

        # counter+=1
        print(79*'_')


'''@error_handler
def show(): #мой вариант
    if book == []:
        print('Your phonebook is empty')
    else:
        n = int(input('How many records should I show at once? ')) #ну, или просто 
        result = book.iterator(n)
        return result'''


@error_handler
def show1():
    number = int(input('Please input the number or record on 1 page: '))
    print("The contacts book is following:")
    # Печать шапки с названием столбцов
    print(79*'_')
    print('|                  Name                   |       Phones         |  Birthday  |')
    print(79*'_')
    iter = book.iterator1(number)
    for i in iter:
        print(i)
        print(
            '------------------------------The end of the page-----------------------------\n')
    return "The end of the contacts book"
##############################################################
# Команды для Handler для работы с NotesBook


@error_handler
def add_note():
    print('Please input your note:')
    # ввод многострочной заметки
    lines = []
    flag = True
    while flag:
        line = input()
        if line:
            lines.append(line)
        else:
            flag = False
    text = '\n'.join(lines)
    # ввод тєгов
    hashtag = input('Please input the hashtag of your note: \n')
    # добавление заметки в NotesBook
    notes_book.add_note(text, hashtag.upper())
    return "Your note is successfully saved"


@error_handler
def delete_note():
    print("Please input a hashtag of note that you would like to delete:")
    hashtag = input().upper()
    notes_book.delete_note(hashtag)
    return f"The note with hashtag '{hashtag}' is deleted"


@error_handler
def edit_note():
    print("Please input a hashtag of note that you would like to edit:")
    hashtag = input().upper()
    notes_book.edit_note(hashtag)
    return "The note is edited"


@error_handler
def find_note():
    print('Please input keyword for search:')
    keyword = input().upper()
    print('THE RESULTS OF SEARCH:')
    print(notes_book.find_note(keyword))
    return "The search is sucessfully finished"


@error_handler
def sort_notes():
    print("What type of sort would you like? Please input:")
    print("1 - to sort from A to Z")
    print("2 - to sort from Z to A")
    print("3 - to sort from old notes to new notes")
    print("4 - to sort from new notes to old notes")
    search_type = input()
    print('The sorted Notes are:')
    print(notes_book.sort_notes(search_type))
    return('The end of sorted Notes')


@error_handler
def show_notes():
    print('Your Notes Book:')
    print(notes_book)
    return "The end of Notes Book"

# Конец конец команд для NotesBook


def help_func():
    print(40*'*')
    print('*Type "add"    to add new contact.\n*Type "change" to change contact\'s phone, name or birthday.\n*Type "find"   to see information that you are looking for.\n*Type "show"   to show you all phonebook.\n*Type "save"   to save and exit.\n*Type "exit"   to exit')

    return (40*'*')


@error_handler
def handler(user_input):
    if user_input in ANSWEARS.keys():
        return ANSWEARS[user_input]()
    else:
        return input_error()


def input_error():
    return 'Wrong input! Type "help" for commands or "exit" to exit'


ANSWEARS = {'add': add, 'change': change, 'close': exit, 'exit': exit,
            'find': find, 'help': help_func, 'save': save, 'show': show1,
            'add note': add_note, 'delete note': delete_note, 'edit note': edit_note,
            'find note': find_note, 'sort notes': sort_notes, 'show notes': show_notes}

if __name__ == '__main__':
    main()

# ANSWEARS = {'add': add, 'change': change, 'close': exit, 'exit': exit,
#             'find': find, 'help': help_func, 'save': save, 'show': show}