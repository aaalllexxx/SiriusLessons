import math

from helpers import input


def task1():
    print(sum(range(16, 25)))


def task2():
    print(int(input("Введите первое число: ")) + int(input("Введите второе число: ")))


def task3():
    color = int(input("Введите цвет позитива: "))
    if 0 <= color <= 255:
        print(255 - color)
        return
    print("Цвет позитива должен быть меньше 255 и при этом неотрицательным")


def task4():
    input_list = [int(input("Введите число: ")) for _ in range(3)]
    print("sum:", sum(input_list), "max:", max(input_list), "min:", min(input_list))


def task5():
    print(f'Расстояние: {abs(int(input("Введите первое число: ")) - int(input("Введите второе число: ")))}')


def task6():
    rub_to_usd = float(input("Курс рубля к доллару: "))
    usd_to_eu = float(input("Курс доллара к евро: "))
    print("Курс евро к рублю:", round(1 / (rub_to_usd * usd_to_eu), 2))


def task7():
    print(f'Можно купить {1572 // int(input("Введите стоимость товара: "))} ед. товара.')


def task8():
    number = int(input("введите трёхзначное число: "))
    a, b, c = number // 100, number // 10 % 10, number % 10
    print("Сумма цифр:", a + b + c)


def task9():
    number = int(input("введите трёхзначное число: "))
    a, b, c = number // 100, number // 10 % 10, number % 10
    print("Развёрнутое число:", c * 100 + b * 10 + a)


def task10():
    start_time = 1970
    inp = int(input("Введите дату в UNIX формате: ")) // 365 // 24 // 60 // 60
    print(inp + start_time)


def task11():
    print(round(int(input("Введите массу: ")) / (int(input("Введите рост: ")) / 100) ** 2, 2))


def task12():
    width = float(input("введите ширину: "))
    height = float(input("введите длину: "))
    paint_spent = int(input("введите расход краски: "))
    paint_v = int(input("введите объём банки краски: "))
    percent = int(input("введите процент запаса: "))
    s = width * height
    required_v = s / paint_spent * (1 + percent / 100)
    bottles_number = math.ceil(required_v / paint_v)
    left = paint_v * bottles_number - required_v
    print(f"Площадь покраски: {round(s, 2)} м^2")
    print(f"Необходимый объём краски: {round(required_v, 2)} л")
    print(f"Необходимое кол-во банок: {bottles_number} шт")
    print(f"После покраски останется: {round(left, 2)} л")

