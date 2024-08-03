class Student:
# Class attribute to keep track of all students
    # THE Bellow looks like an array but it not, so dont confuse it with the JS arrays
    students = []

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        # ADD the new student to the class list

    @classmethod
    def had_good_grades(cls): #cls: class
        """Class method to check if any student has good grades (A or B).
        """

        for student in cls.students: # (the LIST at the top inside the class, line 3)
            if student.grade in ("A 🌈", "B 👍"):
                return True
        return False

    @classmethod
    def get_students_with_good_grades(cls):
        """Class method to get a List o students with good grades (A or B).
        """

        good_students = [student.name for student in cls.students if student.grade in ("A", "B")]

        return good_students

    # Qualifications

    s1 = Student("Filomena", "A")
    s2 = Student("Ludovico", "C")
    s3 = Student("Ana", "B")
    s4 = Student("Yvonne", "D")


#Check if there are any students with good grades
print(Student.had_good_grades())

# GET a list of students with good grades
good_students = Student.get_students_with_good_grades()
print(good_students)
