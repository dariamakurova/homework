import os

from src.generators import filter_by_currency
from src.interaction import get_menu_choice, get_status_choice, get_choice_from_options
from src.open_csv_xlsx import get_transactions_from_csv, get_transactions_from_excel
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import get_financial_operations
from src.widget import get_date


def main():
    """ Основная функция программы """

    print('''
Привет! Добро пожаловать в программу работы с банковскими транзакциями.

Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')

# получаем ответ пользователя по выбранному пункту меню
    menu_choice = get_menu_choice()

# запрашиваем необходимый статус операций
    status_choice = get_status_choice()

# запрашиваем параметры фильтрации
    print("Отсортировать операции по дате? Да/Нет")
    date_filtration = get_choice_from_options("Да", "Нет")
    print("Отсортировать по возрастанию или по убыванию?")
    reverse = get_choice_from_options("По возрастанию", "По убыванию")
    print("Выводить только рублевые транзакции? Да/Нет")
    rub_transactions = get_choice_from_options("Да", "Нет")
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    filter_word_status = get_choice_from_options("Да", "Нет")


# получаем список операций

    if menu_choice == '1':
        path = os.path.join((os.path.dirname(__file__)), "data", "operations.json")
        user_transactions = get_financial_operations(path)
    elif menu_choice == '2':
        path = os.path.join((os.path.dirname(__file__)), "data", "transactions.csv")
        user_transactions = get_transactions_from_csv(path)
    else:
        path = os.path.join((os.path.dirname(__file__)), "data", "transactions_excel.xlsx")
        user_transactions = get_transactions_from_excel(path)

# фильтруем по установленному статусу

    transactions_by_state = filter_by_state(user_transactions, status_choice)

# фильтруем рублевые при необходимости

    if rub_transactions == "да":
        transactions_by_currency = list(filter_by_currency(transactions_by_state, "RUB"))
    else:
        transactions_by_currency = transactions_by_state

# фильтруем по слову при необходимости

    if filter_word_status == "да":
        filter_word = input("Введите слово для фильтрации ")
        transactions_by_word = process_bank_search(transactions_by_currency, filter_word)
    else:
        transactions_by_word = transactions_by_currency


# сортируем по дате и реверсу

    if date_filtration == "да":
        if reverse == "по возрастанию":
            transactions_sorted = sort_by_date(transactions_by_word, is_reverse=False)
        else:
            transactions_sorted = sort_by_date(transactions_by_word)
    else:
        transactions_sorted = transactions_by_word
# выводим итоговый список транзакций

    print('Распечатываю итоговый список транзакций...')
    print(f'\nВсего банковских операций в выборке: {len(transactions_sorted)}')

    for transaction in transactions_sorted:
        print(f'{get_date(transaction["date"])} {transaction["description"]}')





if __name__ == "__main__":
    main()