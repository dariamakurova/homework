import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# тестирование функции filter_by_currency:


def test_filter_by_currency(transactions_list):
    result = filter_by_currency(transactions_list, "USD")
    assert next(result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(result) == {
        "id": 939719572,
        "state": "CANCELLED",
        "date": "2018-07-28T02:08:58.425572",
        "operationAmount": {"amount": "35.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_filter_by_currency_not_in_list(transactions_list):
    result = filter_by_currency(transactions_list, "RUB")
    assert next(result, "Операций не найдено") == "Операций не найдено"


def test_filter_by_currency_empty():
    result = filter_by_currency([], "USD")
    assert next(result, "Операций не найдено") == "Операций не найдено"


# тестирование функции transaction_descriptions:


def test_transaction_descriptions(transactions_list):
    result = list(transaction_descriptions(transactions_list))
    assert result == ["Перевод со счета на счет", "Перевод организации", "Перевод с карты на карту", None]


def test_transaction_descriptions_empty(transactions_empty):
    result = list(transactions_empty)
    assert result == []


# тестирование функции card_number_generator:


@pytest.mark.parametrize(
    "start, stop, result",
    [
        (
            "1",
            "5",
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        ("9999", "10001", ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
        ("-5", "6", ["Допустимый диапазон номеров карт: 0 - 9999999999999999"]),
        ("9999999999999999", "10000000000000000", ["Допустимый диапазон номеров карт: 0 - 9999999999999999"]),
        ("5", "5", ["0000 0000 0000 0005"]),
        ("6", "5", []),
    ],
)
def test_card_number_generator(start, stop, result):
    assert list(card_number_generator(start, stop)) == result
