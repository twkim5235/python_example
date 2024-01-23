import datetime

age: int = int(input("What is your age? "))
year = datetime.datetime.now().year - age + 1

state = "You are"
if year <= 1924:
    print("%s The Greatest Generation" % state)
elif year <= 1945:
    print("%s The Silent Generation" % state)
elif year <= 1964:
    print("%s baby boomer" % state)
elif year <= 1980:
    print("%s Generation X" % state)
elif year <= 1996:
    print("%s millennial" % state)
else:
    print("%s Generation Z" % state)