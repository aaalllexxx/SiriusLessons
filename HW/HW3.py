"""Домашка с условными операторами"""
from helpers import input


def task1():
    eating = input("Введите приём пищи: ").lower()
    if eating == "завтрак":
        print("Рекомендую вам кашу.")
    else:
        confirm = input("Вы хотите плотно поесть? [да/нет]: ").lower()[0]
        if confirm == "д":
            print("Рекомендую плов.")
        else:
            print("Рекомендую котлету с пюре.")


def task2():
    amount = float(input("Введите сумму к оплате: "))
    buy_hour = int(input("Введите текущий час: "))
    if buy_hour < 8 or buy_hour > 22:
        print("Мы закрыты(")
        return
    if 10 <= buy_hour <= 12:
        amount /= 2
    elif 20 <= buy_hour <= 22:
        amount /= 4
    print(f"К оплате: {amount} Р")


def task3():
    amounts = []
    state = 0
    for i in range(3):
        inp = int(input("Введите цену: "))
        if amounts:
            if inp > amounts[-1] and state >= 0:
                state = 1
            elif inp < amounts[-1] and state <= 0:
                state = -1
            else:
                state = 10
        amounts.append(inp)
    if state == 1:
        print(f"Акция!\nК оплате: {sum(amounts) / 2}")
    elif state == -1:
        print(f"Акция!\nК оплате: {sum(amounts) / 3}")
    else:
        print(f"К оплате: {sum(amounts)}")


def task4():
    category = input("Введите категорию товара: ").lower()
    if category == "продукты":
        amount = int(input("Введите цену: "))
        if amount < 100:
            print("Попробуйте нашу выпечку!")
        elif 100 <= amount < 500:
            print("Как насчёт орехов вшоколаде?")
        else:
            print("Попробуйте экзотические фрукты!")
    else:
        print("Загляните в товары для дома!")


def task5():
    a = int(input("Введите число: "))
    a1 = a
    last = a % 10
    all_sum = 0
    while a > 0:
        all_sum += a % 10
        a //= 10
    if last % 2 == 0 and all_sum % 3 ==0:
        print(f"Число {a1} делится на 6 без остатка.")
        return
    print(f"Число {a1} не делится на 6 без остатка.")

