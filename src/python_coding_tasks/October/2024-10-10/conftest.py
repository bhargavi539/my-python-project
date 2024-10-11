import pytest

@pytest.fixture
def launch_chrome():
    print("........launching chrome browser........")
    return "Chrome"


@pytest.fixture
def close_chrome():
    print (".....closing chrome browser.......")
    return "closed"
