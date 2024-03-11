# def hap(x, y):
#     return x + y
#
#
# print((ch03 x, y: x + y)(10, 20))
#
# var = ch03 x, y: x + y
# print(var(10, 20))
# from functools import reduce
#
# print(list(map(ch03 x: x ** 2, range(5))))
#
# print(reduce(ch03 x, y: x + y, range(5)))
#
# print(reduce(ch03 x, y: y + x, 'abcde'))

# print(list(filter(ch03 x: x < 5, range(10))))
#
# print(list(filter(ch03 x: x % 2, range(10))))

def read_rider(text):
    ride_name, limit = map(str.strip, text.split(':'))

    cm_min = cm_max = None
    if '~' in limit:
        cm_min, cm_max = map(lambda x: int(x.replace('cm', '')), limit.split('~'))
    elif '이상' in limit:
        cm_min = int(limit.split("cm")[0])

    return ride_name, cm_min, cm_max

# def read(text):
#     ridename, limit = map(str.strip, text.split(':'))
#     cmMin = cmMax = None
#
#     if '~' in limit:
#         tempList = []
#         for l in limit.split('~'):
#             tempList.append(str.replace(l, 'cm', ''))
#
#         cmMin, cmMax = tempList[0], tempList[1]
#     elif '이상' in limit:
#         cmMin = int(limit.split('cm')[0])
#
#
#     return ridename, cmMin, cmMax

if __name__ == '__main__':
    ride_name, cm_min, cm_max = read_rider(input())
    print("이름: ", ride_name)
    print("하한: ", cm_min)
    print("상한: ", cm_max)