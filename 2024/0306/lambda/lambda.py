# def hap(x, y):
#     return x + y
#
#
# print((lambda x, y: x + y)(10, 20))
#
# var = lambda x, y: x + y
# print(var(10, 20))
# from functools import reduce
#
# print(list(map(lambda x: x ** 2, range(5))))
#
# print(reduce(lambda x, y: x + y, range(5)))
#
# print(reduce(lambda x, y: y + x, 'abcde'))

# print(list(filter(lambda x: x < 5, range(10))))
#
# print(list(filter(lambda x: x % 2, range(10))))

def read(text):
    rideName, limit = map(str.strip, text.split(':'))

    cmMin = cmMax = None
    if '~' in limit:
        cmMin, cmMax = map(lambda x: int(x.replace('cm', '')), limit.split('~'))
    elif '이상' in limit:
        cmMin = int(limit.split("cm")[0])

    return rideName, cmMin, cmMax

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
    ridename, cmmin, cmmax = read(input())
    print("이름: ", ridename)
    print("하한: ", cmmin)
    print("상한: ", cmmax)