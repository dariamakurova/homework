import json
from typing import Any


def get_financial_operations(path: str) -> Any:
    """Получение списка словарей с финансовыми операциями из json файла"""

    try:
        with open(path) as f:
            try:
                financial_operations = json.load(f)
                if isinstance(financial_operations, list):
                    return financial_operations
                else: return []
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    print(get_financial_operations('/Users/dariamakurova/PycharmProjects/Homework/data/for_testing_not_list.json'))