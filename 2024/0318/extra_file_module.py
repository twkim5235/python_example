# users = {'kim': '3kid9', 'sun80': '393948', 'ljm': 'py90390'}
# f = open('txt_file/users', 'wb')
#
# import pickle
#
# pickle.dump(users, f)
# f.close()

from glob import glob
from os.path import isdir

# print(glob('*.exe'))
# print(glob('txt_file/*.txt'))

for x in glob('*'):
    if isdir(x):
        print(x, '<DIR>')
    else:
        print(x)
