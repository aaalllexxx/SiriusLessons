from helpers import input


def __form_bage():
    strng = ("----------------\n"
             "Колледж Сириус\n"
             "Имя: ____\n"
             "Группа: ____")
    return strng


def __get_discount(points):
    if 0 <= points <= 45:
        return 10
    elif 50 <= points <= 99:
        return 15
    return 200


def __get_message_by_points(points):
    return "Вы допущены" if points >= 50 else "Вы отчислены"


def task1():
    """
    Напишите программу печатающую бейджики учеников.
    Программа запрашивает ввод числа учеников и печатает каждому бейджик. Бейдж содержит название учебного заведения:
    «Колледж Сириус», поле для имени:
    «Имя: ____» и поле для школы:
    «Группа: ____». Напиши программу, печатающую бейджики студентов как на картинке. В завершении программа должна печатать:
    «Готово! Заберите бейджики.»
    Функция должна принимать имя и группу ученика.
    """
    count = int(input("Введите кол-во студентов: "))
    for i in range(count):
        print(__form_bage())
    print("Готово! Заберите бейджики.")


def task2():
    """
    Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
    Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
    — от 0 до 49 баллов — «Скидка 10%»;
    — от 50 до 99 баллов — «Скидка 15%»;
    — от 100 баллов и выше — «Скидка 20%».

    Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
    """
    print(f"Ваша скидка: {__get_discount(int(input('ВВедите количество баллов: ')))}%")


def task3():
    """
    Напишите программу определяющую допуск ученика к зачету.
    Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
    и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

    Ученикам без допуска должно печататься "Вы отчислены".

    Выдачу допуска реализуй как функцию.
    """
    count = int(input("Введите коли чество учеников: "))
    for i in range(count):
        print(__get_message_by_points(int(input("Введите количество баллов за тест: "))))
