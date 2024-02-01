from datetime import datetime


def triple(x):
    if x.isdigit():
        x = int(x)

    return x * 3


print(triple(input("값을 입력해주세요: ")))


def korean_age(birthYear):
    todayYear = datetime.today().year
    return todayYear - birthYear + 1


print(korean_age(int(input("태어난 년도를 입력하시오: "))))
