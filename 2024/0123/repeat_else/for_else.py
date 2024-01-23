for n in range(1, 101):
    if n % 3:
        print(n)  # x가 3의 배수가 아니면 출력
    else:
        break  # x가 3의 배수이면 반복문을 빠져나옴
else:
    print("리스트의 원소를 모두 출력하였습니다.")
