import shape

# a = shape.Shape()
# a.area = 20
# b = shape.Shape()
# b.area = 10
#
# print(a + b)
# print(a.__add__(b))
# print(a - b)
# print(a.__sub__(b))

c = shape.Shape()
c.area = 30
d = shape.Shape()
d.area = 20

print(c > d)
if c > d:
    print('c가 더 넓어요')
