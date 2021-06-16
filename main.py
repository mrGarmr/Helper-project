import ClassBook

def error_handler(func):
    def inner(*args):
        try:
            result=func(*args)
            return result
        except:
            result=input_error()
            return result
    return inner


@error_handler
def main():
    global path, book, esc_e
    esc_e=True
    while True:
        print('What do you want to do?\nYou can use commands: "load" to load Adress Book and "new" to create new Book or "exit"/"close" to close application:')
        command=str(input())
        if command=="load":
            print(r'Please write the full path to file. Example: "d:\test\book.txt":')
            path=str(input())
            with open(path, 'rb') as fh:
                book = pickle.load(fh)
                break

        elif command=='new':
            print(r'Please write the full path where to create file. Example: "d:\test\book.txt":')
            path=str(input())
            book=AddressBook()
            break
            

        elif command=='exit' or command=='esc' or command=='close':
            esc=False
            break
        else:
            print('Wrong command.')

    while esc_e:
        user_input=input('What do you want to do? Type "help" for additional commands.\n')
        result=handler(user_input)
        if result:
            print(result)
        elif result==None:
            pass
        else:
            break
 



@error_handler
def add():
    global esc_e, book
    print('Input Name:')
    name=Name(str(input()))
    record1=Record(name)
    esc=True
    while True:
        print('Do you want to add phone-number? "y" (YES) or n (NO). Type "exit" to exit')
        decicion=str(input())
        decicion=decicion.lower()
        if decicion=='y' or decicion=='yes':
            print('Input Phone Number. Example: +380501234567')
            phone=str(input())
            record1.add_phone(phone)
        elif decicion=='exit' or decicion=='esc' or decicion=='close':
            esc_e=False
            break
        elif decicion=='n' or decicion=='not':
            break
    while esc:
        print('Do you want to add Birthday? "y" (YES) or n (NO). Type "exit" to exit')
        decicion=str(input())
        decicion=decicion.lower()
        if decicion=='y' or decicion=='yes':
            print('Input Birthday. Expected day.month.year(Example:25.12.1970)')
            birthday=str(input())
            record1.user['Birthday']=birthday
            book.add_record(record1.user)
            esc=False
            say='Successfully changed'
            return say

        elif decicion=='exit' or decicion=='esc' or decicion=='close':
            book.add_record(record1.user)
            esc_e=False
            return 'close'
            
        elif decicion=='n' or decicion=='not':
            book.add_record(record1.user)
            say='Successfully changed'
            return say

    
@error_handler     
def change():
    global book, esc_e
    print('To change name: type "name", to change phone: type "phone", to change birthday: type "birthday"')
    decicion=str(input())
    decicion=decicion.lower()
    if decicion=='name':
        print('Type name you want to change')
        old_name=str(input())
        old_name=old_name.lower()
        print('Type new name')
        new_name=str(input())
        for i in book:
            if i['Name'].lower()==old_name:
                i['Name']=new_name
                say='Successfully changed'
                return say
            else:
                print(f'{old_name} not in Adress Book')
                    
    elif decicion=='phone':
        print('Type phone you want to change')
        old_name=str(input())
        print('Type new phone')
        new_name=str(input())
        for i in book:
            for j in i['Phones']:
                if j==old_name:
                    i['Phones'].remove(j)
                    i['Phones'].append(new_name)
                    say='Successfully changed'
                    return say
            else:
                print(f'{old_name} not in Adress Book')
    elif decicion=='birthday':
        print('Type birthday you want to change. Expected day.month.year(Example:25.12.1970)')
        old_name=str(input())
        print('Type new birthday. Expected day.month.year(Example:25.12.1970)')
        new_name=str(input())
        for i in book:
            if i['Birthday']==old_name:
                i['Birthday']=new_name
                say='Successfully changed'
                return say
            else:
                print(f'{old_name} not in Adress Book')
                
    elif decicion=='exit' or decicion=='esc' or decicion=='close':
        esc_e=False
        return esc_e
        
@error_handler    
def find():
    global path, book
    print('Put information you want to find')
    find_v=str(input())
    result=book.find_value(find_v)
    return result  
def exit():
    global esc_e
    save()
    esc_e=False
    return "Good Bye"

def save():
    global path, book
    with open(path, 'wb') as fh:
        pickle.dump(book, fh)
        #return 'Successfully saved'

@error_handler
def show():
    #counter=0
    print(79*'_')
    print('|                  Name                   |       Phones         |  Birthday  |')
    print(79*'_')
    for i in book:
        print(f'| {i["Name"]:<40}| { i["Phones"][0] if len(i["Phones"])>=1 else " ":<20} | {i["Birthday"]if i["Birthday"] else " ":<11}|')
        if len(i["Phones"]) > 1:
            for elem in i["Phones"][1:]:
                print(f'|                                         | {elem: <20} |            |')
        
        #counter+=1
        print(79*'_')
     

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


if __name__ =='__main__':
    main()
    
ANSWEARS={'add': add, 'change': change, 'close': exit, 'exit': exit, 'find':find, 'help': help_func, 'save': save, 'show': show}    

       
