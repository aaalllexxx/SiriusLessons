"""Домашка со списками"""
from helpers import input


def task1():
    games = []
    while (game := input("Введите игру: ")) != "0":
        if game not in games:
            games.append(game)
        else:
            print("Эта игра уже записана.")
    print(sorted(games))


def task2():
    str_marks = input("Введите оценки через пробел: ").split()
    marks = [int(mark) for mark in str_marks]
    marks_count = []
    valuable_sum = 0
    for i in range(5):
        marks_count.append(c := marks.count(i + 1))
        if i + 1 >= 3:
            valuable_sum += c
    grade = valuable_sum / len(marks) * 100
    print(f"Список оценок: {', '.join(str_marks)}")
    marks_count = [str(i + 1) + ': ' + str(marks_count[i]) for i in range(len(marks_count))]
    print(f"Список количества оценок: {', '.join(marks_count)}")
    print(f"Успеваемость: {grade}")


def task3():
    str_marks = input("Введите оценки через пробел: ").split()
    marks = [int(mark) for mark in str_marks]
    fives = marks.count(5)
    fives_percent = fives / len(marks) * 100
    print(f"Кол-во оценок 5: {fives}")
    print(f"Процент оценок 5: {fives_percent}%")


def task4():
    data = []
    while (lastname := input("Введите фамилию преподавателя: ")) != "0":
        place = input("Введите должность: ")
        count = [int(c) for c in input("Введите кол-во студентов в группах через пробел: ").split()]
        data.append([lastname, place, count])
        print(data)


def task5():
    nums = [int(c) for c in input("Введите числа через пробел: ").split()]
    if len(nums) <= 1:
        print("Нет")
        return
    diff = nums[1] - nums[0]
    for i, num in enumerate(nums):
        if i == 0:
            continue
        if nums[i] - nums[i - 1] != diff:
            break
    else:
        print("Да")
        return
    print("Нет")
