from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    print(get_mask_card_number())
    print(get_mask_card_number(9123-4567-8912-4567))

    print(get_mask_account(1234567891234567890))
