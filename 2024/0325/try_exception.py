def f(a, b):
    try:
        if a and b:
            return (a * b) + (a / b)
        elif a:
            return '불능'
        else:
            return '부정'
    except:
        return '똑바로 살아라'


print(f(300000, 500000))
print(f(0, 0))
try:
    # print(f(이십, 오))
    print(3/0)
except NameError as e:
    print(e)
except ZeroDivisionError as e:
    print("0으로는 나누지 못합니다.")

