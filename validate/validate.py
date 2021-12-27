def validate(number):
    digits = list(int(i) for i in str(number))

    digits_to_double = digits[-2::-2]
    other_digits = digits[-3::-2]
    check_digit = digits[-1]
    print(digits_to_double, other_digits, check_digit)

    total = 0
    for d in digits_to_double:
        sumdigits = sum(int(i) for i in list(str(d*2)))
        total += sumdigits

    total += sum(other_digits)
    print("total without check_digit", total)

    correct_check = None
    if total % 10 == 0 and check_digit:
        correct_check = 0
    elif (total + check_digit) % 10:
        correct_check = 10 - (total % 10)
    check_string = " " + str(correct_check)

    return "IN" * (correct_check is not None) \
        + "VALID" \
        + ("" if correct_check is None else check_string)


if __name__ == "__main__":
    acctid = int(input("Account Number to validate: "))
    print(validate(acctid))
