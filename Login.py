name = input('Введите Имя:')
surname = input('Введите Фамилию:')
login = input('Введите логин:')
password = input('Введите пароль:')
password2 = input('Введите пароль повторно:')
if password == password2:
    print('Добро пожаловать!', name, surname)
else:
    print('Пароль не правилный!')