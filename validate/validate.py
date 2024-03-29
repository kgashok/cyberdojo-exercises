def validate(number):
    '''validate whether an account number is valid'''

    digits = list(int(i) for i in str(number))

    digits_to_double = digits[-2::-2]
    other_digits = digits[-3::-2]
    check_digit = digits[-1]
    # print(digits_to_double, other_digits, check_digit)

    total = sum(
        map(lambda digit: sum(int(i) for i in str(digit*2)),
            digits_to_double)
    )
    total += sum(other_digits)
    mod10 = total % 10

    correct_check = 10 - mod10 if (total + check_digit) % 10 else \
        0 if mod10 == 0 and check_digit else \
        None
    check_string = " " + str(correct_check)

    return "IN" * (correct_check is not None) \
        + "VALID" \
        + ("" if correct_check is None else check_string)


if __name__ == "__main__":
    acctid = int(input("Account Number to validate: "))
    print(validate(acctid))
