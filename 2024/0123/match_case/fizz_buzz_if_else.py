for n in range(1, 100):
    if n % 3 == 0 and n % 5 == 0:
        print("피즈버즈")
    elif n % 3 == 0:
        print("피즈")
    elif n % 5 == 0:
        print("버즈")
    else:
        print(n)