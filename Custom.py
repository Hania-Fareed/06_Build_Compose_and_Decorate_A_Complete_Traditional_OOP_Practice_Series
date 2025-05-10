# Define a custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18"):
        self.message = message
        super().__init__(self.message)

# Function that raises the exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Must be at least 18.")
    else:
        print(f"Access granted. Age: {age}")

# Example usage
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Please enter a valid number.")
