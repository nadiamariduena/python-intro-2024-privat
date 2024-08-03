class Student:
# Class attribute to keep track of all students
    # THE Bellow looks like an array but it not, so dont confuse it with the JS arrays
    students = [] ## An empty list to keep track of all Student instances

    def __init__(self, name, grade):
        # - self refers to the specific instance of the class that is currently being created or interacted with
        self.name = name
        self.grade = grade
        # ADD the new student to the class list
        Student.students.append(self) # -  # Refers to the instance of Student that is currently being initialized
        # - "Student" class, this line is typically found in the __init__ method, which is the constructor for the class.
        # - Student: This refers to the class itself.

    # Maintaining a Record: This line ensures that every time a new Student instance is created, it is added to the class-level students list.
        #
        #

    @classmethod
    def had_good_grades(cls): #cls: class
        """Class method to check if any student has good grades (A or B).
        """

        for student in cls.students: # (the LIST at the top inside the class, line 3)
            if student.grade in ("A", "B"): # dont add emojis within the "" on the a b etc, you will get a False instead of True, just because of the emoji and not because of the Note
                return True
        return False

    @classmethod
    def get_students_with_good_grades(cls):
        """Class method to get a List o students with good grades (A or B).
        """

        good_students = [student.name for student in cls.students if student.grade in ("A", "B")]

        return good_students

    # Qualifications
#Student.students.append(s1)  # Adds the new Student instance (s1) to the list
# -  s1 is the "self", and so on s2 self, s3 self...
# - self refers to the specific instance of the class that is currently being created or interacted with

s1 = Student("Filomena", "A")
s2 = Student("Ludovico", "C")
s3 = Student("Ana", "B")
s4 = Student("Yvonne", "D")


#Check if there are any students with good grades
print(Student.had_good_grades())

# GET a list of students with good grades
good_students = Student.get_students_with_good_grades()
print(good_students)
