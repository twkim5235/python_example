from functools import reduce


def read_nums():
    return tuple(map(int, input("Enter numbers: ").split()))

def function(nums):

    additional = reduce(lambda x, y: x + y, nums)
    subtraction = reduce(lambda x, y: x - y, nums)
    multiplication = reduce(lambda x, y: x * y, nums)
    division = reduce(lambda x, y: x / y, nums)

    return additional, subtraction, multiplication, division


if __name__ == '__main__':
    nums = read_nums()
    print(function(nums))

