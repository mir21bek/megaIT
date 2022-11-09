car_name = input('Введите название машины:').lower()
year = int(input('Введите год выпуска:'))
miles = int(input('Введите пробег:'))
colors = input('Введите цвет машины:').lower()
rul = input('Введите положение руля:').lower()
owner = int(input('Введите число хозяев:'))
price = int(input('Введите цумму:'))
if car_name == 'lexus' or car_name == 'toyota' and year >= 2004 and miles == 150000:
    if colors == 'white' or colors == 'grey' and rul == 'left' and owner <=2 and price <= 10000:
        print('Мы нашли машину по вашему параметру!')
    else:
        print('Мы не нашли машину по вашему параметру!')
elif car_name == 'lexus' or car_name == 'toyota' and year >= 2004 and miles == 200000:
    if colors == 'white' or colors == 'grey' and rul == 'lef' and owner <= 2 and price <= 8000:
        print('Мы нашли для вас машину.')
else:
    print('Мы не нашли подходящюю машину для вас.')