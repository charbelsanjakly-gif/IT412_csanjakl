# Person base class shared by Student and Instructor.


class Person:
    """Base class holding the name and email common to everyone."""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def displayInformation(self):
        """Print the shared name and email fields."""
        print("Name:", self.name)
        print("Email:", self.email)
