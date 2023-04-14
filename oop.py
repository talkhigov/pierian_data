class Animal():
    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print(' I am eating')

myanimal = Animal()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    def who_am_i(self):
        print('I am a dog')

    def bark(self):
        print('WOOF!')

    def eat(self):
        print('I am a dog and eating')

mydog = Dog()
mydog.who_am_i()
mydog.eat()
        