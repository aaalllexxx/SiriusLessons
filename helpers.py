import fileinput
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


def count_input(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # время старта
        data = func(*args, **kwargs)
        set_temp("INPUT_TIME", get_temp("INPUT_TIME") + time.time() - start_time)  # установка времени запроса данных
        return data
    return wrapper


# реализация метода input, записывающая во временный файл время запроса данных
@count_input
def input(text):
    sys.stdout.write(text)
    sys.stdout.flush()
    data = ""
    while (letter := sys.stdin.read(1)) != "\n":
        data += letter
    return data


def end_task():
    set_temp("INPUT_TIME", 0)
