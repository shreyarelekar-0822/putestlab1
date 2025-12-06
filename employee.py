def employee details(name, emp_id, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee Id: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
    return result
if _name_ == "_main_":

    name = "Alice"
    emp_id = "E1001"
    department = "IT"
    salary = 55000
    print(employee_details(name, emp_id, department, salary))
