countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1
    if input() == '중단':
        break   # while은 break가 걸려도 else문이 실행되지 않는다.
else:
    print('발사 !')