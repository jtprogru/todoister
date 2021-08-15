import pytest
from pytest_schema import schema

# single user schema
user = {
    "username": str,
    "email": str,
}

# multiple users schema
users = [user]


def test_users_endpoint(test_client):
    """
    Test calling a users endpoint and validating its
    response of users info is correct format.
    """
    response = [
        # ✅ Valid
        {"username": "misha", "email": "misha@email.com",},
        {"username": "vasya", "email": "vasya@email.com",},
    ]

    # response = test_client.get("/api/v1/users/")

    assert schema(users) == response


def test_users_endpoint_invalid():
    """
    Test calling a users endpoint and validating its
    response of users info is INVALID format.
    """
    response = [
        # ❌ Invalid
        {
            "id": "null",
            "name": None,
            "age": 0,
            "email": "unknown@msn",
            "role": "unknown",
            "friends": None,
            "address": "5 Sunset St., San Jose, CA, 054053",
        },
    ]

    # Option 1:
    assert schema(users) != response

    # Option 2:
    with pytest.raises(Exception):
        schema(users) == response
