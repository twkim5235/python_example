x = 'banana'
print(x[0])
print(x[2:4])
print(x[:3])
print(x[3:])

x = 'n' + x[1:]
print(x)

s = "hello Python!"
print(s.find('P'))

print(s[0:6])

h = s[0:6]
print(h)

print(h[0:5])
print(h.rstrip())

print(s.split()[1])

prime = [3, 7, 11]
prime.append(5)
print(prime)

prime.sort()
print(prime)

prime.insert(0, 2)
print(prime)

del prime[4]
print(prime)

a = prime.pop()
print(prime)
print(a)

orders = ['potato', ['pizza', 'Coke', 'salad'], 'hamburger']
print(orders[1])
print(orders[1][2])

characters = []
sentence = 'Be happy!'
for char in sentence:
    characters.append(char)

print(characters)

my_int = 213
print(type(str(my_int)))

print(int('123'))
print(float('123').__str__() + '\n')

chulus = [90, 85, 70]
younghee = [88, 79, 92]
yong = [100, 100, 100]
minsu = [90, 70, 60]

students = [chulus, younghee, yong, minsu]

for scores in students:
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    print(scores, total, average)
