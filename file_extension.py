# print('Расширение файла')

file_name = input('напишите расширение файла')
if file_name[-3:] == 'png' or file_name[-3:] == 'txt' or file_name[-3:] == 'mp3':
    print(f'Файл с таким расширением {file_name[-3:]} найдено.')
else:
    print('Файл с таким расширением не найдено')