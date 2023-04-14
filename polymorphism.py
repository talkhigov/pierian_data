class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'
    
class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'
    
niko = Dog('Niko')
felix = Cat('Felix')

# print(niko.speak())
# print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())


class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError
    
class Dog(Animal):

    def speak(self):
        return self.name + ' says woof!'
    
fido = Dog('Fido')
print(fido.speak())
    