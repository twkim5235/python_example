from glob import glob

anthem_list = glob('txt_file/korean_national_*.txt')

out = open('txt_file/out.txt', 'w+')
for anthem in anthem_list:
    lyrics = open(anthem, 'r').read()

    out.write(anthem.replace('txt_file/', '') + '\n')
    out.write('-' * 30 + '\n')
    out.write(lyrics + '\n')
