c = 10
d = 20

c, d = d, c
print(f'{c}, {d}')


def magu_print(*rest):
    print(rest)


magu_print(1, 2, 3, 4, 5, 6, 7, 8, )

t = ('a', 'b', 'c')
print(t)

empty = ()
print(empty)

one = (5,)
print(one)

p = (1, 2, 3)
q = p[:1] + (5,) + p[2:]

print(q)

r = p[:1], 5, p[2:]
print(r)
print(list(r))

p = (1, 2, 3)
q = list(p)
print(q)

r = tuple(q)
print(r)
