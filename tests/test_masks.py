import pytest


from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number_right, card_number_with_symbols, card_number_long, card_number_empty):
    assert get_mask_card_number(card_number_right) == "1234 56** **** 1234"
    assert get_mask_card_number(card_number_with_symbols) == "Номер должен состоять только из цифр без пробелов"
    assert get_mask_card_number(card_number_long) == "Номер должен состоять из 16 цифр"
    assert get_mask_card_number(card_number_empty) == "Номер карты не указан"


def test_get_mask_account_number(account_right, account_with_symbols, account_long, account_empty):
    assert get_mask_account(account_right) == "**4321"
    assert get_mask_account(account_with_symbols) == "Номер должен состоять только из цифр без пробелов"
    assert get_mask_account(account_long) == "Номер должен состоять из 20 цифр"
    assert get_mask_account(account_empty) == "Номер счета не указан"
