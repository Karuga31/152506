class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"{self.name} | ID: {self.employee_id} | Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_salary(self):
        return sum(emp.salary for emp in self.employees)

    def display_all_employees(self):
        for emp in self.employees:
            emp.display_details()


# Interactive test
department = Department("IT Department")

while True:
    print("\n1. Add Employee\n2. View All\n3. Total Salary\n4. Exit")
    choice = input("Option: ")

    if choice == "1":
        name = input("Name: ")
        emp_id = input("Employee ID: ")
        salary = float(input("Salary: "))
        emp = Employee(name, emp_id, salary)
        department.add_employee(emp)
    elif choice == "2":
        department.display_all_employees()
    elif choice == "3":
        print(f"Total salary: {department.calculate_total_salary()}")
    elif choice == "4":
        break
