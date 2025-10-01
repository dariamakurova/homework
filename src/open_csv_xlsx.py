import pandas as pd
import os


def get_transactions_from_csv(path: str, file_delimiter: str =';') -> list:
    """Получение списка транзакций из .csv файла"""
    if os.path.exists(path):
        try:
            transactions = pd.read_csv(path, delimiter=file_delimiter).to_dict(orient='records')
        except pd.errors.ParserError:
            print(f'Ошибка чтения CSV. Проверьте разделитель или формат данных.')
            return []
    else:
        print(f'Файл {path} не найден')
        return []
    return transactions


def get_transactions_from_excel(path: str) -> list:
    """Получение списка транзакций из .xlsx файла"""
    if os.path.exists(path):
        try:
            transactions = pd.read_excel(path).to_dict(orient='records')
        except ValueError:
            return []
    else:
        print(f'Файл {path} не найден')
        return []
    return transactions
