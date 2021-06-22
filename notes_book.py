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
        # for note in self:
        #     result += note[0]+"\n" + note[1]+"\n"

        # Печать шапки с названием столбцов
        result += f"{62*'_'} \n"
        result += '|           TAGS           |             NOTE                 |\n'
        result += f"{62*'_'} \n"
        for note in self:
            result += f'|{note[0]:<26}| {note[1]:<26}|\n'
        return result


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