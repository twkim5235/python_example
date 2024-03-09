def sumOfDigits(s):

    m = map(lambda x: int(x), list(s))

    print(sum(m))


if __name__ == '__main__':
    numStr = input("Enter a number: ")
    sumOfDigits(numStr)