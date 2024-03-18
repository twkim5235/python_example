f = open("/Users/xodn/.pyenv/versions/3.12.2/lib/python3.12/LICENSE.txt", "r")
lines = f.readlines()

for line in lines[-10:]:
    print(line)
