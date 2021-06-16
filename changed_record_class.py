class Record:
    def __init__(self,name,phones=None, birthday=None, address=None, email=None, remark=''):
        self.name = name
        self.phones = []
        self.birthday = None
        self.user = {'Name': name.name, 'Phones': self.phones, 'Birthday': self.birthday}
        self.address = None
        self.email = None
        self.remark = ''

    def add_address(self, address):
        self.address = address

    def add_email(self, email):
        self.email = email

    def add_remark(self, remark):
        self.remark = remark

    def show_birthday_peaple(self):
        n = int(input('Enter the number of days: '))
        current_day = datetime.now()
        days_interval = timedelta(days=n)
        fun_day = current_day + days_interval
        contacts_list = []
        for self.name in self.data:
            info_list = self.data.get(self.name)
            if self.birthday in info_list:
                date_birthday = datetime.strptime(self.birthday, "%d-%m-%y")
                if date_birthday == fun_day.date():
                    contacts_list.append(self.name)
         result = print(contacts_list)
         return result