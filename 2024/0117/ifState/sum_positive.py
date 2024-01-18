
positiveSum: int = 0

while 1:
    num = int(input())
    if num < 0:
        break
    else:
        positiveSum += num

print(positiveSum)