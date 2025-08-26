from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import transactions_list

# тестирование функции filter_by_currency:

def test_filter_by_currency(transactions_list):
    result = filter_by_currency(transactions_list, "USD")
    assert next(result) == {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод со счета на счет",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"}
    assert next(result) == {"id": 939719572,
          "state": "CANCELLED",
          "date": "2018-07-28T02:08:58.425572",
          "operationAmount": {
              "amount": "35.37",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод с карты на карту",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"}

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