def korea_number(num):
    number_dictionary = {1: '일', 2: '이', 3: '삼',
                         4: '사', 5: '오', 6: '육',
                         7: '칠', 8: '팔', 9: '구'}
    print(number_dictionary.get(num))


if __name__ == '__main__':
    korea_number(int(input("Enter a number: ")))