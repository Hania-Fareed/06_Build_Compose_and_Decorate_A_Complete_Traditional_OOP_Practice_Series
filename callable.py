class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    # __call__ method to make the object callable like a function
    def __call__(self, x):
        return x * self.factor

# Example usage
multiplier = Multiplier(5)

# Check if the object is callable
print(callable(multiplier))  # Should return True because the __call__ method is defined

# Use the object like a function
result = multiplier(10)  # Equivalent to multiplier.__call__(10)
print(result)  # Should output 50 because 10 * 5 = 50

