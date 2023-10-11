import json
import os.path
import sys
import time

base_dir = os.path.sep.join(os.path.split(__file__)[:-1])


def get_temp(key=""):
    with open(os.path.join(base_dir, "temp.json"), "r") as file:
        data = json.loads(file.read() or "{}")
        file.close()
    return data.get(key) if key else data


def set_temp(key, value):
    data = get_temp()
    data[key] = value
    with open(os.path.join(base_dir, "temp.json"), "w") as file:
        file.write(json.dumps(data))
        file.close()


# реализация метода input, записывающая во временный файл время запроса данных
def input(text):
    start_time = time.time()  # время старта
    sys.stdout.write(text+"")  # вывод сообщения
    sys.stdout.flush()
    data = ""
    for line in sys.stdin.readlines(1):  # построчный ввод
        data = line
    set_temp("INPUT_TIME", get_temp("INPUT_TIME") + time.time() - start_time)  # установка времени запроса данных

    return data.rstrip("\n")


def end_task():
    set_temp("INPUT_TIME", 0)
