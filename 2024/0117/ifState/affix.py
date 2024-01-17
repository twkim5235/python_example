num = int(input())

kilobyte: int = 10 ** 3
megabyte: int = 10 ** 6
gigabyte: int = 10 ** 9
terabyte: int = 10 ** 12
petabyte: int = 10 ** 15
unit = str()

if num < megabyte:
    print("범위를 벗어났습니다.")
    quit()
elif num >= petabyte:
    num //= petabyte
    unit = 'P'
elif num >= terabyte:
    num //= terabyte
    unit = 'T'
elif num >= gigabyte:
    num //= gigabyte
    unit = 'G'
elif num >= megabyte:
    num //= megabyte
    unit = 'M'
elif num >= kilobyte:
    num //= kilobyte
    unit = 'K'

print(str(num) + unit)