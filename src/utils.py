import json


def get_financial_operations(path: str) -> list[dict]:
    """ Получение списка словарей с финансовыми операциями из json файла"""

    try:
        with open(path) as f:
            try:
                financial_operations = json.load(f)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return financial_operations
