import os
from unittest.mock import patch

import requests.exceptions
from dotenv import load_dotenv
from urllib3.exceptions import RequestError

from src.external_api import convert_transaction_amount
from tests.conftest import transaction_USD, transaction_RUB, transaction_broken


# тестирование работы функции при долларовой транзакции
def test_convert_transaction_amount_USD(transaction_USD):
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 100.11}, 'info': {'timestamp': 1757187665, 'rate': 98.7654}, 'date': '2025-09-06', 'result': 9887.4042}
        load_dotenv()
        EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")
        headers = {"apikey": EXCHANGE_API_KEY}
        assert convert_transaction_amount(transaction_USD) == 9887.40
        mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100.11', headers=headers, data= {})


# тестирование работы функции при рублевой транзакции
def test_convert_transaction_amount_RUB(transaction_RUB):
    result = convert_transaction_amount(transaction_RUB)
    assert result == 10000.99

# тестирование работы функции при отсутствии транзакции
def test_convert_transaction_no_transaction():
    result = convert_transaction_amount("")
    assert result == None

# тестирование работы функции при неполных сведениях в транзакции - KeyError
def test_convert_transaction_key_error(transaction_broken):
    result = convert_transaction_amount(transaction_broken)
    assert result == None

# тестирование работы функции при ошибке подключения
def test_convert_transaction_amount_USD_connection_error(transaction_USD, capsys):

    load_dotenv()
    EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")
    headers = {"apikey": EXCHANGE_API_KEY}

    with patch('src.external_api.requests.get', side_effect=requests.exceptions.RequestException()) as mock_get:
        assert convert_transaction_amount(transaction_USD) == None
        mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100.11', headers=headers, data= {})
        out = capsys.readouterr().out
        assert out == "Ошибка подключения к сервису конвертации\n"


# тестирование работы функции с неизвестной валютой
def test_convert_transaction_YY(transaction_YY):
    result = convert_transaction_amount(transaction_YY)
    assert result == None