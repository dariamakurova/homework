import os
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()
EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_transaction_amount(transaction: dict) -> Optional[float]:
    """Конвертация суммы транзакции в рубли из полученых данных о транзакции"""

    try:
        transaction_amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency == "RUB":
            amount = float(transaction_amount)
            return amount
        elif currency in ["USD", "EUR"]:
                try:
                    url = (
                    f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount="
                    f"{transaction_amount}")
                    headers = {"apikey": EXCHANGE_API_KEY}
                    response = requests.get(url, headers=headers, data={})
                    amount = round((response.json()["result"]), 2)
                    return float(amount)
                except requests.exceptions.RequestException:
                    print("Ошибка подключения к сервису конвертации")
                    return None
        else:
            return None
    except TypeError:
        print("Некорректные данные о транзакции")
        return None
    except KeyError:
        print("Некорректные данные о транзакции")
        return None
