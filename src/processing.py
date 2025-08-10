def filter_by_state(list_of_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая фильтрует список словарей по заданному значению ключа state"""
    new_list = []
    for item in list_of_dicts:
        if item["state"] == state:
            new_list.append(item)
    return new_list

