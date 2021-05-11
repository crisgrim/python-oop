class Animal():
    # Properties
    specie = ''
    height = ''
    weight = ''

    # Constructor
    def __init__(self, specie, height, weight):
        self.specie = specie
        self.height = height
        self.weight = weight

    # Methods
    def eat(self):
        print('I\'m eating')

    def hunt(self):
        print('I\'m going to hunt')

    def sleep(self):
        print('I\'m going to sleep')


class Pet():
    # Properties
    name = ''
    owner = ''

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def sit_down(self):
        print('I\'m sitting')

    def give_paw(self):
        print('I\'m giving my paw')


class Lion(Animal):
    # Constructor
    def __init__(self, height, weight):
        super().__init__('Lion', height, weight)


class Dog(Animal, Pet):
    # Constructor
    def __init__(self, name, owner, height, weight):
        Animal.__init__(self, 'Dog', height, weight)
        Pet.__init__(self, name, owner)


chopper = Dog('Chopper', 'Cristina', 0.5, 7)
jacky = Dog('Jacky', 'Adrián', 0.5, 7)

print(chopper.name)
chopper.eat()
chopper.hunt()
chopper.sleep()
chopper.give_paw()
chopper.sit_down()

print(jacky.name)
jacky.eat()
jacky.hunt()
jacky.sleep()
jacky.give_paw()
jacky.sit_down()
