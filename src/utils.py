import json
from typing import Any, Callable


def get_financial_operations(path: str) -> Any:
    """Получение списка словарей с финансовыми операциями из json файла"""

    try:
        with open(path) as f:
            try:
                financial_operations = json.load(f)
                if type(financial_operations) != list:
                    return []
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return financial_operations
