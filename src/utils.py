import json
from typing import Any
import logging


logger = logging.getLogger('utils_logger')
utils_handler = logging.FileHandler('/Users/dariamakurova/PycharmProjects/Homework/logs/utils.log', mode='w')
utils_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
utils_handler.setFormatter(utils_formatter)
logger.addHandler(utils_handler)
logger.setLevel(logging.DEBUG)


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