import json
import logging
from typing import Any

utils_logger = logging.getLogger("utils_logger")
utils_handler = logging.FileHandler("/Users/dariamakurova/PycharmProjects/Homework/logs/utils.log", mode="w")
utils_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
utils_handler.setFormatter(utils_formatter)
utils_logger.addHandler(utils_handler)
utils_logger.setLevel(logging.DEBUG)


def get_financial_operations(path: str) -> Any:
    """Получение списка словарей с финансовыми операциями из json файла"""

    try:
        utils_logger.info("Получение данных об операциях")
        with open(path) as f:
            try:
                financial_operations = json.load(f)
                if isinstance(financial_operations, list):
                    utils_logger.info("Сформирован список финансовых операций")
                    return financial_operations
                else:
                    utils_logger.error("Ошибка чтения файла")
                    return []
            except json.JSONDecodeError:
                utils_logger.error("Ошибка форматирования json файла")
                return []
    except FileNotFoundError:
        utils_logger.error("Файл не найден")
        return []
