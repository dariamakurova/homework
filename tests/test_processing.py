import pytest

from src.processing import filter_by_state, process_bank_search, sort_by_date, process_bank_operations


# тест фильтра по статусу
@pytest.mark.parametrize(
    "session_info, state, result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "WRONG_WORD",
            [],
        ),
    ],
)
def test_filter_by_state(session_info, state, result):
    assert filter_by_state(session_info, state) == result


# тест сортировки по дате
@pytest.mark.parametrize(
    "session_info, result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": ""},
                {"id": 939719570, "state": "EXECUTED", "date": ""},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": ""},
                {"id": 939719570, "state": "EXECUTED", "date": ""},
            ],
        ),
    ],
)
def test_sort_by_date(session_info, result):
    assert sort_by_date(session_info) == result


# тест сортировки операций по описанию


def test_process_bank_search(transactions_list):
    assert process_bank_search(transactions_list, "перевод") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719571,
            "state": "EXECUTED",
            "date": "2018-07-29T02:08:58.425572",
            "operationAmount": {"amount": "8365.06", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719572,
            "state": "CANCELLED",
            "date": "2018-07-28T02:08:58.425572",
            "operationAmount": {"amount": "35.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


def test_process_bank_search_empty(transactions_empty):
    assert process_bank_search(transactions_empty, "тест") == []


def test_process_bank_search_no_match(transactions_list):
    assert process_bank_search(transactions_list, "несуществующее описание") == []


# тест получения сводки по категориям операций

def test_process_bank_operations(transactions_list):
    categories = ['Перевод организации', 'Перевод с карты на карту']
    assert process_bank_operations(transactions_list, categories) == {
        'Перевод организации': 1,
        'Перевод с карты на карту': 1,}


def test_process_bank_operations_empty(transactions_empty):
    categories = ['Перевод организации', 'Перевод с карты на карту']
    assert process_bank_operations(transactions_empty, categories) == {}


def test_process_bank_operations_non_exist(transactions_list):
    categories = ['Несуществующая категория']
    assert process_bank_operations(transactions_list, categories) == {}