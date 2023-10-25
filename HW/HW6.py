from helpers import input


def task1():
    """
    Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
    """
    print({i: i ** 3 for i in range(1, 11)})


def task2():
    """
    Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
    а в качестве значения количество этих цифр в строке
    """
    numbers = "0139412831055230677798"
    print({i: numbers.count(i) for i in numbers})


def task3():
    """
    Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
    не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
    """
    res = {}
    while (a := input("Введите информацию в формате: место в чарте, исполнитель, название: ")).lower() != "off":
        data = [i.strip() for i in a.split(",")]
        res[(data[0], data[1])] = data[2]
    print(res)


def task4():
    """Создайте словарь с количеством элементов не менее 5-ти.
    Поменяйте местами первый и последний элемент объекта.
    Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
    Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
    """
    dictionary = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
    dictionary[1], dictionary[6] = dictionary[6], dictionary[1]
    del dictionary[2]
    dictionary["new_key"] = "new_value"
    print(dictionary)


def task5():
    """
    Дан словарь email-адресов студентов, в качестве ключа используется домен, а в качестве значения список имен.
    Необходимо вывести все email-адреса в формате Имя@домен.
    """
    emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
              'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
              'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
              'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
              'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
              'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
    for domain in emails:
        for name in emails[domain]:
            print(f"{name}@{domain}")
