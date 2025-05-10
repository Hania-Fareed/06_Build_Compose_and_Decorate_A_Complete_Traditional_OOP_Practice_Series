class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called.")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of Person
        self.subject = subject
        print("Teacher constructor called.")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

# Example usage
t1 = Teacher("Mr. Smith", "Mathematics")
t1.display()
