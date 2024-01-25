def area(base, height):
    return base * height / 2


t_base = int(input("Enter side: "))
t_height = int(input("Enter height: "))
triangle_area = area(t_base, t_height)

print(triangle_area)


def quiz():
    ans = input("1 + 2 = ")
    return 1 + 2 == int(ans)


print(quiz())