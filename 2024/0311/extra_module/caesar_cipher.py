import string

a_l = string.ascii_lowercase
a_u = string.ascii_uppercase[3:] + string.ascii_uppercase[:3]

tt = str.maketrans(a_l, a_u)

print('traue nie dem brutus'.translate(tt))
