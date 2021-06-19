from ClassBook import *
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


#@error_handler
def main():
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
                print('Please write right path to file! This file is empty!')

        elif command == 'new':
            print(r'Please write the full path where to create file. Example: "d:\test\book.txt":')
            path = str(input())
            book = AddressBook()
            notes_book = NotesBook()
            break

        elif command == 'exit' or command == 'esc' or command == 'close':
            esc_e = False
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
   
    if len(book)>0:
        id_n=book[-1]["Id"]+1
    else:
        id_n=1    
    record1 = Record(name,id_n)

    while True:
        print('Do you want to add phone-number? "y" (YES) or n (NO). Type "exit" to exit')
        decicion = str(input())
        decicion = decicion.lower()
        if decicion == 'y' or decicion == 'yes':
            print('Input Phone Number. Example: +380501234567')
            phone = str(input())
            record1.add_phone(phone)
        elif decicion == 'exit' or decicion == 'esc' or decicion == 'close':
            esc_e = False
            break
        elif decicion == 'n' or decicion == 'not':
            break
    while True:
        print('Do you want to add Birthday? "y" (YES) or n (NO). Type "exit" to exit')
        decicion = str(input())
        decicion = decicion.lower()
        if decicion == 'y' or decicion == 'yes':
            print('Input Birthday. Expected day.month.year(Example:25.12.1970)')
            birthday = str(input())
            record1.user['Birthday'] = birthday
            break
        elif decicion == 'exit' or decicion == 'esc' or decicion == 'close':
            book.add_record(record1.user)
            esc_e = False
            return 'close'

        elif decicion == 'n' or decicion == 'not':
            break

    while True:
        print('Do you want to add Address? "y" (YES) or n (NO). Type "exit" to exit')
        decicion = str(input())
        decicion = decicion.lower()
        if decicion == 'y' or decicion == 'yes':
            print('Input Address. Please no more than 30 symbols')
            address = str(input())
            if len(address)>1 and len(address)<30:
                record1.user['Address'] = address
                break    
        elif decicion == 'exit' or decicion == 'esc' or decicion == 'close':
            book.add_record(record1.user)
            esc_e = False
            return 'close'

        elif decicion == 'n' or decicion == 'not':
            break
#START HERE
    while True:
        print('Do you want to add E-mail? "y" (YES) or n (NO). Type "exit" to exit')
        decicion = str(input())
        decicion = decicion.lower()
        if decicion == 'y' or decicion == 'yes':
            print('Input E-mail. Please no more than 25 symbols')
            email = str(input())
            if re.match('([a-zA-Z][a-zA-Z0-9\._!#$%^*=\-]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,})', email):
                if len(email)>1 and len(email)<25:
                    record1.user['E-mail'] = email
                    break 
            else:
                print('Format is wrong. Try again')
             
        elif decicion == 'exit' or decicion == 'esc' or decicion == 'close':
            book.add_record(record1.user)
            esc_e = False
            return 'close'

        elif decicion == 'n' or decicion == 'not':
            break

    while True:
        print('Do you want to add Tags? "y" (YES) or n (NO). Type "exit" to exit')
        decicion = str(input())
        decicion = decicion.lower()
        if decicion == 'y' or decicion == 'yes':
            print('Input Tags. Please no more than 10 symbols')
            tags = str(input())
            if len(tags)>1 and len(tags)<10:
                record1.user['Tags'] = tags
                book.add_record(record1.user)
                save()
                say = 'Successfully changed'
                return say  

        elif decicion == 'exit' or decicion == 'esc' or decicion == 'close':
            book.add_record(record1.user)
            esc_e = False
            return 'close'

        elif decicion == 'n' or decicion == 'not':
            book.add_record(record1.user)
            save()
            say = 'Successfully changed'
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
        result = book.find_value(old_name)
        if len(result)>1:
            print(f"I've found {len(result)} notes with this Name")
            show_find(result)
            print('Please enter Id to change the right name')
            find_v = result[0]["Name"]
            del_input=int(input())
            for i in book:
                if i["Name"]==find_v and i["Id"]==del_input:
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
#START CHaNGE
@error_handler
def birthday():
    print("Please write how many days in advance to warn you about people's birthday")
    n=int(input())
    result=[]
    for i in book:
        if i["Birthday"]!=0 and i["Birthday"]!=None:
            if days_to_birthday(i["Birthday"]) <=n:
                print("HERE")
                result.append(i)

    print(f'In future {n} days you need to congratulate {len(result)} people from your Addressbook')        
    show_find(result)
    

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
    
    if len(result)>1:
        print(f"I've found {len(result)} notes with this Name")
        show_find(result)
        print('Please enter Id to delete the right note')
        find_v = result[0]["Name"]
        del_input=int(input())
        for i in book:
            if i["Name"]==find_v and i["Id"]==del_input:
                book.remove(i)
                print(f"You've deleted {find_v}")
                save()  
    else:
        find_v = result["Name"]
        for i in book:
            if i["Name"]==find_v:
                book.remove(i)
                print(f"You've deleted {find_v}")
                save()           
#end
@error_handler
def find():
    #global path, book
    print('Put information you want to find')
    find_v = str(input())
    result = book.find_value(find_v)
    show_find(result)
    

def show_find(v_list):
    
    print("I've found following:")
    # Печать шапки с названием столбцов
    print(136*'_')
    print('| ID  |           Name           |     Phones      |  Birthday  |           Address            |           E-mail          |    Tags    |')
    print(136*'-')
    
    for i in v_list:
        print(f'|{i["Id"]:<5}| {i["Name"]:<25}| { i["Phones"][0] if len(i["Phones"])>=1 else " ":<15} | {i["Birthday"]if i["Birthday"] else " ":<11}|{i["Address"]if i["Address"] else " ":<30}|  {i["E-mail"]if i["E-mail"] else " ":<25}| {i["Tags"] if i["Tags"] else " ":<11}|')
        if len(i["Phones"]) > 1:
            for elem in i["Phones"][1:]:
                print(f'|     |                          | {elem: <15} |            |                              |                           |            |')
        print(f"{136*'_'}")
       
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

#@error_handler
def show1():
    number = input('Please input the number or record on 1 page: ')
    print("The contacts book is following:")
        # Печать шапки с названием столбцов
    print(137*'_')
    print('| ID  |           Name           |     Phones      |  Birthday  |           Address            |           E-mail          |    Tags    |')
    print(137*'-')
    if number!=0 or number!=None:
        iter = book.iterator1(number)
        for i in iter:
            print(i)
            print(57*'_'+'The end of the page'+58*'_')
        return "The end of the contacts book"
    else:
        iter = book.iterator1(10)
        for i in iter:
            print(i)
            print(57*'_'+'The end of the page'+58*'_')
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
    print('*Type "add"    to add new contact.\n*Type "birthday" to see people that have birthday nearest days.\n*Type "change" to change contact\'s phone, name or birthday.\n*Type "find"   to see information that you are looking for.\n*Type "delete" to delete information that you don\'t need.\n*Type "show"   to show you all phonebook.\n*Type "save"   to save and exit.\n*Type "exit"   to exit')

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
            'delete':delete,'birthday':birthday,
            'add note': add_note, 'delete note': delete_note, 'edit note': edit_note,
            'find note': find_note, 'sort notes': sort_notes, 'show notes': show_notes}

if __name__ == '__main__':
    main()

