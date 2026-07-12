# Student class - inherits from Person.

from classes.person import Person


class Student(Person):
    """A student record with a student ID and program of study."""

    def __init__(self, name, email, student_id, program):
        super().__init__(name, email)
        self.student_id = student_id
        self.program = program

    def displayInformation(self):
        """Print all student fields, including the shared ones."""
        print("Type: Student")
        super().displayInformation()
        print("Student ID:", self.student_id)
        print("Program of Study:", self.program)
