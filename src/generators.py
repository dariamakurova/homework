from typing import Iterator, Any

from tests.conftest import transactions_list


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[Any]:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    return filter(lambda x: x.get("operationAmount").get("currency").get("name") == currency, transactions)


def transaction_descriptions(transactions: list[dict]) -> Iterator[Any]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    return (transaction.get("description") for transaction in transactions)


def card_number_generator(start: int, stop: int) -> Iterator[Any]:
    """Генератор номеров банковских карт в заданном диапазоне"""
    for i in range(start, (stop + 1)):
        zero_numb = 16 - len(str(i))
        full_numb = "0" * zero_numb + str(i)
        final_numb = full_numb[0:4] + " " + full_numb[4:8] + " " + full_numb[8:12] + " " + full_numb[12:16]
        yield final_numb


if __name__ == "__main__":

    transactions = [{
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
          "to": "Счет 11776614605963066702"
},
        {"id": 939719571,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"},
        {"id": 939719572,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "EUR",
                  "code": "EUR"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"}]


    usd_transactions = filter_by_currency(transactions, "RUB")
    print(next(usd_transactions, "Операций не найдено"))
    print(next(usd_transactions, "Операций не найдено"))


    descriptions = transaction_descriptions(transactions)
    for _ in range(3):
        print(next(descriptions))

