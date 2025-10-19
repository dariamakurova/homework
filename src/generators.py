from typing import Any, Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[Any]:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    return filter(lambda x: x.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency, transactions)


def transaction_descriptions(transactions: list[dict]) -> Iterator[Any]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    return (transaction.get("description") for transaction in transactions)


def card_number_generator(start: int, stop: int) -> Iterator[Any]:
    """Генератор номеров банковских карт в заданном диапазоне"""
    if 0 <= int(start) <= 9999999999999999 and 0 <= int(stop) <= 9999999999999999:
        for i in range(int(start), (int(stop) + 1)):
            zero_numb = 16 - len(str(i))
            full_numb = "0" * zero_numb + str(i)
            final_numb = full_numb[0:4] + " " + full_numb[4:8] + " " + full_numb[8:12] + " " + full_numb[12:16]
            yield final_numb
    else:
        yield "Допустимый диапазон номеров карт: 0 - 9999999999999999"
