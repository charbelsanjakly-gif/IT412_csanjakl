# Employee input functions for the Functions Assignment.
# Each function prompts for one field and re-asks until the input is valid.


def get_yes_no(prompt):
    """Prompt with a yes/no question and return True for yes, False for no."""
    while True:
        value = input(prompt).strip().lower()
        if value in ("y", "yes"):
            return True
        if value in ("n", "no"):
            return False
        print("Please answer y or n.")


def get_employee_number():
    """Prompt for an employee number and return it as a positive integer."""
    while True:
        value = input("  Employee number: ").strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a whole number greater than 0.")


def get_employee_name():
    """Prompt for a name made of letters and spaces and return it."""
    while True:
        value = input("  Name: ").strip()
        if value and value.replace(" ", "").isalpha():
            return value
        print("Names can only contain letters.")


def get_hourly_wage():
    """Prompt for an hourly wage and return it as a float greater than 0."""
    while True:
        value = input("  Hourly wage: ").strip()
        try:
            wage = float(value)
            if wage > 0:
                return round(wage, 2)
            print("Wage has to be greater than 0.")
        except ValueError:
            print("That isn't a valid number. Try again.")


def get_department():
    """Prompt for a department made of letters and spaces and return it."""
    while True:
        value = input("  Department: ").strip()
        if value and value.replace(" ", "").isalpha():
            return value
        print("Department can only contain letters.")


def get_full_time():
    """Ask whether the employee is full-time and return True or False."""
    return get_yes_no("  Full-time? (y/n): ")
