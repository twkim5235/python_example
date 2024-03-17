def word_game():
    computer_words = set()
    for e in ('게맛살, 구멍, 글라이더, 기차, 대롱, 더치페이, 롱다리, 리본, 멍게, '
              '박쥐, 본네트, 빨대, 살구, 양심, 이빨, 이자, 자율, 주기, 쥐구멍, 차박, 트라이앵글').split(','):
        computer_words.add(e.lstrip())
    spoken_words = set()

    computer_word = "기차"
    spoken_words.add(computer_word)
    print("<시작>끝말잇기를 하자. 내가 먼저 말할게.")
    print(computer_word)

    while True:
        prev_word = computer_word
        input_word = input('> ')

        if input_word == '졌다':
            print('야호!')
            break

        if input_word in spoken_words:
            print("아까 했던 말이야. 내가 이겼어! <끝>")
            break

        if prev_word[len(prev_word) - 1] == input_word[0]:
            flag = 0
            for key in computer_words:
                if key[0] == input_word[len(input_word) - 1]:
                    computer_word = key
                    print(computer_word)
                    flag = 1
                    spoken_words.add(prev_word)
                    spoken_words.add(input_word)

            if flag == 0:
                print("모르겠다. 내가 졌어 <끝>")
                break
        else:
            print("글자가 안 이어져. 내가 이겼다! <끝>")
            break


if __name__ == '__main__':
    word_game()
