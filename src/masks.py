def get_mask_card_number(card_number: int) -> str:
    """преобразование номера карты клиента в маску вида XXXX XX** **** XXXX"""

    if card_number:
        if str(card_number).isdigit():
            if len(str(card_number)) == 16 and str(card_number).isdigit():
                card_mask = str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[12:16]
                return card_mask
            else:
                return "Номер должен состоять из 16 цифр"
        else:
            return "Номер должен состоять только из цифр без пробелов"
    return "Номер карты не указан"


def get_mask_account(account: int) -> str:
    """преобразование номера счета в маску вида **XXXX"""

    if account:
        if str(account).isdigit():
            if len(str(account)) == 20 and str(account).isdigit():
                account_mask = "**" + str(account)[-4:]
                return account_mask
            else:
                return "Номер должен состоять из 20 цифр"
        else:
            return "Номер должен состоять только из цифр без пробелов"
    return "Номер счета не указан"
