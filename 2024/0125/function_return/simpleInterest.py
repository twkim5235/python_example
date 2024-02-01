def simpleInterest(p: int, r: float, t: float):
    return p * r * t


print(simpleInterest(10000000, 0.03875, 5))

def simpleInterestAmount(p: int, r: float, t: float):
    return p * (1 + r * t)


print(simpleInterestAmount(10000000, 0.03875, 5))