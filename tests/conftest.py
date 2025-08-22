import pytest


# фикстуры для номеров карт
@pytest.fixture
def card_number_right():
    return "1234567890001234"


@pytest.fixture()
def card_number_with_symbols():
    return "9123 - 4567 - 8912 - 4567"


@pytest.fixture
def card_number_long():
    return "12345678900012341234"


@pytest.fixture
def card_number_empty():
    return ""


# фикстуры для номеров счетов


@pytest.fixture
def account_right():
    return "12345678900987654321"


@pytest.fixture()
def account_with_symbols():
    return "12345 - 67890 - 09876 - 54321"


@pytest.fixture
def account_long():
    return "12345678900987654321321"


@pytest.fixture
def account_empty():
    return ""

@pytest.fixture
def transactions_list():
    return [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод со счета на счет",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
},
        {"id": 939719571,
          "state": "EXECUTED",
          "date": "2018-07-29T02:08:58.425572",
          "operationAmount": {
              "amount": "8365.06",
              "currency": {
                  "name": "EUR",
                  "code": "EUR"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"},
        {"id": 939719572,
          "state": "CANCELLED",
          "date": "2018-07-28T02:08:58.425572",
          "operationAmount": {
              "amount": "35.37",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод с карты на карту",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"}]