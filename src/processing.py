import re
from collections import Counter, defaultdict

from mypy.checkexpr import defaultdict

from src.open_csv_xlsx import get_transactions_from_csv


def filter_by_state(list_of_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая фильтрует список словарей по заданному значению ключа state"""
    new_list = []
    for item in list_of_dicts:
        if item["state"] == state:
            new_list.append(item)
    return new_list


def sort_by_date(list_of_dicts: list[dict], is_reverse: bool = True) -> list[dict]:
    """Функция, которая сортирует список словарей по дате"""
    sorted_list = sorted(list_of_dicts, key=lambda item: item["date"], reverse=is_reverse)
    return sorted_list


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""
    return [
        element
        for element in data
        if isinstance(element.get("description"), str) and re.search(search, element["description"], re.IGNORECASE)
    ]

def process_bank_operations(data:list[dict], categories:list)->dict:
    """Функцию, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""

    matched_operations = Counter([element["description"] for element in data if isinstance(element.get("description"), str)
                          and element["description"] in categories])
    result = {}
    for category, amount in matched_operations.items():
        result[category] = amount
    return result

if __name__ == "__main__":
    data = get_transactions_from_csv('/Users/dariamakurova/PycharmProjects/Homework/data/transactions.csv')
    categories = ['Перевод организации', 'Открытие вклада', 'Неизвестная операция']
    print(process_bank_operations(data, categories))
