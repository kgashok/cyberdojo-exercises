from bsearch import binary_search

import pytest
pytestmark = pytest.mark.random_order(disabled=True)


@pytest.fixture
def alist():
    return [1, 3, 5, 7, 9]


@pytest.mark.parametrize(
    "alist, token, expected", [
        (alist, 5, True),
        (alist, 3, True),
        (alist, 7, True),
        (alist, 1, True),
        (alist, 9, True),
        (alist, 4, False),
        (alist, 12, False)
    ], indirect=["alist"]
)
def test_finding_token_in_sample_list(alist, token, expected):
    assert binary_search(alist, token) is expected
