import pandas as pd
import os


def get_transactions_from_csv(path: str, file_delimiter: str =';') -> list:
    """Получение списка транзакций из .csv файла"""
    if os.path.exists(path):
        try:
            transactions = pd.read_csv(path, delimiter=file_delimiter).to_dict(orient='records')
        except pd.errors.EmptyDataError:
            raise ValueError(f'Файл {path} пуст')
        except pd.errors.ParserError:
            raise ValueError(f'Ошибка чтения CSV. Проверь разделитель (сейчас: "{file_delimiter}") или формат данных.')
    else:
        raise FileNotFoundError(f'Файл {path} не найден')
    return transactions


def get_transactions_from_excel(path: str) -> list:
    """Получение списка транзакций из .xlsx файла"""
    if os.path.exists(path):
        try:
            transactions = pd.read_excel(path).to_dict(orient='records')
        except pd.errors.EmptyDataError:
            raise ValueError(f'Файл {path} пуст')
    else:
        raise FileNotFoundError(f'Файл {path} не найден')
    return transactions

# project_dir = os.path.dirname(os.path.dirname(__file__))
# log_dir = os.path.join(project_dir, 'data', 'transactions.csv')

