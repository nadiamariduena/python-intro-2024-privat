class Student:
# Class attribute to keep track of all students
    students = []

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        # ADD the new student to the class list
