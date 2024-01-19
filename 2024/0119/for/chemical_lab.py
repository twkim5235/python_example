minMax = input()
min, max = map(int, minMax.split())

measures = input()

for measure in map(int, measures.split()):
    if measure == -999:
        quit()

    if min <= measure <= max:
        print('Nothing to  report')
    else:
        print('Alert!')
        quit()
