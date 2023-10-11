"""Домашка с циклами"""
from helpers import input


def task1():
    for _ in range(3):
        input("Введите музыкальное предпочтение: ")
        print("Предпочтение учтено.")
    print("Система рекомендаций настроена!")


def task2():
    print("Команды: game, off")
    com = input("Введите команду: ")
    while com != "off":
        if com == "game":
            for i in range(3):
                number = int(input("Введите число: "))
                if number == 5:
                    print("Вы виграли билеты на концерт!")
                    break
        com = input("Введите команду: ")


def task3():
    bad_symb = "=?*^$№@_ "
    resp = []
    login = input("Введите логин: ")
    for symb in bad_symb:
        if symb in login:
            resp.append(symb)
    print(f'Запрещённые символы: {", ".join(resp)}')


def task4():
    while True:
        response = input("Введите отзыв или off: ")
        if response == "off":
            print("Система предпочтений настроена")
            break
        print("Спасибо, ваш отзыв принят!")


def task5():
    sale_percent = 5
    amount = 1
    while amount:
        amount = int(input("Введите стоимость без скидки: "))
        if amount:
            print(f"Стоимость со скидкой: {amount * (1 - sale_percent * 0.01)}")


def task6():
    buy_sum = 0
    while (amount := int(input("Введите цену товара: "))) != 0:
        buy_sum += amount
    if buy_sum % 2 == 0:
        while buy_sum % 2 == 0:
            buy_sum /= 2
    else:
        buy_sum = 0.85 * buy_sum

    print(f"К оплате: {buy_sum}")
