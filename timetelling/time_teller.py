# from pprint import pprint


hourDB = {angle: angle // 30 for angle in range(0, 361, 1)}

minuteDB = {angle: ((angle * 5) // 30) % 60 for angle in range(0, 361, 1)}


def time_teller(hourangle, minuteangle, hourDB=hourDB, minuteDB=minuteDB):

    hour = hourDB[hourangle]
    minute = minuteDB[minuteangle]
    res = f'{hour}:{minute%60:02}{"pm"*(hourangle > 360)}'
    return res
