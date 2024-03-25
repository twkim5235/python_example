number_dictionary = {0: '영', 1: '일', 2: '이', 3: '삼',
                     4: '사', 5: '오', 6: '육',
                     7: '칠', 8: '팔', 9: '구'}


def korean_number(num):
    result = str('')
    if num == 100:
        result += '백'
        return result

    elif num >= 10:
        print(num / 10)
        ten_number = number_dictionary.get(num // 10)
        result += ten_number + '십'

    result += number_dictionary.get(num % 10)
    return result
