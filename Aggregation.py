class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def display_info(self):
        return f"{self.name} is a {self.position}"

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: Department refers to an Employee

    def display_department_info(self):
        print(f"Department: {self.department_name}")
        print(f"Employee Info: {self.employee.display_info()}")

# Example usage
emp1 = Employee("Alice", "Software Engineer")
dept1 = Department("Engineering", emp1)

dept1.display_department_info()
