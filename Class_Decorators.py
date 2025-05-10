# Class decorator
def add_greeting(cls):
    # Add a greet method to the class
    def greet(self):
        return "Hello from Decorator!"
    
    # Attach the greet method to the class
    cls.greet = greet
    return cls

# Applying the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"

# Example usage
person = Person("Alice")
print(person.introduce())  # Existing method
print(person.greet())      # New method added by decorator
