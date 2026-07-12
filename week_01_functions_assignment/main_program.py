# Functions Assignment - main program
# Collects up to 5 employees using the functions in functions/employee_functions.py

from functions.employee_functions import (
    get_yes_no,
    get_employee_number,
    get_employee_name,
    get_hourly_wage,
    get_department,
    get_full_time,
)

employees = []

print("Enter information for up to 5 employees.\n")

# loop up to 5 times, building one employee dictionary per pass
for i in range(5):
    print(f"Employee {i + 1}:")

    # each field comes from its own validating function
    employees.append({
        "employee_number": get_employee_number(),
        "name":            get_employee_name(),
        "hourly_wage":     get_hourly_wage(),
        "department":      get_department(),
        "full_time":       get_full_time()
    })

    # stop early if the user doesn't want to add another
    if i < 4:
        if not get_yes_no("Add another? (y/n): "):
            break
        print()

# print the finished list of employees
print("\nAll employees:")
print(employees)
