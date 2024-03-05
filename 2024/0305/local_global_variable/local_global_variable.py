# jjang = '09'
# jjang = 'pig dad'
#
# print(jjang)
#
# def ban():
#     jjang = '07'
#     print('jjang =', jjang)
#
# ban()
# print(jjang)

# def d_is_10():
#     d = 10
#     print('d 값은', d, '입니다.')
#
# d_is_10()
#
# d라는 변수는 지역변수이기에 함수가 끝나면 사라짐
# print(d)

# x = 10
#
# def printx():
#     print(x)
#
# printx()

def e_is_10():
    global e  # e는 전역변수
    e = 10
    print('e 값은 ', e, '입니다.')


e_is_10()
print(e)
