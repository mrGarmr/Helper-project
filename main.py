import pathlib
import pickle
from ClassBook import *
from clean import *
from datetime import datetime, timedelta, date
from notes_book import NotesBook


def error_handler(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except:
            #print('я внутри error_handler ')
            result = input_error()
            return result
    return inner


@error_handler
def main():
    global path, book, notes_book, esc_e
    esc_e = True
    while True:
        print('What do you want to do?\nYou can use commands: "load" to load Adress Book and "new" to create new Book or "exit"/"close" to close application:')
        command = str(input())
        if command == "load" or command == "дщфв":
            print(r'Please write the full path to file. Example: "d:\test\book.txt":')
            path = str(input())
            try:
                with open(path, 'rb') as fh:
                    book = pickle.load(fh)
                    notes_book = pickle.load(fh)
                    break
            except:
                print('Please write right path to file! This file is empty!')

        elif command == 'new' or command == "туц":
            print(
                r'Please write the full path where to create file. Example: "d:\test\book.txt":')
            path = str(input())
            book = AddressBook()
            notes_book = NotesBook()
            break

        elif command == 'exit' or command == 'esc' or command == 'close' or command == 'учше':
            esc_e = False
            break
        else:
            print('Wrong command.')

    while esc_e:
        user_inpu = input(
            'What do you want to do? Type exact command you want to do, "exit" to exit or "help" for list of commands.\n')
        user_inpu = user_inpu.lower()
        result = handler(user_inpu)
        if result:
            print(result)
        elif result == None:
            pass
        else:
            break


@error_handler
def add():
    say = 'Successfully changed'
    global esc_e, book
    print('Input Name:')
    name = Name(str(input()))
    if name == 'exit' or name == 'esc' or name == 'close' or name == 'учше':
        esc_e = False
        return "Not saved"
    if len(book) > 0:
        id_n = book[-1]["Id"]+1
    else:
        id_n = 1
    record1 = Record(name, id_n)

    while True:
        print('Do you want to add phone-number? "y" (YES) or n (NO). Type "exit" to exit')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            print('Input Phone Number. Example: +380501234567')
            phone = str(input())
            if re.fullmatch('[+]?[0-9]{3,12}', phone):
                record1.add_phone(phone)
            else:
                print(
                    'Wrong input! Phone must start with + and have 12 digits. Example +380501234567')

        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision == 'учше':
            esc_e = False
            return 'Closed'
        elif decision == 'n' or decision == 'not' or decision == 'no' or decision == 'нет' or decision == 'тщ' or decision == 'тще' or decision == 'т':
            break
        else:
            print('Wrong input!')

    while True:
        print('Do you want to add Birthday? "y" (YES) or n (NO). Type "exit" to exit')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            print('Input Birthday. Expected day.month.year(Example:25.12.1970)')
            birthday = str(input())
            record1.user['Birthday'] = birthday
            break
        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision == 'учше':
            book.add_record(record1.user)
            esc_e = False
            return 'Closed'

        elif decision == 'n' or decision == 'not' or decision == 'no' or decision == 'нет' or decision == 'тщ' or decision == 'тще' or decision == 'т':
            break

        else:
            print('Wrong input!')

    while True:
        print('Do you want to add Address? "y" (YES) or n (NO). Type "exit" to exit')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            print('Input Address. Please no more than 30 symbols')
            address = str(input())
            if len(address) > 1 and len(address) <= 30:
                record1.user['Address'] = address
                break
            else:
                print(
                    f'Your Address is {len(address)} symbols. Please no more than 30 symbols')
        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision == 'учше':
            book.add_record(record1.user)
            esc_e = False
            return 'Closed'

        elif decision == 'n' or decision == 'not' or decision == 'no' or decision == 'нет' or decision == 'тщ' or decision == 'тще' or decision == 'т':
            break
        else:
            print('Wrong input!')

# START HERE
    while True:
        print('Do you want to add E-mail? "y" (YES) or n (NO). Type "exit" to exit')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            print('Input E-mail. Please no more than 30 symbols')
            email = str(input())
            if re.match('([a-zA-Z][a-zA-Z0-9\._!#$%^*=\-]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,})', email):
                if len(email) > 1 and len(email) <= 30:
                    record1.user['E-mail'] = email
                    break
                else:
                    print(
                        f'Your E-mail is {len(email)} symbols. Please no more than 30 symbols')
            else:
                print(
                    'Format is wrong. Try again in format: your_nickname@something.domen_name')

        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision == 'учше':
            book.add_record(record1.user)
            esc_e = False
            return 'Closed'

        elif decision == 'n' or decision == 'not' or decision == 'no' or decision == 'нет' or decision == 'тщ' or decision == 'тще' or decision == 'т':
            break

        else:
            print('Wrong input!')

    while True:
        print('Do you want to add Tags? "y" (YES) or n (NO). Type "exit" to exit')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            print('Input Tags. Please no more than 15 symbols')
            tags = str(input())
            if len(tags) > 1 and len(tags) <= 15:
                record1.user['Tags'] = tags
                book.add_record(record1.user)
                save()
                return say
            else:
                print(
                    f'Your Tags is {len(tags)} symbols. Please no more than 15 symbols')

        elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision == 'учше':
            book.add_record(record1.user)
            esc_e = False
            return 'Closed'

        elif decision == 'n' or decision == 'not' or decision == 'no' or decision == 'нет' or decision == 'тщ' or decision == 'тще' or decision == 'т':
            book.add_record(record1.user)
            save()
            return say
        else:
            print('Wrong input!')


@error_handler
def change():
    global book, esc_e
    say = 'Successfully changed'
    print('Type name of record you want to change')
    old_name = str(input())
    old_name = old_name.lower()
    result = book.find_value(old_name)
    for i in result:
        if i["Name"] != old_name:
            result.remove(i)
    show_find(result)

    print('To change Name: type "name".\nTo change Phone: type "phone".\nTo change Birthday: type "birthday".\nTo change Address: type "address".\n')
    print('To change E-mail: type "email".\nTo change Tags: type "tags".')
    decision = str(input())
    decision = decision.lower()

    if decision == 'name' or decision == 'тфьу':
        print('Type new name')
        new_name = str(input())

        if len(result) > 1:
            print(f"I've found {len(result)} notes with this Name")
            show_find(result)
            print('Please enter Id to change the right name')
            find_v = result[0]["Name"]
            del_input = int(input())
            for i in result:
                if i["Name"] == find_v and i["Id"] == del_input:
                    i['Name'] = new_name
                    save()
                return say
        elif len(result) == 1:
            for i in result:
                i['Name'] = new_name
                save()
            return say

        else:
            print(f'{old_name} not in Adress Book')

    elif decision == 'phone' or decision == 'зрщту':
        print('Type phone you want to change.If there are no phones - just press "enter".')
        old_name = str(input())
        print('Type new phone')
        new_name = str(input())
        for i in result:
            if len(i['Phones']) > 1:
                for j in i['Phones']:
                    if j == old_name:
                        i['Phones'].remove(j)
                        i['Phones'].append(new_name)
                        save()
                        return say
                    else:
                        print(f'{old_name} not in Adress Book')
            elif len(i['Phones']) == 1:
                i['Phones'].remove(old_name)
                i['Phones'].append(new_name)
                return say
            elif len(i['Phones']) == 0:
                i['Phones'].append(new_name)
                save()
                return say

    elif decision == 'birthday' or decision == 'ишкервфн':
        print('Type birthday you want to change. Expected day.month.year(Example:25.12.1970). If there is no birthday - just press "enter".')
        old_name = str(input())
        print('Type new birthday. Expected day.month.year(Example:25.12.1970)')
        new_name = str(input())
        for i in result:
            if i['Birthday'] == old_name:
                i['Birthday'] = new_name
                save()
                return say
            elif i['Birthday'] == None:
                i['Birthday'] = new_name
                save()
                return say
            else:
                print(f'{old_name} not in Adress Book')

    elif decision == 'address' or decision == 'adress' or decision == 'adres' or decision == 'фввкуіі' or decision == 'фвкуі':
        print(
            'Type address you want to change. If there is no address - just press "enter".')
        old_name = str(input())
        print('Type new address.')
        new_name = str(input())
        for i in result:
            if i['Address'] == old_name:
                i['Address'] = new_name
                save()
                return say
            elif i['Address'] == None:
                i['Address'] = new_name
                save()
                return say
            else:
                print(f'{old_name} not in Adress Book')

    elif decision == 'email' or decision == 'e-mail' or decision == 'уьфшд':
        print('Type E-mail you want to change.)')
        old_name = str(input())
        print('Type new E-mail.')
        new_name = str(input())
        for i in result:
            if i['E-mail'] == old_name:
                i['E-mail'] = new_name
                save()
                return say
            elif i['E-mail'] == None:
                i['E-mail'] = new_name
                save()
                return say
            else:
                print(f'{old_name} not in Adress Book')

    elif decision == 'tags' or decision == 'tag' or decision == 'ефп':
        print('Type Tags you want to change. If there are no Tags - just press "enter"')
        old_name = str(input())
        print('Type new Tags.')
        new_name = str(input())
        for i in result:
            if i['Tags'] == old_name:
                i['Tags'] = new_name
                save()
                return say
            elif i['Tags'] == None:
                i['Tags'] = new_name
                save()
                return say
            else:
                print(f'{old_name} not in Adress Book')

    elif decision == 'exit' or decision == 'esc' or decision == 'close' or decision == 'учше':
        esc_e = False
        return esc_e
# START CHaNGE


@error_handler
def clean_folder():
    #global user_input
    print(100*"_")
    print('Welcome to clean folder instrument!')
    print(100*"_")
    print('Please enter path to clean and structurise.')
    user_input = str(input())

    path = pathlib.Path(user_input)
    print_recursive(path, user_input)
    delete_dir(user_input)
    # D:\Tresh
    return 'Everything done! Please check yor folder!'


@error_handler
def birthday():
    print("If you want to find, who'll have birthday in exact date TYPE 1.\nIf you need to know who'll have birthday in period of time TYPE 2.\nIf you need to know how many days to somebody's birthday TYPE 3.")
    decision = int(input())
    result = []

    if decision == 1:
        print("Please write in how many days will be people's birthday")
        n = int(input())
        today_d = datetime.now().date()
        d = timedelta(days=n)
        bday = today_d+d
        bday = bday.strftime("%d.%m.%Y")
        for i in book:
            if i["Birthday"] != 0 and i["Birthday"] != None:
                if days_to_birthday(i["Birthday"]) == n:
                    result.append(i)
        print(
            f'On {bday} you need to congratulate {len(result)} people from your Addressbook')
        show_find(result)

    elif decision == 2:
        print("Please write how many days in advance to warn you about people's birthday")
        n = int(input())
        for i in book:
            if i["Birthday"] != 0 and i["Birthday"] != None:
                if days_to_birthday(i["Birthday"]) <= n:
                    result.append(i)
        print(
            f'In future {n} days you need to congratulate {len(result)} people from your Addressbook')
        show_find(result)

    elif decision == 3:
        print("Please write name to know how many days left to birthday")
        name = input()
        result = book.find_value(name)
        if len(result) > 1:
            print(f"I've found {len(result)} notes with this Name")
            show_find(result)
            print(
                'Please enter Id to know how many days left to birthday the exact person')
            find_v = result[0]["Name"]
            id_input = int(input())
            for i in result:
                if i["Name"] == find_v and i["Id"] == id_input:
                    days = days_to_birthday(i['Birthday'])
                    print(
                        f'{i["Name"]} from your Addressbook will have birthday in {days} days. Do not forget to congratulate!')

        elif len(result) == 1:
            for i in result:
                days = days_to_birthday(i['Birthday'])
                print(
                    f'{i["Name"]} from your Addressbook will have birthday in {days} days. Do not forget to congratulate!')

    else:
        print('Not found this Name!')


def days_to_birthday(bday):
    today_d = datetime.now().date()
    bday = datetime.strptime(bday, "%d.%m.%Y").date()
    bday = date(today_d.year, bday.month, bday.day)

    if today_d > bday:
        bday = date(today_d.year+1, bday.month, bday.day)
        days_left = (bday-today_d)
    else:
        days_left = (bday-today_d)

    return days_left.days


@error_handler
def delete():
    print('Put Name, you want to find and delete from your addressbook')
    find_v = str(input())
    result = book.find_value(find_v)
    for i in result:
        if i["Name"] != find_v:
            result.remove(i)

    if len(result) > 1:
        print(f"I've found {len(result)} notes with this Name")
        show_find(result)
        print('Please enter Id to delete the right note')

        del_input = int(input())
        for i in book:
            if i["Name"] == find_v and i["Id"] == del_input:
                book.remove(i)
                print(f"You've deleted {find_v}")
                save()

    elif len(result) == 1:
        for i in result:
            if i["Name"] == find_v:
                book.remove(i)
                print(f"You've deleted {find_v}")
                save()

    else:
        print(f"{find_v} not found")
# end


@error_handler
def find():

    print('Put word, half of word or digits you want to find')
    find_v = str(input())
    result = book.find_value(find_v)
    show_find(result)


def show_find(v_list):

    print("I've found following:")
    # Печать шапки с названием столбцов
    print(145*'_')
    print('| ID  |           Name           |     Phones      |  Birthday  |           Address            |              E-mail            |       Tags     |')
    print(145*'-')

    for i in v_list:
        print(f'|{i["Id"]:<5}| {i["Name"]:<25}| { i["Phones"][0] if len(i["Phones"])>=1 else " ":<15} | {i["Birthday"]if i["Birthday"] else " ":<11}|{i["Address"]if i["Address"] else " ":<30}|  {i["E-mail"]if i["E-mail"] else " ":<30}| {i["Tags"] if i["Tags"] else " ":<15}|')
        if len(i["Phones"]) > 1:
            for elem in i["Phones"][1:]:
                print(
                    f'|     |                          | {elem: <15} |            |                              |                                |                |')
        print(f"{145*'_'}")


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
        # return 'Successfully saved'

# @error_handler


def show1():
    number = input('Please input the number or record on 1 page: ')
    try:
        number = int(number)
    except:
        number = 10
    print("The contacts book is following:")
    if number == 0 or number == None:
        number = 10
    iter = book.iterator1(number)
    for i in iter:
        # Печать шапки с названием столбцов
        print(145*'_')
        print('| ID  |           Name           |     Phones      |  Birthday  |           Address            |              E-mail            |      Tags      |')
        print(145*'-')
        print(i)
        print(63*'_'+'The end of the page'+63*'_')
        input()
    return "The end of the contacts book"
##############################################################
# Команды для Handler для работы с NotesBook


@error_handler
def add_note():
    print('Please input your note (press double Enter to finish):')
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
    save()
    return "Your note is successfully saved"


@error_handler
def delete_note():
    print("Please input a hashtag of note that you would like to delete:")
    hashtag = input().upper()
    notes_book.delete_note(hashtag)
    save()
    return f"The note with hashtag '{hashtag}' is deleted"


@error_handler
def edit_note():
    print("Please input a hashtag of note that you would like to edit:")
    hashtag = input().upper()
    notes_book.edit_note(hashtag)
    save()
    return "The note is edited"


@error_handler
def find_note():
    print('Please input keyword for search:')
    keyword = input().upper()
    print('THE RESULTS OF SEARCH:')
    if notes_book.find_note(keyword):
        print(notes_book.find_note(keyword))
        result = "The search is sucessfully finished"
    else:
        result = f"The keyword {keyword} is absent in Notes Book"
    return result


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
    print(60*'*')
    print(20*'*'+'WORKING WITH ADDRESSBOOK:'+20*'*')
    print('*Type "add"    to add new contact.\n*Type "birthday" to see people that have birthday nearest days.\n*Type "change" to change contact\'s phone, name or birthday.\n*Type "find"   to see information that you are looking for.\n*Type "delete" to delete information that you don\'t need.\n*Type "show"   to show you all phonebook.\n*Type "save"   to save and exit.\n*Type "exit"   to exit')
    print(20*'*'+'WORKING WITH NOTESBOOK:'+20*'*')
    print('*Type "add note"    to add new note.\n*Type "delete note"    to delete note.\n*Type "edit note"    to edit note.\n*Type "find note"    to look through notes.\n*Type "sort notes"    to sort notes.\n*Type "show notes"    to show your notes.\n')
    print(20*'*'+'WORKING WITH CLEANFOLDER:'+20*'*')
    print('*Type "clean"    to clean and structurise folder.\n')
    return (60*'*')


@error_handler
def handler(user_inpu):
    if user_inpu in ANSWEARS.keys():
        return ANSWEARS[user_inpu]()
    elif user_inpu in ADD:
        print('Maybe you mean "add" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return add()
    elif user_inpu in CHANGE:
        print('Maybe you mean "change" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return change()

    elif user_inpu in FIND:
        print('Maybe you mean "find" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return find()

    elif user_inpu in HELP:
        print('Maybe you mean "help" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return help()

    elif user_inpu in DELETE:
        print('Maybe you mean "delete" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return delete()

    elif user_inpu in BIRTHDAY:
        print('Maybe you mean "birthday" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return birthday()

    elif user_inpu in CLEAN:
        print('Maybe you mean "clean" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return clean_folder()

    elif user_inpu in SHOW:
        print('Maybe you mean "show" command?\nIf YES type "yes" or "y"\nIf NO type "no" or "n"')
        decision = str(input())
        decision = decision.lower()
        if decision == 'y' or decision == 'yes' or decision == 'нуі' or decision == 'н' or decision == 'да' or decision == 'д':
            return show1()
    else:
        return input_error()


def input_error():
    return 'Wrong input! Type exact command you want to do,"exit" to exit or "help" for list of commands.'


ANSWEARS = {'add': add, 'ad': add, '+': add, 'фвв': add, 'change': change, 'срфтпу': change, 'close': exit, 'exit': exit, 'учше': exit,
            'find': find, 'аштв': find, 'help': help_func, 'рудз': help_func, 'хелп': help_func, 'save': save, 'іфму': save, 'ыфму': save, 'show': show1, 'ырщц': show1, 'ірщц': show1,
            'delete': delete, 'del': delete, 'вуд': delete, 'вудуеу': delete, 'birthday': birthday, 'ишкервфн': birthday, 'clean': clean_folder, 'сдуфт': clean_folder,
            'add note': add_note, 'фвв тщеу': add_note, 'delete note': delete_note, 'вудуеу тщеу': delete_note, 'edit note': edit_note, 'увше тщеу': edit_note,
            'find note': find_note, 'аштв тщеу': find_note, 'sort notes': sort_notes, 'ыщке тщеуы': sort_notes, 'show notes': show_notes, 'ырщц тщеуы': show_notes}

ADD = ['a', 'ad', 'addd', 'asd', 'asdd', 'sdd', 'adf', 'фів', 'івв',
       'фівв', 'фввв', 'фва', 'вв', 'ыва', 'фвы', 'фыв', 'явв', 'фв']
CHANGE = ['chane', 'chnge', 'cange', 'chenge', 'hange', 'chng', 'cchenge', 'chhenge', 'cheenge',
          'chaange', 'сменить', 'chang', 'срутпу', 'срутп', 'менять', 'изменить', 'срфтп', 'рсфтпу', 'срутпу']
FIND = ['fnd', 'ind', 'fid', 'fin', 'faind', 'fand', 'ffind', 'fiind', 'finnd', 'findd',
        'seek', 'look', 'look for', 'атв', 'афтв', 'штв', 'афт', 'поиск', 'искать', 'найти', 'шштв']
HELP = ['&', '?', 'hlp', 'what', 'why', 'where', 'how', 'elp', 'hep', 'hel', 'healp',
        'halp', 'hhelp', 'heelp', 'hellp', 'helpp', 'рфдз', 'рдз', 'руз', 'руд', 'помощь']
DELETE = ['вуд', '-', 'del', 'вудуеу', 'вуфдуеу', 'dealete', 'elete', 'elet',
          'delet', 'dlte', 'dlt', 'lete', 'dealete', 'вудуе', 'удалить', 'clear', 'pop']
BIRTHDAY = ['lf', 'birsday', 'bersday', 'bezday', 'bethday', 'birzday', 'bearsday', 'birthdey', 'beersday', 'brthday', 'иууксвфн', 'ишквфн',
            'др', 'рождение', 'бездей', 'бирсдей', 'днюха', 'birthday people', 'birthday boy', 'birthday girl', 'birthda', 'birtda', 'birth']
CLEAN = ['cleen', 'clan', 'clin', 'cleane', 'cleene', 'klin', 'klean', 'lean', 'clen',
         'kleen', 'суф', 'лдуут', 'лдуфт', 'сдуфту', 'клн', 'клин', 'разобрать', 'мусор']
SHOW = ['ырща', 'ырщцу', 'showe', 'schow', 'schove', 'chov', 'shove', 'schov',
        'schowe', 'how', 'sho', 'shouv', 'шов', 'ірщцу', 'показать', 'рщц', 'ірщм']


if __name__ == '__main__':
    main()
