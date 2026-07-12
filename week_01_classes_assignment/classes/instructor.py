# Instructor class - inherits from Person.

from classes.person import Person


class Instructor(Person):
    """An instructor record with an ID, institution, and degree."""

    def __init__(self, name, email, instructor_id, institution, degree):
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.institution = institution
        self.degree = degree

    def displayInformation(self):
        """Print all instructor fields, including the shared ones."""
        print("Type: Instructor")
        super().displayInformation()
        print("Instructor ID:", self.instructor_id)
        print("Last Institution:", self.institution)
        print("Highest Degree:", self.degree)
