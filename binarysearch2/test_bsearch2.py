from bsearch import binary_search

import pytest


@pytest.fixture
def alist():
    return [1, 3, 5, 7, 9]


@pytest.mark.parametrize(
    "alist, token, expected", [
        (alist, 5, 2),
        (alist, 3, 1),
        (alist, 7, 3),
        (alist, 9, 4),
        (alist, 1, 0),
        (alist, 4, -1)
    ], indirect=["alist"]
)
def test_finding_token_in_sample_list(alist, token, expected):
    assert binary_search(alist, token) is expected
