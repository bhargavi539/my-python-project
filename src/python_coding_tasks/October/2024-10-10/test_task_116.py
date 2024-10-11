# Fixture concept with another example

import pytest

@pytest.fixture
def create_token():
    return "abc"

@pytest.fixture
def create_booking_id():
    return 123

def test_update_req1(create_token,create_booking_id):
    print("token -> ",create_token)
    print("booking_id -> ",create_booking_id)


def test_update_req2(create_token,create_booking_id):
    print("token -> ",create_token)
    print("booking_id -> ",create_booking_id)

