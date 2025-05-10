# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()  # Call the original function
    return wrapper

# Applying the decorator to the say_hello function
@log_function_call
def say_hello():
    print("Hello, world!")

# Example usage
say_hello()
