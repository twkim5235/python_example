# 내가 짠 코드
def palindrome(str):
    index = 0
    strLen = len(str)
    finalIndex = strLen - 1

    while index < strLen / 2:
        if str[index] != str[finalIndex - index]:
            return False
        index += 1

    return True


print(palindrome(input("Enter a string: ").lower().replace(' ', '')))


def isPalindrome(str):
    return str == str[::-1]


print(isPalindrome(input("Enter a string: ").lower().replace(' ', '')))
