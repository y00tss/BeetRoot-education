class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.students = []
        self.teachers = []

class Student(Person):
    def __init__(self, name, surname, age, gender, education_type, course, specialization):
        super().__init__(name, surname, age, gender)
        self.education_type = education_type
        self.course = course
        self.specialization = specialization


class Teacher(Person):
    def __init__(self, name, surname, age, gender, subject, salary, rank):
        super().__init__(name, surname, age, gender)
        self.sugject = subject
        self.salary = salary
        self.rank = rank

"""
Получается, что переменные:
Для студента education_type, course, specialization
Для учителя subject, salary, rank
Переменные - name, surname, age, gender - являются общими для студента и учителя.

"""


