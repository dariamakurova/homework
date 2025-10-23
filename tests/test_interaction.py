from unittest.mock import patch

from src.interaction import get_choice_from_options, get_menu_choice, get_status_choice, transaction_formatted_info


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


# тестирование get_choice_from_options

def test_get_choice_from_options():
    with patch("builtins.input", return_value="да"):
        assert get_choice_from_options("да", "нет") == "да"
    with patch("builtins.input", return_value="нет"):
        assert get_choice_from_options("да", "нет") == "нет"


def test_get_choice_from_options_wrong(capsys):
    with patch("builtins.input", side_effect=["test", "да"]):
        get_choice_from_options("да", "нет")
    out = capsys.readouterr().out.strip().splitlines()
    assert out[0] == 'Выберите да или нет'

# тестирование форматирования вывода информации о транзакции


def test_transaction_formatted_info_trans():
    transaction = {"id": 214024827,
                   "state": "EXECUTED",
                   "date": "2018-12-20T16:43:26.929246",
                   "operationAmount":
                       {"amount": "70946.18",
                        "currency":
                            {"name": "USD",
                             "code": "USD"}},
                   "description": "Перевод организации",
                   "from": "Счет 10848359769870775355",
                   "to": "Счет 21969751544412966366"}

    assert (transaction_formatted_info(transaction)) == """20.12.2018 Перевод организации
Счет **5355 -> Счет **6366
Сумма: 70946.18 USD\n"""


def test_transaction_formatted_info_():
    transaction = {
        "id": 596171168,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {
          "amount": "79931.03",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Открытие вклада",
        "to": "Счет 72082042523231456215"
      }
    assert (transaction_formatted_info(transaction)) == """11.07.2018 Открытие вклада
Счет **6215
Сумма: 79931.03 руб.\n"""
