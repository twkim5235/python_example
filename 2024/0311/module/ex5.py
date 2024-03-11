import ex4


def together_ride(heights):

    set_list = []

    for h in heights:
        set_list.append(set(ex4.allowedrides(h)))

    for ride in set.intersection(*set_list):
        print(ride)


if __name__ == "__main__":
    m = list(map(lambda x: int(x), input().split()))

    together_ride(m)
