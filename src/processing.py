import re


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
    # pattern = re.compile(search)
    return [
        element
        for element in data
        if isinstance(element.get("description"), str) and re.search(search, element["description"], re.IGNORECASE)
    ]
