import os
from dotenv import load_dotenv
import requests

load_dotenv()
EXCHANGE_API_KEY = os.getenv('EXCHANGE_API_KEY')


def convert_transaction_amount(transaction: dict) -> float:
    """ Конвертация суммы транзакции в рубли из полученых данных о транзакции"""

    try:
        transaction_amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency == "RUB":
            amount = transaction_amount
            return amount
        elif currency in ["USD", "EUR"]:
            try:
                url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={transaction_amount}"
                headers = {"apikey": EXCHANGE_API_KEY}
                response = requests.get(url, headers=headers, data={})
                amount = round((response.json()['result']), 2)
                return amount
            except requests.exceptions.RequestException:
                print("Ошибка подключения к сервису конвертации")
    except KeyError:
        print("Некорректные данные о транзакции")
