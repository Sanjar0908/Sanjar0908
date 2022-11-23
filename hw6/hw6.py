# У вас есть файл MOCK_DATA.txt, в котором 1000 строк с данными (Имя и
# Фамилия, емайл, название файла с расширением и код цвета)
# 1. Написать программу, где отображается меню с опциями: 1 - Считать имена и фамилии, 2
# - Считать все емайлы, 3 - Считать названия файлов, 4 - Считать цвета, 5 - Выход
# 2. При выборе опции меню необходимо считать соответствующую информацию из файла с
# данными при помощи регулярных выражений и сохранить считанные данные в новый
# файл.
# 3. Если пользователь выбирает пункт в меню 1: считываются все имена и фамилии (1000
# строк) и сохраняются в файл под названием names.txt. Если пользователь выбирает пункт в
# меню 2: считываются все емайлы (1000 строк) и сохраняются в файл под названием
# emails.txt и тд.
# 4. До тех пор пока пользователь не выбрал пункт 5 программа работает и предлагает
# опции меню.
# 5. При повторном выборе какого-то из пунктов меню, существующий файл с данными,
# например names.txt - полностью перезаписывается.


import re
while True:
    with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    user_input = input("1 - Считать имена и фамилии, \n"
                       "2 - Считать все емайлы, \n"
                       "3 - Считать названия файлов, \n"
                       "4 - Считать цвета, \n"
                       "5 - Выход\n")
    if user_input == "4":
        colors = re.findall(r"#[0-9A-Fa-f]+", content)
        with open("colors.txt", 'w', encoding='utf-8') as file:
            print('посмотрите в файл colors.txt')
            for color in colors:
                file.write(f"{color}\n")


    elif user_input == "1":
        full_name_mock = re.findall(r"\b[A-Z][A-Za-z-]+\s[A-Za-z\' ]+\b\s", content)
        with open("names.txt", "w", encoding='UTF-8') as file:
            print('посмотрите в файл names.txt')
            for i in full_name_mock:
                file.write(f"{i}\n")

    elif user_input == "2":
        emails = re.findall(r"\b([\w\-]+)(@)[\w]+(\.[\w]+)+", content)
        with open("emails.txt", "w", encoding='UTF-8') as file:
            print('посмотрите в файл emails.txt')
            for i in emails:
                file.write(f"{i}\n")

    elif user_input == "3":
        file_name_mock = re.findall(r"\t[A-Za-z][a-zA-Z]+\.[a-z]+", content)
        with open("file_names.txt", "w", encoding='UTF-8') as file:
            print('посмотрите в файл file_names.txt')
            for i in file_name_mock:
                file.write(f"{i[1:]}\n")
    elif user_input == "5":
        print("пока!")
        break
