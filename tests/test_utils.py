from src.utils import get_financial_operations


# тестирование вывода информации о транзакции при наличии корректных входных данных в файле
def test_get_financial_operations():
    path = "/Users/dariamakurova/PycharmProjects/Homework/data/operations.json"
    result = get_financial_operations(path)
    example_transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert example_transaction in result


# тетсирование работы на реальном примере
def test_get_financial_valid_operations():
    path = "/Users/dariamakurova/PycharmProjects/Homework/data/for_testing_operations_valid.json"
    result = get_financial_operations(path)
    example_transactions = [
        {"id": 441945886, "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}},
        {"id": 41428829, "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}},
        {"id": 939719570, "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}},
    ]

    assert example_transactions == result


# тестирование работы при пустом файле
def test_get_financial_operations_empty_file():
    path = "/Users/dariamakurova/PycharmProjects/Homework/data/for_testing_operations_empty.json"
    result = get_financial_operations(path)
    assert result == []


# тестирование работы при отсутствии файла
def test_get_financial_operations_no_file():
    path = "/Users/dariamakurova/PycharmProjects/Homework/data/not_existing.json"
    result = get_financial_operations(path)
    assert result == []


# тестирование работы при неверном формате в файле (не список)
def test_get_financial_operations_not_list_in_file():
    path = "/Users/dariamakurova/PycharmProjects/Homework/data/for_testing_operations_not_list.json"
    result = get_financial_operations(path)
    assert result == []


# тестирование работы при битом файле json
def test_get_financial_operations_broken_json():
    path = "/Users/dariamakurova/PycharmProjects/Homework/data/for_testing_operations_broken.json"
    result = get_financial_operations(path)
    assert result == []
