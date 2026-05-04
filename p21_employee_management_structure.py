class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __str__(self):
        return f"Name: {self.name}, Department: {self.department}"


class Developer(Employee):
    def __init__(self, name, department, programming_language, experience_years):
        super().__init__(name, department)
        self.programming_language = programming_language
        self.experience_years = experience_years

class Manager(Employee):
    def __init__(self, name, department, team_size, project):
        super().__init__(name, department)
        self.team_size = team_size
        self.project = project

class Intern(Employee):
    def __init__(self,name, department, duration_months, mentor):
        super().__init__(name, department)
        self.duration_months = duration_months
        self.mentor = mentor


class Directory:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        for current_employee  in self.employees:
            if current_employee.name.lower() == employee.name.lower():
                print("Employee already exists")
                return
        self.employees.append(employee)

    def view_employee(self):
        for employee in self.employees:
            print(employee)

    def __len__(self):
        return len(self.employees)

    def search_by_attribute(self, attribute_name, value):
        for employee in self.employees:
            value = getattr(employee, attribute_name, None)
        print(value)


if __name__ == "__main__":
    developer = Developer("John", "IT", "Python", 5)
    manager = Manager("Alice", "HR", 10, "HR Project")
    intern = Intern("Bob", "Marketing", 2, "Marketing Mentor")

    directory = Directory()
    directory.add_employee(developer)
    directory.add_employee(manager)
    directory.add_employee(intern)
    directory.view_employee()
    print(len(directory))
    directory.search_by_attribute("name", "John")




