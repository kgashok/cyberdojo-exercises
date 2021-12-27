def validate(number):
    digits = list(str(number))[::-1]
    double = ""
    for i in range(len(digits)):
        if (i % 2 != 0):
            double += str(int(digits[i]) * 2)
        else:
            double += digits[i]
    total = sum([int(x) for x in list(double)])
    print("\nnumber", number)
    print("doubled as", double, "\ntotal", total)
    if (total % 10 == 0):
        return "VALID"
    else:
        bad_check = number % 10
        revised_total = total - bad_check
        good_check = 10 - (revised_total % 10)
        return "INVALID " + str(good_check)
