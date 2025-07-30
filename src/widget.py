from masks import get_mask_card_number, get_mask_account

def mask_account_card(card_info: str) -> str:
    """Функция, которая маскирует номер карты или счета в полученной строке с информауией"""
    card_number = None
    account_number = None
    comment = []
    undefined_number = []
    for item in card_info:
        if item.isdigit():
            undefined_number.append(item)
        else: comment.append(item)

    if len(undefined_number) == 16:
         card_number = int("".join(undefined_number))
         return "".join(comment) + get_mask_card_number(card_number)

    elif len(undefined_number) == 20:
         account_number = int("".join(undefined_number))
         return "".join(comment) + get_mask_account(account_number)


if __name__ == "__main__":
    card_info = "Счет 73654108430135874305"
    print (mask_account_card(card_info))
