
student_info = {}


surname = input("введи фамилию: ")
name = input("введи имя: ")
patronymic = input("введи отчество: ")
age = input("введи свой возраст: ")
class_number = input("введи свой класс: ")

student_info['фамилия'] = surname
student_info['имя'] = name
student_info['отчество'] = patronymic
student_info['возраст'] = age
student_info['класс'] = class_number

key = input("введи ключ: ")

if key in student_info:
    print(student_info[key])
else:
    print("такого ключа не существует")
