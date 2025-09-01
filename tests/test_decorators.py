import pytest
from src.decorators import log


def test_log_with_filename_ok():  # тестирование декоратора с заданным файлом и работающей функцией
    @log(filename="mylog.txt")
    def add(x, y):
        return x + y

    add(1, 2)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        text = file.read()
        assert text == "add OK"


def test_log_with_filename_type_error():  # тестирование декоратора с заданным файлом и TypeError
    @log(filename="mylog.txt")
    def add(x, y):
        return x + y

    with pytest.raises(TypeError, match="can only concatenate str \(not \"int\"\) to str"):
        add("f", 2)

    with open("mylog.txt", "r", encoding="utf-8") as file:
        text = file.read()
        assert text == "add error: can only concatenate str (not \"int\") to str. Inputs: ('f', 2), {}"


def test_log_with_filename_zerodivision_error():  # тестирование декоратора с заданным файлом и ZeroDivisionError
    @log(filename="mylog.txt")
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(5, 0)

    with open("mylog.txt", "r", encoding="utf-8") as file:
        text = file.read()
        assert text == "divide error: division by zero. Inputs: (5, 0), {}"


def test_log_nofilename_ok(capsys):  # тестирование декоратора с выводом в консоль и работающей функцией
    @log(filename="")
    def add(x, y):
        return x + y

    add(1, 2)
    out = capsys.readouterr().out
    assert out == "add OK\n"


def test_log_nofilename_type_error(capsys):  # тестирование декоратора с выводом в консоль и TypeError
    @log(filename="")
    def add(x, y):
        return x + y

    with pytest.raises(TypeError, match="can only concatenate str \(not \"int\"\) to str"):
        add("f", 2)

    out = capsys.readouterr().out
    assert out == "add error: can only concatenate str (not \"int\") to str. Inputs: ('f', 2), {}\n"


def test_log_with_nofilename_zerodivision_error(capsys):  # тестирование декоратора с выводом в консоль
    # и ZeroDivisionError
    @log(filename="")
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(5, 0)

    out = capsys.readouterr().out
    assert out == "divide error: division by zero. Inputs: (5, 0), {}\n"


def test_log_with_filename_capsys(capsys):  # проверка, что в консоль ничего не выводится при заданном файле
    @log(filename="mylog.txt")
    def add(x, y):
        return x + y

    add(1, 2)
    out = capsys.readouterr().out
    assert out == ""
