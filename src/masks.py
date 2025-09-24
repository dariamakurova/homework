import logging


masks_logger = logging.getLogger('masks_logger')
masks_handler = logging.FileHandler('/Users/dariamakurova/PycharmProjects/Homework/logs/masks.log', mode='w')
masks_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
masks_handler.setFormatter(masks_formatter)
masks_logger.addHandler(masks_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """преобразование номера карты клиента в маску вида XXXX XX** **** XXXX"""
    masks_logger.info('Проверка наличия номера карты')
    if card_number:
        masks_logger.info('Проверка номера карты на соответствие формату')
        if str(card_number).isdigit():
            if len(str(card_number)) == 16 and str(card_number).isdigit():
                masks_logger.info('Номер введен корректно, сформирован зашифрованный номер карты')
                card_mask = str(card_number)[:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[12:16]
                return card_mask
            else:
                masks_logger.error('Неверное количество символов')
                return "Номер должен состоять из 16 цифр"
        else:
            masks_logger.error('Неверный формат номера карты')
            return "Номер должен состоять только из цифр без пробелов"
    masks_logger.error('Отсутствует номер карты')
    return "Номер карты не указан"


def get_mask_account(account: int) -> str:
    """преобразование номера счета в маску вида **XXXX"""
    masks_logger.info('Проверка наличия номера счета')
    if account:
        masks_logger.info('Проверка номера счета на соответствие формату')
        if str(account).isdigit():
            masks_logger.info('Номер введен корректно, сформирован зашифрованный номер счета')
            if len(str(account)) == 20 and str(account).isdigit():
                account_mask = "**" + str(account)[-4:]
                return account_mask
            else:
                masks_logger.error('Неверное количество символов')
                return "Номер должен состоять из 20 цифр"
        else:
            masks_logger.error('Неверный формат номера счета')
            return "Номер должен состоять только из цифр без пробелов"
    masks_logger.error('Отсутствует номер счета')
    return "Номер счета не указан"
