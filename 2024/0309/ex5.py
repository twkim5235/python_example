def printPrimeNumber(l):
    result = []

    for i in range(len(l)):
        if l[i] != 0:
            result.append(l[i])

            for j in range(i + 1, len(l)):
                if l[j] % l[i] == 0:
                    l[j] = 0

    print(result)


if __name__ == '__main__':
    i = int(input("Enter a number: "))
    printPrimeNumber(list(range(2, i + 1)))
