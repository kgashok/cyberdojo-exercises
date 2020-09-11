from time_teller import time_teller

import pytest


@pytest.fixture()
def resource():
    print("setup")
    hourDB = {angle: (angle // 30) % 12 for angle in range(0, 721, 1)}

    minuteDB = {angle: ((angle * 5) // 30) % 60 for angle in range(0, 361, 1)}

    yield hourDB, minuteDB
    print("teardown")


def test_return_3_for90_and_0():
    assert time_teller(90, 0) == "3:00"


def test_return_315_for90_and90():
    assert time_teller(90, 120) == "3:20"

    assert time_teller(100, 120) == "3:20"


def test_return__1155_for_330_and_330():
    assert time_teller(330, 330) == "11:55"


def test_return_correct_values_for_boundaries():
    assert time_teller(360, 360) == "12:00"
    assert time_teller(0, 0) == "0:00"


def test_non_30_multiples_for_minutes(resource):
    hourDB, minuteDB = resource
    assert time_teller(100, 126, hourDB, minuteDB) == "3:21"


def test_for_24_hour_time_telling(resource):
    hourDB, minuteDB = resource
    assert time_teller(460, 126, hourDB, minuteDB) == "3:21pm"
