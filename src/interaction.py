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
    """ Функция, которая проверяет ввод пользователя на соответствие предлоденным вариантам"""

    while True:
        user_choice = input().lower()
        available_options = [option_1, option_2]
        if user_choice.lower() in available_options:
            return user_choice
        else:
            print( f'Выберите {option_1} или {option_2}')
