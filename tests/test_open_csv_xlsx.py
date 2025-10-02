import os
from unittest.mock import patch

import pandas as pd

from src.open_csv_xlsx import get_transactions_from_csv, get_transactions_from_excel


# тестирование работы функции get_transactions_from_csv:
# тестирование работы функции при корректном файле
@patch("pandas.read_csv")
def test_get_transactions_from_csv_ok(mock_read):
    mock_read.return_value.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    assert get_transactions_from_csv(mock_read) == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    mock_read.assert_called_once()


# тестирование работы функции при отсутствии файла
def test_get_transactions_from_csv_no_file(capsys):
    path = "data/fake.csv"
    assert get_transactions_from_csv(path) == []
    out = capsys.readouterr().out
    assert out == f"Файл {path} не найден\n"


# тестирование работы функции при некорректном формате данных в файле
def test_get_transactions_from_csv_empty_file(capsys):
    with patch("pandas.read_csv", side_effect=pd.errors.ParserError("broken csv")) as mock_read:
        assert get_transactions_from_csv(mock_read) == []
    out = capsys.readouterr().out
    assert out == "Ошибка чтения файла. Проверьте разделитель или формат данных.\n"
    mock_read.assert_called_once()


# тестирование работы функции get_transactions_from_excel:
# тестирование работы функции при корректном файле
@patch("pandas.read_excel")
def test_get_transactions_from_excel_ok(mock_read):
    mock_read.return_value.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    assert get_transactions_from_excel(mock_read) == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    mock_read.assert_called_once()


# тестирование работы функции при отсутствии файла
def test_get_transactions_from_excel_no_file(capsys):
    path = "data/fake.xlsx"
    assert get_transactions_from_excel(path) == []
    out = capsys.readouterr().out
    assert out == f"Файл {path} не найден\n"


# тестирование работы функции при пустом файле
def test_get_transactions_from_excel_empty_file(capsys):
    path = os.path.join((os.path.dirname(os.path.dirname(__file__))), "data", "for_testing_empty.xlsx")
    assert get_transactions_from_excel(path) == []
