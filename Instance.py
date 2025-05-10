class Dog:
    def __init__(self, name, breed):
        self.name = name      # instance variable
        self.breed = breed    # instance variable

    def bark(self):           # instance method
        print(f"🐶 {self.name} the {self.breed} says: Woof!")

# Example usage
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()
