"""Домашка со строками"""
from helpers import input


def task1():
    print(input("Введите строку:") + input("Введите строку:"))


def task2():
    print("r" * int(input("Введите кол-во повторений: ")))


def task3():
    inp_string = input("Введите строку: ")
    print(inp_string[::-1])
    print("".join([inp_string[(len(inp_string)) - i - 1] for i in range(len(inp_string))]))


def task4():
    print(" ".join(reversed(input("Введите два числа: ").split())))


def task5():
    print(input("Введите почту: ").split("@")[0])


def task6():
    print(input("Введите номер телефона: ")[2:5])


def task7():
    name = input("Введите имя: ").split()
    print(f"{name[0]} {name[1][0]}. {name[2][0]}.")


def task8():
    text = input("Введите текст: ")
    print(text.replace("ический", ".").replace("ическая", "."))


def task9():
    text = input("Введите текст: ")
    print(text.replace("--", "——"))


def task10():
    phone = input("Введите телефон: ")
    phone = phone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
    print(phone)


def task11():
    phone = input("Введите телефон: ")
    phone = f'<a href="tel:{phone}">{phone}</a>'
    print(phone)


def task12():
    amount = input("Введите тег: ")
    amount = amount.replace("<span>", "").replace("</span>", "")
    amount = amount.replace("&nbsp;", "").replace("P", "").replace("Р", "")
    print(amount)


def task13():
    adresses = [i for i in input("Введите текст: ").split() if "@" in i]
    for address in adresses:
        print(address)
