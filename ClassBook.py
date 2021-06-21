import pickle
import re
from collections import UserList
from datetime import datetime, timedelta, date


class Field:
    def __init__(self, value):
        self.__value = value
        # self.value=value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class AddressBook(UserList):

    data = []

    def add_record(self, record):
        self.data.append(record)

    def find_value(self, f_value):
        f_value = f_value.lower()

        result = []
        for i in self:
            for value in i.values():
                if (isinstance(value, str)):
                    value = value.lower()
                    if value.find(f_value) != -1:
                        if i not in result:
                            result.append(i)
                            break
                elif value != None:
                    if (isinstance(value, list)):
                        for j in value:
                            j = j.lower()
                            if j.find(f_value) != -1:
                                result.append(i)
                                break
        return result

    def iterator1(self, n):
        counter = 0
        result = ""
        for i in self:
            # записываем в result строку которая содержит описание 1 контакта (Record) c AdressBook
            #  взято с Володи кода
            # Именно 'этот кусочек надо редактировать чтобы добавить адрес и email
            
            result += f'|{i["Id"]:<5}| {i["Name"]:<25}| { i["Phones"][0] if len(i["Phones"])>=1 else " ":<15} | {i["Birthday"]if i["Birthday"] else " ":<11}|{i["Address"]if i["Address"] else " ":<30}|  {i["E-mail"]if i["E-mail"] else " ":<30}| {i["Tags"] if i["Tags"] else " ":<15}|\n'
            if len(i["Phones"]) > 1:
                for elem in i["Phones"][1:]:
                    result += f'|     |                          | {elem: <15} |            |                              |                                |                | \n'
            result += f"{145*'_'}\n"
            # конец записи строки с описанием 1 контакта
            counter += 1
            if counter == n:
                result = result.rstrip("\n")
                yield result
                result = ""
                counter = 0
        if result:
            result = result.rstrip("\n")
            yield result

#START OF CHANGING
class Address(Field):
    def __init__(self, address):
        self.address = address

class Tags(Field):
    def __init__(self, tags):
        self.tags = tags

class Id(Field):
    def __init__(self, id_n):
        self.id_n = id_n

class Email(Field):
    def __init__(self, email):
        self.email=email

class Birthday(Field):
    def __init__(self, value):
        self.__birthday = None
        self.birthday = value

    @ property
    def birthday(self):
        return self.__birthday.strftime('%d.%m.%Y')

    @ birthday.setter
    def birthday(self, birthday):
        try:
            self.__birthday = datetime.strptime(birthday, '%d.%m.%Y')
        except Exception:
            print("Incorrect format, expected day.month.year (Example:25.12.1970)")
    

class Record:
    def __init__(self, name, id_n, phones=None, birthday=None, address=None, email=None, tags=None ):
        self.id_n = id_n
        self.phones = []
        self.birthday = None
        self.address=None
        self.email=None
        self.tags=None
        self.user = {'Id': self.id_n, 'Name': name.name,
                     'Phones': self.phones, 
                     'Birthday': self.birthday, 
                     'Address':self.address, 
                     'E-mail':self.email, 
                     'Tags':self.tags}
#Start to add


    def add_address(self, address):
        self.address = address

    def add_email(self, email):
        self.email = email

    def add_id(self, id_n):
        self.id_n = id_n
    
    #End       
    def add_phone(self, phone):
        phone = str(phone)
        try:
            num = re.fullmatch('[+]?[0-9]{3,12}', phone)
            if num:
                self.phones.append(phone)
        except:
            print('Phone must start with + and have 12 digits. Example +380501234567 ADD')

    

    def remove_phone(self, phone):
        for i in range(len(self.phones)):
            if self.phones[i].phone == phone:
                self.phones.pop(i)

    def edit_phone(self, phone, new_phone):
        self.remove_phone(phone)
        self.add_phone(new_phone)


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        phones = []
        self.phones = list()
        self.__phone = phone

    @ property
    def phone(self):
        return self.__phone

    @ phone.setter
    def phone(self, value):
        self.__phone = ''
        if re.fullmatch('[+]?[0-9]{3,12}', value):
            self.__phone = value
        else:
            print(
                'Phone must start with + and have 12 digits. Example +380501234567')

    # def __str__(self):
        # return self.phone
    def __repr__(self):
        return self.phone
