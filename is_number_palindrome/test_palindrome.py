from palindrome import is_number_palindrome


def test_simple_palindrome_number():
    assert is_number_palindrome(121) is True


def test_palindrome_number_with_all_same_digits():
    assert is_number_palindrome(888) is True


def test_non_palindrome_number_with_more_than_3_digits():
    assert is_number_palindrome(1321) is False


def test_palindrome_number_which_is_really_big():
    assert is_number_palindrome(12345654321) is True


def test_negative_palindrome_numbers():
    assert is_number_palindrome(-232) is True
    assert is_number_palindrome(-12321) is True


def test_negative_non_palindrome_numbers():
    assert is_number_palindrome(-1112) is False


def test_for_zero():
    assert is_number_palindrome(0) is True
