# import random
# import os
# import string
# import platform
# import sys
# import my_modul
'''
Внутри my_module.py создайте вызваннную print которая выводит текст
"Я функция из my_module.py".
А затем импортируйте my_module.py в другой файл.
'''
# my_modul.print_hello()


'''
Вам дан список имён names = ["Aibek", "Joomart", "Adinai", "Ermek",
    "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek",
    "Alymbek", "Dastan", "Maksat"]
    и вытащите 4 рандомных имени оттуда и сохраните в другой список.
'''
# # print(sys.platform)
# print(platform.system)
# name = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat",\
#      "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# num = 4
# new_name = []
# a = random.SystemRandom().sample(name,num)
# new_name.append(a)
# print(new_name)

'''
Через Python у себя на рабочем столе создайте директорию,\
    а внутри дериктории создайте 5 РАНДОМНЫХ файлов.
'''
# list_of_randoms = [random.randrange(1000) for i in range(5)]
# path_to_desktop = '/home/user/Desktop/Megacom/First-month1'
# os.mkdir(path_to_desktop+'new')
# for name in list_of_randoms:
#     with open(path_to_desktop+'new/'+str(name), 'wt', encoding='UTF-8') as file:
#         file.write(''.join([random.choice(string.ascii_letters) for i in range(10)]))

'''
Возьмите список имён из задания №2 и сформируйте 4 разные команды из всех участников.
'''
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat",\
#          "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# A = 3
# B = 4
# sunshine = []
# sunset = []
# koshuna = []
# taanysh = []
# num1 = random.SystemRandom().sample(names, A)
# num2 = random.SystemRandom().sample(names, A)
# num3 = random.SystemRandom().sample(names, A)
# num4 = random.SystemRandom().sample(names, B)
# sunshine.append(num1)
# sunset.append(num2)
# koshuna.append(num3)
# taanysh.append(num4)
# print(sunshine)
# print(sunset)
# print(koshuna)
# print(taanysh)