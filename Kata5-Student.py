class User():
    # Properties
    name = ''
    last_name = ''
    __dni = ''
    __age = 0

    # Constructor
    def __init__(self, name, last_name, dni, age):
        self.name = name
        self.last_name = last_name
        self.__dni = dni
        self.__age = age

    # Getters / Setters
    @property
    def dni(self):
        return self.__dni

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            raise Exception('Age is an invalid value')

    # Methods
    def greet(self):
        print(f'Hello, my name is {self.name}')

    def increment_age(self):
        self.__age += 1


class Student(User):
    # Properties
    subjects = []

    # Constructor
    def __init__(self, name, last_name, dni, age):
        super().__init__(name, last_name, dni, age)

    # Methods
    def add_subject(self, subject):
        self.subjects.append(subject)


class Teacher(User):
    # Properties
    specialty = ''

    # Constructor
    def __init__(self, name, last_name, dni, age):
        super().__init__(name, last_name, dni, age)


class Subject():
    # Properties
    __id = 0
    __grade = 0
    name = ''

    # Constructor
    def __init__(self, name):
        self.name = name

    # Getters / Setters
    @property
    def id(self):
        return self.__id

    @property
    def grade(self):
        return self.__grade

    # Methods
    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.__grade = grade


class Group():
    # Properties
    __id = 0
    teacher = None
    students = []
    subjects = []

    # Constructor
    def __init__(self, teacher, students, subjects):
        self.teacher = teacher
        self.__load_students(students)
        self.__load_subjects(subjects)

    # Getters / Setters
    @property
    def id(self):
        return self.__id

    # Methods
    def show_group(self):
        for student in self.students:
            print(student.name)
        for subject in self.subjects:
            print(subject.name)

    def __load_subjects(self, subjects):
        for subject in subjects:
            new_subject = Subject(subject)
            self.add_subject(new_subject)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        self.subjects.remove(subject)

    def __load_students(self, students):
        for student in students:
            new_student = Student(student, '', '', 0)
            self.add_student(new_student)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)
