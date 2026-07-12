# Classes Assignment - main program
# Collects instructors and students, validates each field, stores them in
# college_records, then prints every record at the end.

from classes.validator import Validator
from classes.student import Student
from classes.instructor import Instructor

college_records = []
v = Validator()

# keep collecting people until the user says they're done
while True:

    # figure out the type first, re-ask until it's instructor or student
    kind = input("Instructor or student? ").strip().lower()
    while kind not in ("instructor", "student"):
        print("Please type instructor or student.")
        kind = input("Instructor or student? ").strip().lower()

    # name is required for both types
    name = input("Name: ").strip()
    while not v.checkName(name):
        print("Invalid name, try again.")
        name = input("Name: ").strip()

    # email is required for both types
    email = input("Email: ").strip()
    while not v.checkEmail(email):
        print("Invalid email, try again.")
        email = input("Email: ").strip()

    if kind == "student":
        # student-specific fields
        student_id = input("Student ID: ").strip()
        while not v.checkStudentID(student_id):
            print("Student ID must be a number 7 digits or less.")
            student_id = input("Student ID: ").strip()

        program = input("Program of study: ").strip()
        while not v.checkRequired(program):
            print("Program of study is required.")
            program = input("Program of study: ").strip()

        person = Student(name, email, student_id, program)

    else:
        # instructor-specific fields
        instructor_id = input("Instructor ID: ").strip()
        while not v.checkInstructorID(instructor_id):
            print("Instructor ID must be a number 5 digits or less.")
            instructor_id = input("Instructor ID: ").strip()

        institution = input("Last institution graduated from: ").strip()
        while not v.checkRequired(institution):
            print("Institution is required.")
            institution = input("Last institution graduated from: ").strip()

        degree = input("Highest degree earned: ").strip()
        while not v.checkRequired(degree):
            print("Degree is required.")
            degree = input("Highest degree earned: ").strip()

        person = Instructor(name, email, instructor_id, institution, degree)

    # add the finished record to the list
    college_records.append(person)

    # stop when the user is done
    done = input("Are you done? (y/n): ").strip().lower()
    if done in ("y", "yes"):
        break

# print every record we collected
print()
for person in college_records:
    person.displayInformation()
    print()
