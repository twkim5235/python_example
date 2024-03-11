def rule_90():
    dic = dict()
    dic = {'111': '0', '110': '1', '101': '0',
           '100': '1', '011': '1', '010': '0',
           '001': '1', '000': '0'}

    col_width = 61
    mid_index = col_width // 2
    line = '0' * mid_index + '1' + '0' * mid_index
    print(line)

    while line[1] != '1':
        prev = line
        line = '0'

        for i in range(col_width - 2):
            line += dic[prev[i: i + 3]]

        line += '0'
        print(line)


if __name__ == '__main__':
    rule_90()
