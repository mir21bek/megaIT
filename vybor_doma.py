raion = input('Введите название района:').lower()
uchastok = int(input('Введите плошадь участка:'))
price = int(input('Введите сумму:'))
karkas = input('Дом из кирпича или из пескоблока?').lower()
if raion == 'ортосай' or raion == 'байтик' or raion == 'чон арык':
    raion == raion
if uchastok <= 4:
    if price <= 50000:
        if karkas == 'кирпич':
            print('мы нашли для вас дом')
            print(f'Район:', raion, 'Участок:', uchastok, 'Цена:', price, 'Стена:', karkas)
    elif uchastok <= 5 and price <= 45000 and karkas == 'Пескоблок':
        karkas == karkas
        print(f'Участок:', uchastok, 'Цена:', price, 'Стена:', karkas)
else:
    print('Дом по вашему запросу не найдено!')
