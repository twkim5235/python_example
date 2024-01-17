height: float = 100
bounce = 3 / 5

i: int = 1
while i <= 10:
    height *= bounce
    print(i, round(height, 4))
    i += 1
