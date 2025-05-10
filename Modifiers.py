class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public
        self._salary = salary   # Protected (convention)
        self.__ssn = ssn        # Private (name mangling)

    def display(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN (inside class):", self.__ssn)

# Create an object
emp = Employee("Alice", 50000, "123-45-6789")

# Accessing variables
print("Public name:", emp.name)         # ✅ Accessible

print("Protected salary:", emp._salary) # ⚠️ Technically accessible, but discouraged

# Try to access private variable
try:
    print("Private SSN:", emp.__ssn)    # ❌ Will raise AttributeError
except AttributeError as e:
    print("Error accessing private SSN:", e)

# Access private variable using name mangling (not recommended)
print("Private SSN (via mangling):", emp._Employee__ssn)  # ✅ Works, but not standard practice
