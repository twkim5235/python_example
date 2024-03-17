import string
import random

# print(string.ascii_uppercase)
#
# print(string.ascii_lowercase)
#
# print(string.ascii_letters)
#
# print(string.digits)

alpha_numeric = string.ascii_letters + string.digits
# print(alpha_numeric)
#
# print(len(alpha_numeric))
#
chars = list(set(alpha_numeric) - set('lIO0')) + ['_']
# print(chars)

# print(len(chars))
# print(random.choice(chars))

pw = str()
for i in range(16):
    pw += random.choice(chars)

print(pw)
