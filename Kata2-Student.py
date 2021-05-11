class Student():
    # Properties
    name = ''
    last_name = ''
    dni = ''
    age = 0
    subjects = []

    # Constructor
    def __init__(self, name, last_name, dni, age):
        self.name = name
        self.last_name = last_name
        self.dni = dni
        self.age = age

    # Methods
    def greet(self):
        print(f'Hello, my name is {self.name}')

    def increment_age(self):
        self.age += 1

    def add_subjet(self, subject):
        self.subjects.append(subject)


student1 = Student('Cristina', 'Ponce', '34124312Z', 18)
student1.greet()
student1.increment_age()

class Subject():
    # Properties
    name = ''
    grade = ''

    # Constructor
    def __init__(self, name):
        self.name = name

    # Methods
    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grade = grade
