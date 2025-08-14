import pytest

# фикстуры для номеров карт
@pytest.fixture
def card_number_right():
    return '1234567890001234'


@pytest.fixture()
def card_number_with_symbols():
    return '9123 - 4567 - 8912 - 4567'


@pytest.fixture
def card_number_long():
    return '12345678900012341234'


@pytest.fixture
def card_number_empty():
    return ''


# фикстуры для номеров счетов

@pytest.fixture
def account_right():
    return '12345678900987654321'


@pytest.fixture()
def account_with_symbols():
    return '12345 - 67890 - 09876 - 54321'


@pytest.fixture
def account_long():
    return '12345678900987654321321'


@pytest.fixture
def account_empty():
    return ''
