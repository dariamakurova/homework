import os
from src.interaction import get_menu_choice, get_status_choice
from src.open_csv_xlsx import get_transactions_from_csv, get_transactions_from_excel
from src.utils import get_financial_operations


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
    date_filtration = input("Отсортировать операции по дате? Да/Нет ").lower()
    reverse = input("Отсортировать по возрастанию или по убыванию? ").lower()
    rub_transactions = input("Выводить только рублевые транзакции? Да/Нет ").lower()
    filter_word_status = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ").lower()
    if filter_word_status == "да":
        filter_word = input("Введите слово для фильтрации")

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




if __name__ == "__main__":
    main()