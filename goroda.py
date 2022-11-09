data = {'city': []}
while True:
    choice = int(input('добавить новый город (1), Отобразить список городов (2), \
заменить город (3), удалить город (4), выход (5)'))
    if choice == 1:
        print('Новый город:')
        city = input('Добавить новый город')
        if city not in data['city']:
            data['city'].append(city)
            print('город добавлен')
        else:
            print('такой город уже есть!')
    if choice == 2:
        print('отобразить список городов')
        print(data)
    if choice == 3:
        actual_city = input('Введите название текущего город')
        new_city = input('Введите название нового города')
        if actual_city in data['city']:
            data['city'].remove(city)
            data['city'].append(new_city)
            print('Город заменен!')
            if actual_city not in data['city']:
                print('Такой город отсуствует')
            elif new_city in data['city']:
                print(f'Такой город уже есть: {city}')
        else:
            print('некоректное название')
    if choice == 4:
        print('удалить город:')
        name_city = input('Введите название города')
        if name_city in data['city']:
            data['city'].remove(city)
            print('Город удален!')
        elif name_city not in data['city']:
            print('Такой город отсуствует')
        else:
            print('Некоректное название!')
    if choice == 5:
        print('До свидание!')
        break
