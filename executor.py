"""Лучше запускать через терминал(можно через терминал пайчарма), а не значком запуска"""
import sys
import time
from ast import literal_eval
from importlib import import_module
import os
from helpers import get_temp, set_temp, end_task
import tracemalloc as tl
import shutil

term_size = shutil.get_terminal_size()[0]  # размер терминала

hw_number = -1
set_temp("INPUT_TIME", 0)
homeworks = [i.split(".")[0] for i in os.listdir("HW")]

CLEAR = '\x1b[1A\x1b[2K'


def clear():
    sys.stdout.write(CLEAR)


def run_task(module, task_name):
    """Запуск задачи из модуля"""
    func = module.__getattribute__(task_name)  # импорт задачи
    print("Выполняется...")
    print(f"\n{'-' * term_size}\n")
    start_time = time.time()  # начало отсчёта времени
    tl.start()  # старт мониторинга памяти
    func()  # запуск задачи
    memory = tl.get_traced_memory()  # получение памяти
    tl.stop()  # остановка мониторинга памяти
    input_time = get_temp("INPUT_TIME")  # получение времени ввода данных
    print(f"\n{'-' * term_size}\n")  # разделитель
    print(f"Выполнено за {time.time() - start_time - input_time} секунд.")
    print(f"Пиковый расход памяти: {memory[1]} bytes")
    end_task()  # окончание задачи


def task_input(module):
    tasks = sorted([i for i in dir(module) if i.startswith("task")],
                   key=lambda x: int(x.strip("task")))  # получение спика заданий из модуля
    print("Доступные задания:")
    for i in tasks:
        print(f"\t{i}")
    task_name = input("\nВведите название или номер задания: ")
    if isinstance(literal_eval(task_name), int):  # если введено просто число, то приписываем его к task
        task_name = f"task{task_name}"
    return task_name


print("Введите h, чтобы посмотреть список доступных домашних заданий.")
print("Введите 0, чтобы выйти.")
print("id задания - строка в формате номер файла и номер задания через знак '_'.")
print("Пример id задания: 1_1 (1 дз 1 задание), 15_12 (15 дз 12 задание).\n")

while hw_number != 0:
    task_id = input(f"Введите название файла с дз, номер дз и ли id задания: ")
    try:
        # если в данных нет "_" то пробуем преобразовать в другой тип данных
        task_id = literal_eval(task_id) if not "_" in task_id else task_id
    except ValueError:
        pass
    try:
        if task_id == "h":
            print("\nСписок доступных домашних заданий:")
            for el in homeworks:
                if not el.startswith("_"):  # отфильтровываем файлы и папки по типу __pycache__
                    print(f"\t{el}")
        elif task_id == 0:
            break

        elif isinstance(task_id, int):
            module_path = f"HW.HW{task_id}"
            module = import_module(module_path)
            task = task_input(module)  # ввод задачи
            run_task(module, task)  # запуск задачи

        elif "_" in task_id:
            ids = task_id.split("_")  # разделить данные по "_"
            module_path = f"HW.HW{ids[0]}"
            module = import_module(module_path)
            task_name = f"task{ids[1]}"
            run_task(module, task_name)  # запуск задачи

        elif task_id in homeworks:
            module_path = f"HW.{task_id}"
            module = import_module(module_path)
            task = task_input(module)  # ввод задачи
            run_task(module, task)  # запуск задачи
    except ModuleNotFoundError:
        print(f"\n{'-' * term_size}\n")
        print("Домашняя работа не найдена, проверьте правильность введённых данных.")
    except AttributeError:
        print(f"\n{'-' * term_size}\n")
        print("Задание не найдено, проверьте правильность введённых данных.")
    except ValueError:
        print(f"\n{'-' * term_size}\n")
        print("Проверьте правильность введённых данных.")
    print(f"\n{'-' * term_size}\n")
