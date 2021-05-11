class Person():
    # Properties
    name = ''
    age = ''

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, person):
        couple = Couple(self, person)
        return couple


class Couple():
    # Properties
    couple = []

    # Constructor
    def __init__(self, person1, person2):
        self.couple.append(person1)
        self.couple.append(person2)

    def __add__(self, person):
        family = Family()
        family.add_member(person)
        family.add_member(self.couple[0])
        family.add_member(self.couple[1])
        return family

    def show(self):
        for person in self.couple:
            print(person.name)


class Family():
    # Properties
    members = []

    # Methods
    def add_member(self, member):
        self.members.append(member)

    def show(self):
        for person in self.members:
            print(person.name)


person1 = Person('Cristina', 18)
person2 = Person('Adrián', 20)
person3 = Person('Ragnar', 1)
person4 = Person('Lagertha', 2)

couple = person1 + person2
couple.show()

print('-------')

family = couple + person3
family.show()

