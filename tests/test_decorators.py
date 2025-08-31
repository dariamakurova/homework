from src.decorators import log
import pytest


def test_log_with_filename_ok(): #тестирование декоратора с заданным файлом и работающей функцией
    @log(filename="mylog.txt")
    def add(x, y):
        return x + y

    add(1,2)
    with open ("mylog.txt", "r", encoding="utf-8") as file:
        text = file.read()
        assert text == "add OK"

def test_log_with_filename_error(): #тестирование декоратора с заданным файлом и TypeError
    @log(filename="mylog.txt")
    def add(x, y):
        return x + y

    add("f", 2)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        text = file.read()
        assert text == 'add error: can only concatenate str (not "int") to str. Inputs: (\'f\', 2), {}'


def test_log_with_filename_error(): #тестирование декоратора с заданным файлом и ZeroDivisionError
    @log(filename="mylog.txt")
    def divide(x, y):
        return x / y

    divide(5, 0)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        text = file.read()
        assert text == 'divide error: division by zero. Inputs: (5, 0), {}'