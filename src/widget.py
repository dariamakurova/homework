from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Функция, которая маскирует номер карты или счета в полученной строке с информацией"""
    card_number = None
    account_number = None
    comment = []
    undefined_number = []
    for item in card_info:
        if item.isdigit():
            undefined_number.append(item)
        else:
            comment.append(item)

    if len(undefined_number) == 16:
        card_number = int("".join(undefined_number))
        return str("".join(comment) + get_mask_card_number(card_number))

    elif len(undefined_number) == 20:
        account_number = int("".join(undefined_number))
        return str("".join(comment) + get_mask_account(account_number))

    else:
        return "Проверьте правильность ввода"


def get_date(date: str) -> str:
    """Функция для перевода даты из формата 'ГГГГ-ММ-ДДTЧЧ:ММ:СС.СССССС' 'ДД.ММ.ГГГГ' в"""
    if date:
        new_date = date[8:10] + "." + date[5:7] + "." + date[0:4]
        return new_date
    else:
        return "Дата не указана"


# if __name__ == "__main__":
#     card_info = ""
#     print(mask_account_card(card_info))
#     card_info = "Счет 64686473678894779589"
#     print(mask_account_card(card_info))
#     date = ""
#     print(get_date(date))
