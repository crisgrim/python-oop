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

class Group():
    teacher = None
    students = []
    subjects = []

    def __init__(self, teacher, students, subjects):
        self.load_students(students)
        self.load_subjects(subjects)

    def show_group(self):
        for student in self.students:
            print(student.name)
        for subject in self.subjects:
            print(subject.name)

    def load_subjects(self, subjects):
        for subject in subjects:
            new_subject = Subject(subject)
            self.add_subject(new_subject)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        self.subjects.remove(subject)

    def load_students(self, students):
        for student in students:
            new_student = Student(student, '', '', 0)
            self.add_student(new_student)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)


student1 = Student('Cristina', 'Ponce', '34124312Z', 18)
student1.greet()
student1.increment_age()

students = ['Cristina', 'Adrián']
subjects = ['Lengua', 'Inglés']

group = Group('Isabel', students, subjects)
group.show_group()
