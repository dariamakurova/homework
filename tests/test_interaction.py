from unittest.mock import patch

from src.interaction import get_menu_choice, get_status_choice


# тестирование get_menu_choice
def test_get_menu_choice_1(capsys):  # тестируем 1
    with patch("builtins.input", return_value="1"):
        assert get_menu_choice() == "1"
    out = capsys.readouterr().out
    assert out == "Для обработки выбран JSON-файл\n"


def test_get_menu_choice_2(capsys):  # тестируем 2
    with patch("builtins.input", return_value="2"):
        assert get_menu_choice() == "2"
    out = capsys.readouterr().out
    assert out == "Для обработки выбран CSV-файл\n"


def test_get_menu_choice_3(capsys):  # тестируем 3
    with patch("builtins.input", return_value="3"):
        assert get_menu_choice() == "3"
    out = capsys.readouterr().out
    assert out == "Для обработки выбран XLSX-файл\n"


def test_get_menu_choice_4(capsys):  # тестируем 4
    with patch("builtins.input", side_effect=["4", "1"]):
        get_menu_choice()
    out = capsys.readouterr().out.split("\n")
    assert out[0] == "Выберите пункт меню 1, 2 или 3"
    assert out[1] == "Для обработки выбран JSON-файл"


# тестирование get_status_choice


def test_get_status_choice(capsys):
    with patch("builtins.input", return_value="Executed"):
        assert get_status_choice() == "EXECUTED"
    out = capsys.readouterr().out
    assert out == '\nОперации отфильтрованы по статусу "EXECUTED"\n'


def test_get_status_choice_wrong(capsys):
    with patch("builtins.input", side_effect=["test", "Canceled"]):
        get_status_choice()
    out = capsys.readouterr().out.strip().splitlines()
    assert out[0] == 'Статус операции "TEST" недоступен.'
    assert out[2] == 'Операции отфильтрованы по статусу "CANCELED"'
