import person


class Student(person.Person):
    def study(self):
        print('열공열공...')


if __name__ == '__main__':
    lee = person.Person()
    print(lee.mouth)
    lee.talk()

    print('-' * 50)

    kim = Student()
    print(kim.mouth)
    kim.talk()
    kim.study()


