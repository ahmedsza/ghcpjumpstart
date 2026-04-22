import pytest
from utils import is_valid_email

@pytest.mark.parametrize("email", [
    "user@example.com",
    "user.name+tag@sub.domain.co",
    "user_name@domain.org",
    "user-name@domain.io",
    "user123@domain123.com",
    "u@d.co",
    "user.name@domain.travel",
    "user@localhost.localdomain"
])
def test_is_valid_email_valid(email):
    assert is_valid_email(email) is True

@pytest.mark.parametrize("email", [
    "plainaddress",
    "@missingusername.com",
    "username@.com",
    "username@com",
    "username@domain..com",
    "username@domain.c",
    "username@domain.corporate1",
    "user name@domain.com",
    "user@domain,com",
    "user@domain",
    "user@.domain.com",
    "user@domain.com.",
    "",
    None
])
def test_is_valid_email_invalid(email):
    assert is_valid_email(email) is False