score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]

stemLeaf = [[], [], []]

# for s in score:
#     tenDigit = s // 10
#     num = s % 10
#     stemLeaf[tenDigit].append(num)


for s in score:
    d, m = divmod(s, 10)
    stemLeaf[d].append(m)

for i in range(len(stemLeaf)):
    print(f'{i}: {stemLeaf[i]}')
