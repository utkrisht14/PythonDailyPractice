class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        return f"Name: {self.name}, Employee ID: {self.employee_id}"

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method")


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        if monthly_salary <= 0:
            raise ValueError("Monthly salary must be greater than 0")
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id)
        if hours_worked <= 0 or hourly_rate <= 0:
            raise ValueError("Hours worked and hourly rate must be greater than 0")
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


class Intern(Employee):
    def __init__(self, name, employee_id, stipend):
        super().__init__(name, employee_id)
        if stipend <= 0:
            raise ValueError("Stipend must be greater than 0")
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


# Usage
emp1 = FullTimeEmployee("John", 101, 5000)
emp2 = PartTimeEmployee("Alice", 102, 80, 20)
emp3 = Intern("Bob", 103, 1000)

employees = [emp1, emp2, emp3]

for emp in employees:
    print(emp.display_info())
    print(f"Salary: {emp.calculate_salary()}")
    print("-" * 30)