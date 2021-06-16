class Address(Field):
    def __init__(self, address):
        self.address = address


class Email(Field):
    def __init__(self, email):
        self.email = email

    @property
    def value(self):
        return self.__email

    @email.setter
    def value(self, value):
         if re.match('([a-zA-Z][a-zA-Z0-9\._!#$%^*=\-]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,})', value):
             self.__email = value
        else :
            print('Format is wrong. Try again')