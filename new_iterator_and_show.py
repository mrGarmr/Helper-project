#мой итератор(вернее, списанный)

def iterator(self, n):
        if len(self.data) < n:
            raise IndexError()
        else:
            data_list = list(self.data.items())
            while data_list:
                result = '\n'.join(
                    [f'\n\tContact <{el[0]}> has following data:\
                        \n\tbirthday info - {list(el[1].items())[0][1]}\
                        \n\tphon/s - {"; ".join(list(el[1].items())[1][1])}' for el in data_list[:n]])
                yield result
                data_list = data_list[n:]

#твой с моим вмешательством

def iterator(self,n):
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
                yield result
                #тут, наверное, еще что-то нужно, завершающая строка

#тогда def show выглядит так   

@error_handler
def show():
    if book == []:
        print('Your phonebook is empty')
    else:
        n = int(input('How many records should I show at once? ')) #ну, или просто 
        result = book.iterator(n)
        return result
