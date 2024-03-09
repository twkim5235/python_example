def read_date():
    return tuple(map(int, input("Enter a date: ").split()))


def print_date(date):
    year, month, day = date
    print("%02d/%02d/%04d" % (month, day, year))


def advance_date(date):
    year, month, day = date

    # in의 안에 month, day가 포함하는가?
    # 조건문을 바깥에도 쓸 수 있다니 신기하다. 혁명이다 혁명이여
    end_of_month = (month, day) in [(1, 31), (2, 28), (3, 31), (4, 30),
                                    (5, 31), (6, 30), (7, 31), (8, 31),
                                    (9, 30), (10, 31), (11, 30), (12, 31)]

    end_of_year = month == 12 and day == 31

    if end_of_month:
        if end_of_year:
            year, month, day = year + 1, 1, 1
        else:
            month, day = month + 1, 1

    else:
        day += 1

    return year, month, day


if __name__ == "__main__":
    date = read_date()
    advance_date = advance_date(date)

    print_date(date)
    print_date(advance_date)
