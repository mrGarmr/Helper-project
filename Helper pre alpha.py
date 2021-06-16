import pickle
import re
from collections import UserList
from datetime import datetime,timedelta,date

class Field:
    def __init__(self,value):
        self.__value=value
        #self.value=value
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self,new_value):
        self.__value=new_value

class AddressBook(UserList):
    
    data = []
    
    def add_record(self, record):
        self.data.append(record)
    
    def find_value(self,f_value):
        #f_value=str(f_value)
        f_value=f_value.lower()

        result=[]
        for i in self:
            for value in i.values():
                if (isinstance(value, str)):
                    value=value.lower()
                    if value.find(f_value)!=-1:
                        result.append(i)
                elif value!=None:
                    if (isinstance(value, list)):
                        for j in value:
                            j=j.lower()
                            if j.find(f_value)!=-1:
                                result.append(i)                  
                        
        return result
                    
        
    def iterator(self,n=2):
        f=1
        k = 0
        result=[]
        while k < n:

            result=self.data[k:f]
            k += 1
            f+=1
            if result:
                yield result
            else:
                break
    
class Birthday(Field):
    def __init__(self,value):
        self.__birthday = None
        self.birthday=value
        
    @property
    def birthday(self):
        return self.__birthday.strftime('%d.%m.%Y')
        

    @birthday.setter
    def birthday(self, birthday):
        try:
            self.__birthday = datetime.strptime(birthday, '%d.%m.%Y')
        except Exception:
            print("Incorrect format, expected day.month.year (Example:25.12.1970)")

class Record:
    def __init__(self,name,phones=None, birthday=None):
        #self.name = name
        self.phones = []
        self.birthday = None
        self.user = {'Name': name.name, 'Phones': self.phones, 'Birthday': self.birthday}
        
    def add_phone(self, phone):
        phone=str(phone)
        try:
            num=re.match('[+]?[0-9]{12}', phone)
            if num:
                self.phones.append(phone)
        except:
            print('Phone must start with + and have 12 digits. Example +380501234567 ADD')          
    
    def days_to_birthday(self):
        if self.birthday:
            today_d = datetime.now().date()
            bday=datetime.strptime(self.birthday,"%d.%m.%Y").date()
            bday=date(today_d.year,bday.month,bday.day)
            if today_d>bday:
                bday=date(today_d.year+1,bday.month,bday.day)
                days_left=(bday-today_d)
            else:
                days_left=(bday-today_d)
            return days_left.days
        
    def remove_phone(self,phone):
        for i in range(len(self.phones)):
            if self.phones[i].phone == phone:
                self.phones.pop(i)
    
    def edit_phone(self,phone,new_phone):
        self.remove_phone(phone)
        self.add_phone(new_phone)


class Name(Field):
    def __init__(self,name):
        self.name=name
        
class Phone(Field):
    def __init__(self,phone):
        phones=[]
        self.phones =list()
        self.__phone=phone
        
    @property  
    def phone(self):
        return self.__phone
    @phone.setter    
    def phone(self,value):
        self.__phone=''
        if re.match('[+]?[0-9]{12}',value):
            self.__phone=value
        else:
            print('Phone must start with + and have 12 digits. Example +380501234567 SETT')          
    
    #def __str__(self):
        #return self.phone
    def __repr__(self):
        return self.phone

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
        
ANSWEARS={'add': add, 'change': change, 'close': exit, 'exit': exit, 'find':find, 'help': help_func, 'save': save, 'show': show}    

if __name__ =='__main__':
    main()
       
        


        
        
