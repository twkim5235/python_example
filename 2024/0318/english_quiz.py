import random

answer = open('txt_file/ko_en.txt', 'r').read()

answer_split = answer.split('\n')
answer_dict = dict()
for line in answer_split[1:len(answer_split)-1]:
    ko, en = tuple(line.split('\t'))
    answer_dict[ko] = en

while True:
    print('Write the following sentence in English.')
    key_list = list(answer_dict.keys())
    quiz = random.choice(key_list)
    print(quiz)

    answer = input('\nyour answer: ')
    if answer_dict[quiz] == answer:
        print("\nresult: Correct!")
    else:
        print("\nresult: Incorrect!")
        print(f"right answer: {answer_dict[quiz]}")
        break

    print('----------------------------------------------------------------------')

