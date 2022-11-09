money = 0
transaction = 0
while transaction < 6:
    print(f'{transaction +1} Транзакция')
    input_money = int(input())
    if 0 < input_money <= 100:
        if money + input_money <= 100:
            money += input_money
            transaction += 1
    else:
        print(f'Не вместится! В копилке {money} сомов!')
        continue
    if money <= 100:
        print(f'ПОздравляю! вы нокопили {money} сомов!')
    else:
        print(f'Копилка не вмешает в себя больше чем 100 сом!')
    if money == 100: 
        print(f'Поздравляю! вы накопили желаеммую сумму!')
        break #Останавливается когда набирается нужная сумма