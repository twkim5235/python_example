class Animal(object):
    def cry(self):
        print('...')

class Feline(Animal):
    pass

class Tiger(Feline):
    def cry(self):
        print('어흥')

class Cat(Feline):
    def cry(self):
        print('야옹')
