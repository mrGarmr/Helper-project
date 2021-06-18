from collections import UserList


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

###################################################################
# команды для handler - наверное надо перенести в основной модуль.
# После переноса раскомментировать @error_handler
# Я тестила: перенесла в основной модуль, добавила @error_handler,
# и все функции NotesBook заработали
###################################################################


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


# @error_handler
def delete_note():
    print("Please input a hashtag of note that you would like to delete:")
    hashtag = input().upper()
    notes_book.delete_note(hashtag)
    return f"The note with hashtag '{hashtag}' is deleted"


# @error_handler
def edit_note():
    print("Please input a hashtag of note that you would like to edit:")
    hashtag = input().upper()
    notes_book.edit_note(hashtag)
    return "The note is edited"


# @error_handler
def find_note():
    print('Please input keyword for search:')
    keyword = input().upper()
    print('THE RESULTS OF SEARCH:')
    print(notes_book.find_note(keyword))
    return "The search is sucessfully finished"


# @error_handler
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


# @error_handler
def show_notes():
    print('Your Notes Book:')
    print(notes_book)
    return "The end of Notes Book"


def notes_main():
    # техническая функция для проверки работы модуля, можно удалить
    global notes_book
    notes_book = NotesBook()

    print(add_note())
    print(add_note())
    # print(find_note())
    # print(sort_notes())
    # print(delete_note())

    print(edit_note())
    print(show_notes())


if __name__ == '__main__':
    notes_main()
