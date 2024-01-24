row = 11
column = 11

table = [[0 for x in range(column)] for y in range(row)]


def multiplication_table(i, j):
    if j == 10:
        return

    if table[i][j] != 0 or table[j][i] != 0:
        print(f"{i} * {j} = {table[i][j]}")

    elif table[i][j] == 0:
        table[i][j] = i * j
        table[j][i] = i * j
        print(f"{i} * {j} = {table[i][j]}")

    multiplication_table(i, j + 1)


for i in range(2, 10):
    multiplication_table(i, 1)
