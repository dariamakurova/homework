import re

from src.widget import get_date, mask_account_card


def get_menu_choice() -> str | None:
    """Функция, которая выводит наименование выбранного пункта меню"""

    while True:
        user_choice = input()
        if user_choice in ["1", "2", "3"]:
            if user_choice == "1":
                print("Для обработки выбран JSON-файл")
            elif user_choice == "2":
                print("Для обработки выбран CSV-файл")
            else:
                print("Для обработки выбран XLSX-файл")
            return user_choice

        else:
            print("Выберите пункт меню 1, 2 или 3")


def get_status_choice() -> str | None:
    """Функция, которая выводит наименование выбранного статуса для фильтрации операций"""

    while True:
        user_choice = input(
            """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        ).upper()
        available_status = ["EXECUTED", "CANCELED", "PENDING"]
        if user_choice.upper() in available_status:
            print(f'\nОперации отфильтрованы по статусу "{user_choice}"')
            return user_choice
        else:
            print(f'\nСтатус операции "{user_choice}" недоступен.')


def get_choice_from_options(option_1: str, option_2: str) -> str | None:
    """ Функция, которая проверяет ввод пользователя на соответствие предложенным вариантам"""

    while True:
        user_choice = input().lower()
        available_options = [option_1.lower(), option_2.lower()]
        if user_choice.lower() in available_options:
            return user_choice
        else:
            print(f'Выберите {option_1} или {option_2}')


def transaction_formatted_info(transaction: dict) -> str:
    """ Функция, которая выводит информацию о транзакции в заданном формате"""

    date = get_date(transaction.get("date", ""))
    description = transaction.get("description", "")
    if isinstance(transaction.get("description"), str) and re.search("перевод", transaction["description"],
                                                                     re.IGNORECASE):
        from_info = mask_account_card(transaction.get("from"))

    to_info = mask_account_card(transaction.get("to"))

    if transaction.get("operationAmount", {}).get("amount"):
        amount = transaction.get("operationAmount", {}).get("amount", "")
    else:
        amount = transaction.get("amount", "")

    if transaction.get("operationAmount", {}).get("currency", {}).get("name"):
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", "")
    else:
        currency = transaction.get("currency_name", "")

    transaction_format = ""
    if isinstance(transaction.get("description"), str) and re.search("перевод", transaction["description"],
                                                                     re.IGNORECASE):
        transaction_format = (f'{date} {description}\n'
                              f'{from_info} -> {to_info}\n'
                              f'Сумма: {amount} {currency}\n')
    else:
        transaction_format = (f'{date} {description}\n'
                              f'{to_info}\n'
                              f'Сумма: {amount} {currency}\n')
    return transaction_format
