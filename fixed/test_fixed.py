from fixedp import has_fixed
import pytest


def test_for_fixed_point():
    """ """
    assert has_fixed([-6, 0, 2, 4]) == 2


# @pytest.mark.skip
def test_for_absence_of_fixed_point():
    """ """
    assert has_fixed([1, 5, 7, 8]) is False


def test_for_boundary_cases():
    """ """
    assert has_fixed([1, 1, 4, 5]) == 1

# @pytest.mark.skip


def test_for_efficiency_of_approach():
    """ """

    million = range(1, 1_000_000)
    assert has_fixed(million) is False

# @pytest.mark.skip


def test_for_million_plus_edge_case():
    """ """

    million = range(1, 1_000_000)
    million_plus = list(million) + [999_999]

    zipl = list(enumerate(million_plus))
    print(zipl[-2:])
    assert has_fixed(million_plus) == 999_999


@pytest.mark.skip
def test_for_ten_million_plus_edge_case():
    """ """
    million10 = list(range(1, 16_000_000))
    million10_plus = million10 + [15_999_999]

    # zipl = list(enumerate(million10_plus))
    # print(zipl[-2:])
    assert has_fixed(million10_plus) == 15_999_999


def test_for_ten_million_plus_edge_case_at_the_start():
    """ """
    million10 = list(range(1, 17_000_000))
    m2 = [0] + million10
    assert has_fixed(m2) == 0
