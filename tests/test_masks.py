from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(1234567890001234) == "1234 56** **** 1234"
    assert get_mask_card_number(9123 - 4567 - 8912 - 4567) == "Номер должен состоять только из цифр без пробелов"
    assert get_mask_card_number(12345678900012347) == "Номер должен состоять из 16 цифр"
    assert get_mask_card_number(()) == "Номер карты не указан"


def test_get_mask_account_number():
    assert get_mask_account(12345678999987654321) == "**4321"
    assert get_mask_account(12345 - 67899 - 99876 - 54321) == "Номер должен состоять только из цифр без пробелов"
    assert get_mask_account(1234567899998765432100) == "Номер должен состоять из 20 цифр"
    assert get_mask_account(()) == "Номер счета не указан"
