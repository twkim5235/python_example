numberSplit = input("Enter a number: ").split(" ")

numTuple = tuple(map(lambda x: int(x), numberSplit))

addition = sum(numTuple)
subtraction = numTuple[0] - numTuple[1]
multiply = numTuple[0] * numTuple[1]
division = numTuple[0] / numTuple[1]

print(addition, subtraction, multiply, division)



