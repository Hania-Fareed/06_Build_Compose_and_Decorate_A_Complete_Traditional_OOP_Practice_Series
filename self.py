class Student:
    def __init__(self, name, marks):
        self.name = name         # using self to assign name
        self.marks = marks       # using self to assign marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Example usage
student1 = Student("Alice", 85)
student1.display()
