# set은 집합을 표현한다.

if __name__ == '__main__':
    # fruits = {'apple', 'banana', 'orange'}
    # fruits.add('mango')
    # print(type(fruits))
    #
    # companies = {'apple', 'microsoft', 'google'}
    # print(type(companies))
    #
    # print(fruits & companies)  # 교집합
    # print(fruits | companies)  # 합집합
    #
    # list_of_sets = [fruits, companies]
    # set.intersection(*list_of_sets)
    # set.union(*list_of_sets)

    alphabet = list('google')
    print(alphabet)
    print(set(alphabet))

    S1 = {1, 2, 3, 4, 5, 6, 7}
    S2 = {3, 6, 9}
    print(S1 - S2)

