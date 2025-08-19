import pytest

from src.widget import get_date, mask_account_card


# тест маскировки данных
@pytest.mark.parametrize(
    "info, mask_number",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Maestro ", "Проверьте правильность ввода"),
        ("", "Проверьте правильность ввода"),
    ],
)
def test_mask_account_card(info, mask_number):
    assert mask_account_card(info) == mask_number


# тест форматирования даты
@pytest.mark.parametrize(
    "date, format_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-06-30T02:08:58", "30.06.2018"),
        ("2000-01-01", "01.01.2000"),
        ("", "Дата не указана"),
    ],
)
def test_get_date(date, format_date):
    assert get_date(date) == format_date
