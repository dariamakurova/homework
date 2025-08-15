import pytest

from src.widget import mask_account_card, get_date


# def test_get_date():
#     pass

@pytest.mark.parametrize('info, mask_number', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('Maestro ', 'Проверьте правильность ввода'),
    ('', 'Проверьте правильность ввода')
])
def test_mask_account_card(info, mask_number):
    assert mask_account_card(info) == mask_number