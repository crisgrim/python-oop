class Student():
    # Properties
    name = ''
    last_name = ''
    dni = ''
    age = 0
    grade = 0

    # Constructor
    def __init__(self, name, last_name, dni, age):
        self.name = name
        self.last_name = last_name
        self.dni = dni
        self.age = age

    # Methods
    def greet(self):
        print(f'Hello, my name is {self.name}')

    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grade = grade

    def increment_age(self):
        self.age += 1


student1 = Student('Cristina', 'Ponce', '34124312Z', 18)
print(student1.name, student1.last_name, student1.dni, student1.age, student1.grade)
student1.greet()
student1.add_grade(10)
student1.increment_age()
print(student1.name, student1.last_name, student1.dni, student1.age, student1.grade)
