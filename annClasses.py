#import pickle
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
        # f_value=str(f_value)
        f_value = f_value.lower()

        result = []
        for i in self:
            for value in i.values():
                if (isinstance(value, str)):
                    value = value.lower()
                    if value.find(f_value) != -1:
                        result.append(i)
                elif value != None:
                    if (isinstance(value, list)):
                        for j in value:
                            j = j.lower()
                            if j.find(f_value) != -1:
                                result.append(i)

        return result

    def iterator1(self, n):
        counter = 0
        result = ""
        for i in self:
            # записываем в result строку которая содержит описание 1 контакта (Record) c AdressBook
            #  взято с Володи кода
            # Именно 'этот кусочек надо редактировать чтобы добавить адрес и email
            result += f'| {i["Name"]:<40}| { i["Phones"][0] if len(i["Phones"])>=1 else " ":<20} | {i["Birthday"]if i["Birthday"] else " ":<11}| \n'
            if len(i["Phones"]) > 1:
                for elem in i["Phones"][1:]:
                    result += f'|                                         | {elem: <20} |            | \n'
            result += f"{79*'_'}\n"
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

    def iterator(self, n=2):
        f = 1
        k = 0
        result = []
        while k < n:

            result = self.data[k:f]
            k += 1
            f += 1
            if result:
                yield result
            else:
                break

    '''def iterator(self,n): #мой вариант, не провереный
        f=1
        k = 0
        result=[]
        while k < n:
            result=self.data[k:f]
            k += 1
            f+=1
            if result:
                print(79*'_')
                print('|                  Name                   |       Phones         |  Birthday  |')
                print(79*'_')
                for i in self.data: #или result?
                    print(f'| {i["Name"]:<40}| { i["Phones"][0] if len(i["Phones"])>=1 else " ":<20} | {i["Birthday"]if i["Birthday"] else " ":<11}|')
                    if len(i["Phones"]) > 1:
                        for elem in i["Phones"][1:]:
                            print(f'|                                         | {elem: <20} |            |')       
                    print(79*'_') 
                yield result'''


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
    def __init__(self, name, phones=None, birthday=None):
        # self.name = name
        self.phones = []
        self.birthday = None
        self.user = {'Name': name.name,
                     'Phones': self.phones, 'Birthday': self.birthday}

    def add_phone(self, phone):
        phone = str(phone)
        try:
            num = re.match('[+]?[0-9]{12}', phone)
            if num:
                self.phones.append(phone)
        except:
            print('Phone must start with + and have 12 digits. Example +380501234567 ADD')

    def days_to_birthday(self):
        if self.birthday:
            today_d = datetime.now().date()
            bday = datetime.strptime(self.birthday, "%d.%m.%Y").date()
            bday = date(today_d.year, bday.month, bday.day)
            if today_d > bday:
                bday = date(today_d.year+1, bday.month, bday.day)
                days_left = (bday-today_d)
            else:
                days_left = (bday-today_d)
            return days_left.days

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
        if re.fullmatch('[+]?[0-9]{12}', value):
            self.__phone = value
        else:
            print(
                'Phone must start with + and have 12 digits. Example +380501234567 SETT')

    # def __str__(self):
        # return self.phone
    def __repr__(self):
        return self.phone

class NotesBook(UserList):
    # список списков: список заметок, каждая заметка - список с 2 элементов:
    # заметка[0]-множество тєгов, заметка[1] - текст заметки

    def add_note(self, text, hashtag):
        # добавляет заметку в NotesBook
        note = [hashtag, text]
        self.append(note)

    def delete_note(self, hashtag):
        # удаляет заметку из NotesBook, которая имеет заметка[0]==hashtag
        for note in self:
            if note[0] == hashtag:
                self.remove(note)

    def edit_note(self, hashtag):
        # удаляет заметку из NotesBook, которая имеет заметка[0]==hashtag
        # редактирование заметки происходит построчно
        # помощник печатает строку для редактирование,
        # далее пользователь вводит строку, на которую надо заменить напечатанную строку.
        # Если пользователь ничего не ввел строка осталась без изменения
        for note in self:
            if note[0] == hashtag:
                # находим нужную заметку с заданным ключевым словом
                # изменяем текст заметки, который находится в  note[1]
                print('You would like to edit the following note:')
                print(note[1])

                lines = note[1].split('\n')
                counter = 0
                for line in lines:
                    print('Please edit:')
                    print(line)
                    new_line = input()
                    if new_line:
                        lines.pop(counter)
                        lines.insert(counter, new_line)
                    counter += 1
                note[1] = '\n'.join(lines)

    def find_note(self, keyword):
        # находит все заметки, в тэгах которых содержится keyword
        result = NotesBook()
        for i in self:
            if keyword in i[0]:
                result.append(i)
        return result

    def sort_notes(self, search_type="1"):
        # выводит список заметков в отсортированном виде
        # "1" - в алфавитном порядке
        # "2" - в обратном алфавитном порядке
        # "3" - от старых заметок к новым
        # "4" - от новых заметок к старым
        if search_type == "1":
            sorted_list = sorted(self)  # возвращает список
        elif search_type == "2":
            sorted_list = sorted(self)
            sorted_list.reverse()
        elif search_type == "3":
            sorted_list = list(self)
        elif search_type == "4":
            sorted_list = list(self)
            sorted_list.reverse()
        result = NotesBook()
        for note in sorted_list:
            result.append(note)
        return result

    def __str__(self):
        result = ""
        for note in self:
            result += note[0]+"\n" + note[1]+"\n"
        return result