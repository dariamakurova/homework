import pandas as pd


def get_transactions_from_csv(path: str) -> list:
    """Получение списка транзакций из .csv файла"""
    transactions = pd.read_csv(path, delimiter=';')
    transactions_dict = transactions.to_dict(orient='records')
    return transactions_dict


def get_transactions_from_excel(path: str) -> list:
    """Получение списка транзакций из .xlsx файла"""
    transactions = pd.read_excel(path)
    transactions_dict = transactions.to_dict(orient='records')
    return transactions_dict

# project_dir = os.path.dirname(os.path.dirname(__file__))
# log_dir = os.path.join(project_dir, 'data', 'transactions_excel.xlsx')
#
# print(get_transactions_from_excel(log_dir))
