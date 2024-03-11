def sum_dice():
    dice1 = (1, 2, 3, 4, 5, 6)
    dice2 = (2, 3, 5, 7, 11, 13)
    sum_set = set()

    for e in dice1:
        for x in dice2:
            sum_set.add(x + e)

    print(sum_set)


if __name__ == '__main__':
    sum_dice()
