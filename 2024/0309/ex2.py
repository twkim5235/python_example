def sumOfDigits(nums):
    result = 0

    for num in list(nums):
        result += int(num)

    return result


nums = input("Enter Num: ")
print(sumOfDigits(nums))
