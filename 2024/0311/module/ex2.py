import math


def hypotenuse(a, b):
    return round(math.sqrt(a ** 2 + b ** 2), 2)


if __name__ == '__main__':
    print(hypotenuse(10, 20))
