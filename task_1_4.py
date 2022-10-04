database = {'Max': [1563, True], 'Leo': [2567, False], 'Mark': [4545, True], 'Tor': [2153, False], 'Den': [1211, True]}
login = input('введите login: ')
password = int(input('Введите пароль: '))

def check_login_1(login, password):
    """Функция производит аутентификацию пользователей системы
       Сложность: O(n).
       """
    dev_list = []                                                            #O(n)
    for k, v in database.items():                                            #O(n)
        if login == k and password == v[0] and v[1] == True:                 #O(1)
            print('Доступ разрешен')                                         #O(1)
        elif login == k and password == v[0] and v[1] == False:              #O(1)
            print('Ваша учетная запись не активирована')                     #O(1)
            activate = input('Активировать вашу учетную запись да/нет: ')    #O(1)
            if activate == 'да':                                             #O(1)
                database[k] = [password, True]                               #O(1)
                print('Доступ разрешен')                                     #O(1)
            else:
                print('Доступ запрещен пока не активируете учетную запись')  #O(1)
        elif login == k and password != v[0]:                                #O(1)
            print('Вы ввели неправильный пароль, доступ запрешен')           #O(1)
        else:
            dev_list.append(1)                                               #O(1)
    if len(dev_list) == len(list(database.keys())):                          #O(n)
        print('Учетная запись не найдена')                                   #O(1)
# Итоговая сложность O(n) + O(n)(12 * O(1)) + O(n) + O(1) = O(n)


def check_login_2(login, password):
    """Функция производит аутентификацию пользователей системы
       Сложность: O(1).
       """
    if database.get(login) == None:                                           #O(1)
        print('Учетная запись не найдена')                                    #O(1)
    elif database.get(login)[0] == password:                                  #O(1)
        if database.get(login)[1] == True:                                    #O(1)
            print('Доступ разрешен')                                          #O(1)
        else:
            print('Ваша учетная запись не активирована')                      #O(1)
            activate = input('Активировать вашу учетную запись (да/нет): ')   #O(1)
            if activate == 'да':                                              #O(1)
                database.get(login)[1] == True                                #O(1)
                print('Ваша учетная запись активирована, доступ разрешен')    #O(1)
            else:
                print('Доступ запрещен, пока учетная запись не активирована') #O(1)
    else:
        print('Введен неправильный пароль, доступ запрещен')                  #O(1)

# Итоговая сложность 12 * O(1) = O(1)
# вывод : второе решение более эффективно, т.к. имеем константную сложность



check_login_2(login, password)

check_login_1(login, password)