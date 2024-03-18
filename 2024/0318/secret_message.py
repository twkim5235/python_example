import re

postcard = open('txt_file/postcard.txt', 'r').readlines()

result = ''
for line in postcard[3: len(postcard) - 3]:
    # print(re.sub('[.,:]','',line), end='')
    # print(re.sub('[.,:]', '', line).upper(), end='')
    text = re.sub('[:.,]', '', line).upper()
    word = text.split()[:2]
    result += ' '.join(word)

print(result)
