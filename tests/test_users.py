from typing import List
import pytest


__masha = {
            "username": "Masha",
            "email": "masha@email.com",
        }
__pasha = {
            "username": "Pasha",
            "email": "pasha@email.com",
        }

__test_user_list = list([
    __masha,
    __pasha,
])


def test_get_user_list():
    assert __test_user_list == list([__masha, __pasha])
